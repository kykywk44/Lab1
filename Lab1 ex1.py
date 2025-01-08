try:
    n = int(input('введите число:'))

    if n>0:
        for i in range(1,n+1):
            print(i)

    if n<0:
        i = 1
        while i!=n-1:
            print(i)
            i = i - 1

except ValueError:
    print('')

