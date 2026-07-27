def funkprime(n):
    i = 1
    for i in range(2, n):
        i += n
        if n % i == 0:
            return True
        else:
            return False


print(funkprime(4))







        




























