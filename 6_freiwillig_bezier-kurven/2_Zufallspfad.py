"""
Zufallspfad
"""
width = width()
height = height()
print("randomWidth", width*random())
randomPoints = [(width*random(), height*random()),
(width*random(), height*random()),
(width*random(), height*random()),
]

stroke(0)
fill(None)

newPath()
moveTo(randomPoints[0])

for xyPoint in randomPoints:
    x = xyPoint[0]
    y = xyPoint[1]
    lineTo((x, y))

closePath()

drawPath()

"""
Versuche das Programm zu verstehen.

Schreibe ein paar weitere beliebige Punktkoordinaten in die Liste randomPoints und erstelle damit ein zufälliges Vieleck (Überschneidungen sind erlaubt).

Bonus: Kannst du die Zufallspunkte auch von Drawbot generieren lassen?

"""