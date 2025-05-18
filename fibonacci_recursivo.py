#Fibonacci Recursivo
def fib_rec(n):
  if not instance(n, int) or n<0:
    print ("N não pode ser um número negativo")
    return None

if n == 0:
  return 0
elif n == 1:
  return 1

return fib_rec(n-1) + fib_rec(n-2)
#O maior diferencial do código de Fibonacci linear está acima, essa função é um tanto divertida de pensar o funcionamento
#Ela acaba se utilizando até chegar no caso base de n == 0 e n == 1, e disso retornar o resultado de uma soma para a chamada anterior
#A chamada anterior agora com um valor é utilizada em uma soma, e dependendo do caso, esse resultado é utilizado por uma chamada superior até chegar em quem
#pediu por ela primeiro

n = int(input(Digite um número N maior ou igual a 0 : )
print(f"Resultado de : {n} igual a {fib_rec(n)}")
