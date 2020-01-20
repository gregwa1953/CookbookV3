#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.27m
#  in conjunction with Tcl version 8.6
#    Jan 13, 2020 04:06:44 PM CST  platform: Linux
#    Jan 14, 2020 02:55:15 PM CST  platform: Linux
#    Jan 15, 2020 03:17:23 AM CST  platform: Linux
#    Jan 15, 2020 03:47:02 AM CST  platform: Linux
#    Jan 15, 2020 05:33:34 AM CST  platform: Linux
#    Jan 19, 2020 07:01:49 PM CST  platform: Linux
#    Jan 19, 2020 08:00:03 PM CST  platform: Linux

import sys
import os
import platform
import datetime
import sqlite3
import shared
from PIL import ImageTk, Image
from dbutils import quote

# try:
#     import Tkinter as tk
# except ImportError:
#     import tkinter as tk
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
    global IdLableShow
    IdLableShow = tk.StringVar()
    IdLableShow.set('Label')

    global selectedButton
    selectedButton = tk.IntVar()
    global che46
    che46 = tk.IntVar()
    global EntryText
    EntryText = tk.StringVar()
    global TimeDisp
    TimeDisp = tk.StringVar()
    TimeDisp.set('Label')

    global RecipeTitle
    RecipeTitle = tk.StringVar()
    RecipeTitle.set('Label')

    global RecipeSource
    RecipeSource = tk.StringVar()
    RecipeSource.set('Label')

    global RecipeServings
    RecipeServings = tk.StringVar()
    RecipeServings.set('Label')

    global RecipeNotes
    RecipeNotes = tk.StringVar()
    RecipeNotes.set('Message')

    global RecipeCategories
    RecipeCategories = tk.StringVar()
    RecipeCategories.set('Message')

    global Title
    Title = tk.StringVar()
    Title.set('Label')
    global Source
    Source = tk.StringVar()
    Source.set('Label')
    global Servings
    Servings = tk.StringVar()
    Servings.set('Label')
    global Notes
    Notes = tk.StringVar()
    Notes.set('Message')

def on_btnScrape():
    if shared.debug:
        print('cbv3Main_support.on_btnScrape')
        sys.stdout.flush()

def on_chkClick():
    if shared.debug:
        print('cbv3Main_support.on_chkClick')
        sys.stdout.flush()

def on_btnAdd():
    if shared.debug:
        print('test3_support.on_btnAdd')
        sys.stdout.flush()
    title = "Add New Recipe"
    msg = "Sorry, but the Add New Recipe function is not yet complete"
    messagebox.showinfo(title, msg)

def on_btnDelete():
    if shared.debug:
        print('test3_support.on_btnDelete')
        sys.stdout.flush()
    title = "Delete Recipe"
    msg = "Sorry, but the Delete Recipe function is not yet complete"
    messagebox.showinfo(title, msg)

def on_btnEdit():
    if shared.debug:
        print('test3_support.on_btnEdit')
        sys.stdout.flush()
    title = "Edit Recipe"
    msg = "Sorry, but the Edit Recipe function is not yet complete"
    messagebox.showinfo(title, msg)

def on_btnExit():
    if shared.debug:
        print('cbv3Main_support.on_btnExit')
        sys.stdout.flush()
    destroy_window()

def on_rbClick():
    # ======================================================
    # Handles sorting of recipes by Title, Ingredients and Category
    # ======================================================
    if shared.debug:
        print('test3_support.on_rbClick')
        sys.stdout.flush()
    which = selectedButton.get()
    if shared.debug:
        print(which)
    if which == 0:
        # Title
        w.Entry1.configure(state='disabled')
        tv_fill_title()

    elif which == 1:
        # Ingredient
        w.Entry1.configure(state='normal')

    elif which == 2:
        # Category
        w.Entry1.configure(state='disabled')
        tv_fill_cats()

    else:
        pass

def on_TV_Click(e):
    if shared.debug:
        print('On_TV_Click')
    global CurrentID
    if (shared.tv_mode == 1) or (shared.tv_mode == 3):
        row = w.Scrolledtreeview1.identify_row(e.y)
        col = w.Scrolledtreeview1.identify_column(e.x)
        # print(f'Row: {row}  Col: {col}')
        # title = w.Scrolledtreeview1.set(row, 0)
        CurrentID = w.Scrolledtreeview1.set(row, 1)
        # print(f'Title: {title} CurrentID: {CurrentID}')
        load_form(CurrentID)
    elif shared.tv_mode == 2:
        row = w.Scrolledtreeview1.identify_row(e.y)
        col = w.Scrolledtreeview1.identify_column(e.x)
        # print(type(col))
        # print(f'Row: {row}  Col: {col}')
        if col != '#1':
            pass
        else:
            # print(f'Row: {row}  Col: {col}')
            # title = w.Scrolledtreeview1.set(row, 1)
            CurrentID = w.Scrolledtreeview1.set(row, 1)
            # clear_labels()
            clear_form()
            # print(f'Title: {title} CurrentID: {CurrentID}')
            # set_labels()
            load_form(CurrentID)

