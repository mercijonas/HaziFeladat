
def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b
    return(a,b)
def main():
    print(feladat_1(8,-6))
if __name__=='__main__':
    main()

def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<2:
        return x*x
    elif x>2:
        return 10
    else:
        return("A függvény nincs értelmezve")


def main():
    print(feladat_3(2))

if __name__=='__main__':
    main()

import math
def feladat_4(a,b,c):
    m=min(a,b,c)
    ab=abs(a)
    bb=abs(b)
    cb=abs(c)
    maxi=max(ab,bb,cb)
    return(m,maxi)
def main():
    print(feladat_4(2,3,-9))

if __name__=='__main__':
    main()

def feladat_5(a,b,c,d):
    if d>=0:
        return(a,c,b,d)
    else:
        return(a,b,d,c)
def main():
    print(feladat_5(2,3,4,5))
if __name__=='__main__':
    main()

import math
def feladat_6(a,b,c):
    while True:
        a=float(a)
        b=float(b)
        c=float(c)
        if a<=0 or b<=0 or c<=0:
            print("Nem megfelelő adatok!")
        else:
            break
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        T=math.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=a*b*c/(4*T)
        print("R=%.2f és r=%.2f" % (R,r))
    else:
        print("Nem képezhetik")
def main():
    print(feladat_6(2,4,5))

if __name__=='__main__':
    main()

def feladat_8(x):
    if x<5:
        fx=3*x-5
    elif x>=5 and x<=10:
        fx=10
    elif x>10:
        fx=9*x+1
    return fx
def feladat_8b(a,b,c,d):
    if a+c>2*d and b>0:
        Eabcd=d-3*b
    elif a+c<2*d and b<0:
        Eabcd=d+3*b
    else:
        Eabcd=4
    return Eabcd



def main():
    print(feladat_8(-3),feladat_8b(2,4,7,9))

if __name__=='__main__':
    main()

def feladat_10(a,b):
    db=0
    for i in range(a,b+1):
        if i%4==0 and i%100!=0 or i%400==0:
            db+=1
            i+=1
    return db
def main():
    print(feladat_10(2001,2034))

if __name__=='__main__':
    main()
