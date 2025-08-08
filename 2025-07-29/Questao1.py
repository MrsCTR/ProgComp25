import requests
import datetime
import json
import csv

strURLMoedas = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURLMoedas += '/Moedas?$top=100&$format=json'
dicMoedas = requests.get(strURLMoedas).json()

strURLCotacoes = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURLCotacoes += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURLCotacoes += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURLCotacoes += '@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&'
strURLCotacoes += '@dataFinalCotacao=%2712-31-2023%27&$format=json'

dicCotacoes = requests.get(strURLCotacoes).json()

def Calcular_Media_Mensal(Cotacoes):
    if 'value' not in Cotacoes or not Cotacoes['value']:
        return {"Erro: Não há dados de cotação para o período e moeda selecionados."}
    Meses_pt = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Marco', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
    Media_Mensal = {}
    Cotacoes_Mes = {}
    for Cotacao in Cotacoes:
        try:
        # Pega a data e converte para datetime
            Data = datetime.datetime.strptime(Cotacao['dataHoraCotacao'][:10], '%Y-%m-%d')
            Mes_Numero = Data.month
            Mes_Nome = Meses_pt[Mes_Numero]
            Cotacao_Compra = Cotacao['cotacaoCompra']
            Cotacao_Venda = Cotacao['cotacaoVenda']

            if Mes_Nome not in Cotacoes_Mes:
                Cotacoes_Mes[Mes_Nome] = {'Compras': [], 'Vendas': []}
            
            Cotacoes_Mes[Mes_Nome]['Compras'].append(Cotacao_Compra)
            Cotacoes_Mes[Mes_Nome]['Vendas'].append(Cotacao_Venda)

        except (ValueError, TypeError) as e:
            return f"Erro ao processar dados de cotação: {e}"

    for Mes_Numero, Dados in Cotacoes_Mes.items():
        Media_Compra = sum(Dados['Compras']) / len(Dados['Compras'])
        Media_Venda = sum(Dados['Vendas']) / len(Dados['Vendas'])
        
        Media_Mensal[Mes_Nome[Mes_Numero]] = {
            "mediaCompra": round(Media_Compra, 3),
            "mediaVenda": round(Media_Venda, 3)
        }

    return Media_Mensal
def main():
# Obter e validar o ano
    Ano_Atual = datetime.datetime.now().year
    while True:
        try:
            Ano = int(input(f"Digite o ano desejado (não pode ser superior a {Ano_Atual}): "))
            if 1999 <= Ano <= Ano_Atual: # Essa API tem coleta de dados desde de 1990
                break
            else:
                print(f"Erro: O ano informado deve estar entre 1999 e {Ano_Atual}.")
        except ValueError:
            print("Erro: Por favor, digite um ano válido (número inteiro).")
# Obter e validar a moeda
    Moedas_Validas = {Moeda['simbolo']: Moeda['nomeFormatado'] for Moeda in dicMoedas['value']}
    print("\n Moedas Disponíveis:")
    for Simbolo, Nome in Moedas_Validas.items():
        print(f"  - {Simbolo}: {Nome}")
    
    while True:
        Moeda = input("\n Digite a sigla da moeda desejada (ex: USD, EUR): ").upper()
        if Moeda in Moedas_Validas:
            break
        else:
            print("Erro: Moeda inválida. Por favor, escolha uma das opções acima.")

    Data_Inicial = f'01-01-{Ano}'
    Data_Final = f'12-31-{Ano}'
# Construção da URL de requisição com os dados do usuário
    strURLCotacoes  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    strURLCotacoes += f'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    strURLCotacoes += f'@moeda=\'{Moeda}\'&@dataInicial=\'{Data_Inicial}\'&@dataFinalCotacao=\'{Data_Final}\'&$format=json'
    try:
        dicCotacoes = requests.get(strURLCotacoes).json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição para a API do Banco Central: {e}")
        return
# Calcular as médias mensais
    Media_Mensal = Calcular_Media_Mensal(dicCotacoes)
    if Calcular_Media_Mensal in Media_Mensal:
        
    if "Erro" in Media_Mensal:
        print(f'Erro: {Media_Mensal}')
        return
# Salvar em arquivo JSON
    nome_arquivo_json = f"medias_cotacoes_{Moeda}_{Ano}.json"
    try:
        with open(nome_arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(Media_Mensal, f, indent=4, ensure_ascii=False)
        print(f"\nArquivo JSON '{nome_arquivo_json}' criado com sucesso!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo JSON: {e}")
# Salvar em arquivo CSV
    Nome_arq_csv = f"medias_cotacoes_{Moeda}_{Ano}.csv"
    try:
        with open(Nome_arq_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['moeda', 'mes', 'mediaCompra', 'mediaVenda'])
            # Ordena os meses para o arquivo CSV
            meses_ordenados = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
                               'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
            for mes in meses_ordenados:
                if mes in Media_Mensal:
                    dados = Media_Mensal[mes]
                    # Formata a saída para o CSV
                    writer.writerow([Moeda, mes, f"{dados['mediaCompra']:.3f}".replace('.',','), f"{dados['mediaVenda']:.3f}".replace('.',',')])
        print(f"Arquivo CSV '{Nome_arq_csv}' criado com sucesso!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

if __name__ == "__main__":
    main()
