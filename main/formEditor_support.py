#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.27p
#  in conjunction with Tcl version 8.6
#    Jan 22, 2020 05:25:22 AM CST  platform: Linux
#    Jan 22, 2020 08:24:34 AM CST  platform: Linux
#    Jan 26, 2020 05:36:56 AM CST  platform: Linux
# ======================================================
# Written by G.D. Walters
# ------------------------------------------------------
# Last modification date: 21 January, 2020
# ======================================================
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
    global EntryIngredient
    EntryIngredient = tk.StringVar()
    global RecipeTitle
    RecipeTitle = tk.StringVar()
    global RecipeSource
    RecipeSource = tk.StringVar()
    global RecipeServes
    RecipeServes = tk.StringVar()
    global RecipeTotalTime
    RecipeTotalTime = tk.StringVar()
    global RecipeRating
    RecipeRating = tk.StringVar()
    global che49
    che49 = tk.IntVar()
    global RecordNumber
    RecordNumber = tk.StringVar()
    RecordNumber.set('Label')
    global SelectedCats
    SelectedCats = tk.StringVar()
    SelectedCats.set('Message')

def on_btnExit():
    if shared.debug:
        print('formEditor_support.on_btnExit')
        sys.stdout.flush()

    isok = check_attr(shared, 'remote')
    if isok:
        cbv3Main_support.show_me()
        hide_me()
    else:
        destroy_window()

def on_btnSave():
    if shared.debug:
        print('formEditor_support.on_btnSave')
        sys.stdout.flush()
    title = 'Save functions'
    msg = "Sorry, but the Save functions are not yet implemented"
    messagebox.showinfo(title, msg)

def on_chkActive():
    if shared.debug:
        print('formEditor_support.on_chkActive')
        sys.stdout.flush()

def on_btnAdd():
    print('formEditor_support.on_btnAdd')
    sys.stdout.flush()
    # Get the entry data
    ing = EntryIngredient.get()
    # Add to ingredients list box
    w.Scrolledlistbox1.insert('end', str(ing))
    # Clear Entry widget
    EntryIngredient.set('')

def on_btnDelete():
    # TODO - Add check for selection before attempt to delete
    print('formEditor_support.on_btnDelete')
    sys.stdout.flush()
    pos = w.Scrolledlistbox1.curselection()
    # print(f'About to delete item at pos {pos} - {w.Scrolledlistbox1.get(pos)}')
    w.Scrolledlistbox1.delete(pos)

def on_customClick(s=None):
    if shared.debug:
        print('on_customClick')
    update_label()

def on_keytab(e, which):
    print('on_keytab')
    print(which)
    if which == 1:     # entryTitle
        pass
    elif which == 2:   # entrySource
        pass
    elif which == 3:   # entryServes
        pass
    elif which == 4:   # entryTotalTime
        pass
    elif which == 5:   # entryRating
        pass
    elif which == 6:   # stNotes
        w.Scrolledtext1.focus_set()
    elif which == 7:   # Scrolledtext1
        w.Scrolledlistbox1.focus_set()

def on_focusout(e, which):
    print('on_focusout')
    print(which)

def on_imageLocal(p1):
    print('on_imageLocal')
    global path1
    # pth = filedialog.askopenfile()
    pth = ''
    pth = filedialog.askopenfilename(initialdir = path1,
                                   title = "choose your file",
                                   filetypes = (("jpg files","*.jpg"),
                                                ("png files","*.png"),
                                                ("all files","*.*")))
    # if pth = '', user pressed cancel
    if pth != '':
        print(f'FilePath = {pth}')
        shared.imagePath = pth
    # Load the image into the label
    load_image()

def on_popPaste(p1):
    print(f'on_popPaste - {p1}')
    global eWidgets
    if p1 == 1:
        RecipeTitle.set(root.clipboard_get())
    elif p1 == 2:
        RecipeSource.set(root.clipboard_get())
    elif p1 == 3:
        RecipeServes.set(root.clipboard_get())
    elif p1 == 4:
        RecipeTotalTime.set(root.clipboard_get())
    elif p1 == 5:
        RecipeRating.set(root.clipboard_get())
    elif p1 == 6:
        pass
    elif p1 == 7:
        pass
    elif p1 == 8:
        EntryIngredient.set(root.clipboard_get())
    else:
        pass


def on_popCopy(p1):
    print(f'on_popCopy - {p1}')
    global eWidgets
    # field_value = eWidgets[p1].get()  # "1.0", 'end-1c')
    # root.clipboard_clear()  # clear clipboard contents
    # root.clipboard_append(field_value)


def on_popClear(p1):
    print(f'on_popClear - {p1}')
    global eWidgets
    # eWidgets[p1].set('')


