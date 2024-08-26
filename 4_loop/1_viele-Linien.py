"""
viele Linien
"""
for i in range(100):
 r,g,b = random(), random(), random()
 randomX = random()* width()
 randomY = random()* height()
 randomStrokeWidth = random()* 10
 stroke(r,g,b)
 strokeWidth(randomStrokeWidth)
 line( (width()/2, height()/2), (randomX, randomY))


"""
Aufgabe: 
    – zeichne eine Linie von der Mitte an eine beliebige Position auf der Fläche
    – versuche nun mit einem Loop ganz viele Linien von der Mitte an eine beliebige Position zu zeichnen.
    
    – setze jetzt für alle Linien dieselbe zufällige Farbe
    –  und jetzt für jede Linie eine eigene zufällige Strichstärke
    
"""

