grille=[[' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def puissance4(grille):
    for x in range(len(grille)-1, -1, -1):
        for y in range(len(grille[x])-1, -1, -1):
            if grille[x][y]!=' ' :
                if y>=len(grille[0])-4:
                    if grille[x][y]==grille[x][y-1]==grille[x][y-2]==grille[x][y-3]:
                        return True
                if x>=3:
                    if grille[x][y]==grille[x-1][y]==grille[x-2][y]==grille[x-3][y]:
                        return True
                    if y<=len(grille[0])-4 and grille[x][y]==grille[x-1][y+1]==grille[x-2][y+2]==grille[x-3][y+3]:
                        return True
                    if y>=len(grille[0])-4 and grille[x][y]==grille[x-1][y-1]==grille[x-2][y-2]==grille[x-3][y-3]:
                        return True
                else:
                    return False

def placement(grille, tour):
    print(f"joueur {tour%2+1} à toi de jouer !")
    colonne=int(input("Colonne : "))-1
    ligne=ligne_grille(colonne, grille)
    if tour%2==1:
        grille[ligne][colonne]='X'
    else:
        grille[ligne][colonne]='O'

def ligne_grille(colonne, grille):
    ligne=0
    while grille[0][colonne]!=' ':
        colonne=int(input("Colonne Invalide : "))-1
    while ligne<=len(grille)-1 and grille[ligne][colonne]==' ':
        ligne+=1
    return ligne-1

def affichage_numero(grille):
    print()
    largeur = len(grille[0])
    for i in range(1, largeur+1):
        num = str(i)
        k = True
        while len(num) < 5:
            if k:
                num = " " + num
            else:
                num = num + " "
            k = not(k)
        print(" "+num, end="")
    print()

def affichage(grille):
    affichage_numero(grille)
    largeur = len(grille[0])
    print(" "+"_"*(largeur*(6)-1))
    for ligne in grille:
        print("|"+(" "*(5)+"|")*largeur)
        print("|", end="")
        for element in ligne:
            element = str(element)
            k = True
            while len(element) < 3:
                if k:
                    element = " " + element
                else:
                    element = element + " "
                k = not(k)
            print(" "+element+" |", end="")
        print()
        print("|"+("_"*(5)+"|")*largeur)
    affichage_numero(grille)
    print()


if __name__ == '__main__':
    tour=1
    affichage(grille)
    while not puissance4(grille) and tour<43:
        placement(grille, tour)
        affichage(grille)
        tour+=1
    print(f'Bravo joueur {tour%2+1} !')