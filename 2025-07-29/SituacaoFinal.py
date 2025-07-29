def SituacaoFinal(Media:int, ProvaFinal:int, Reprovado:int):
    if not isinstance(Media, int):
        raise ValueError('Informe media inteiro')
    if Media <0 or Media >100:
        raise Exception('Media deve ser entre 60 e 100')
# Verificando a situação do aluno
    if Media >= 60:
      situacao = 'Aprovado'
    elif Media >= 20:
      situacao = 'Prova Final'
    else:
      situacao = 'Reprovado'
 # Retornando a situacao ao programa
    return situacao