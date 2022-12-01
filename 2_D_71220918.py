def kata():
    a = str(input("Masukan kata : "))
    if len(a)%2==0:
        print("Huruf paling ujung pada kata",a,"adalah",a[-3:])
    else:
        print("Huruf paling ujung pada kata",a, "adalah",a[0:3])
kata()
