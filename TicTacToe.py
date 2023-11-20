# Die Main Funktion
def main():
    intro()
    board = erstelle_Spielfeld()
    gebe_Spielfeld_aus(board)
    symbol_1, symbol_2 = symbol_abfragen()
    board_voll(board, symbol_1, symbol_2)

# Die Funktion stellt die Spielregel vor 
def intro():
    print("Hallo! Willkommen zum TIC TAC TOE Spiel" + "\n")
    input("Drücke enter zum fortfahren." + "\n")

# Die Funktion erstellt ein leeres Spielboard
def erstelle_Spielfeld():
    print("Hier ist das Spielfeld: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

# Die Funktion fragt die Spieler nach den Symbolen ab
def symbol_abfragen():
    symbol_1 = input("Möchten Sie X oder O sein ? ")
    if symbol_1 == "0":
        symbol_2 = "X"
        print("Du bist O. ")
    else:
        symbol_2 = "0"
        print("Du bist X. ")
    input("Drücke enter zum fortfahren." + "\n")
    return symbol_1, symbol_2


# Die Funktion startet das Spiel
def starte_Spiel(board, symbol_1, symbol_2, zaehler):
    spieler=0
    
    if zaehler % 2 == 0:
        spieler = symbol_1
    elif zaehler % 2 == 1:
        spieler = symbol_2
    print("Spieler "+ spieler + ", es ist deine Reihe. ")
    reihe = int(input("Wähle eine Reihe:"
                    "[letzte reihe: gebe 0 ein, mittlere Reihe:  gebe 1 ein, untere Reihe:  gebe 2 ein]:"))
    spalte = int(input("Wähle eine Spalte:"
                       "[linke Spalte: gebe eine 0 ein, mittlere Spalte gebe eine 1 ein, rechte Spalte gebe eine 2 ein]"))
    
    while (reihe > 2 or reihe < 0) or (spalte > 2 or spalte < 0):
        print("Es kann nur 0,1 oder 2 ausgewählt werden ")
        reihe = int(input("Wähle eine Reihe:"
                    "[letzte reihe: gebe 0 ein, mittlere Reihe:  gebe 1 ein, untere Reihe:  gebe 2 ein]:"))
        spalte = int(input("Wähle eine Spalte:"
                       "[linke Spalte: gebe eine 0 ein, mittlere Spalte gebe eine 1 ein, rechte Spalte gebe eine 2 ein]"))
        
    while (board[reihe][spalte] == symbol_1)or (board[reihe][spalte] == symbol_2):
        print("Ist schon befüllt. Wähle ein neues Feld")
        reihe = int(input("Wähle eine Reihe:"
                    "[letzte reihe: gebe 0 ein, mittlere Reihe:  gebe 1 ein, untere Reihe:  gebe 2 ein]:"))
        spalte = int(input("Wähle eine Spalte:"
                       "[linke Spalte: gebe eine 0 ein, mittlere Spalte gebe eine 1 ein, rechte Spalte gebe eine 2 ein]"))  
    
    if spieler == symbol_1:
        board[reihe][spalte] = symbol_1     
    else:
        board[reihe][spalte] = symbol_2
    return board

# Prüft ob das Feld voll ist
def board_voll(board, symbol_1, symbol_2):
    zaehler=1
    gewinner = True

    while zaehler < 10 and gewinner:
        starte_Spiel(board, symbol_1, symbol_2, zaehler)
        gebe_Spielfeld_aus(board)  
        if zaehler == 9:
            print("Das Feld ist voll. Game over.")
            if gewinner:
                print("Sie sind der Gewinner ")
    
        gewinner=pruefe_auf_Gewinner(board, symbol_1, symbol_2, zaehler)
        zaehler += 1
    if not gewinner:
        print("Game over.")

    
# Gebe das Board aus
def gebe_Spielfeld_aus(board):
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board


# Prüft ob es ein Gewinner gibt
def pruefe_auf_Gewinner(board, symbol_1, symbol_2, count):
    gewinner = True
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            gewinner = False
            print("Player " + symbol_1 + ", du hast gewonnen")
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            gewinner = False
            print("Player " + symbol_2 + ", du hast gewonnen")     
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            gewinner = False
            print("Player " + symbol_1 + ", du hast gewonnen")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            gewinner = False
            print("Player " + symbol_2 + ", du hast gewonnen")
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        gewinner = False 
        print("Player " + symbol_1 + ", du hast gewonnen")
    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        gewinner = False
        print("Player " + symbol_2 + ", du hast gewonnen")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        gewinner = False
        print("Player " + symbol_1 + ", du hast gewonnen")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        gewinner = False
        print("Player " + symbol_2 + ", du hast gewonnen")
    return gewinner


main()

 