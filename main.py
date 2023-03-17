import bil

looping = True
True #för att avsluta programmet
volvo_svart = bil.Bil("Volvo", "Svart", 5)
Volvo_vit = bil.Bil("Volvo", "Vit" 2)
Daihatsu_grön = bil.Bil("Daihatsu", "grön", 4)

while looping:

    print("-_-")
    print("\n-:BilAutomat:-\n")

    #avslutar proggramet
    go = input("\n Vill du avsluta progrannet? j/n")

    if (go == "j"):
        break