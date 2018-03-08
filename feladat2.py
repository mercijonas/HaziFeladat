def feladat_1(x):
    darab=0
    for i in range(1,10000):
        if x%i==0:
            darab+=1
    if darab==4:
        return True
    return False
def main():
    print(feladat_1(16))
if __name__=='__main__':
    main()

def feladat_3(n):
    for i in range(0,10000):
        k=2**i
        if k>=n:
            return k
def main():
    print(feladat_3(513))
if __name__=='__main__':
    main()

def feladat_8(n):
    osszeg=0
    db=0
    for i in range(1,n):
        osszeg+=i
        db+=1
        if osszeg>=n:
            return db
def main():
    print(feladat_8(16))
if __name__=='__main__':
    main()

def feladat_9():
    magassag=1
    perc=0
    while magassag<=300:
        k=2
        magassag=magassag+(1/k)
        k+=1
        perc+=1
    return perc
def main():
    print(feladat_9())
if __name__ == '__main__':
    main()

def feladat_10():
    try:
        fajl=open("be.txt",mode="r")
        maxi=0
        for sor in fajl:
            sor=sor.strip()
            if (sor[0].isupper() and len(sor)>maxi):
                    maxi=len(sor)
        return maxi
    except Exception as e:
        print(e)
    fajl.close()

def main():
    print(feladat_10())
if __name__ == '__main__':
    main()

def feladat_11():
    try:
        fajl=open("be.txt",mode="r")
        mini=10000
        lst="aábccsddzdzseéfggyhiíjkllymnnyoóöőpqrsszttyuúüűvwxyzzs"
        for sor in fajl:
            sor=sor.strip()
            if sor[-1] not in lst and len(sor)<mini:
                    mini=len(sor)
        return mini
    except Exception as e:
        print(e)
    fajl.close()

def main():
    print(feladat_11())
if __name__ == '__main__':
    main()

def feladat_18():
    try:
        fajl1=open("be.txt",mode="r")
        for sor in fajl1:
            ls=sor.split(" ")
            pontok=ls[-1].split(":")
            if int(pontok[0])>int(pontok[1]):
                print(ls[0])
            else:
                print(ls[2])
    except Exception as e:
        print(e)
    fajl1.close()
def main():
    feladat_18()
if __name__ == '__main__':
    main()

