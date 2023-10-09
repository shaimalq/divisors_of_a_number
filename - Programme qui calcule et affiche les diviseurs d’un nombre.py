n=int(input("entrer un nombre:"))
if n>0:
    for i in range (1,n+1):
     if n% i==0:
        print("les diviseurs de",n, "sont",i)
else:
    print("entrer un nombre positif")