import sys
if len(sys.argv) == 2:
    doss = sys.argv[1]
    eulafile = "./"+doss+"/eula.txt"
    i=0
    cluf = ""
    with open(eulafile,"r") as file:
        for ligne in file:
            i+=1
            if i != 3:
                cluf+=ligne
    cluf+= "eula=true\n"
    file.close()
    with open(eulafile,"w") as file:
        file.write(cluf)
else:
    print("il n'y a pas le bon nombre d arguments, il en faut un [dossier]")
