from random import*


def genrnd(n):
    print(n)

n = [randint(-50, 50) for x in range(50)]

print()
genrnd(n)   
print()


def producto_gnrnd(n):
    producto = 1

    for num in n:
        producto *= num

    return producto


print (producto_gnrnd(n))
