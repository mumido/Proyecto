from random import*


def genrnd(n):
    print(n)

n = [randint(-50, 50) for x in range(50)]

print()
genrnd(n)   
print()

def media_del_vector (num):
    suma = 0
    for n in num:
        suma += n

    return suma/len(num)

print(media_del_vector(n))
