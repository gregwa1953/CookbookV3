#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5a
#  in conjunction with Tcl version 8.6
#    Jan 25, 2020 03:59:42 AM CST  platform: Linux
#    Jan 25, 2020 04:09:27 AM CST  platform: Linux
#    Jan 25, 2020 05:15:04 AM CST  platform: Linux
#    Jan 29, 2020 03:24:16 PM CST  platform: Linux
#    Jan 31, 2020 05:23:26 PM CST  platform: Linux

import sys
from PIL import Image, ImageTk
import os
import platform
import requests
import shutil
import shared
import sqlite3
from dbutils import quote
from ScrolledCheckedListBox import ScrolledCheckedListBox
import cbv3Main
import cbv3Main_support

try:
    import Tkinter as tk
    import tkFileDialog as filedialog
    import tkMessageBox as messagebox
    import tkFont as font
    import tksimpledialog as simpledialog
except ImportError:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import font
    from tkinter import filedialog
    from tkinter import simpledialog

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def set_Tk_var():
    global NewCat
    NewCat = tk.StringVar()
    global RecsNoImages
    RecsNoImages = tk.StringVar()
    RecsNoImages.set('Label')

    global CatCount
    CatCount = tk.StringVar()
    CatCount.set('Label')

    global WorkingRecord
    WorkingRecord = tk.StringVar()
    WorkingRecord.set('Label')

    global RecipeCount
    RecipeCount = tk.StringVar()
    RecipeCount.set('# of Recipes: 9999')


def on_btnDupes():
    print('formDbMaint_support.on_btnDupes')
    sys.stdout.flush()
    # title = "Duplicate Recipe Check"
    # txt = "Sorry, but the Duplicate Check function is not implemented yet."
    # messagebox.showinfo(title, txt)
    w.Scrolledtext1.delete(1.0, tk.END)
    w.Scrolledtext1.insert(tk.END, "Duplicate Recipe Check\n")
    global connection, cursor
    sql = "SELECT RecipeText, COUNT(*) c FROM recipes GROUP BY RecipeText HAVING c > 1"
    results = list(cursor.execute(sql))
    if len(results) > 0:
        for r in results:
            w.Scrolledtext1.insert(
                tk.END, f'RecipeText: {r[0]} - Count: {r[1]} - Records: ')
            sql2 = f'SELECT idRecipes FROM recipes where RecipeText like "%{r[0]}%"'
            ids = list(cursor.execute(sql2))
            if len(ids) > 0:
                w.Scrolledtext1.insert(tk.END, f'{ids}\n')
    else:
        w.Scrolledtext1.insert(tk.END, 'No duplicate records found...')


def on_btnExit():
    print('formDbMaint_support.on_btnExit')
    sys.stdout.flush()
    isok = check_attr(shared, 'remote')
    if isok:
        cbv3Main_support.show_me()
        hide_me()
    else:
        destroy_window()


def on_btnOrphans():
    print('formDbMaint_support.on_btnOrphans')
    sys.stdout.flush()
    # title = "Orphan Record Check"
    # txt = "Sorry, but the Orphan Record Check function is not implemented yet."
    # messagebox.showinfo(title, txt)
    w.Scrolledtext1.delete(1.0, tk.END)
    w.Scrolledtext1.insert(tk.END, "Orphan Check\n")
    global connection, cursor
    sql = 'SELECT idRecipes, RecipeText FROM recipes'
    recipes = list(cursor.execute(sql))
    if len(recipes) > 0:
        orphIngs = []
        orphInst = []
        for r in recipes:
            working = r[0]
            WorkingRecord.set(working)
            sql2 = f"SELECT * FROM ingredients WHERE RecipeID = {working}"
            ings = list(cursor.execute(sql2))
            if len(ings) == 0:
                orphIngs.append(f'Recipe: {working} - {r[1]}')
            sql2 = f"SELECT * FROM instructions WHERE RecipeID = {working}"
            inst = list(cursor.execute(sql2))
            if len(inst) == 0:
                orphInst.append(f'Recipe: {working} - {r[1]}')
    w.Scrolledtext1.insert(tk.END, 'Finished\n\n')
    # print(f'Recipes with no ingredients: {len(orphIngs)}\n')
    w.Scrolledtext1.insert(
        tk.END, f'Recipes with no ingredients: {len(orphIngs)}\n')
    for i in orphIngs:
        # print(i)
        w.Scrolledtext1.insert(tk.END, f'    {i}\n')
    # print(f'Recipes with no instructions: {len(orphInst)}\n')
    w.Scrolledtext1.insert(
        tk.END, f'\nRecipes with no instructions: {len(orphInst)}\n')
    for i in orphInst:
        # print(i)
        w.Scrolledtext1.insert(tk.END, f'    {i}\n')


