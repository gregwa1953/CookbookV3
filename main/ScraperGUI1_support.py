#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.27o
#  in conjunction with Tcl version 8.6
#    Jan 16, 2020 09:00:01 AM CST  platform: Linux
#    Jan 19, 2020 03:25:29 PM CST  platform: Linux
#    Jan 20, 2020 05:06:04 AM CST  platform: Linux
#    Jan 20, 2020 09:52:23 AM CST  platform: Linux
# ======================================================
# Written by G.D. Walters
# ------------------------------------------------------
# Last modification date: 20 January, 2020
# ======================================================
import sys
from recipe_scrapers import scrape_me, SCRAPERS
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
from urllib.parse import urlparse

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


def on_btnSaveToDB():
    if shared.debug:
        print('ScraperGUI1_support.on_btnSaveToDB')
    sys.stdout.flush()
    # Check to see if there are any categories set
    lst = w.Custom1.get()
    print(len(lst))
    if len(lst):
        WriteToDb()
    else:
        title = 'No Categories'
        txt = 'There are no categories selected.  Do you still want to save to database?'
        resp = messagebox.askyesno(title, txt)
        if resp:
            WriteToDb()


def set_Tk_var():
    global msgCategories
    msgCategories = tk.StringVar()
    msgCategories.set('Message')

    global EntryWebsite
    EntryWebsite = tk.StringVar()
    global sRecipeTitle
    sRecipeTitle = tk.StringVar()
    sRecipeTitle.set('Label')
    global sTotalTime
    sTotalTime = tk.StringVar()
    sTotalTime.set('Label')
    global sYields
    sYields = tk.StringVar()
    sYields.set('Label')
    global sImageURL
    sImageURL = tk.StringVar()
    sImageURL.set('Label')


def on_btnExit():
    if shared.debug:
        print('ScraperGUI1_support.on_btnExit')
        sys.stdout.flush()
    isok = check_attr(shared, 'remote')
    if isok:
        cbv3Main_support.show_me()
        hide_me()
    else:
        destroy_window()


