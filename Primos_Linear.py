def prim(n):
  if n < 2:
    return False
  for i in range (2, int(n** 0.5)+1):
    if n%i == 0:
      return False
  return True
  #Acima a validação sobre o número primo

def listando_os_priminhos_pois_no_exemplo_eles_eram_apresentados_em_formato_de_lista(k):
  if not instantece(k, int) or k <= 1:
    print ("K deveria ser um número maior que 1, além de ser um inteiro")
    return []
  primos = []
  num = 2
  while len(primos) < k:
    if prim(num):
      primos.append(n)
    num += 1
  return primos

k = input(int("Digite um valor N inteiro maior que 1 : "))
print(f"Os primeiros {k} números primos são: {listando_os_priminhos_pois_no_exemplo_eles_eram_apresentados_em_formato_de_lista(k)}")
    
