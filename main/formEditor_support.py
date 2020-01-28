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
    write_to_db()


def on_chkActive():
    if shared.debug:
        print('formEditor_support.on_chkActive')
        sys.stdout.flush()


def on_btnAdd():
    if shared.debug:
        print('formEditor_support.on_btnAdd')
    sys.stdout.flush()
    global ingindex
    if ingindex != None:
        w.Scrolledlistbox1.delete(ingindex)
        ing = EntryIngredient.get()
        w.Scrolledlistbox1.insert(ingindex, str(ing))
    else:
        # Get the entry data
        ing = EntryIngredient.get()
        # Add to ingredients list box
        w.Scrolledlistbox1.insert('end', str(ing))
    # Clear Entry widget
    EntryIngredient.set('')
    ingindex = None


def on_btnDelete():
    # TODO - Add check for selection before attempt to delete
    if shared.debug:
        print('formEditor_support.on_btnDelete')
    sys.stdout.flush()
    pos = w.Scrolledlistbox1.curselection()
    # print(f'About to delete item at pos {pos} - {w.Scrolledlistbox1.get(pos)}')
    w.Scrolledlistbox1.delete(pos)
    EntryIngredient.set('')
    global ingindex
    ingindex = None


def on_customClick(s=None):
    if shared.debug:
        print('on_customClick')
    update_label()


def on_keytab(e, which):
    if shared.debug:
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
    if shared.debug:
        print('on_focusout')
        print(which)


def on_imageLocal(p1):
    if shared.debug:
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
        # print(f'FilePath = {pth}')
        shared.imagePath = pth
    # Load the image into the label
    load_image()


def on_popPaste(p1):
    if shared.debug:
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
        w.stNotes.insert(tk.END, root.clipboard_get())
    elif p1 == 7:
        w.Scrolledtext1.insert(tk.END, root.clipboard_get())
    elif p1 == 8:
        EntryIngredient.set(root.clipboard_get())
    else:
        pass


def on_popCopy(p1):
    if shared.debug:
        print(f'on_popCopy - {p1}')
    global eWidgets
    if p1 == 1:
        field_value = RecipeTitle.get()
    if p1 == 2:
        field_value = RecipeSource.get()
    if p1 == 3:
        field_value = RecipeServes.get()
    if p1 == 4:
        field_value = RecipeTotalTime.get()
    if p1 == 5:
        field_value = RecipeRating.get()
    if p1 == 6:
        field_value = w.stNotes.get("1.0", tk.END)
    if p1 == 7:
        field_value = w.Scrolledtext1.get("1.0", tk.END)
    if p1 == 8:
        field_value = EntryIngredient.get()
    else:
        pass
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(field_value)


def on_popClear(p1):
    if shared.debug:
        print(f'on_popClear - {p1}')
    global eWidgets
    if p1 == 1:
        RecipeTitle.set('')
    elif p1 == 2:
        RecipeSource.set('')
    elif p1 == 3:
        RecipeServes.set('')
    elif p1 == 4:
        RecipeTotalTime.set('')
    elif p1 == 5:
        RecipeRating.set('')
    elif p1 == 6:
        w.stNotes.delete('1.0', tk.END)
    elif p1 == 7:
        w.Scrolledtext1.delete('1.0', tk.END)
    elif p1 == 8:
        EntryIngredient.set('')
    else:
        pass


def on_entryKeyPress(e):
    if shared.debug:
        print('EntryKeyPress')
    if e.keysym == 'Return':
        on_btnAdd()


def on_listboxSelect(e):
    # print('on_listboxSelect')
    indx = w.Scrolledlistbox1.curselection()
    itm = w.Scrolledlistbox1.get(indx[0])
    # print(f'Index selected: {indx} - {itm}')
    EntryIngredient.set(itm)
    global ingindex
    ingindex = indx




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
    src = shared.imagePath
    w.Label1.configure(image=_img2)
    ti = RecipeTitle.get()
    d1 = ti.replace(" ", "")
    pos = src.rfind(".")

    ext = src[pos:]
    # fnstart = pos(src.rfind('/'))

    if ext == '.jpeg':
        ext = '.jpg'
    dst = './database/recipeimages/' + d1 + ext
    shared.imagePath = dst
    if os.path.exists(dst):
        pass
    else:
        print(f'Attemptying to copy {src} to {dst}')
        try:
            shutil.copyfile(src, dst)
            os.remove(src)
        except Exception:
            pass