def on_time_update():
    # ======================================================
    # Callback function for the Time display
    # ======================================================
    global timer_id
    nowstring = (f"{datetime.datetime.now():%X}")
    TimeDisp.set(nowstring)
    timer_id = root.after(500, on_time_update)

def on_Entry_Return(e):
    if e.keysym == 'Return':
        if shared.debug:
            print('Return key press in w.Entry1')
            print(f'Text entered = {EntryText.get()}')
        tv_fill_ingreds(EntryText.get())

def update_tree(e):
    if shared.debug:
        print('Update_Tree')
    # global CurrentID
    # row = w.Scrolledtreeview1.identify_row(e.y)
    # col = w.Scrolledtreeview1.identify_column(e.x)
    # print(f'Row: {row}  Col: {col}')
    # title = w.Scrolledtreeview1.set(row, 0)
    # CurrentID = w.Scrolledtreeview1.set(row, 1)
    # print(f'Title: {title} CurrentID: {CurrentID}')
    # # fill_form

def clear_main_treeview():
    for i in w.Scrolledtreeview1.get_children():
        w.Scrolledtreeview1.delete(i)
    # clear_labels()

def clear_form():
    # Main recipe info
    RecipeTitle.set('')
    RecipeSource.set('')
    RecipeServings.set('')
    RecipeCategories.set('')
    # Instructions
    w.Scrolledtext1.delete('1.0', tk.END)
    # Ingredients
    w.Scrolledlistbox1.delete(0, tk.END)
    # Image

def load_form(id):
    global connection, cursor
    clear_form()
    # set_labels()
    IdLableShow.set(id)

    sql = (f"SELECT * FROM recipes WHERE recipes.idRecipes = {id}")
    # print(sql)
    recs = list(cursor.execute(sql))
    for r in recs:
        # curid = r[0]
        RecipeTitle.set(r[1])
        RecipeSource.set(r[2])
        RecipeServings.set(r[3])
    # ======================================================
    # Load the ingredients
    # if int(id) < 90:
    #     sql = (
    #         f"SELECT IngredientQty, IngredientUnit, IngredientData FROM ingredients WHERE RecipeID = {id}")
    #     ingreds = list(cursor.execute(sql))
    #     if len(ingreds)>0:
    #         for i in ingreds:
    #             # print(f'I Type: {type(i)} Len: {len(i)} I: {i}')
    #             line = (" ".join(i))
    #             # print(line)
    #             w.Scrolledlistbox1.insert('end', line)
    # else:
    sql = (f'SELECT IngredientItem from ingredients WHERE RecipeID = {id}')
    ingreds = list(cursor.execute(sql))
    # ingreds = cursor.execute(sql)
    if len(ingreds):
        for i in ingreds:
            # print(type(i))
            print(str(i[0]))
            w.Scrolledlistbox1.insert('end', str(i[0]))
    # ======================================================
    # Load the instructions
    sql = (f"SELECT InstructionsData FROM instructions WHERE RecipeID = {id}")
    recs = list(cursor.execute(sql))
    for r in recs:
        w.Scrolledtext1.insert(tk.END, r[0])
    # ======================================================
    # RecipeCategories
    sql2 = ("SELECT recipes."
            "idRecipes, "
            "categoriesmain.CatText "
            "FROM recipes "
            "INNER JOIN recipecategories ON "
            "(recipes.idRecipes=recipecategories.RecipeId) "
            "INNER JOIN categoriesmain ON "
            "(recipecategories.MainCatKey=categoriesmain.idCategoriesMain) "
            "WHERE recipes.idRecipes = {0}").format(id)
    cats = list(cursor.execute(sql2))
    if len(cats):
        catnames = ""
        icount = 1
        for cat in cats:
            if icount < len(cats):
                catnames = catnames + cat[1] + ", "
            else:
                catnames = catnames + cat[1]
            icount += 1
        RecipeCategories.set(catnames)
    # image
    global _img2
    sql = f"SELECT * from images where recipeID = {id}"
    recs = list(cursor.execute(sql))
    if len(recs):
        for r in recs:
            path = r[2]
            if shared.debug:
                print(path)
            original = Image.open(path)
            wid, hei = original.size
            if shared.debug:
                print(f'Width: {wid} - Height: {hei}')
            if wid >= hei:
                ratio = 300.0/wid
                if shared.debug:
                    print(ratio)
                w2 = wid * ratio
                h2 = hei * ratio
            else:
                ratio = 300./hei
                if shared.debug:
                    print(ratio)
                w2 = wid * ratio
                h2 = hei * ratio
            if shared.debug:
                print(f'New Width = {int(w2)} - New Height = {int(h2)}')
            # global _img2
            _img1 = original.resize((int(w2), int(h2)), Image.ANTIALIAS)
            _img2 = ImageTk.PhotoImage(_img1)
            w.lblImage.configure(image=_img2)
    else:
        global _img3
        #_img2 = None
        # w.lblImage.configure(image=None)
        img = Image.open('./images/NoImage.png')
        _img3 = ImageTk.PhotoImage(img)
        w.lblImage.configure(image=_img3)
        # w.lblImage.configure(text='Image not available')
    RecipeNotes.set('No description available')

