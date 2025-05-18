def prim(num, divisor=None):
  if num < 2:
    return False
  if divisor is None:
    divisor = int(num**0.5)
  if divisor < 2:
    return True
  if num % divisor == 0:
    return False
  return prim(num, divisor-1)

def primos_rec(n, num=2, lista=None):
  if lista is None:
    lista = []
  if len(lista) == n:
    return lista
  if prim(num):
    return primos_rec(n, num+1, lista + [num])
  else :
    return primos_rec(n, num+1, lista)

n = int(input("Digite um valor N inteiro maior que 1 : "))
print(f"Primeiros {n} primos: {primos_rec(n)}")
