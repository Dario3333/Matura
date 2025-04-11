import random
import csv


def dice_roll():
    """Simuliert einen Würfelwurf mit zwei sechsseitigen Würfeln."""
    return random.randint(1, 6) + random.randint(1, 6)


def auswertung(ergebnis, passline, dpassline, come, come_active, balance):
    """Berechnet den Gewinn basierend auf den Wetten."""

    # Pass-Line-Wette
    if ergebnis == 1:
        balance += passline * 2  # Gewinn
    else:
        balance += dpassline * 2  # Don't-Pass gewinnt stattdessen

    # Come-Wette auswerten
    if come_active == "win":  # Falls die Come-Wette direkt gewinnt
        balance += come * 2
    elif come_active == "lose":  # Falls sie direkt verliert
        balance -= come
    elif come_active == "point_win":  # Falls der Come-Point getroffen wird
        balance += come * 2
    elif come_active == "point_lose":  # Falls eine 7 kommt, bevor der Come-Point getroffen wird
        balance -= come

    return balance


def game(passline, dpassline, come, balance):
    """Simuliert ein Spiel mit Pass-Line- und Come-Wetten."""
    
    sum = dice_roll()
    come_active = None  # Status der Come-Wette (win, lose, point, etc.)
    come_point = None  # Speichert den Punkt für die Come-Wette

    # **Erster Wurf (Come-Out Roll)**
    if sum in (7, 11):
        ergebnis = 1  # Pass-Line gewinnt sofort
    elif sum in (2, 3, 12):
        ergebnis = 0  # Pass-Line verliert sofort
    else:
        point = sum  # Der geworfene Wert wird der "Point"
        s2 = 0

        # **Come-Wette setzen**
        come_roll = dice_roll()

        if come_roll in (7, 11):
            come_active = "win"  # Sofortiger Gewinn für die Come-Wette
        elif come_roll in (2, 3, 12):
            come_active = "lose"  # Sofortiger Verlust für die Come-Wette
        else:
            come_point = come_roll  # Der geworfene Wert wird der "Come-Point"

        # **Phase 2: Shooter würfelt weiter, bis Point oder 7**
        while s2 != point and s2 != 7:
            s2 = dice_roll()

            # Falls eine aktive Come-Wette existiert, prüfen
            if come_point is not None:
                if s2 == come_point:
                    come_active = "point_win"  # Come-Wette gewinnt
                    come_point = None  # Come-Wette abgeschlossen
                elif s2 == 7:
                    come_active = "point_lose"  # Come-Wette verliert

        ergebnis = 0 if s2 == 7 else 1  # 7 verliert, Point gewinnt

    return auswertung(ergebnis, passline, dpassline, come, come_active, balance)


def crapsmontecarlo(iterationen, filename="craps_results.csv"):
    wins = 0
    losses = 0
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Versuch", "Ergebnis", "Come Bet Aktiv", "Come Bet Ergebnis"])
        
        for i in range(1, iterationen + 1):
            balance = 0
            passline = random.randint(0, 1)  # 50% Chance für Pass-Line-Wette
            dpassline = 1 if passline == 0 else 0  # Don't Pass ist das Gegenteil
            come = random.randint(0, 1)  # 50% Chance, eine Come-Wette zu setzen

            balance = game(passline, dpassline, come, balance)  # Jetzt mit Come-Bets
            print(balance) 

            if balance > 0:  # Gewinn
                wins += 1
                writer.writerow([i, "win", come])
            else:  # Verlust
                losses += 1
                writer.writerow([i, "loss", come,])
    
    print("You won", wins, "times and lost", losses, "times")
    print("You won", (wins / iterationen) * 100, "% of your games")




