#!/usr/bin/env python3
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
#    Jan 21, 2020 03:05:04 PM CST  platform: Linux
#    Jan 22, 2020 02:57:49 AM CST  platform: Linux
#    Jan 28, 2020 03:30:01 AM CST  platform: Linux
#    Jan 29, 2020 03:45:53 PM CST  platform: Linux
#    Apr 01, 2020 04:57:19 AM CDT  platform: Linux
#    Oct 01, 2020 05:14:44 AM CDT  platform: Linux
# ======================================================
# Written by G.D. Walters
# ------------------------------------------------------
# Last modification date: 19 December, 2020
# ======================================================
# To do before first release:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Fix write/read categories - done
# Create New/Edit Form - done
# Support "deleted" records in main table - mostly done
# Create HTML print routine - done
# Write program to clean orphans in database - partially done
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
import os
import platform
import datetime
import sqlite3
import shared
import webbrowser
from PIL import ImageTk, Image
from dbutils import quote
import ScraperGUI1_support
import ScraperGUI1
import formEditor
import formEditor_support
import formDbMaint
import formDbMaint_support
import configparser
# import formConfig
# import formConfig_support
import printtemp
import formTips

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
    global LableFavorite
    LableFavorite = tk.StringVar()
    LableFavorite.set('Label')

    global RecipeRating
    RecipeRating = tk.StringVar()
    RecipeRating.set('Label')

    global RecipeTotalTime
    RecipeTotalTime = tk.StringVar()
    RecipeTotalTime.set('Label')
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
    # if shared.debug:
    print('cbv3Main_support.on_btnScrape')
    # sys.stdout.flush()
    shared.remote = True
    ScraperGUI1.create_Scraper(root)
    hide_me()

def on_chkClick():
    global activeonly
    if shared.debug:
        print('cbv3Main_support.on_chkClick')
        sys.stdout.flush()
    AO = activeonly
    print(f'ChkValue: {che46.get()} AO: {AO}')
    if che46.get() == 0:
        activeonly = True
        init_tree(w.Scrolledtreeview1)
    else:
        activeonly = False
        init_tree(w.Scrolledtreeview1)

def on_btnAdd():
    if shared.debug:
        print('test3_support.on_btnAdd')
        sys.stdout.flush()
        shared.rectouse = CurrentID
    shared.remote = True
    shared.EditMode = 'New'
    hide_me()
    formEditor.create_formEditor(root)

def on_btnDelete():
    global connection, cursor
    if shared.debug:
        print('test3_support.on_btnDelete')
        sys.stdout.flush()
    title = "Delete Recipe"
    msg = "Are you sure you want to delete this record?"
    resp = messagebox.askyesno(title, msg)
    if resp:
        sql = f"UPDATE recipes SET Active = 0 WHERE idRecipes = {CurrentID}"
        cursor.execute(sql)
        connection.commit()
        init_tree(w.Scrolledtreeview1)

def on_btnEdit():
    global CurrentID
    if shared.debug:
        print('test3_support.on_btnEdit')
        sys.stdout.flush()
    shared.remote = True
    shared.rectouse = CurrentID
    shared.EditMode = 'Edit'
    hide_me()
    formEditor.create_formEditor(root)

def on_btnExit():
    if shared.debug:
        print('cbv3Main_support.on_btnExit')
        sys.stdout.flush()
    global _img3, _img2
    _img3 = None
    _img2 = None
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
        w.Entry1.configure(state='normal')
        tv_fill_title()
        find_in_treeview()

    elif which == 1:
        # Ingredient
        w.Entry1.configure(state='normal')

    elif which == 2:
        # Category
        w.Entry1.configure(state='disabled')
        tv_fill_cats()

    elif which == 3:
        # Favorites
        w.Entry1.configure(state='disabled')
        tv_fill_favs()
    else:
        pass

def on_TV_Click(e):
    if shared.debug:
        print('On_TV_Click')
    print(f'tv_mode = {shared.tv_mode}')
    global CurrentID
    if (shared.tv_mode == 1) or (shared.tv_mode == 3) or (shared.tv_mode == 4):
        row = w.Scrolledtreeview1.identify_row(e.y)
        col = w.Scrolledtreeview1.identify_column(e.x)
        print(f'Row: {row}  Col: {col}')
        title = w.Scrolledtreeview1.set(row, 0)
        CurrentID = w.Scrolledtreeview1.set(row, 1)
        print(f'Title: {title} CurrentID: {CurrentID}')
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
    shared.rectouse = CurrentID

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