def get_image_from_web(url):
    # Attempt to get image from url and place it in w.lblImage
    global _img2
    pic_url = url
    if shared.debug:
        print(f'Attempting to get {url}')
    try:
        with open('pic1.jpg', 'wb') as handle:
            response = requests.get(pic_url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
        # with open('pic1.jpg', 'wb') as handle:
        #     user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        #     headers = {'User-Agent': user_agent}
        #     # response = requests.get(pic_url, headers=headers, stream=True)
        #     response = requests.get(pic_url, stream=True)

        # for block in response.iter_content(1024):
        #     if not block:
        #         break

        #     handle.write(block)

        jpgfile = Image.open('pic1.jpg')
        jpgfile.save('local_image.png')

        original = Image.open('local_image.png')
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
        _img1 = original.resize((int(w2), int(h2)), Image.ANTIALIAS)
        _img2 = ImageTk.PhotoImage(_img1)
        w.lblImage.configure(image=_img2)
        src = 'local_image.png'
        d1 = shared.title.replace(" ", "")
        d1 = d1.replace("!", '')
        dst = path1 + '/database/recipeimages/' + d1 + ".png"
        shared.imgname = '/database/recipeimages/' + d1 + '.png'
        print(f'Attemptying to copy {src} to {dst}')
        shutil.copyfile(src, dst)
        # os.remove(original)
        # os.remove(jpfile)
        # os.rename(src, dst)
    except Exception:
        boxTitle = "Image Error"
        boxMessage = "An error occured getting the image."
        messagebox.showerror(boxTitle, boxMessage)
        print("An error occured getting the image")
        _img2 = None
        w.lblImage.configure(image=_img2)


def on_btnGo():
    url_to_get = EntryWebsite.get()
    # ======================================================
    # Check the url to see if it is currently supported by scraper
    #    Hopefully, this will save the user frustration
    # ------------------------------------------------------------
    # GDW 28 January 2020
    # ======================================================
    domain = urlparse(url_to_get).netloc
    domain = domain.replace("www.", "")
    oktorun = True
    # for l in SCRAPERS:
    #     print(l)
    if domain in SCRAPERS:
        print('ok to run')
    else:
        print('domain not supported')
        oktorun = False
    # ======================================================
    if oktorun:
        busyStart()
        print('ScraperGUI1_support.on_btnGo')
        url_to_get = EntryWebsite.get()
        clear_form()
        if shared.debug:
            print(f'Attempting to contact {EntryWebsite.get()}')
        sys.stdout.flush()
        # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        # headers = {'User-Agent': user_agent}
        scraper = scrape_me(url_to_get)
        shared.title = scraper.title()
        shared.total_time = scraper.total_time()
        shared.yields = scraper.yields()
        shared.ingredients = scraper.ingredients()
        shared.instructions = scraper.instructions()
        try:
            shared.description = scraper.description()
        except Exception:
            shared.description = ''
        try:
            imgpath = scraper.image()
            if imgpath != None:
                shared.image = scraper.image()
        except:
            shared.image = None

        if shared.debug:
            print(shared.title)
            print(shared.total_time)
            print(shared.yields)
            print(shared.ingredients)
            print(shared.instructions)
            print(shared.description)
            print(shared.image)
        # get_image_from_web(image)
        # ======================================================
        # Fill in the GUI widgets
        # ======================================================
        fill_form()
        # except Exception:
        #     print('oh-oh')
        busyEnd()
    else:
        titl = 'Cookbook Scraper'
        msg = f'{domain} is not currently supported by the recipe scraper.'
        messagebox.showerror(titl, msg)


def on_popPaste(p1):
    # if shared.debug:
    #     print('PopPaste')
    print('PopPaste')
    if p1 == 1:
        EntryWebsite.set('')
        clear_form()
        EntryWebsite.set(root.clipboard_get())  # type='UTF8_String'))
        on_btnGo()
    elif p1 == 2:
        w.stDescription.insert(tk.END, root.clipboard_get())


def on_popClear(p1):
    if shared.debug:
        print('PopClear')
    if p1 == 1:
        EntryWebsite.set('')
    elif p1 == 2:
        w.stDescription.delete('1.0', tk.END)


def on_popCopy(p1):
    if shared.debug:
        print('PopCopy')
    # get field value from event, but remove line return at end
    if p1 == 1:
        field_value = EntryWebsite.get()  # "1.0", 'end-1c')
        root.clipboard_clear()  # clear clipboard contents
        root.clipboard_append(field_value)
    elif p1 == 2:
        field_value = w.stDescription.get('1.0', tk.END)


def on_entryKeyPress(e):
    if shared.debug:
        print('EntryKeyPress')
    if e.keysym == 'Return':
        on_btnGo()


def on_customClick(s=None):
    if shared.debug:
        print('on_customClick')
    update_label()
    # keep a list for updating database


def fill_form():
    if shared.debug:
        print('Into fill_form')
    sRecipeTitle.set(shared.title)
    sTotalTime.set(f'{shared.total_time} minutes')
    sYields.set(shared.yields)
    w.stDescription.insert(tk.END, shared.description)
    sImageURL.set(shared.image)
    if shared.image != None:
        get_image_from_web(shared.image)
    else:
        titl = 'Image issue'
        msg = 'The scraper was not able to get the image.'
        messagebox.showerror(titl, msg)
    # ingredients
    load_ingredients()
    # instructions
    load_instructions()


def clear_form():
    w.Scrolledtext1.delete('1.0', tk.END)
    w.Scrolledlistbox1.delete(0, tk.END)
    w.stDescription.delete('1.0', tk.END)
    w.Custom1.clear()
    msgCategories.set('')
    sRecipeTitle.set('')
    sTotalTime.set('')
    sYields.set('')
    sImageURL.set('')


def load_ingredients():
    for line in shared.ingredients:
        w.Scrolledlistbox1.insert('end', line)


def load_instructions():
    w.Scrolledtext1.insert('end', shared.instructions)


def testdb():
    global cursor
    global connection

    sql = 'SELECT * from recipes'
    recs = list(cursor.execute(sql))
    if len(recs):
        print(len(recs))


def WriteToDb():
    global connection, cursor

    busyStart()
    try:
        cur = cursor
        NewRecipe = True
        if NewRecipe is True:
            # -----------------------
            # Write Title,Source and Servings - Retain Record Number
            # -----------------------
            sql = ("Insert into recipes "
                   "(RecipeText,RecipeSource,RecipeServes,TotalTime,Notes,Active) "
                   "VALUES ({0},{1},{2},{3},{4},{5});").format(
                quote(sRecipeTitle.get()),
                quote(EntryWebsite.get()),
                quote(sYields.get()),
                quote(sTotalTime.get()),
                quote(w.stDescription.get('1.0', tk.END)),
                1)

            # Everything depends on the last_insert_rowid being available
            # so if this fails, we have to abort and have the user try again
            cur.execute(sql)
            connection.commit()
            if shared.debug:
                print('Main Record Written')
            # LastRecord is the last id that was saved in the recipe table
            # We will use it to link the rest of the data to this recipe
            LastRecord = cur.lastrowid
            shared.rectouse = LastRecord
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

            cur.execute(sql)
            connection.commit()
            if shared.debug:
                print('Instructions written')

            # -----------------------
            # Write Ingredients
            # -----------------------

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

            for c in checks:
                sql = (
                    "INSERT INTO recipecategories (RecipeId, MainCatKey) VALUES ({1}, {0})".format(c[1], LastRecord))
                print(sql)
                cur.execute(sql)
            connection.commit()

            # -----------------------
            # Write ImageURL
            if shared.imgname == None:
                pass
            else:
                sql = ('INSERT INTO images (recipeID, image) '
                       'VALUES ({0}, {1})'.format(
                           LastRecord, quote(shared.imgname)))
                cur.execute(sql)
                connection.commit()
                if shared.debug:
                    print('Image Written')
            # -----------------------
            # connection.commit()
            messagebox.showinfo('Data Actions', 'Recipe Saved')
            busyEnd()
    except:
        busyEnd()
        messagebox.showerror(
            'Error', 'Something went wrong when trying to write to database!')

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


def fix_path():
    global path1
    if "main" in path1:
        pass
    else:
        path1 = path1 + "/main"


def start_up():
    global connection
    global cursor

    connection = sqlite3.Connection(path1 + "/database/cookbook-original.db")
    cursor = connection.cursor()
    # Setup binding for entry widget
    w.Entry1.bind('<Button-3>', lambda e: w.popup1(e, 1))
    w.Entry1.bind('<KeyRelease>', lambda e: on_entryKeyPress(e))
    w.stDescription.bind('<Button-3>', lambda e: w.popup1(e, 2))
    # set up for cursors
    global busyCursor, preBusyCursors, busyWidgets
    busyCursor = 'watch'
    preBusyCursors = None
    busyWidgets = (root, )
    # Centre the screen
    centre_screen(1211, 822)
    # Clear the text from the image label
    w.lblImage.configure(text='')
    # Set up the debug flag
    shared.debug = False
    # Fill the entry widget for testing purposes
    initialize_custom_widget()
    EntryWebsite.set(
        'Right click here to paste a website URL from the clipboard')
    set_mode()
    clear_form()
    shared.debug = False


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # My init code starts...
    # ======================================================
    global version
    version = '0.4.0'
    pv = platform.python_version()
    print(f"Running under Python {pv}")
    # Set the path for the icon files
    global path1
    path1 = os.getcwd()
    fix_path()
    print(path1)
    print(f"Version: {version}")
    start_up()
    root.title("Greg's Recipe Website Scraper")


def clear_label():
    msgCategories.set('')


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
    msgCategories.set(s)


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
    clear_label()
    set_labels()

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


def set_mode():
    tbcolour = 'gray72'
    widgetlist = [root, w.btnExit, w.Label1, w.Entry1, w.lblTitle, w.lblTotalTime,
                  w.lblYields, w.lblImageURL, w.btnGo, w.Label2, w.Label3, w.Label4,
                  w.Label5, w.lblImage, w.Label7, w.Label8, w.btnSaveToDB, w.Label8,
                  w.frameCustomWidget, w.Message1, w.stDescription, w.Label6, w.Label8_1]
    l = len(widgetlist)
    for widg in widgetlist:
        widg.configure(background="#919191")
    print('finished applying backgrounds')
    w.Scrolledlistbox1.configure(background=tbcolour)
    w.Scrolledtext1.configure(background=tbcolour)
    w.stDescription.configure(background=tbcolour)

# =================================================================
# Window stuff
# =================================================================


def show_me():
    root.deiconify()
    root.attributes("-topmost", True)
    # reload treeview here


def hide_me():
    cbv3Main_support.show_me()
    root.withdraw()


def set_icon():
    # ======================================================
    # Sets the application icon...
    # ======================================================
    # global p1
    # p1 = tk.Image("photo", file='images/chef.png')
    global path1
    shared.p1 = ImageTk.PhotoImage(file=path1 + 'images/chef.png')
    root.tk.call('wm', 'iconphoto', root._w, shared.p1)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


# Custom = tk.Frame  # To be updated by user with name of custom widget.
Custom = ScrolledCheckedListBox

if __name__ == '__main__':
    import ScraperGUI1
    ScraperGUI1.vp_start_gui()
