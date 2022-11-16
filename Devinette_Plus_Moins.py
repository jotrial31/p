import random
parties = random.randint(5,10)
reponse2 = ""
parties_gagnees = 0
reponse3 = ""

print(f'\t\t\tBIENVENUE AU JEU DU NOMBRE SECRET !!! \n\nLe nombre de partie est déterminé dès le début aléatoirement. (min-2/max-8) \n')
print(f'Le nombre secret à trouver et le nombre de tentative changent aléatoirement sur chaque partie. \n')
print(f'VOUS avez obtenu {[parties]} parties \n')

while parties != 0 and reponse2 == "oui" or reponse2 == "":
    secret = random.randint(0,10000)
    nbr_essais = random.randint(10,20)
    print(f'IL vous reste {[parties]} partie(s)\n')
    reponse2 = input(f'VOUS ËTES PRËT !? \n[oui] pour continuer / [non] pour quitter : ')
    parties -= 1
    #print(f' Le nombre secret est :  {secret} , il s\'affiche seulement pour faire des tests :) ')
    if reponse2.lower() == "oui":
        while nbr_essais != 0:
            print(f'Tentatives restantes ->{[nbr_essais]} / partie(s) restante(s) -> {[parties]}')  #¤¤¤ [Ceci est le code secret: ->{[secret]}]¤¤¤')
            devinette = int(input(f'DEVINNEZ le nombre secret entre [0 et 10 000] : '))
            nbr_essais -= 1
            if devinette == secret:
                parties_gagnees += 1
                print(f'BRAVO vous avez trouvé !!! \nPartie(s) gagnée(s):{[parties_gagnees]} \nPartie(s) restante(s): {[parties]}')
                reponse2 = input("Voulez-vous rejouer ? ")
                break
            elif nbr_essais > 0 and secret > devinette:
                print(f'¤¤¤¤ [PLUS] ¤¤¤¤')
            else:
                print(f' ¤¤¤¤ [MOINS] ¤¤¤¤')

        else:
            print("PERDU vous n'avez pas réussi à trouver. ")
            print(f'Le nombre secret était {[secret]}')
            reponse2 = input("Voulez-vous retenter votre chance ? : ")
else:
    print(f'¤¤¤¤     [FIN DU GAME]     ¤¤¤¤')
    print(f'vous aviez {[parties]} partie(s)')
    print(f'Vous avez {[parties_gagnees]} partie(s) gagnée(s)')