def on_entryKeyPress(e):
    if shared.debug:
        print('EntryKeyPress')
    if e.keysym == 'Return':
        on_btnAdd()

def clear_labels():
    RecipeTotalTime.set('')
    RecipeSource.set('')
    RecipeServes.set('')
    RecipeTotalTime.set('')
    RecipeRating.set('')
    RecordNumber.set('')
    SelectedCats.set('')
    # Instructions
    w.Scrolledtext1.delete('1.0', tk.END)
    # Ingredients
    w.Scrolledlistbox1.delete(0, tk.END)
    # Categories
    w.Custom1.clear()

def set_labels():
    pass

def update_label():
    dat = w.Custom1.get()
    lst = []
    for x in dat:
        if len(x) == 2:
            t = x[0]
            # k = x[1]
            lst.append(t)
        else:
            lst.append(x)
    s = ", ".join(lst)
    SelectedCats.set(s)

def load_image():
    original = Image.open(shared.imagePath)
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
    global _img2
    _img1 = original.resize((int(w2), int(h2)), Image.ANTIALIAS)
    _img2 = ImageTk.PhotoImage(_img1)
    w.Label1.configure(image=_img2)

def fill_form():
    global connection, cursor, datacheck
    clear_labels()
    # Get the recipe basics
    sql = f'SELECT * FROM recipes WHERE idRecipes = {shared.rectouse}'
    print(sql)
    mainrec = list(cursor.execute(sql))
    if len(mainrec) > 0:
        print(mainrec)
        r = mainrec[0]
    RecordNumber.set(shared.rectouse)
    RecipeTitle.set(r[1])
    datacheck.append(r[1])
    RecipeSource.set(r[2])
    datacheck.append(r[2])
    RecipeServes.set(r[3])
    datacheck.append(r[3])
    RecipeTotalTime.set(r[4])
    datacheck.append(r[4])
    RecipeRating.set(r[5])
    datacheck.append(r[5])
    if r[6] == 1:
        che49.set(1)
        shared.IsActive = True
    else:
        che49.set(0)
        shared.IsActive = False
    datacheck.append(shared.IsActive)
    print(r[8])
    if r[8] != None:
        w.stNotes.insert(tk.END, r[8])
        datacheck.append(r[8])
    else:
        datacheck.append('')
    # Now fill in the image, if there is one.
    shared.imagePath = ''
    sql = (f'SELECT * FROM images WHERE recipeID = {shared.rectouse}')
    imgrec = list(cursor.execute(sql))
    if len(imgrec) > 0:
        r = imgrec[0]
        shared.imagePath = r[2]
    datacheck.append(shared.imagePath)
    if shared.imagePath != '':
        load_image()
    # ===================================
    # Fill in the ingredients
    # ===================================
    sql = (
        f'SELECT IngredientItem from ingredients WHERE RecipeID = {shared.rectouse}')
    ingRecs = list(cursor.execute(sql))
    if len(ingRecs) > 0:
        for i in ingRecs:
            w.Scrolledlistbox1.insert('end', str(i[0]))
    datacheck.append(ingRecs)
    # ===================================
    # Fill in the instructions
    # ===================================
    sql = (
        f"SELECT InstructionsData FROM instructions WHERE RecipeID = {shared.rectouse}")
    recs = list(cursor.execute(sql))
    for r in recs:
        w.Scrolledtext1.insert(tk.END, r[0])
    datacheck.append(recs)
    # ===================================
    # Set the categories
    # ===================================
    sql2 = ("SELECT recipes.idRecipes,"
            "categoriesmain.CatText "
            "FROM recipes "
            "INNER JOIN recipecategories ON "
            "(recipes.idRecipes=recipecategories.RecipeId) "
            "INNER JOIN categoriesmain ON "
            "(recipecategories.MainCatKey=categoriesmain.idCategoriesMain) "
            "WHERE recipes.idRecipes = {0}").format(shared.rectouse)
    cats = list(cursor.execute(sql2))
    if len(cats):
        # print(cats)
        tlist = []
        for r in cats:
            tlist.append(r[1])
            # w.Custom1.set(r[1])
            # tlist.append(r[1])
            # tlist.append(r[0])
            # catlist.append(tlist)
            # tlist = []
    w.Custom1.set(tlist)
    update_label()
    x = w.Custom1.get()
    # print(x)
    datacheck.append(x)
    # ===================================
    shared.isDirty = False
    if shared.debug:
        print('Datacheck:')
        print(datacheck)

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

