# ======================================================
# printtemp.py
# ------------------------------------------------------
# Written by G.D. Walters
# Creation date: 27 January, 2020
# ------------------------------------------------------
# Purpose: Part of the cookbook V3 project
#          Reads a recipe from the database and creates
#          a HTML file.  That file will then be sent to
#          the default web browser for printing.
# ======================================================
# To be perfectly honest, this module is an absolute mess
#    and I'm not happy with it.  However, it's been so many
#    years since I've done HTML, it's a good start.  Many
#    hours of cleanup still do do.
# ======================================================
import os
import platform
import webbrowser
import sqlite3


def getMainRecipeData(rectouse):
    global connection, cursor
    sql = f'SELECT * FROM recipes WHERE idRecipes = {rectouse}'
    mainrec = list(cursor.execute(sql))
    if len(mainrec) > 0:
        return mainrec


def getImageData(rectouse):
    global connection, cursor
    sql = (f'SELECT * FROM images WHERE recipeID = {rectouse}')
    imgrec = list(cursor.execute(sql))
    if len(imgrec) > 0:
        # r = imgrec[0]
        return imgrec


def getIngredientData(rectouse):
    global connection, cursor
    sql = (
        f'SELECT IngredientItem from ingredients WHERE RecipeID = {rectouse}')
    ingRecs = list(cursor.execute(sql))
    if len(ingRecs) > 0:
        return ingRecs


def getInstructionData(rectouse):
    global connection, cursor
    sql = (
        f"SELECT InstructionsData FROM instructions WHERE RecipeID = {rectouse}")
    recs = list(cursor.execute(sql))
    if len(recs) > 0:
        return recs


def getCatData(rectouse):
    global connection, cursor
    sql2 = ("SELECT recipes.idRecipes,"
            "categoriesmain.CatText "
            "FROM recipes "
            "INNER JOIN recipecategories ON "
            "(recipes.idRecipes=recipecategories.RecipeId) "
            "INNER JOIN categoriesmain ON "
            "(recipecategories.MainCatKey=categoriesmain.idCategoriesMain) "
            "WHERE recipes.idRecipes = {0}").format(rectouse)
    cats = list(cursor.execute(sql2))
    if len(cats) > 0:
        return cats


def fix_path():
    global path1
    if "main" in path1:
        pass
    else:
        path1 = path1 + "/main"


