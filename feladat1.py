
def feladat_1(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a, b)


def main():
    print(feladat_1(8, -6))


if __name__ == '__main__':
    main()

def feladat_2():
    a=4
    b=-423
    c=-7
    if a<=b<=c:
        print(a,b,c)
    elif a<=c<=b:
        print(a,c,b)
    elif b<=a<=c:
        print(b,a,c)
    elif b<=c<=a:
        print(b,c,a)
    elif c<=a<=b:
        print(c,a,b)
    elif c<=b<=a:
        print(c,b,a)
def main():
    feladat_2()
if __name__=='__main__':
    main()


def feladat_3(x):
    if x > -2 and x < 0:
        return 2 * x
    elif x >= 0 and x < 2:
        return x * x
    elif x > 2:
        return 10
    else:
        return ("A függvény nincs értelmezve")


def main():
    print(feladat_3(2))


if __name__ == '__main__':
    main()

import math


def feladat_4(a, b, c):
    m = min(a, b, c)
    ab = abs(a)
    bb = abs(b)
    cb = abs(c)
    maxi = max(ab, bb, cb)
    return (m, maxi)


def main():
    print(feladat_4(2, 3, -9))


if __name__ == '__main__':
    main()


def feladat_5(a, b, c, d):
    if d >= 0:
        return (a, c, b, d)
    else:
        return (a, b, d, c)


def main():
    print(feladat_5(2, 3, 4, 5))


if __name__ == '__main__':
    main()

import math


def feladat_6(a, b, c):
    while True:
        a = float(a)
        b = float(b)
        c = float(c)
        if a <= 0 or b <= 0 or c <= 0:
            print("Nem megfelelő adatok!")
        else:
            break
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        T = math.sqrt(p * (p - a) * (p - b) * (p - c))
        r = T / p
        R = a * b * c / (4 * T)
        print("R=%.2f és r=%.2f" % (R, r))
    else:
        print("Nem képezhetik")


def main():
    print(feladat_6(2, 4, 5))


if __name__ == '__main__':
    main()

def feladat_7(hossz,szelesség,drothossz):
    maradek=drothossz-((hossz+szelesség)*2)
    szukseges=drothossz-maradek
    if maradek<0 or szukseges<0:
        print("Nem megfelelő hosszú a drót")
    else:
        print(maradek,szukseges)
def main():
    feladat_7(5,4,16)
if __name__=='__main__':
    main()


def feladat_8(x):
    if x < 5:
        fx = 3 * x - 5
    elif x >= 5 and x <= 10:
        fx = 10
    elif x > 10:
        fx = 9 * x + 1
    return fx


def feladat_8b(a, b, c, d):
    if a + c > 2 * d and b > 0:
        Eabcd = d - 3 * b
    elif a + c < 2 * d and b < 0:
        Eabcd = d + 3 * b
    else:
        Eabcd = 4
    return Eabcd


def main():
    print(feladat_8(-3), feladat_8b(2, 4, 7, 9))


if __name__ == '__main__':
    main()