def on_Source_Click(e):
    browse = webbrowser.get('firefox')
    link = RecipeSource.get()
    browse.open(link)

def on_btnPrint():
    if shared.debug:
        print('cbv3Main_support.on_btnPrint')
        sys.stdout.flush()
    global CurrentID
    printtemp.main(CurrentID)

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
    RecipeTotalTime.set('')
    RecipeRating.set('')
    w.stNotes.delete('1.0', tk.END)
    # Instructions
    w.Scrolledtext1.delete('1.0', tk.END)
    # Ingredients
    w.Scrolledlistbox1.delete(0, tk.END)
    # Image

def show_fav(which):
    global favImage
    if which == True:
        img = Image.open(path1 + '/images/star-48.png')
        favImage = ImageTk.PhotoImage(img)
        w.lblFave.configure(image=favImage)
    else:
        # global favImage
        img = Image.open(path1 + '/images/blank.png')
        favImage = ImageTk.PhotoImage(img)
        w.lblFave.configure(image=favImage)

def load_form(id):
    global connection, cursor, activeonly, imgpath, path1
    clear_form()
    # set_labels()
    IdLableShow.set(id)
    if activeonly:
        sql = (
            f"SELECT * FROM recipes WHERE recipes.idRecipes = {id} and recipes.Active = 1"
        )
    else:
        sql = (f"SELECT * FROM recipes WHERE recipes.idRecipes = {id}")
    recs = list(cursor.execute(sql))
    print(recs)
    for r in recs:
        # curid = r[0]
        RecipeTitle.set(r[1])
        RecipeSource.set(r[2])
        RecipeServings.set(r[3])
        RecipeTotalTime.set(r[4])
        RecipeRating.set(r[5])
        print(f'Fav = {r[9]}')
        if r[9] == 1:
            show_fav(True)
        else:
            show_fav(False)

        # active = r[6]
        # photoid = r[7]
        # print(r[8])
        if r[8] == None:
            w.stNotes.insert(tk.END, '')
        else:
            w.stNotes.insert(tk.END, str(r[8]))
        # w.msgNotes.configure(text=r[8])
        # RecipeNotes.set(r[8])
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
    #  and recipes.Active = 1'
    # if activeonly:
    #     sql = (f'SELECT IngredientItem, recipes.Active from ingredients WHERE RecipeID = {id} and recipes.Active = 1')
    # else:
        sql = (f'SELECT IngredientItem from ingredients WHERE RecipeID = {id}')

    ingreds = list(cursor.execute(sql))
    # ingreds = cursor.execute(sql)
    if len(ingreds):
        for i in ingreds:
            if shared.debug:
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
            original = Image.open(path1 + path)
            wid, hei = original.size
            if shared.debug:
                print(f'Width: {wid} - Height: {hei}')
            if wid >= hei:
                ratio = 300.0 / wid
                if shared.debug:
                    print(ratio)
                w2 = wid * ratio
                h2 = hei * ratio
            else:
                ratio = 300. / hei
                if shared.debug:
                    print(ratio)
                w2 = wid * ratio
                h2 = hei * ratio
            if shared.debug:
                print(f'New Width = {int(w2)} - New Height = {int(h2)}')
            _img1 = original.resize((int(w2), int(h2)), Image.ANTIALIAS)
            _img2 = ImageTk.PhotoImage(_img1)
            w.lblImage.configure(image=_img2)
    else:
        global _img3
        img = Image.open(path1 + '/images/NoImage.png')
        _img3 = ImageTk.PhotoImage(img)
        w.lblImage.configure(image=_img3)
    # RecipeNotes.set('No description available')

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
    global first, CurrentID
    recs = None
    if shared.tv_mode == 1:
        recs = load_base_recipes()
    elif shared.tv_mode == 3:
        recs = load_ingredient_list()
    elif shared.tv_mode == 4:
        recs = load_fav_list()
    parent = node
    cntr = 0
    for r in recs:
        title = r[1]
        recid = r[0]
        id = tree.insert(parent, tk.END, values=(title, recid))
        if cntr == 0:
            first = id
        cntr += 1
    tree.item(node, open=True)
    tree.focus(first)
    tree.selection_set(first)
    # print(f'first: {first}')
    # title = w.Scrolledtreeview1.set(first, 0)
    CurrentID = w.Scrolledtreeview1.set(first, 1)
    # if shared.tv_mode == 1:
    #     sort_by(tree, 'Recipe', 0)
    load_form(CurrentID)
    shared.rectouse = CurrentID

