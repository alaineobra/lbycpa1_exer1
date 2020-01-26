# # Author: Al1Paine Marie Robles Obra
# Date: January 22 2020
# Course: LBYCPA1

# Program Description
"""This is my Laboratory Acitivity #4. There are two complex engineering equations
used, namely the Ideal Gas Law and Boyles Law. User will choose which eequation
will be used, and will choose the variable that is being looked for."""




while True:
    menu = False

    # Formula Selection Screen
    print("\n[1] Ideal Gas Law")
    print("[2] Boyles' Law")
    print("[Q] Quit")

    Formula = input("\nPlease select a formula: ")





    # Ideal Gas Law
    if Formula == "1":
        while True:
            if menu:
                break
            print("\nIdeal Gas Law")
            print("\nP V = n R T ")
            print("\nR = 0.0821 L•atm/mol•k")
                
            #Assinging constant
            R = 0.0821

            print("\n[1] Pressure")
            print("[2] Volume")
            print("[3] Number of Moles")
            print("[4] Temperature")
            print("[M] Main Menu")

            IDLVar = input("\nWhat variable would you like to compute? ")

            while True:
                #if Pressure is required
                if IDLVar == "1":
                    Vvar = float(input("V = "))
                    nvar = float(input("n = "))
                    Tvar = float(input("T = "))

                    # Transposed 
                    IDLVar = (nvar * R * Tvar) / Vvar

                    print("\nP =", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break
                

                #if Volume is required
                elif IDLVar == "2":
                    Pvar = float(input("P = "))
                    nvar = float(input("n = "))
                    Tvar = float(input("T = "))

                    # Transposed
                    IDLVar = (nvar * R * Tvar) / Pvar

                    print("\nV =", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break
                

                #if Amount of Substance is required
                elif IDLVar == "3":
                    Pvar = float(input("P = "))
                    Vvar = float(input("V = "))
                    Tvar = float(input("T = "))

                    # Transposed
                    IDLVar = (Pvar * Vvar) / (R * Tvar)

                    print("\nn =", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break
                

                #if Temperature is required
                elif IDLVar == "4":
                    Pvar = float(input("P = "))
                    Vvar = float(input("V = "))
                    nvar = float(input("n = "))

                    # Transposed
                    IDLVar = (Pvar * Vvar) / (R * nvar)

                    print("\nT = ", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break
            
                #if Back
                elif IDLVar == "M":
                    menu = True
                    break

                else:
                    print("\nInput is Invalid!")

        # END OF IDEAL GAS LAW








    # Boyles' Law
    elif Formula == "2":
        while True:
            if menu:
                break
            print("\nBoyles' Law")
            print("\nP1 V1 = P2 V2 ")

            print("\n[1] Pressure1")
            print("[2] Volume1")
            print("[3] Pressure2")
            print("[4] Volume2")
            print("[M] Main Menu")

            IDLVar = input("\nWhat variable would you like to compute? ")

            while True:
                #if Pressure1 is required
                if IDLVar == "1":
                    P2Var = float(input("P2 = "))
                    V1Var = float(input("V1 = "))
                    V2Var = float(input("V2 = "))

                    # Transposed 
                    IDLVar = (P2Var * V2Var) / V1Var

                    print("\nP1=", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break
                

                #if Volume1 is required
                elif IDLVar == "2":
                    P1Var = float(input("P1 = "))
                    P2Var = float(input("P2 = "))
                    V2Var = float(input("V2 = "))

                    # Transposed 
                    IDLVar = (P2Var * V2Var) / P1Var

                    print("\nV1=", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break
                

                #if Pressure2 is required
                elif IDLVar == "3":
                    P1Var = float(input("P1 = "))
                    V1Var = float(input("V1 = "))
                    V2Var = float(input("V2 = "))

                    # Transposed 
                    IDLVar = (P1Var * V1Var) / V2Var

                    print("\nP2=", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break

                #if Volume2 is required
                elif IDLVar == "4":
                    P1Var = float(input("P1 = "))
                    P2Var = float(input("P2 = "))
                    V1Var = float(input("V1 = "))

                    # Transposed 
                    IDLVar = (P1Var * V1Var) / P2Var

                    print("\nV2=", IDLVar)

                    print("\n[N] New variable\n[Q] Quit")

                    NewVar = input("\nWhat do you want to do? ")

                    if NewVar == "N":
                        break
                    elif NewVar == "Q":
                        break
                        quit
                    else: 
                        print("\nInput is Invalid!")
                        break

                #if Back
                elif IDLVar == "M":
                   menu = True
                   break
                
                else:
                    print("\nInput is Invalid!")
                # END OF BOYLES LAW



    elif Formula == "Q":
        print("Thank you!")
        break 
    
    else:
        print("\nInput is Invalid!")