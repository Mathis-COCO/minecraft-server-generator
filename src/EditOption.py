import os
import time

def Clear():
    os.system('cls')

def Modification1P(opt1, user_number,option_no_param):
    while True :
        try:
            parameter_chosen = int(input("veuillez choisir une valeur : "))
        except ValueError :
            print ('Valeur invalide')
        else:
            if opt1 < parameter_chosen :
                parameter_chosen = str(parameter_chosen)
                new_parameter = option_no_param[0]+"="+parameter_chosen
                print(new_parameter)
                break
    return new_parameter

def Modification2P(opt1, opt2, user_number,option_no_param):
    while True :
        try:
            parameter_chosen = int(input("veuillez choisir une valeur : "))
        except ValueError :
            print ('Valeur invalide')
        else:
            if opt1 < parameter_chosen <= opt2:
                parameter_chosen = str(parameter_chosen)
                new_parameter = option_no_param[0]+"="+parameter_chosen
                print(new_parameter)
                break
    return new_parameter


def EditOption(serveur):
    i = -2
    server_options = []
    serverPath = "./" + serveur + "/server.properties"
    with open(serverPath,"r") as options :
        for line in sorted(options) :
            i += 1
            if i > 0 :
                print(i," - ", line)
                server_options.append(line)

        change_options = True
        while change_options == True :
            try:
                user_number = int(input("Quelle option souhaitez modifier : "))
            except ValueError :
                Clear()
                print(f"veuillez choisir un nombre compris entre 1 et {i}")
                pass
            else:
                if user_number > i or user_number < 0:
                    Clear()
                    print(f"veuillez choisir un nombre compris entre 1 et {i}")
                    user_number = int(input("Quelle option souhaitez modifier : "))
                user_number -= 1
                change_options == False
                Clear()
                break
        Clear()
        server_options[user_number]
        option_no_param = server_options[user_number].split("=", 1)
        print(f'option choisie   : {option_no_param[0]}')
        parameter_chosen = 'toto'
        parameter = option_no_param[1]
        print(f"paramètre actuel : {parameter}")
        if ('true' in parameter) or ('false' in parameter):
            while True :
                try:
                    parameter_chosen = str(input("veuillez choisir le paramètre true ou false : "))
                except ValueError:
                    print("Paramètre invalide")
                else:
                    parameter_chosen = parameter_chosen.lower()
                    if (parameter_chosen == 'true') or (parameter_chosen == 'false') :
                        new_parameter = option_no_param[0]+"="+parameter_chosen
                        break
        elif ('easy' in parameter) or ('medium' in parameter) or ('hardcore' in parameter) :
            while True :
                try:
                    parameter_chosen = str(input("veuillez choisir le paramètre easy, medium ou hardcore : "))
                except ValueError:
                    print("Paramètre invalide")
                else:
                    parameter_chosen = parameter_chosen.lower()
                    if parameter_chosen == 'easy' or parameter_chosen == 'medium' or parameter_chosen == 'hardcore' :
                        new_parameter = option_no_param[0]+"="+parameter_chosen
                        break
        else:
            if i == 50:
                num_list = [11,13,21,22,23,24,25,26,28,29,32,33,35,39,44,48]
                if user_number in num_list:
                    if 'percentage' in option_no_param[0] :
                        new_parameter = Modification2P(0,100, user_number,option_no_param)
                    if user_number == 13 :
                        new_parameter = Modification2P(0,3, user_number,option_no_param)
                    if (user_number == 32) or (user_number == 39) or (user_number == 35) :
                        new_parameter = Modification2P(0,65535, user_number,option_no_param)
                    if (user_number == 21) or (user_number == 26):
                        new_parameter = Modification2P(0,256, user_number,option_no_param)
                    if (user_number == 22) or (user_number == 23) or (user_number == 24) :
                        new_parameter = Modification1P(0, user_number,option_no_param)
                    if user_number == 28:
                        new_parameter = Modification2P(0,4, user_number,option_no_param)
                    if (user_number == 29) or (user_number == 33) or (user_number == 44) :
                        new_parameter = Modification1P(-1, user_number,option_no_param)
                    if user_number == 48 :
                        new_parameter = Modification1P(0, user_number,option_no_param)
                    if user_number == 25 :
                        parameter_chosen = input("choisir une valeur : ")
                        new_parameter = option_no_param[0]+"="+parameter_chosen
            else :
                while True :
                    try:
                        parameter_chosen = input("veuillez choisir une valeur : ")
                    except ValueError :
                        print ('Valeur invalide')
                    else:
                        parameter_chosen = str(parameter_chosen)
                        new_parameter = option_no_param[0]+"="+parameter_chosen
                        break
        options = open(serverPath,"w+")
        user_number = int(user_number)
        server_options[user_number] = new_parameter+"\n"
        new_options = "#Minecraft server properties\n#date\n"+("".join(map(str, server_options)))
        with open(serverPath,"a") as opt: 
            opt.write(new_options)
        print("parameter changed")
        keep_modifying = " "
        while True :
            try:
                keep_modifying = str(input("Changer d'autres options ? : "))
            except ValueError :
                print('valeur invalide')
            else :
                if "i" in keep_modifying or "u" in keep_modifying :
                    EditOption(serveur)
                return