def load_fav_list():
    # Does nothing for the moment.
    global connection, cursor, activeonly
    # if activeonly:
    #     sql = "SELECT * from recipes where recipes.Active = 1 order by RecipeText ASC"
    # else:
    #     sql = "SELECT * from recipes order by RecipeText ASC"
    sql = "SELECT * FROM recipes WHERE Favorite = 1 order by RecipeText ASC"
    recs = list(cursor.execute(sql))
    titl = shared.formTitle + f" - {len(recs)} Favorites"
    root.title(titl)
    print(f'{len(recs)} Records)')
    if len(recs):
        return (recs)

def load_base_recipes():
    global connection, cursor, activeonly
    if activeonly:
        sql = "SELECT * from recipes where recipes.Active = 1 order by RecipeText ASC"
    else:
        sql = "SELECT * from recipes order by RecipeText ASC"
    recs = list(cursor.execute(sql))
    titl = shared.formTitle + f" - {len(recs)} Recipes"
    root.title(titl)
    print(f'{len(recs)} Records)')
    if len(recs):
        return (recs)

def init_tree(tree):
    clear_treeview()
    tree["columns"] = ("Recipe", "Recid")
    tree.column('#0', width=40, stretch=tk.NO)
    tree.column('Recipe', width=400, stretch=tk.NO)
    tree.column("Recid", width=100, stretch=tk.NO)
    tree.heading('#0', text='', anchor=tk.W)
    tree.heading('Recipe', text='Recipe', anchor=tk.W)
    tree.heading('Recid', text='Recid', anchor=tk.W)
    global node
    node = tree.insert('', 1, text='', image=shared.folder)
    populate_tree(tree, node)

def setup_treeview():
    w.Scrolledtreeview1.bind('<<TreeviewSelect>>', lambda e: update_tree(e))
    w.Scrolledtreeview1.bind('<<TreeviewOpen>>', lambda e: tree_open(e))
    w.Scrolledtreeview1.bind('<<TreeviewClose>>', lambda e: tree_close(e))
    w.Scrolledtreeview1.bind('<Button-1>', lambda e: on_TV_Click(e))
    init_tree(w.Scrolledtreeview1)

def clear_treeview():
    w.Scrolledtreeview1.delete(*w.Scrolledtreeview1.get_children())

def tv_fill_title():
    clear_main_treeview()
    shared.tv_mode = 1
    setup_treeview()

def tv_fill_favs():
    tree = w.Scrolledtreeview1
    clear_main_treeview()
    clear_form()
    shared.tv_mode = 4
    init_tree(w.Scrolledtreeview1)    
    # # shared.searchfor = text
    # tree["columns"] = ("Recipe", "Recid")
    # tree.column('#0', width=150, stretch=tk.NO, anchor=tk.W)
    # tree.column('Recipe', width=400, stretch=tk.NO, anchor=tk.W)
    # tree.column("Recid", width=100, stretch=tk.NO, anchor=tk.W)
    # tree.heading('#0', text='Favorite', anchor=tk.W)    
    # tree.heading('Recipe', text='Recipe', anchor=tk.W)
    # tree.heading('Recid', text='Recid', anchor=tk.W)
    # tree["displaycolumns"] = ("Recipe")
    # global activeonly
    # sql = "SELECT * FROM recipes WHERE Favorite = 1"
    # # init_tree(w.Scrolledtreeview1)
    # recs = list(cursor.execute(sql))
    # if len(recs):
    #     # print(f'Returned {len(recs)} records')
    #     lastcat = ''
    #     for r in recs:
    #         cat = r[0]
    #         title = r[1]
    #         # catid = r[3]
    #         recipeid = r[2]
    #         parentid = None
    #         id = tree.insert(parentid, tk.END, values=(title, recipeid))