def main(inrec=None):
    global version
    version = '0.1.2'
    pv = platform.python_version()
    print(f"Running under Python {pv}")
    # Set the path for the icon files
    global path1
    path1 = os.getcwd()
    fix_path()
    print(path1)
    print(f"Version: {version}")
    global browse 
    browse = webbrowser.get('firefox')
    global connection, cursor
    connection = sqlite3.Connection(path1 + "/database/cookbook-original.db")
    cursor = connection.cursor()
    # ======================================================
    # Set the filename and open the file for writing
    # ======================================================
    filename = './tempprint.html'
    f = open(filename, "w+")
    # ======================================================
    # Get the recipe main record data
    # ======================================================
    if inrec == None:
        reciperec = 144   # Figure out how this will be passed into the module
    else:
        reciperec = inrec
    mainrecs = getMainRecipeData(reciperec)
    if len(mainrecs) > 0:
        # print(mainrecs)
        line = '<html>'
        f.write(line)
        line = '<!-- Thanks to https://projects.raspberrypi.org/en/projects/recipe -->'
        f.write(line)
        line = '<head>'
        f.write(line)
        line = '<link rel="stylesheet" href="style.css">'
        f.write(line)
        # line = f"Greg's Cookbook - Air Fryer Apple Pies - Recipe {reciperec}"
        line = f"Greg's Cookbook - {mainrecs[0][1]} - Recipe ID {reciperec}"
        f.write(line)
        line = '</head>'
        f.write(line)
        line = '<body>'
        f.write(line)
        line = f'<h1>{mainrecs[0][1]}</h1>'
        f.write(line)
        # ======================================================
        # Now write image information
        # ======================================================
        imgdata = getImageData(reciperec)
        # print(imgdata)
        if imgdata != None:
            line = f'<img src="{path1 + imgdata[0][2]}" height="300" width="300">'
            f.write(line)
        # ======================================================
        # Write description information
        # ======================================================
        line = '<!--Description here-->'
        f.write(line)
        line = '<h3>'
        f.write(line)
        # print(mainrecs[0][8])
        if mainrecs[0][8] != None:
            line = f'<i> {str(mainrecs[0][8])} </i>'
            f.write(line)
        line = '</h3>'
        f.write(line)
        # line = '</body>'
        # f.write(line)
        # line = '</html>'
        # f.write(line)
        # ======================================================
        # Source
        # ======================================================
        line = f'<h3>Source: {str(mainrecs[0][2])}</h3>'
        f.write(line)

        # ======================================================
        # Servings, Total Time and ratings
        # ======================================================
        line = '<!-- Servings Total Time Ratings-->'
        f.write(line)
        line = '<div style="float: left; width: 33%;">'
        f.write(line)
        line = '<ul style="list-style-type:none">'
        f.write(line)
        line = '<li>Servings</li>'
        f.write(line)
        if mainrecs[0][3] != None:
            line = f'<li>{str(mainrecs[0][3])}</li>'
        else:
            line = '<li> -- </li>'
        f.write(line)
        line = '</ul>'
        f.write(line)
        line = '</div>'
        f.write(line)
        line = '<div style="float: left; width: 33%;">'
        f.write(line)
        line = '<ul style="list-style-type:none">'
        f.write(line)
        line = '<li>Total Time</li>'
        f.write(line)
        if mainrecs[0][4] != None:
            line = f'<li>{str(mainrecs[0][4])}</li>'
        else:
            line = '<li> -- </li>'
        f.write(line)
        line = '</ul>'
        f.write(line)
        line = '</div>'
        f.write(line)
        line = '<div style="float: right; width: 33%;">'
        f.write(line)
        line = '<ul style="list-style-type:none">'
        f.write(line)
        line = '<li>Ratings</li>'
        f.write(line)
        if mainrecs[0][5] != None:
            line = f'<li>{str(mainrecs[0][5])}</li>'
        else:
            line = '<li> -- </li>'
        f.write(line)
        line = '</ul>'
        f.write(line)
        line = '</div>'
        f.write(line)
        # ======================================================
        # Now for the ingredients and instructions
        # ======================================================
        line = '<!-- Ingredients -->'
        f.write(line)
        line = '<div style="float: left; width: 50%;">'
        f.write(line)
        line = '<h3>Ingredients:</h3>'
        f.write(line)
        line = '<ul>'
        f.write(line)
        # ======================================================
        # Read the ingredients and embed each one in a '<li></li>' bracket
        # ======================================================
        ings = getIngredientData(reciperec)
        if len(ings) > 0:
            for i in ings:
                # print(i[0])
                line = f'<li>{i[0]}</li>'
                f.write(line)
        line = '</ul>'
        f.write(line)
        line = '</div>'
        f.write(line)
        # ======================================================
        # Instructions...
        # ======================================================
        line = "<div style='float: right width: 50%''><h3>Instructions:</h3><ol>"
        f.write(line)
        inst = getInstructionData(reciperec)
        if len(inst) > 0:
            for ins in inst:
                # print(ins)
                line = f'<li>{ins[0]}</li>'
                f.write(line)
        line = '</ol></div>'
        f.write(line)
        line = '</body></html>'
        f.write(line)
        # ======================================================
        # Finish up
        # ======================================================
        f.close()
        # Send it to the default webbrowser
        # webbrowser.open(filename)
        browse.open(filename)


if __name__ == "__main__":
    main()