def clear_labels():
    w.Label2.configure(text='')
    w.Label3.configure(text='')
    w.Label5.configure(text='')
    w.Label5.configure(text='')
    w.Label7.configure(text='')

def set_labels():
    w.Label2.configure(text='''Recipe Source:''')
    w.Label3.configure(text='''Recipe Servings:''')
    w.Label5.configure(text='''Ingredients:''')
    w.Label5.configure(text='''Instructions:''')
    w.Label7.configure(text='''Categories''')

def tree_close(e):
    # clear_labels()
    pass
    # print('Tree_close')

def tree_open(e):
    # print('Tree_open')
    global first
    if shared.tv_mode == 1:
        tree = w.Scrolledtreeview1
        tree.focus(first)
        tree.selection_set(first)
        # print(f'first: {first}')
        # title = w.Scrolledtreeview1.set(first, 0)
        CurrentID = w.Scrolledtreeview1.set(first, 1)
        # set_labels()
        load_form(CurrentID)

def populate_tree(tree, node):
    global first
    if shared.tv_mode == 1:
        recs = load_base_recipes()
    elif shared.tv_mode == 3:
        recs = load_ingredient_list()
    # nd = tree.item(node)
    cntr = 0
    for r in recs:
        title = r[1]
        recid = r[0]
        id = tree.insert(node, 2, values=(title, recid))
        if cntr == 0:
            first = id
        cntr += 1
    tree.item(node, open=True)
    tree.focus(first)
    tree.selection_set(first)
    # print(f'first: {first}')
    # title = w.Scrolledtreeview1.set(first, 0)
    CurrentID = w.Scrolledtreeview1.set(first, 1)
    load_form(CurrentID)

def load_base_recipes():
    global connection, cursor
    sql = "SELECT * from recipes"    # order by RecipeText ASC"
    recs = list(cursor.execute(sql))
    if len(recs):
        return(recs)

def init_tree(tree):
    # global folder
    tree["columns"] = ("Recipe", "Recid")
    tree.column('#0', width=40, stretch=tk.NO)
    tree.column('Recipe', width=400, stretch=tk.NO)
    tree.column("Recid", width=100, stretch=tk.NO)
    tree.heading('#0', text='', anchor=tk.W)
    tree.heading('Recipe', text='Recipe', anchor=tk.W)
    tree.heading('Recid', text='Recid', anchor=tk.W)

    node = tree.insert('', 1, text='', image=shared.folder)
    populate_tree(tree, node)

def setup_treeview():
    w.Scrolledtreeview1.bind('<<TreeviewSelect>>',
                             lambda e: update_tree(e))
    w.Scrolledtreeview1.bind('<<TreeviewOpen>>',
                             lambda e: tree_open(e))
    w.Scrolledtreeview1.bind('<<TreeviewClose>>',
                             lambda e: tree_close(e))
    w.Scrolledtreeview1.bind('<Button-1>', lambda e: on_TV_Click(e))
    init_tree(w.Scrolledtreeview1)

def tv_fill_title():
    clear_main_treeview()
    shared.tv_mode = 1
    setup_treeview()

