def confere_texto(e):
    chochetes = []
    i = 0 
    
    for elemento in e:
        if elemento == ']':
            i = len(chochetes) 
        elif elemento == '[':
            i = 0
        else:
            chochetes.insert(i, elemento)
            i += 1 
    
    resultado = "" 
    for char in chochetes: 
      resultado += char
      
    return resultado
  
while True:
  try:
    entrada = input()
    confere_texto(entrada)
  except EOFError:
    break
