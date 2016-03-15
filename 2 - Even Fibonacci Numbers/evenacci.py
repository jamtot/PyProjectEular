def even_fib_sum():
    a = 1
    b = 2
    sum = 0
    while a<4000000 and b<4000000:
        if a%2==0: sum+=a
        if b%2==0: sum+=b
        a = a+b
        b = a+b

    print sum

even_fib_sum()
