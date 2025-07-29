def mediaIFRN(Nota1:int, Nota2:int):
    if not isinstance(Nota1, int):
        raise ValueError('Informe Nota1 inteiro')
    if not isinstance(Nota2, int):
        raise ValueError('Informe Nota2 inteiro')
    
    if Nota1 <0 or Nota1 >100:
        raise Exception('Nota1 deve ser entre 0 e 100')
    if Nota2 <0 or Nota2 >100:
        raise Exception('Nota2 deve ser entre 0 e 100')
    media = (Nota1 *2 + Nota2 *3) /5
    return int(round(media, 0))
