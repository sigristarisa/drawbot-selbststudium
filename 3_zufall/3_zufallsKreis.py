"""
Ein Kreis zufälliger Grösse an zufälliger Position.
"""

newPage("A4")

pageWidth = width()
pageHeight = height()
print("pageWidth:", pageWidth, "pageHeight:", pageHeight)

randomDiameter = random() * pageWidth
print("randomDiameter", randomDiameter)
randomX = (pageWidth - randomDiameter) * random()
randomY = (pageHeight - randomDiameter) * random()
print("randomX:", randomX, "randomY", randomY)

oval(randomX, randomY, randomDiameter, randomDiameter)

"""
- Kannst du die Variablen randomX und randomY so ändern, dass der Kreis nie über den Rand der Fläche ragt?
"""