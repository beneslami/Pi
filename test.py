import math
import turtle


def sqrt(n,m):
    m1=10**16
    m2=float((n*m1)//m)/m1
    b=(int(m1*math.sqrt(m2))*m)//m1
    n_m=n*m
    while True:
        a=b
        b=(b+n_m//b)//2
        if b==a:
            break
    return b


def power(n):
    if n==0:
        return 1
    r=power(n//2)
    if n%2==0:
        return r*r
    return r*r*10


def pi():
     m = power(100000)
     c = (640320**3)//24
     n = 1
     Ak = m
     Asum = m
     Bsum = 0
     while Ak != 0 :
          Ak *= -(6*n-5)*(2*n-1)*(6*n-1)
          Ak //= n*n*n*c
          Asum += Ak
          Bsum += n * Ak
          n = n + 1
          result = (426880*sqrt(10005*m,m)*m)//(13591409*Asum+545140134*Bsum)
          return result


if __name__ == "__main__":
    stringPi = str(pi())
    t = turtle.Turtle()
    t.shape("circle")
    t.color("black")
    #t.stamp()
    move = 36
    position = {0: (220.00, 0.00), 1: (177.98, -129.31), 2: (67.98, -209.23), 3: (-67.98, -209.23), 4: (-177.98, -129.31), 5: (-220.00, -0.00), 6: (-177.98, 129.31), 7: (-67.98, 209.23), 8: (67.98, 209.23), 9: (177.98, 129.31)}
    for i in range(10):
        t.penup()
        t.forward(220)
        t.stamp()
        print(t.pos())
        t.home()
        t.right(move)
        move = move + 36
    for i in range(10):
        t.penup()
        t.forward(240)
        t.write(str(i))
        t.home()
        t.right(move)
        move = move + 36

    i = 2
    point1 = position[int(stringPi[1])]
    t.penup()
    while True:
        point2 = position[int(stringPi[i])]
        t.goto(point1)
        t.pendown()
        t.goto(point2)
        point1 = point2
        i += 1

    t.done()