def tv_fill_cats():
    tree = w.Scrolledtreeview1
    clear_main_treeview()
    clear_form()
    shared.tv_mode = 2
    tree["columns"] = ("Recipe", "Recid")
    tree.column('#0', width=150, stretch=tk.NO, anchor=tk.W)
    tree.column('Recipe', width=400, stretch=tk.NO, anchor=tk.W)
    tree.column("Recid", width=100, stretch=tk.NO, anchor=tk.W)
    tree.heading('#0', text='Category', anchor=tk.W)

    tree.heading('Recipe', text='Recipe', anchor=tk.W)
    tree.heading('Recid', text='Recid', anchor=tk.W)
    tree["displaycolumns"] = ("Recipe")

    shared.pic = ImageTk.PhotoImage(file=path1 +
                                    '/images/applications-science.png')
    parent = tree.insert('', 0, text='', image=shared.pic, open=True)
    global activeonly
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
                id = tree.insert(parentid, tk.END, values=(title, recipeid))
                lastcat = cat
            else:
                id = tree.insert(parentid, tk.END, values=(title, recipeid))
    else:
        # TODO - Support messagebox here!
        print('ERROR!!!')
    find_in_treeview()

def tv_fill_ingreds(text):
    if shared.debug:
        print(f'Into tv_fill_ingredients - searchfor: {text}')
    clear_main_treeview()
    clear_form()
    # clear_labels()
    shared.tv_mode = 3
    shared.searchfor = text

    init_tree(w.Scrolledtreeview1)
    # populate_tree(w.Scrolledtreeview1,node)

def load_ingredient_list():
    global activeonly
    if activeonly:
        sql = ("SELECT recipes.idRecipes, "
               "recipes.RecipeText, "
               "recipes.RecipeSource, "
               "recipes.RecipeServes, "
               "recipes.RecipeRating, "
               "ingredients.IngredientItem "
               "FROM ingredients "
               "INNER JOIN recipes ON "
               "(ingredients.RecipeID = recipes.idRecipes) "
               "WHERE recipes.Active = 1 AND ingredients.IngredientItem "
               "like '%{0}%'").format(str(shared.searchfor))
    else:
        sql = ("SELECT recipes.idRecipes, "
               "recipes.RecipeText, "
               "recipes.RecipeSource, "
               "recipes.RecipeServes, "
               "recipes.RecipeRating, "
               "ingredients.IngredientItem "
               "FROM ingredients "
               "INNER JOIN recipes ON "
               "(ingredients.RecipeID = recipes.idRecipes) "
               "WHERE ingredients.IngredientItem "
               "like '%{0}%'").format(str(shared.searchfor))
    if shared.debug:
        print(sql)
    recs = list(cursor.execute(sql))
    return recs

def sort_by(tree, col, descending):
    # ======================================================
    # Sorts the treeview
    # ======================================================
    # grab values to
    print('into sort_by')
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(
        col, command=lambda col=col: sort_by(tree, col, int(not descending)))

def set_btn_labels():
    global printButton, imgpath
    img = Image.open(path1 + '/images/32/document-print.png')
    printButton = ImageTk.PhotoImage(img)
    w.btnPrint.configure(image=printButton)

    global exitButton
    img = Image.open(path1 + '/images/32/app-exit.png')
    exitButton = ImageTk.PhotoImage(img)
    w.btnExit.configure(image=exitButton)

    global addButton
    img = Image.open(path1 + '/images/32/list-add.png')
    addButton = ImageTk.PhotoImage(img)
    w.btnAdd.configure(image=addButton)

    global deleteButton
    img = Image.open(path1 + '/images/32/list-remove.png')
    deleteButton = ImageTk.PhotoImage(img)
    w.btnDelete.configure(image=deleteButton)

    global editButton
    img = Image.open(path1 + '/images/32/edit-paste.png')
    editButton = ImageTk.PhotoImage(img)
    w.btnEdit.configure(image=editButton)

    global scrapeButton
    img = Image.open(path1 + '/images/32/internet.png')
    scrapeButton = ImageTk.PhotoImage(img)
    w.btnScrape.configure(image=scrapeButton)

    global dbMaintButton
    img = Image.open(path1 + '/images/32/utilities.png')
    dbMaintButton = ImageTk.PhotoImage(img)
    w.btnUtils.configure(image=dbMaintButton)

    global configButton
    img = Image.open(path1 + '/images/32/system-run.png')
    configButton = ImageTk.PhotoImage(img)
    w.btnConfig.configure(image=configButton)

    global tipsButton
    img = Image.open(path1 + '/images/32/icons8-light-32.png')
    tipsButton = ImageTk.PhotoImage(img)
    w.btnTips.configure(image=tipsButton)

    global favsLabel
    img = Image.open(path1 + '/images/EmptyHeart.png')
    favsLabel = ImageTk.PhotoImage(img)
    w.lblFave.configure(image=favsLabel)

