# Die Main Funktion
def main():
   while True:
        intro()
        board = erstelle_spielfeld()
        gebe_spielfeld_aus(board)
        symbol_1, symbol_2 = sym()
        voll(board, symbol_1, symbol_2)

        if not neues_spiel():
            print("Vielen Dank fürs Spielen. Auf Wiedersehen!")
            break


# Die Print Funktion- Willkommen zum Spiel
def intro():
    print("Hallo! Willkommen zum TIC TAC TOE Spiel" + "\n")
    input("Drücke Enter zum Fortfahren." + "\n")


# Die Funktion erstellt ein leeres Spielboard
def erstelle_spielfeld():
    print("Hier ist das Spielfeld: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


# Die Funktion fragt die Spieler nach den Symbolen ab
def sym():
    symbol_1 = input("Möchten Sie X oder O sein? ")
    if symbol_1 == "O":
        symbol_2 = "X"
        print("Du bist O.")
    else:
        symbol_2 = "O"
        print("Du bist X.")
    input("Drücke Enter zum Fortfahren." + "\n")
    return symbol_1, symbol_2


# Die Funktion startet das Spiel
def starte_spiel(board, symbol_1, symbol_2, zaehler):
    spieler = symbol_1 if zaehler % 2 == 0 else symbol_2

    print("Spieler " + spieler + ", es ist deine Reihe. ")
    reihe = int(input("Wähle eine Reihe:"
                      "[letzte Reihe: gebe 0 ein, mittlere Reihe:  --> 1, untere Reihe --> 2]:"))
    spalte = int(input("Wähle eine Spalte:"
                       "[inke Spalte: gebe eine 0 ein, mittlere Spalte --> 1, rechte Spalte --> 2]"))

    while not (0 <= reihe <= 2) or not (0 <= spalte <= 2):
        print("Es kann nur 0, 1 oder 2 ausgewählt werden.")
        reihe = int(input("Wähle eine Reihe:"
                          "[letzte Reihe: gebe 0 ein, mittlere Reihe:  --> 1, untere Reihe --> 2]:"))
        spalte = int(input("Wähle eine Spalte:"
                           "[linke Spalte: gebe eine 0 ein, mittlere Spalte --> 1, rechte Spalte --> 2]"))

    while board[reihe][spalte] in [symbol_1, symbol_2]:
        illegal()
        reihe = int(input("Wähle eine Reihe:"
                          "[letzte Reihe: gebe 0 ein, mittlere Reihe:  --> 1, untere Reihe --> 2]:"))
        spalte = int(input("Wähle eine Spalte:"
                           "[inke Spalte: gebe eine 0 ein, mittlere Spalte --> 1, rechte Spalte --> 2]"))

    if spieler == symbol_1:
        board[reihe][spalte] = symbol_1
    else:
        board[reihe][spalte] = symbol_2
    return board


# Die Prüft ob Spielfeld voll ist
def voll(board, symbol_1, symbol_2):
    zaehler = 1
    gewinner = True

    while zaehler < 10 and gewinner:
        starte_spiel(board, symbol_1, symbol_2, zaehler)
        gebe_spielfeld_aus(board)
        if zaehler == 9:
            print("Das Feld ist voll. Game over.")
            if gewinner:
                print("Sie sind der Gewinner ")
        gewinner = pruefe_auf_gewinner(board, symbol_1, symbol_2)
        zaehler += 1
    if not gewinner:
        print("Game over.")


# Die Print Spielfeld
def gebe_spielfeld_aus(board):
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

# Die prueft auf gewinner
def pruefe_auf_gewinner(board, symbol_1, symbol_2):
    gewinner = True

    # ueberpruefe reihen
    for row in board:
        if not check_line(symbol_1, symbol_2, row):
            gewinner = False

    # Überprüfe Spalten
    for col in zip(*board):
        if not check_line(symbol_1, symbol_2, col):
            gewinner = False

    # Überprüfe Diagonalen
    if not check_line(symbol_1, symbol_2, [board[i][i] for i in range(3)]) or \
            not check_line(symbol_1, symbol_2, [board[i][2 - i] for i in range(3)]):
        gewinner = False

    if board[0][0] == board[1][1] == board[2][2] == symbol_1 or \
            board[0][2] == board[1][1] == board[2][0] == symbol_1:
        gewinner = False
        print("Player " + symbol_1 + ", du hast gewonnen")
    elif board[0][0] == board[1][1] == board[2][2] == symbol_2 or \
            board[0][2] == board[1][1] == board[2][0] == symbol_2:
        gewinner = False
        print("Player " + symbol_2 + ", du hast gewonnen")

    return gewinner

# Die Funktion prueft, o es ein Gewinner gibt, der eine Linie befüllt hat
def check_line(symbol_1, symbol_2, line):
    if all(cell == symbol_1 for cell in line):
        print("Player " + symbol_1 + ", du hast gewonnen")
        return False
    elif all(cell == symbol_2 for cell in line):
        print("Player " + symbol_2 + ", du hast gewonnen")
        return False
    return True

# print Funkion
def illegal():
    print("Ist schon befüllt. Wähle ein neues Feld")

def neues_spiel():
    antwort = input("Möchten Sie ein neues Spiel starten? (ja/nein): ")
   
    return antwort.lower() == 'ja'


main()
