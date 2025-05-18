#Fibonacci Recursivo
def fib_rec(n):
  if not isinstance(n, int) or n<0:
    print("N não pode ser um número negativo")
#O uso do isinstance verifica se N é do tipo inteiro, funcionando quase igual a algo como type(x) == int, mas essa última função acaba não funcionando direito quando usada em subclasse
  if n == 0:
    return 0
  elif n == 1:
    return 1
#Acima só foi estabelecido "casos base"

  a,b = 0,1
  for i in range(2, n+1):
    