def fix_path():
    global path1
    if "main" in path1:
        pass
    else:
        path1 = path1 + "/main"
    path1 = '/home/greg/GitHub/gregwa/CookbookV3/main/'

def setup_styles():
    from ttkthemes import ThemedStyle
    s = ThemedStyle()
    s.set_theme("default")
    style = ttk.Style()
    style.theme_use('elegance')
    # style.configure('Treeview', fieldbackground="#919191")
    style.configure('Treeview', fieldbackground="#595959")
    style.configure('.', background='#919191')
    style.configure('.', foreground='#111111')
    # style.configure('Treeview', font=('DejaVu Sans Mono', 11, 'bold'))
    style.configure('Treeview', font=('DejaVu Sans', 11, 'bold'))
    # ======================================================
    # This is the theme setting for the treeview from the elegance ttk code...
    # Hopefully I can modify it to provide a better background/foreground
    # for the treeview object
    # ======================================================
    # # -----------------------------------------------------------------
    # # Tree
    # #
    # ::ttk::style element create Treeheading.cell \
    #     image [list $I(list-header) pressed $I(list-header-prelight)] \
    #     -border {4 10} -padding 4 -sticky ewns
    # ::ttk::style map Treeview \
    #     -background [list selected $colors(-selectbg)] \
    #     -foreground [list selected $colors(-selectfg)]

def read_config():
    config = configparser.ConfigParser()
    config.read('/home/greg/GitHub/gregwa/CookbookV3/main/config.ini')
    csections = config.sections()
    print(csections)
    print(config['DEFAULT']['defaultimagepath'])
    if 'DEFAULT' in config:
        shared.defaultImagePath = config['DEFAULT']['defaultimagepath']
    if 'Themes' in config:
        shared.defaultTheme = config['Themes']['defaulttheme']

def startup():
    global version, path1, progname
    pv = platform.python_version()
    print(f"Running under Python {pv}")
    # Set the path for the icon files
    path1 = os.getcwd()
    fix_path()
    print(path1)

    print(f'Progam Name: {progname}')
    print(f"Version: {version}")
    shared.debug = False
    global timer_id
    timer_id = root.after(0, on_time_update)
    global connection, cursor
    dbpath = path1 + "/database/cookbook-original.db"
    print(dbpath)
    global imgpath
    imgpath = path1 + "/images/"
    connection = sqlite3.Connection(dbpath)
    cursor = connection.cursor()
    img = Image.open(path1 + '/images/document.png')
    shared.folder = ImageTk.PhotoImage(img)  # file='./images/document.png')
    root.title("Greg's Cookbook V3")
    shared.formTitle = "Greg's Cookbook V3"
    # =================================================
    # Default to only show 'Active' recipes
    global activeonly
    w.Checkbutton1.configure(state='normal')
    che46.set(0)
    activeonly = True
    # =================================================
    shared.tv_mode = 1
    setup_treeview()
    set_btn_labels()
    set_icon()
    set_mode()
    centre_screen(1270, 861)
    w.lblSource.bind("<Button-1>",lambda e: on_Source_Click(e))
    shared.debug = False
    read_config()
    global isFav
    isFav = False
    setup_styles()

def find_in_treeview():
    global node, CurrentID
    print('Into find_in_treeview()')
    kids = w.Scrolledtreeview1.get_children(node)
    isok = False
    # print(kids)
    print(f'RecToUse = {shared.rectouse}')
    for i in kids:
        title = w.Scrolledtreeview1.set(i, 0)
        ID = w.Scrolledtreeview1.set(i, 1)
        if int(shared.rectouse) == int(ID):
            print(f'Found {ID}')
            w.Scrolledtreeview1.selection_set(i)
            load_form(ID)
            isok = True
            break
    if isok:
        w.Scrolledtreeview1.see(i)
        root.update()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # My init code here...
    # ======================================================
    global version
    version = '3.4.9.0'
    global progname
    progname = "Cookbook V3"
    startup()

