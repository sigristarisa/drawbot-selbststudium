"""
Gitter
"""

newPage(300, 300)

for i in range(0, width(), 10): 
    print(i)
    stroke(0)
    line((i, 0), (i, height()))
    
for i in range(0, height(), 10): 
    print(i)
    stroke(0)
    line((0, i), (width(), i))
    
    

"""
Frage: 
    - Welchen Koordinaten entspricht i? 
    => x-Position
    - Was bewirkt die Variable i in der Funktion line()?
    => die Startpunkt und Endpunkt von X-Positionen
    
Aufgabe: 
    - Schaffst du es mit einem zweiten Loop ein Gittermuster 
      herzustellen? 
"""