def tv_fill_cats():
    tree = w.Scrolledtreeview1
    clear_main_treeview()
    clear_form()
    shared.tv_mode = 2
    tree["columns"] = ("Recipe", "Recid")
    tree.column('#0', width=150, stretch=tk.NO, anchor=tk.W)
    tree.column('Recipe', width=400,
                stretch=tk.NO, anchor=tk.W)
    tree.column("Recid", width=100,
                stretch=tk.NO, anchor=tk.W)
    tree.heading('#0', text='Category', anchor=tk.W)

    tree.heading('Recipe', text='Recipe', anchor=tk.W)
    tree.heading('Recid', text='Recid', anchor=tk.W)
    tree["displaycolumns"] = ("Recipe")

    shared.pic = ImageTk.PhotoImage(file='images/applications-science.png')
    parent = tree.insert('', 0, text='', image=shared.pic, open=True)

    sql = ("""SELECT \
            categoriesmain.CatText,  \
            recipes.RecipeText,  \
            recipes.idRecipes,  \
            categoriesmain.idCategoriesMain  \
            FROM  \
            recipecategories  \
            INNER JOIN categoriesmain  \
            ON recipecategories.MainCatKey = categoriesmain.idCategoriesMain  \
            INNER JOIN recipes  \
            ON recipecategories.RecipeId = recipes.idRecipes  \
            GROUP BY  \
            categoriesmain.CatText,  \
            recipes.RecipeText,  \
            recipes.idRecipes,  \
            categoriesmain.idCategoriesMain""")
    recs = list(cursor.execute(sql))
    if len(recs):
        # print(f'Returned {len(recs)} records')
        lastcat = ''
        for r in recs:
            cat = r[0]
            title = r[1]
            # catid = r[3]
            recipeid = r[2]
            # print(f'{cat} - {lastcat} - {title} - {recipeid} - {catid}')
            if lastcat != cat:
                parentid = tree.insert(parent, tk.END, text=(str(cat)))
                id = tree.insert(parentid, tk.END,
                                 values=(title, recipeid))
                lastcat = cat
            else:
                id = tree.insert(parentid, tk.END,
                                 values=(title, recipeid))
    else:
        print('ERROR!!!')

def tv_fill_ingreds(text):
    if shared.debug:
        print(f'Into tv_fill_ingredients - searchfor: {text}')
    clear_main_treeview()
    clear_form()
    # clear_labels()
    shared.tv_mode = 3
    shared.searchfor=text

    init_tree(w.Scrolledtreeview1)
    # populate_tree(w.Scrolledtreeview1,node)

def load_ingredient_list():
    sql = ("SELECT recipes.idRecipes, "
            "recipes.RecipeText, "
            "recipes.RecipeSource, "
            "recipes.RecipeServes, "
            "recipes.RecipeRating, "
            "ingredients.IngredientData "
            # "ingredients.IngredientItem "
            "FROM ingredients "
            "INNER JOIN recipes ON "
            "(ingredients.RecipeID = recipes.idRecipes) "
            "WHERE ingredients.IngredientData "
            "like '%{0}%'").format(str(shared.searchfor))
    if shared.debug:
        print(sql)
    recs = list(cursor.execute(sql))
    return recs
    # if len(recs):
    #     for r in recs:
    #         print(r)
    #         title = r[1]
    #         idkey = r[0]

def startup():
    global version, path1, progname
    pv = platform.python_version()
    print(f"Running under Python {pv}")
    # Set the path for the icon files
    path1 = os.getcwd()
    print(path1)
    print(f'Progam Name: {progname}')
    print(f"Version: {version}")
    shared.debug = False
    global timer_id
    timer_id = root.after(0, on_time_update)
    global connection, cursor
    connection = sqlite3.Connection("./database/cookbook-original.db")
    cursor = connection.cursor()
    # global folder
    # folder = tk.PhotoImage(file='./images/document.png')
    shared.folder = ImageTk.PhotoImage(file='./images/document.png')
    shared.tv_mode = 1
    setup_treeview()
    set_icon()
    root.title("Greg's Cookbook")
    centre_screen(1270,861)
    che46.set(0)
    shared.tv_mode = 1
    shared.debug = False

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # My init code here...
    # ======================================================
    global version
    version = '3.0.1'
    global progname
    progname = "Cookbook"
    startup()

def centre_screen(wid, hei):
    # ======================================================
    # Centers the screen
    # ======================================================
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (wid/2)
    y = (hs/2) - (hei/2)
    root.geometry('%dx%d+%d+%d' % (wid, hei, x, y))

def set_icon():
    # ======================================================
    # Sets the application icon...
    # ======================================================
    # global p1
    # p1 = tk.Image("photo", file='images/chef.png')
    shared.p1 = ImageTk.PhotoImage(file='images/chef.png')
    root.tk.call('wm', 'iconphoto', root._w, shared.p1)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import cbv3Main
    cbv3Main.vp_start_gui()





