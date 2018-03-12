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

def feladat_19():
    try:
        fajl=open("be2.txt",mode="r")
        oldal=[]
        szam=[]
        for sor in fajl:
            sor=sor.strip()
            oldalak,szamok=sor.split(" ")
            oldal.append(oldalak)
            szam.append(int(szamok))
        legnagyobb=1
        for i in szam:
            if i>legnagyobb:
                legnagyobb=i
            elif i==legnagyobb:
                print(oldal[i])
    except Exception as e:
        print(e)
def main():
    feladat_19()
if __name__ == '__main__':
    main()

def feladat_21():
    try:
        fajl=open("be3.txt",mode="r")
        fajl2=open("ki3.txt",mode="w")
        for sor in fajl:
            sor=sor.strip()
            ls=sor.split(";")
            osszeg=0
            utolso=ls[-1]
            for i in ls[1:]:
                i=int(i)
                if i!=utolso:
                    osszeg+=i
            fajl2.write("%s %d \n"% (ls[0],osszeg))
    except Exception as e:
        print(e)
    fajl.close()
    fajl2.close()
def main():
    feladat_21()
if __name__ == '__main__':
    main()

def feladat_23():
    try:
        fajl=open("be.txt",mode="r")
        max=0
        db=0
        sor_db=0
        for szam in fajl:
            szam=int(szam)
            sor_db+=1
            if szam>max:
                max=szam
                db+=1
        if db==sor_db-1:
            print("YES")
        else:
            print("NO")
    except Exception as e:
        print(e)
    fajl.close()
def main():
    feladat_23()
if __name__ == '__main__':
    main()

def feladat_24():
    try:
        fajl=open("be.txt",mode="r")
        li=[]
        uj_li=[]
        osszeg=0
        for sor in fajl:
            sor=sor.strip()
            if " " in sor:
                li=sor.split(" ")
                for i in li:
                    i=int(i)
                    osszeg+=i
                uj_li.append(osszeg)
        teki=uj_li[0]
        csiga=uj_li[1]-uj_li[0]
        if teki>csiga:
            print("%d\n%s" % (2*teki,"TURTLE"))
        elif csiga>teki:
            print("%d\n%s" % (2*csiga,"SNAIL"))
        elif teki==csiga:
            print("%d\n%s" % (2*csiga,"DRAW"))
    except Exception as e:
        print(e)
    fajl.close()
def main():
    feladat_24()
if __name__ == '__main__':
    main()

def feladat_25():
    try:
        fajl=open("szotar.txt",mode="r")
        angol1=[]
        magyar1=[]
        for sor in fajl:
            sor=sor.strip()
            if ":" in sor:
                angol,magyar=sor.split(":")
                angol1.append(angol)
                magyar1.append(magyar)
        angol_db=1
        for i in angol1:
            k=angol1.count(i)
            if k==1:
                angol_db+=1
        magyar_db=1
        for i in magyar1:
            l=magyar1.count(i)
            if l==1:
                magyar_db+=1
        print("%d\n%d" % (angol_db,magyar_db))

    except Exception as e:
        print(e)
    fajl.close()
def main():
    feladat_25()
if __name__ == '__main__':
    main()