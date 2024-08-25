"""
Zufallspfad
"""

randomPoints = [(630, 729),
(106, 874),
(660, 467),
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