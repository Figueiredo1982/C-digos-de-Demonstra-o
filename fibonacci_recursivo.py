def fib_rec(n):
  if not instance(n, int) or n<0:
    print ("N não pode ser um número negativo")
    return None

if n == 0:
  return 0
elif n == 1:
  return 1

return fib_rec(n-1) + fib_rec(n-2)

n = int(input(Digite um número N maior ou igual a 0 : )
print(f"Resultado de : {n} igual a {fib_rec(n)}")