def set_bindings():
    w.entryTitle.bind('<KeyPress-Tab>', lambda e: on_keytab(e, 1))
    w.entryTitle.bind('<FocusOut>', lambda e: on_focusout(e, 1))
    w.entryTitle.bind('<Button-3>', lambda e: w.popup1(e, 1))
    w.entrySource.bind('<KeyPress-Tab>', lambda e: on_keytab(e, 2))
    w.entrySource.bind('<FocusOut>', lambda e: on_focusout(e, 2))
    w.entrySource.bind('<Button-3>', lambda e: w.popup1(e, 2))
    w.entryServes.bind('<KeyPress-Tab>', lambda e: on_keytab(e, 3))
    w.entryServes.bind('<FocusOut>', lambda e: on_focusout(e, 3))
    w.entryServes.bind('<Button-3>', lambda e: w.popup1(e, 3))
    w.entryTotalTime.bind('<KeyPress-Tab>', lambda e: on_keytab(e, 4))
    w.entryTotalTime.bind('<FocusOut>', lambda e: on_focusout(e, 4))
    w.entryTotalTime.bind('<Button-3>', lambda e: w.popup1(e, 4))
    w.entryRating.bind('<KeyPress-Tab>', lambda e: on_keytab(e, 5))
    w.entryRating.bind('<FocusOut>', lambda e: on_focusout(e, 5))
    w.entryRating.bind('<Button-3>', lambda e: w.popup1(e, 5))
    w.stNotes.bind('<Control-Return>', lambda e: on_keytab(e, 6))
    w.stNotes.bind('<FocusOut>', lambda e: on_focusout(e, 6))
    w.stNotes.bind('<Button-3>', lambda e: w.popup1(e, 6))
    w.Scrolledtext1.bind('<Control-Return>', lambda e: on_keytab(e, 7))
    w.Scrolledtext1.bind('<Button-3>', lambda e: w.popup1(e, 7))
    w.Scrolledtext1.bind('<FocusOut>', lambda e: on_focusout(e, 7))
    # Bind image label to right click for local image load
    w.Label1.bind('<Button-3>', on_imageLocal)
    # Bind right click to ingredient entry widget
    w.entIngredient.bind('<Button-3>', lambda e: w.popup1(e, 8))
    w.entIngredient.bind('<KeyRelease>', lambda e: on_entryKeyPress(e))
    global eWidgets
    eWidgets = [w.entryTitle, w.entrySource, w.entryServes, w.entryTotalTime, w.entryRating, w.stNotes, w.Scrolledtext1, w.entIngredient]


def get_ingredient_list():
    pass

def write_to_db():
    # Get the data from the form
    title = RecipeTitle.get()
    source = RecipeSource.get()
    serves = RecipeServes.get()
    totaltime = RecipeTotalTime.get()
    rating = RecipeRating.get()
    # active = che49.get()
    # descrip = R
    # Create the sql statements and write them
    if shared.EditMode:
        # Use update
        pass
    else:
        # Use Insert
        sql = ("Insert into recipes "
            "(RecipeText,RecipeSource,RecipeServes,TotalTime, RecipeRating, Notes, Active) "
            "VALUES ({0},{1},{2},{3},{4},{5},{6});").format(
            quote(title),
            quote(source),
            quote(serves),
            quote(totaltime),
            quote(rating),
            quote(w.stNotes.get(1.0, tk.END)),
            1)
        # print(sql)
        # Everything depends on the last_insert_rowid being available
        # so if this fails, we have to abort and have the user try again
        cur.execute(sql)
        connection.commit()
        if shared.debug:
            print('Main Record Written')
        # LastRecord is the last id that was saved in the recipe table
        # We will use it to link the rest of the data to this recipe
        LastRecord = cur.lastrowid
        if shared.debug:
            print(f'LastRecord inserted at {LastRecord}')
        # -----------------------
        # Write Instructions
        # -----------------------
        sql = ("Insert into instructions "
            "(RecipeID,InstructionsData) "
            "VALUES ({0},{1})").format(LastRecord,
                                        quote(
                                            w.Scrolledtext1.get(
                                                1.0, tk.END)))
        # print(sql)
        # r = input('Press a key ->')
        cur.execute(sql)
        connection.commit()
        if shared.debug:
            print('Instructions written')
        # -----------------------
        # Write ImageURL
        # STILL TO DO
        sql = ('INSERT INTO images (recipeID, image) '
            'VALUES ({0}, {1})'.format(
                LastRecord, quote(shared.imgname)))
        # print(sql)
        # cur.execute(sql)
        # connection.commit()
        if shared.debug:
            print('Image Written')

        # -----------------------
        # Write Ingredients
        # -----------------------
        # ilist = GetIngredientItems(w.Scrolledlistbox1, 'I', 3)
        # print(ilist)
        # r = raw_input('Press a key -> ')
        for line in shared.ingredients:
            sql = ("INSERT INTO ingredients "
                "(RecipeID,Ingredientitem) "
                "VALUES ({0},{1})").format(
                LastRecord, quote(line))

            cur.execute(sql)
        connection.commit()
        if shared.debug:
            print('Ingredients Written')
        # -----------------------
        # Write Categories
        # Get checked cateegories
        checks = w.Custom1.get()
        print(checks)
        for c in checks:
            sql = (
                "INSERT INTO recipecategories (RecipeId, MainCatKey) VALUES ({1}, {0})".format(c[1], LastRecord))
            print(sql)
            cur.execute(sql)
        connection.commit()
        # -----------------------
        # connection.commit()
        messagebox.showinfo('Data Actions', 'Recipe Saved')
        busyEnd()
        #
    msgTitle = 'Save Recipe Changes'
    msgMsg = 'All data saved'
    messagebox.showinfo(msgTitle, msgMsg)

