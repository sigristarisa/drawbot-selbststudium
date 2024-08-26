"""
Zufallsspektrum
"""

myRandomRange = randint(100, 200)
newPage(myRandomRange, myRandomRange)
diameter = myRandomRange/2
oval(width()-diameter, height()/4, diameter, diameter )

"""
Die Funktion randint() liefert eine zufällige Ganzzahl (ohne Kommastelle) zwischen Wert 1 und Wert 2.

1. Gib in Zeile 5 eigene Zufallsspektren ein.
2. Platziere einen Kreis an zufälliger Position in der rechten Seitenhälfte
"""