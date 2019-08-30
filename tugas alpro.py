def menu() :

    print("print Opsi Menu\na.Saldo\nb.TOP UP\nc.Pembelian")
    opsi = input("Opsi : ").lower()
    if opsi == "a" :
        print("Saldo Anda Rp. 1.500.000")
    if opsi == "b" :
        x = eval(input("Jumlah TOP UP = "))
        b = 1500000+x
        print("TOP UP SUKSES ~")
        print("TOTAL SALDO = ",b)
    if opsi == "c" :
        y = eval(input("Total Pembelian = "))
        c = 1500000-y
        if y<1500000 :
            print("Pembelian SUKSES ~ ")
            print("Sisa Saldo = ",c)
        if y>1500000 :
            print("Saldo Anda KURANG!")
    print("1.Back\n2.Exit")
    sc = input("pilih short cut = ").lower()
    if sc == "1" :
        menu()
    if sc == "2" :
        print("Good Bye")
menu()