def centre_screen(wid, hei):
    # ======================================================
    # Centers the screen
    # ======================================================
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (wid / 2)
    y = (hs / 2) - (hei / 2)
    root.geometry('%dx%d+%d+%d' % (wid, hei, x, y))

def set_icon():
    # ======================================================
    # Sets the application icon...
    # ======================================================
    # global p1
    # p1 = tk.Image("photo", file='images/chef.png')
    global imgpath
    # shared.p1 = ImageTk.PhotoImage(file='images/chef.png')
    shared.p1 = ImageTk.PhotoImage(file=imgpath + '/chef.png')
    root.tk.call('wm', 'iconphoto', root._w, shared.p1)

def set_mode():
    tbcolour = 'gray72'
    widgetlist = [
        root, w.frameToolbar, w.frameStatus, w.lblTimeDisplay, w.frameNavigate,
        w.Frame2, w.Label1, w.rbTitle, w.rbCategories, w.rbIngredients,
        w.Checkbutton1, w.Frame3, w.Frame1, w.lblTitle, w.lblImage,
        w.lblSource, w.lblServings, w.msgCategories, w.lblID, w.Label2,
        w.Label3, w.Label4, w.lblTotalTime, w.Label5, w.Label6, w.Label7
    ]
    ln = len(widgetlist)

    for widg in widgetlist:
        widg.configure(background="#919191")
    w.stNotes.configure(background=tbcolour)
    w.Scrolledlistbox1.configure(background=tbcolour)
    w.Scrolledtext1.configure(background=tbcolour)
    w.rbTitle.configure(highlightbackground="#919191")
    w.rbCategories.configure(highlightbackground='#919191')
    w.rbIngredients.configure(highlightbackground='#919191')
    w.Checkbutton1.configure(highlightbackground='#919191')
    w.rbTitle.configure(activebackground="#919191")
    w.rbCategories.configure(activebackground='#919191')
    w.rbIngredients.configure(activebackground='#919191')
    w.Checkbutton1.configure(activebackground='#919191')
    w.lblFave.configure(background="#919191")
    w.rbFavorites.configure(background="#919191")
    w.rbFavorites.configure(activebackground='#919191')
    w.rbFavorites.configure(highlightbackground='#919191')
    print('finished applying backgrounds')

# =================================================================
# Window stuff
# =================================================================

def show_me():
    global root
    root.deiconify()
    # root.attributes("-topmost", True)
    centre_screen(1270, 861)
    # reload treeview here
    shared.tv_mode = 1
    tv_fill_title()
    find_in_treeview()

def hide_me():
    global root
    root.withdraw()

def on_btnConfig():
    print('cbv3Main_support.on_btnConfig')
    sys.stdout.flush()
    title = "Configuration Utility"
    txt = "Sorry, but the Configuration Utility is not implemented yet."
    messagebox.showinfo(title, txt)

def on_btnUtils():
    print('cbv3Main_support.on_btnUtils')
    sys.stdout.flush()
    shared.remote = True
    formDbMaint.create_formDbMaint(root)
    hide_me()

def on_btnTips():
    print('cbv3Main_support.on_btnTips')
    sys.stdout.flush()
    # title = 'Under Construction'
    # msg = 'Sorry, but the tips portion of the program is not yet completed.'
    # messagebox.showinfo(title, msg)
    shared.remote = True
    print(f'Rectouse: {shared.rectouse}')
    formTips.create_Toplevel1(root)
    hide_me()

def on_lblFaveClick(p1):
    print('cbv3Main_support.on_lblFaveClick')
    sys.stdout.flush()
    global isFav, favsLabel, favsLabel2
    print(f'Favorite: {isFav}')
    if isFav:
        img = Image.open(path1 + '/images/blank.png')
        favsLabel = ImageTk.PhotoImage(img)
        w.lblFave.configure(image=favsLabel)
        isFav = False
    else:
        img = Image.open(path1 + '/images/star-48.png')
        favsLabel2 = ImageTk.PhotoImage(img)
        w.lblFave.configure(image=favsLabel2)
        isFav = True
    root.update()
    print(f'Favorite is now: {isFav}')
    # update database record...
    print(f'CurrentID = {CurrentID}')
    sql = f"UPDATE recipes SET Favorite = {isFav} WHERE idRecipes = {CurrentID}"
    cursor.execute(sql)
    connection.commit()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import cbv3Main
    cbv3Main.vp_start_gui()





