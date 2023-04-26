#A sequência de Fibonacci é uma sequência de números tal que qualqer número, exceto o primeiro e o segundo, é a soma dos dois números anteriores.
#fib(n) = fib(n-1) + fib(n-2)

def fibonacci(n):
  if (n == 0):
    return 0
  elif (n == 1):
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

#Testando:
# n = 20
# while(n>=0):
#   print(fibonacci(n))
#   n-=1