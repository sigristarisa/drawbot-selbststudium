"""
Kurve berechnen
"""
stroke(0)
strokeWidth(3)
fill(None)

newPath()
moveTo((100, 100))
curveTo((300, 300),(500, 700), (900, 100))
drawPath()


"""
Die Funktion newPath() generiert einen neuen Pfad, zeichnet aber noch nichts. 
moveTo() setzt den Startpunkt.
curveTo() beschreibt die Kurve zum Endpunkt (letztes Zahlenpaar) und die zwei Griffe.

Kannst du die Kurve über die Koordinaten der Griffe runder machen?
"""