def fill_form():
    global connection, cursor, datacheck
    clear_labels()
    # Get the recipe basics
    sql = f'SELECT * FROM recipes WHERE idRecipes = {shared.rectouse}'
    mainrec = list(cursor.execute(sql))
    if len(mainrec) > 0:
        # print(mainrec)
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
    # print(r[8])
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
    tlist = []
    if len(cats):
        for r in cats:
            tlist.append(r[1])

    w.Custom1.set(tlist)
    update_label()
    x = w.Custom1.get()

    datacheck.append(x)
    # ===================================
    shared.isDirty = False
    # if shared.debug:
        # print('Datacheck:')
        # print(datacheck)


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
    w.Scrolledlistbox1.bind('<<ListboxSelect>>', on_listboxSelect)
    global eWidgets
    eWidgets = [w.entryTitle, w.entrySource, w.entryServes, w.entryTotalTime, w.entryRating, w.stNotes, w.Scrolledtext1, w.entIngredient]


def get_ingredient_list():
    pass


def write_to_db():
    global connection, cursor
    # Get the data from the form
    title = RecipeTitle.get()
    source = RecipeSource.get()
    serves = RecipeServes.get()
    totaltime = RecipeTotalTime.get()
    rating = RecipeRating.get()
    notes = w.stNotes.get('1.0', tk.END)
    active = che49.get()
    # Create the sql statements and write them
    if shared.EditMode == 'Edit':
        # Use update for recipes, image and instructions tables
        # Delete and replace for ingredients and cats tables
        try:
            sql = ("UPDATE recipes SET "
                "RecipeText = {0}, RecipeSource = {1}, "
                "RecipeServes = {2}, TotalTime = {3}, "
                "RecipeRating = {4}, Notes = {5}, "
                "Active = {6} WHERE idRecipes = {7}").format(
                    quote(title),
                    quote(source),
                    quote(serves),
                    quote(totaltime),
                    quote(rating),
                    quote(notes),
                    active, shared.rectouse)
            # print(sql)
            isok = cursor.execute(sql)
            connection.commit()
            # ========================
            # Instructions
            # ========================
            sql = ("UPDATE instructions SET "
                   "InstructionsData = {0} WHERE RecipeID = {1}").format(
                   quote(w.Scrolledtext1.get(1.0, tk.END)),
                   shared.rectouse)
            # print(sql)
            isok = cursor.execute(sql)
            connection.commit()

            # ========================
            #  Ingredients
            # For ingredients and categories, we first need to delete the existing records
            # and then insert the new ones, since it would be alot of code to verify existance and positions
            # of any new records.
            # ========================
            sql = (f"DELETE FROM ingredients WHERE RecipeID = {shared.rectouse}")
            # print(sql)
            isok = cursor.execute(sql)
            connection.commit()
            # ========================
            # Now, write the records back in.
            ilist = w.Scrolledlistbox1.get(0, tk.END)
            for line in ilist:
                sql = ("INSERT INTO ingredients "
                    "(RecipeID,Ingredientitem) "
                    "VALUES ({0},{1})").format(
                    shared.rectouse, quote(line))
                # print(sql)
                cursor.execute(sql)
            connection.commit()

            # ========================
            #  Cats
            # ========================
            # Like ingredients, delete existing records, then insert the "new" ones.
            sql = (f"DELETE FROM images WHERE recipeID = {shared.rectouse}")
            # print(sql)
            cursor.execute(sql)
            connection.commit()
            checks = w.Custom1.get()
            # print(checks)
            for c in checks:
                sql = (
                    "INSERT INTO recipecategories (RecipeId, MainCatKey) VALUES ({1}, {0})".format(c[1], shared.rectouse))
                # print(sql)
                cursor.execute(sql)
            connection.commit()
            # ========================
            #  Image
            # ========================
            sql = (f'SELECT * FROM images WHERE recipeID = {shared.rectouse}')
            resp = list(cursor.execute(sql))
            # print(resp)
            if len(resp) > 0:

                sql = ("UPDATE images SET image = {1} WHERE recipeID = {0}").format(
                        shared.rectouse, quote(shared.imagePath))
            else:
                sql = ('INSERT INTO images (recipeID, image) '
                       'VALUES ({0}, {1})'.format(
                        shared.rectouse, quote(shared.imagePath)))
            print(sql)
            cursor.execute(sql)
            result = cursor.rowcount
            print(f'Result: {result}')
            connection.commit()

            msgTitle = 'Save Recipe Changes'
            msgMsg = 'All data saved'
            messagebox.showinfo(msgTitle, msgMsg)
        except Exception:
            print('write fail')
            msgTitle = 'Save Recipe Changes'
            msgMsg = 'An error occured writing data'
            messagebox.showerror(msgTitle, msgMsg)
    else:
        # Use Insert
        try:
            sql = ("Insert into recipes "
                "(RecipeText,RecipeSource,RecipeServes,TotalTime, RecipeRating, Notes, Active) "
                "VALUES ({0},{1},{2},{3},{4},{5},{6});").format(
                quote(title),
                quote(source),
                quote(serves),
                quote(totaltime),
                quote(rating),
                quote(notes),
                1)
            # Everything depends on the last_insert_rowid being available
            # so if this fails, we have to abort and have the user try again
            cursor.execute(sql)
            connection.commit()
            # LastRecord is the last id that was saved in the recipe table
            # We will use it to link the rest of the data to this recipe
            LastRecord = cursor.lastrowid
            # -----------------------
            # Write Instructions
            # -----------------------
            sql = ("Insert into instructions "
                    "(RecipeID,InstructionsData) "
                    "VALUES ({0},{1})").format(LastRecord,
                                                quote(
                                                    w.Scrolledtext1.get(
                                                        1.0, tk.END)))
            cursor.execute(sql)
            connection.commit()
            # -----------------------
            # Write ImageURL
            sql = ('INSERT INTO images (recipeID, image) '
                    'VALUES ({0}, {1})'.format(
                        LastRecord, quote(shared.imagePath)))
            cursor.execute(sql)
            connection.commit()
            # -----------------------
            # Write Ingredients
            # -----------------------
            ilist = w.Scrolledlistbox1.get(0, tk.END)
            for line in ilist:
                sql = ("INSERT INTO ingredients "
                    "(RecipeID,Ingredientitem) "
                    "VALUES ({0},{1})").format(
                    LastRecord, quote(line))
                cursor.execute(sql)
            connection.commit()
            # -----------------------
            # Write Categories
            # Get checked cateegories
            checks = w.Custom1.get()
            # print(checks)
            for c in checks:
                sql = (
                    "INSERT INTO recipecategories (RecipeId, MainCatKey) VALUES ({1}, {0})".format(c[1], LastRecord))
                cursor.execute(sql)
            connection.commit()
            msgTitle = 'Save Recipe Changes'
            msgMsg = 'All data saved'
            messagebox.showinfo(msgTitle, msgMsg)
        except Exception:
            print('Write Failed')
            msgTitle = 'Save Recipe Changes'
            msgMsg = 'An error occured writing data'
            messagebox.showerror(msgTitle, msgMsg)

        busyEnd()
        # -----------------------
        #  End of write_to_db
        # -----------------------


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
    shared.debug = False
    global datacheck
    datacheck = []
    shared.imagePath = ''
    global ingindex
    ingindex = None
    w.Label1.configure(text = 'Right click here to insert image...')
    # Fill the entry widget for testing purposes
    initialize_custom_widget()
    # Set the entry widgets bindings
    set_bindings()
    set_mode()
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
    version = '0.5.4'
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
    global is_child
    testmode = True
    # Use the following check to see if we are running as a child or standalone
    # attr = getattr(shared, 'remote', False)
    isok = check_attr(shared, 'remote')
    if isok is False:
        is_child = False
        if testmode == True:
            shared.testmode = True
            shared.EditMode = 'Edit'
            shared.rectouse = 118  # 108
            root.title(progname + " - Standalone mode - TEST Edit MODE!")
            fill_form()
        else:
            shared.EditMode = 'New'
            root.title(progname + " - Standalone mode - TEST New MODE")
            w.chkActive.configure(state='disabled')
            w.lblRecNumber.configure(state='disabled')
            w.Label11.configure(state='disabled')
            clear_labels()
    else:
        is_child = True
        if shared.EditMode == 'Edit':
            isok = check_attr(shared, 'rectouse')
            root.title(progname + ' - Edit Mode')
            fill_form()
        else:
            root.title(progname + ' - New Form')
            w.chkActive.configure(state='disabled')
            w.lblRecNumber.configure(state='disabled')
            w.Label11.configure(state='disabled')
            clear_labels()


def get_Custom_Cats():
    global connection, cursor
    sql = 'SELECT CatText, idCategoriesMain FROM categoriesmain order by CatText ASC'
    recs = list(cursor.execute(sql))
    if shared.debug:
        print(recs)
    return recs


def initialize_custom_widget():
    w.Custom1.cback = on_customClick
    # To use a single list of item names comment out the next line and
    # uncomment the second line down.
    ListInfo2 = get_Custom_Cats()
    w.Custom1.load(ListInfo2)
    w.Custom1.clear()


def set_mode():

    tbcolour = 'NavajoWhite3'
    w.stNotes.configure(background=tbcolour)
    w.Scrolledlistbox1.configure(background=tbcolour)
    w.Scrolledtext1.configure(background=tbcolour)
    widgetlist = [w.entryTitle, w.entrySource, w.entryServes, w.entryTotalTime, w.entryRating, w.entIngredient]
    for widg in widgetlist:
        widg.configure(background=tbcolour)


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