def start_up():
    global connection, cursor

    connection = sqlite3.Connection("./database/cookbook-original.db")
    cursor = connection.cursor()
    # set up for cursors
    global busyCursor, preBusyCursors, busyWidgets
    busyCursor = 'watch'
    preBusyCursors = None
    busyWidgets = (root, )
    # Clear the text from the image label
    lblImage = w.Label1
    lblImage.configure(text='')
    # Set up the debug flag
    shared.debug = True
    global datacheck
    datacheck = []
    shared.imagePath = ''
    w.Label1.configure(text = 'Right click here to insert image...')
    # Fill the entry widget for testing purposes
    initialize_custom_widget()
    # Set the entry widgets bindings
    set_bindings()
    # set the window icon
    set_icon()
    # Centre the screen
    centre_screen(1139, 773)
    w.entryTitle.focus_set()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # My init code starts...
    # ======================================================
    global version
    version = '0.2.1'
    pv = platform.python_version()
    print(f"Running under Python {pv}")
    # Set the path for the icon files
    global path1
    path1 = os.getcwd()
    print(path1)
    print(f"Version: {version}")
    progname = 'Editor v' + version
    # root.title(progname)
    start_up()
    # ======================================================
    # At this point, we want to check to see if the program was called
    # remotely or from the command line...
    # ======================================================
    isok = check_attr(shared, 'remote')
    if isok:   # Cookbook main will set 'remote' to True
        # Check to see if we are starting in Edit mode or New Recipe mode...
        if shared.EditMode == 'Edit':
            # shared.rectouse
            root.title(progname + ' - Edit Mode')
            fill_form()
        else:
            root.title(progname + ' - New Form')
            clear_labels()
    else:
        # We are running in standalone mode.
        # Record to use for testing/development
        testrec = 118
    # print(shared.rectouse)
    isok = check_attr(shared, 'rectouse')
    # attr = getattr(shared, 'rectouse', False)
    if isok is False:
        shared.rectouse = testrec
        testmode = True
    else:
        testmode = False
    # shared.rectouse = 118  # 108
    global is_child
    # Use the following check to see if we are running as a child or standalone
    # attr = getattr(shared, 'remote', False)
    isok = check_attr(shared, 'remote')
    if isok is False:
        is_child = False
        if testmode == True:
            shared.testmode = True
            shared.EditMode = 'Edit'
            root.title(progname + " - Standalone mode - TEST Edit MODE!")
            fill_form()
        else:
            shared.EditMode = 'New'
            root.title(progname + " - Standalone mode - TEST New MODE")
            clear_labels()
    else:
        is_child = True
        if shared.EditMode == 'Edit':
            root.title(progname + ' - Edit Mode')
            fill_form()
        else:
            root.title(progname + ' - New Form')
            clear_labels()

def get_Custom_Cats():
    global connection, cursor
    sql = 'SELECT CatText, idCategoriesMain FROM categoriesmain order by CatText ASC'
    recs = list(cursor.execute(sql))
    if shared.debug:
        print(recs)
    return recs
    # if len(recs) > 0:
    #     for r in recs:

def initialize_custom_widget():
    w.Custom1.cback = on_customClick
    # To use a single list of item names comment out the next line and
    # uncomment the second line down.
    ListInfo2 = get_Custom_Cats()
    w.Custom1.load(ListInfo2)
    w.Custom1.clear()
    # w.Custom1.load(ListInfo)
    # clear_label()
    # set_labels()

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
    root.attributes("-topmost", True)

def hide_me():
    cbv3Main_support.show_me()
    root.withdraw()

def set_icon():
    # ======================================================
    # Sets the application icon...
    # ======================================================
    # global p1
    # p1 = tk.Image("photo", file='images/chef.png')
    shared.p1 = ImageTk.PhotoImage(file='images/chef.png')
    root.tk.call('wm', 'iconphoto', root._w, shared.p1)

# Custom = tk.Frame  # To be updated by user with name of custom widget.
Custom = ScrolledCheckedListBox

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import formEditor
    formEditor.vp_start_gui()





