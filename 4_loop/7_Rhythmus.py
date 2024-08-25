"""
Zweierreihe, Dreierreihe
"""

newPage(200, 200)

yPos = 80


for i in range(0, 20, 2):
    xPos = 0
    print(i * 10)    
    rect(xPos, yPos, 10, 10)

 
"""
Der Loop erstellt eine Zweierreihe für i.
Was wird gezeichnet, wenn du die Zweierreihe mit 10 multipliziert an der x-Position einsetzt?
Kannst du oberhalb der Reihe eine weitere Zeile zeichnen, in welcher jedes dritte Feld schwarz ist?
"""