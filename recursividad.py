def suma_lista(n):
    
    if len(n)==1:
        return n[0]
    else:
        actual=n.pop()
        return actual+suma_lista(n)
def factorial(n):
         if n == 0:
                  return 1
         else:
                  return n * factorial (n-1)

def main():
    lista=[3,5,2,1]
    print(suma_lista(lista))
    print(factorial(9))

main()
