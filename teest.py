from array import array


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

#print(dont_give_me_five(1,9))


 #return sum('5' not in str(i) for i in range(start, end + 1))
#moving zeroes to the end
def move_zeros(array):
    for index, value in enumerate(array):
        if value == 0:
            array.append(value)
            del array[index]
    return array

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))