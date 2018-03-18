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

def feladat_2(n):
    li=[]
    sz=1
    while sz!=0:
        db=1
        for i in range(1,(sz//2)+1):
            if sz%i==0:
                db+=1
        if db==2:
            li.append(sz)
        sz+=1
        if len(li)==n:
            break
    print(li[-1])
def main():
    feladat_2(5)
if __name__ == '__main__':
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

def feladat_4():
    li=[]
    for i in range(100,1000):
        harmadik=i%10
        elso=i//100
        masodik=(i//10)%10
        if elso!=masodik and elso!=harmadik and masodik!=harmadik:
            li.append(i)
    print(li)
def main():
    feladat_4()
if __name__ == '__main__':
    main()

def osztok_szama(szam):
    db=2
    for i in range(2,szam//2+1):
        if szam%i==0:
            db+=1
    return db

def feladat_5(n):
    max_db=1
    for i in range(2,n+1):
        if max_db<osztok_szama(i):
            max_db=osztok_szama(i)
            print(i)
def main():
    feladat_5(4)
if __name__ == '__main__':
    main()

def feladat_6(x,y):
    x_szamjegyek=[]
    y_szamjegyek=[]
    while x>0:
        k=x%10
        if k not in x_szamjegyek:
            x_szamjegyek.append(k)
        x=x//10
    while y>0:
        h=y%10
        if h not in y_szamjegyek:
            y_szamjegyek.append(h)
        y=y//10
    db=0
    for i in x_szamjegyek:
        if i in y_szamjegyek:
            db+=1
    if db>=2:
        print("Rokonok")
    else:
        print("Nem rokonok")
def main():
    feladat_6(444,34)
if __name__ == '__main__':
    main()

def feladat_7(x,y):
    x_szamjegyek=[]
    y_szamjegyek=[]
    while x>0:
        k=x%10
        if k not in x_szamjegyek:
            x_szamjegyek.append(k)
        x=x//10
    while y>0:
        h=y%10
        if h not in y_szamjegyek:
            y_szamjegyek.append(h)
        y=y//10
    db=0
    for i in x_szamjegyek:
        if i in y_szamjegyek:
            db+=1
    if db>=1:
        print("Baratok")
    else:
        print("Nem baratok")
def main():
    feladat_7(444,34)
if __name__ == '__main__':
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

def feladat_12():
    try:
        fajl=open("be1.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        db=1
        for szam in fajl:
            utolso=int(szam[-1])
            k=len(szam)
        for i in range(1,k-1):
            if int(szam[i])==int(szam[i+1]):
                db+=1
        if db>=utolso:
            fajl2.write("Igen tartalmaz")
        elif db!=utolso:
            fajl2.write("Nem tartalmaz")
    except Exception as e:
        print(e)
    fajl.close()
    fajl2.close()
def main():
    feladat_12()
if __name__ == '__main__':
    main()

def feladat_13():
    try:
        fajl1=open("be1.txt",mode="r")
        db=0
        for szam in fajl1:
            szam=szam.strip()
            utolso=int(szam[-1])
            k=len(szam)
        for i in range(0,k-1):
            for j in range(i+1,i+2):
                if abs((int(szam[i])-int(szam[j])))<=utolso:
                    db+=1
        print(db)
    except Exception as e:
        print(e)
    fajl1.close()
def main():
    feladat_13()
if __name__ == '__main__':
    main()

def feladat_15():
    try:
        fajl=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajl:
            if sor=="\n":
                break
            else:
                fajl2.write("%s\n" % (sor.strip()))

    except Exception as e:
        print(e)
    fajl.close()
    fajl2.close()
def main():
    feladat_15()
if __name__ == '__main__':
    main()

def feladat_16():
    try:
        fajl=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajl:
            sor=sor.strip()
            ls=sor.split(" ")
            for i in ls:
                if i[0].isupper() and i[1:].islower():
                    fajl2.write(i)
                    return
    except Exception as e:
        print(e)
    fajl.close()
    fajl2.close()
def main():
    feladat_16()
if __name__ == '__main__':
    main()

def feladat_17():
    try:
        fajl=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajl:
            sor=sor.strip()
            ls=sor.split(" ")
            for i in ls:
                if i.islower():
                    fajl2.write(i)
                    return
    except Exception as e:
        print(e)
    fajl.close()
    fajl2.close()
def main():
    feladat_17()
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

def feladat_20():
    try:
        fajl=open("be1.txt",encoding="UTF-8",mode="r")
        fajl2=open("ki.txt",encoding="UTF-8",mode="w")
        varos=""
        lakos=100000
        for sor in fajl:
            sor=sor.strip()
            v,o,l=sor.split(";")
            if int(l)>int(lakos):
                lakos=l
                varos=v
        fajl2.write(varos)
    except Exception as e:
        print(e)
    fajl.close()
    fajl2.close()
def main():
    feladat_20()
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

def feladat_22():
    try:
        fajl=open("be1.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        nev=""
        eredmeny=1000
        for sor in fajl:
            sor=sor.strip()
            n,o,e=sor.split(";")
            if float(e)<float(eredmeny):
                eredmeny=e
                nev=n
        fajl2.write(nev)
    except Exception as e:
        print(e)
    fajl.close()
    fajl2.close()
def main():
    feladat_22()
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