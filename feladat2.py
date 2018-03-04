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