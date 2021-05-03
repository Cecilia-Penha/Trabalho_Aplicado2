import math
#Trabalho Aplicado 2 - Cecília Penha
#Problema 1
def func(v,x,y):
    f1 = (y*2*v)-(x*2)
    f2 = f1/2
    return f2
v = float(input("digite v:\n"))
x = float(input("digite x:\n"))
y = float(input("digite y:\n"))
r = func(v,x,y)
c = (x*r)*2
print("raio =  ",r,", custo =  ",c)
