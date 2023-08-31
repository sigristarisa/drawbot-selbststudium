"""
Gitter
"""

newPage(300, 300)

for i in range(0, width(), 10): 
    print(i)
    stroke(0)
    line((i, 0), (i, height()))
    
    

"""
Frage: 
    - Welchen Koordinaten entspricht i? 
    - Was bewirkt die Variable i in der Funktion line()?
    
Aufgabe: 
    - Schaffst du es mit einem zweiten Loop ein Gittermuster 
      herzustellen? 
"""