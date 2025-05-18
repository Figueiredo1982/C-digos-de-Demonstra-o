#Fibonacci Recursivo
def fib_lin(n):
  if not isinstance(n, int) or n<0:
    print("N não pode ser um número negativo")
    return None
#O uso do isinstance verifica se N é do tipo inteiro, funcionando quase igual a algo como type(x) == int, mas essa última função acaba não funcionando direito quando usada em subclasse
  if n == 0:
    return 0
  elif n == 1:
    return 1
#Acima só foi estabelecido "casos base"

  anterior, atual = 0,1
  for i in range(2, n+1):
    anterior , atual = anterior + atual
  return atual
#Acima, além da declaração de duas variáveis ele vai trabalhar com um simples loop 

n = int(input("Digite um Número de N maior ou igual a 0 : "))
print(f"Resultado de : {n} igual a {fib_lin(n)}")
