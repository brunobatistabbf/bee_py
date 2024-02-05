
tipo_1 = input()
tipo_2 = input()
tipo_3 = input()


def tipo_animal(tipo_1, tipo_2, tipo_3):
    
    #vertebrado
    if tipo_1 == "vertebrado":
        if tipo_2 == "ave":
            if tipo_3 == "carnivoro":
                print("aguia")
            elif tipo_3 == "onivoro":
                print("pomba")
            else:
                print("Insira uma palavra válida.")
                return 0
        elif tipo_2 == "mamifero":
            if tipo_3 == "onivoro":
                print("homem")
            elif tipo_3 == "herbivoro":
                print("vaca")
            else:
                print("Insira uma palavra válida.")
                return 0
        else:
            print("Insira uma palavra válida.")
            return 0
    #invertebrado
    elif tipo_1 == "invertebrado":
        if tipo_2 == "inseto":
            if tipo_3 == "hematofago":
                print("pulga")
            elif tipo_3 == "herbivoro":
                print("lagarta")
            else:
                print("Insira uma palavra válida.")
                return 0
        elif tipo_2 == "anelideo":
            if tipo_3 == "hematofago":
                print("sanguessuga")
            elif tipo_3 == "onivoro":
                print("minhoca")
            else:
                print("Insira uma palavra válida.")
                return 0
        else:
            print("Insira uma palavra válida.")
            return 0    
    else:
        print("Insira uma palavra válida.")
        return 0 


tipo_animal(tipo_1, tipo_2, tipo_3)
    