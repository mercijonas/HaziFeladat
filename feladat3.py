def feladat_2():
    paros=0
    paratlan=0
    for i in range(1,101):
        if i%2==0:
            paros+=1
        elif i%2==1:
            paratlan+=1
    arany=paros/paratlan
    print(arany)
def main():
    feladat_2()
if __name__ == '__main__':
    main()

def feladat_3(n):
    tomb=[]
    s=0
    for i in range(n):
        szam=int(input("adjon egy szamot:"))
        s+=abs(szam)
    print(s/n)
def main():
    feladat_3(4)
if __name__ == '__main__':
    main()

def feladat_4(n):
    szorzat=1
    szamtani_kozep=0
    negativ_db=0
    for i in range(n):
        szam=int(input('Adjon egy szamot:'))
        if szam%2==0 and szam!=0:
            szorzat=szorzat*szam
        elif szam%2==1:
            szamtani_kozep+=szam
            negativ_db+=1
    print(szorzat,szamtani_kozep/negativ_db)
def main():
    feladat_4(5)
if __name__ == '__main__':
    main()

def feladat_5(n):
    t=[]
    szorzat=1
    osszeg=0
    for i in range(n):
        szam=int(input("Adjon egy szamot:"))
        t.append(szam)
    for i in t:
        if i<7:
            szorzat=szorzat*i
        elif i>10:
            osszeg+=i
    print(szorzat,osszeg)
def main():
    feladat_5(5)
if __name__ == '__main__':
    main()
