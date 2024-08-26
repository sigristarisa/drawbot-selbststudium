"""
Wörter verteilen
"""

size(300, 300)
lieblingsfilme = ["Before Sunrise", "Blue Valentine", "Enter the Void", "Blue is the Warmest Color"]

for i, film in enumerate(lieblingsfilme):
    print("i", i)
    text(film, (i*random()*150, i*random()*100))

    
    

"""
Aufgabe: 
    - Ergänze die Liste Lieblingsfilme mit Filmen, die du gerne magst. 
    
Warum werden alle Titel übereinander platziert? 
=> weil die X, Y Positionen fix sind
Kannst du sie zufällig auf der Fläche verteilen? 
"""