def feladat_10(a, b):
    db = 0
    for i in range(a, b + 1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            db += 1
            i += 1
    return db


def main():
    print(feladat_10(2001, 2034))


if __name__ == '__main__':
    main()

def feladat_12(pontszám,maximum):
    if maximum*0.6>=pontszám:
        return("Sikeres!")
    else:
        return("Sikertelen!")
def main():
    print(feladat_12(40,60))

if __name__=='__main__':
    main()

def feladat_13(erdemjegy):
    if erdemjegy==5:
        return("Jeles")
    elif erdemjegy==4:
        return("Jó")
    elif erdemjegy==3:
        return("Közepes")
    elif erdemjegy==2:
        return("Elégséges")
    elif erdemjegy==1:
        return("Elégtelen")
    else:
        return("Nincs értelmezve!")
def main():
    print(feladat_13(-3))

if __name__=='__main__':
    main()

def feladat_14(sorszam):
    if sorszam==1:
        return("Január")
    elif sorszam==2:
        return("Február")
    elif sorszam==3:
        return("Március")
    elif sorszam==4:
        return("Április")
    elif sorszam==5:
        return("Május")
    elif sorszam==6:
        return("Június")
    elif sorszam==7:
        return("Július")
    elif sorszam==8:
        return("Augusztus")
    elif sorszam==9:
        return("Szeptember")
    elif sorszam==10:
        return("Október")
    elif sorszam==11:
        return("November")
    elif sorszam==12:
        return("December")
    else:
        return("Nincs ilyen sorszámú hónap!")
def main():
    print(feladat_14(98))

if __name__=='__main__':
    main()

def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados=hanyados+1
        a=a-b
    return hanyados
def main():
    print(feladat_15(9,2))
if __name__=='__main__':
    main()

def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a
def main():
    print(feladat_16(798,312))

if __name__=='__main__':
    main()

def feladat_17(szam):
    masolat=szam
    ujszam=0
    while szam>0:
        szamjegy=szam%10
        ujszam=ujszam*10+szamjegy
        szam=szam//10
    return ujszam==masolat
def main():
    print(feladat_17(12334))

if __name__=='__main__':
    main()


def feladat_18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if x%2==1:
            p=p+y
        else:
            break
        x=x//2
        y=y+y
    return p
def main():
    print(feladat_18(11,68))

if __name__=='__main__':
    main()


import math
def feladat_19(n):
    prim=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            prim=False
            break
    return prim
def main():
    print(feladat_19(109))

if __name__=='__main__':
    main()

def feladat_20(n):
    a=1
    b=1
    k=0
    while k<n:
        print("%.2f" % (a/b),end=" ")
        a=a+b
        b=a-b
        k+=1
def main():
    feladat_20(10)

if __name__=='__main__':
    main()

def feladat_21(n):
    ujszam=0
    while n!=0:
        ujszam=ujszam*10+n%10
        n=n//10
    return ujszam
def main():
    print(feladat_21(28765))

if __name__=='__main__':
    main()

def feladat_22(alap,kitevo):
    eredmeny=1
    while kitevo>0:
        if kitevo%2==1:
            eredmeny=eredmeny*alap
            kitevo-=1
        else:
            break
        alap=alap*alap
        kitevo=kitevo//2
    return eredmeny
def main():
    print(feladat_22(2,3))

if __name__=='__main__':
    main()

def feladat_24():
    szam=int(input("Adj egy számot:"))
    maradek5=0
    maradek7=0
    while szam!=0:
        szam = int(input("Adj egy számot:"))
        if szam%7==5:
            maradek5+=1
        elif szam%13==7:
            maradek7+=1
    return maradek5,maradek7
def main():
    print(feladat_24())
if __name__=='__main__':
    main()

def feladat_25():
    lakosok=int(input("lakosok száma:"))
    terulet=int(input("terület:"))
    nepsuruseg=lakosok//terulet
    if nepsuruseg<=50:
        return (nepsuruseg,"Ritkán lakott terület")
    elif nepsuruseg>=50 and nepsuruseg<300:
        return(nepsuruseg,"Átlagos népsűrűségű")
    else:
        return(nepsuruseg,"Sűrűn lakott terület")
def main():
    print(feladat_25())
if __name__=="__main__":
    main()

def feladat_31():
    n=1000
    for i in range(1,n+1):
        if n%i==0:
            print(i)
            i+=1
def main():
    feladat_31()
if __name__=='__main__':
    main()

def feladat_32(n1,n2,k):
    for i in range(n1,n2):
        if i%k==0:
            print(i)
            i+=1
def main():
    feladat_32(2,23,3)
if __name__=="__main__":
    main()


def feladat_38():
    db=0
    szamjegyek=input("Adjon meg 9 számjegyből alló számot:")
    szam=input("Adjon meg egy számjegyet:")
    for i in szamjegyek[0:10]:
        if szam==i:
            db+=1
        elif len(szamjegyek)>9:
            return("Hibás szám")
        elif szam!=i:
            return ("A számjegy nem fordul elő a számban")
    return db
def main():
    print(feladat_38())
if __name__=='__main__':
    main()
