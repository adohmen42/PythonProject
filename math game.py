# Printing Dictionary Items
highScores = {"Beth" : 1000, "Jack" : 925, "Mike" : 840, "Sarah" : 405}
print(highScores)
print(highScores["Beth"])
 
# Adding and Updating Dictionary Items
highScores["Sarah"] = 1200
print(highScores)
highScores["Kyle"] = 875
print(highScores)
 
# Deleting Dictionary Items
del highScores["Mike"]
print(highScores)
highScores.clear()
print(highScores)
