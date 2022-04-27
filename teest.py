def green(n):
    num = n ** 2
    numlen = len(str(num))
    print(numlen)
    nlen = len(str(n))
    print(nlen)
    part = numlen - nlen
    print(part)
    if num[part:] == n:
        print("green")

def dont_give_me_five(start, end):
    # count the numbers from start to end that don't contain the digit 5
    counter = 0
    num = start
    while num < end:
        if num % 5 != 0 and num % 10 == 0:
            counter += 1
        num += 1
            
        
    return counter

print(dont_give_me_five(1,9))
