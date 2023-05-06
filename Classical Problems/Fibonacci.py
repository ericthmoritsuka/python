#A sequência de Fibonacci é uma sequência de números tal que qualquer número, exceto o primeiro e o segundo, é a soma dos dois números anteriores.
#fib(n) = fib(n-1) + fib(n-2)

# Primeira versão com dois casos base.
def fibonacciv1(n):
  if (n == 0):
    return 0
  elif (n == 1):
    return 1
  else:
    return fibonacciv1(n-1) + fibonacciv1(n-2)

# Segunda versão com um caso base (as duas versões são a mesma coisa).
def fibonacciv2(n):
  if (n < 2):
    return n
  else:
    return fibonacciv2(n-1) + fibonacciv2(n-2)

# Terceira versão, otimizada com dicionário para guardar respostas já calculadas e evitar a o recálculo de cada valor a cada chamada:
respostas = {0:0, 1:1}
contador = 0
def fibonacciv3(n):
  if n not in respostas:
    respostas[n] = fibonacciv3(n-1) + fibonacciv3(n-2)
  return respostas[n]

#Testando:
# n = 20
# while(n>=0):
#   print(fibonacci(n))
#   n-=1

#print(fibonacciv3(40))