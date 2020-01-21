
import sys
import os
import platform
import datetime
import sqlite3
# import shared
# from PIL import ImageTk, Image
# from dbutils import quote

global connection, cursor

global version, path1, progname
pv = platform.python_version()
print(f"Running under Python {pv}")
# Set the path for the icon files
path1 = os.getcwd()
print(path1)
# print(f'Progam Name: {progname}')
# print(f"Version: {version}")
# shared.debug = False

global connection, cursor
connection = sqlite3.Connection("./database/cookbook-original.db")
cursor = connection.cursor()

recnum = 99

sql = "SELECT * FROM recipes WHERE idRecipes = 99"
recs = list(cursor.execute(sql))
print(len(recs))
print(recs[0])
# Get units of measure
sql = "SELECT UOMText from uom"
uomrecs = list(cursor.execute(sql))
print(len(uomrecs))
print(uomrecs)

# sql = "SELECT IngredientItem from ingredients where RecipeID = 99"
# ings = list(cursor.execute(sql))
# print(len(ings))
# print(ings)

checkfor = "chicken"
sql = f"SELECT idIngredients, RecipeID, IngredientItem FROM ingredients WHERE IngredientItem like %'{checkfor}'%"
ings = list(cursor.execute(sql))
for ing in ings:
    # s = ing[0]
    print(ing)

    # print(ing[1])