def on_btnMigrate():
    print('formDbMaint_support.on_btnMigrate')
    sys.stdout.flush()
    title = "Migrate Database"
    txt = "Sorry, but the Migrate Database function is not implemented yet."
    messagebox.showinfo(title, txt)

# ======================================================
# function check_attr()
# ------------------------------------------------------
# When using a shared.py empty module for inter-module
# communications, if the program tries to access a variable that
# hasn't bee defined, it will crash the program with an error.
# This attemps to make it safe.
# ======================================================


def check_attr(module, variable):
    attr = getattr(module, variable, False)
    if attr is False:
        return False
    else:
        return True


def db_start():
    global connection, cursor
    # Get number of records
    sql = "SELECT * from recipes"
    recs = list(cursor.execute(sql))
    rcnt = len(recs)
    RecipeCount.set(f'# of Recipes: {rcnt}')
    # Get number of categories
    sql = "SELECT idCategoriesMain FROM categoriesmain"
    recs = list(cursor.execute(sql))
    numCats = len(recs)
    CatCount.set(numCats)
    # Get number of images
    sql = "SELECT idRecipes, RecipeText FROM recipes"
    recip = list(cursor.execute(sql))
    noimg = 0
    if len(recip) > 0:
        for r in recip:
            rec = r[0]
            sql2 = f"SELECT pkID FROM images WHERE recipeID = {r[0]}"
            images = list(cursor.execute(sql2))
            if len(images) > 0:
                pass
            else:
                noimg += 1
    RecsNoImages.set(noimg)


def start_up():
    global connection, cursor, path1

    connection = sqlite3.Connection(path1 + "/database/cookbook-original.db")
    cursor = connection.cursor()
    # set up for cursors
    global busyCursor, preBusyCursors, busyWidgets
    busyCursor = 'watch'
    preBusyCursors = None
    busyWidgets = (root, )

    set_icon()
    # Centre the screen
    centre_screen(677, 689)
    db_start()


def fix_path():
    global path1
    if "main" in path1:
        pass
    else:
        path1 = path1 + "/main"


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # My init code starts...
    # ======================================================
    global version
    version = '0.1.4'
    pv = platform.python_version()
    print(f"Running under Python {pv}")
    # Set the path for the icon files
    global path1
    path1 = os.getcwd()
    fix_path()
    print(path1)
    print(f"Version: {version}")
    progname = 'Db Maint v' + version
    root.title(progname)
    start_up()

# =================================================================
# cursor stuff
# =================================================================


def busyStart(newcursor=None):
    global preBusyCursors

    if not newcursor:
        newcursor = busyCursor
    newPreBusyCursors = {}
    for component in busyWidgets:
        newPreBusyCursors[component] = component['cursor']
        component.configure(cursor=newcursor)
        component.update_idletasks()
    preBusyCursors = (newPreBusyCursors, preBusyCursors)


def busyEnd():
    global preBusyCursors
    if not preBusyCursors:
        return
    oldPreBusyCursors = preBusyCursors[0]
    preBusyCursors = preBusyCursors[1]
    for component in busyWidgets:
        try:
            component.configure(cursor=oldPreBusyCursors[component])
        except KeyError:
            pass
        component.update_idletasks()


def centre_screen(wid, hei):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (wid/2)
    y = (hs/2) - (hei/2)
    root.geometry('%dx%d+%d+%d' % (wid, hei, x, y))

# =================================================================
# Window stuff
# =================================================================


def show_me():
    root.deiconify()
    # root.attributes("-topmost", True)


def hide_me():
    cbv3Main_support.show_me()
    root.withdraw()


def set_icon():
    # ======================================================
    # Sets the application icon...
    # ======================================================
    shared.p1 = ImageTk.PhotoImage(file=path1 + '/images/chef.png')
    root.tk.call('wm', 'iconphoto', root._w, shared.p1)


def on_btnAdd():
    global connection, cursor
    print('formDbMaint_support.on_btnAdd')
    sys.stdout.flush()
    CatToAdd = NewCat.get()
    sql = f"SELECT CatText FROM categoriesmain where CatText like '%{CatToAdd}%'"
    recs = list(cursor.execute(sql))
    if len(recs) > 0:
        titl = "Add Category"
        msg = "The category you are trying to add already exists"
        messagebox.showerror(titl, msg)
        NewCat.set('')
    else:
        sql = f"INSERT INTO categoriesmain (CatText) VALUES ({quote(CatToAdd)})"
        print(sql)
        cursor.execute(sql)
        connection.commit()
        titl = "Add Category"
        msg = f"{CatToAdd} added successfully."
        messagebox.showinfo(titl, msg)
        NewCat.set('')


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import formDbMaint
    formDbMaint.vp_start_gui()
