ipk = float(input("input your IPK :"))
Memakai_telkomsel = input("pengguna telkomsel ? Y/N  :")

if ipk < 4 and ipk > 0 :
        if Memakai_telkomsel == "Y" : 
            if ipk > 3 :
                print ("bonus iphone x ") 
                print ("ipk>3")
            if ipk > 2.5 : 
                print("voucher ps4 ")
            if ipk > 2 and ipk < 2.5 :
                print("voucher menginap di darul tauhid")
                print ("ipk > 2 and ipk < 2.5")
            if ipk < 2 :
                print ("selamat & terimakasih")
                print ("ipk < 2")
        if Memakai_telkomsel == "N" : 
            if ipk > 3 : 
                print("galaxy j series")
                print("ipk > 3")
            if ipk > 2.5 : 
                print("voucher menginap di trans studio mall")
                print("ipk > 2.5")
            if ipk > 2 and ipk < 2.5 :
                print("Kontrol ke psikater")
                print("ipk > 2 and ipk < 2.5")
            if ipk < 2 :
                print ("selamat & terimakasih")
                print("ipk < 2")
else : 
    print("MOHON COBALAGI")    