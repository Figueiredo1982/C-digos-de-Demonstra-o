def prim(n):
  if n < 2:
    return False
  for i in range (2 int(n** 0,5)+1):
    if n%i == 0:
      return False
  return True
  #Acima a validação sobre o número primeiro

def listando_os_priminhos_pois_no_exemplo_eles_eram_apresentados_em_formato_de_lista(k):
  if not instantece(n, int) or n <= 1:
    print ("K deveria ser um número maior que 1, além de ser um inteiro")
  primos = []
  n = 2
  while len(primos) < n:
    if prim(n):
      primos.append(n)
    k += 1
  return primos

n = input(int("Digite um valor N inteiro maior que 1 : "))
print(f"Os primeiros {k} números primos são: {listando_os_priminhos_pois_no_exemplo_eles_eram_apresentados_em_formato_de_lista(k)}")
    
