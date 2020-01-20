#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.27o
#  in conjunction with Tcl version 8.6
#    Jan 19, 2020 07:59:55 PM CST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import cbv3Main_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    cbv3Main_support.set_Tk_var()
    top = formCookbookMain (root)
    cbv3Main_support.init(root, top)
    root.mainloop()

w = None
def create_formCookbookMain(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    cbv3Main_support.set_Tk_var()
    top = formCookbookMain (w)
    cbv3Main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_formCookbookMain():
    global w
    w.destroy()
    w = None

class formCookbookMain:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans Mono} -size 9"
        font16 = "-family {Liberation Sans} -size 9 -weight bold"
        font9 = "-family {DejaVu Sans} -size 9"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1270x861+248+56")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1, 1)
        top.title("Greg's Cookbook v3")
        top.configure(highlightcolor="black")

        self.frameToolbar = tk.Frame(top)
        self.frameToolbar.place(relx=0.002, rely=0.002, relheight=0.058
                , relwidth=0.997)
        self.frameToolbar.configure(relief='ridge')
        self.frameToolbar.configure(borderwidth="3")
        self.frameToolbar.configure(relief="ridge")

        self.btnExit = tk.Button(self.frameToolbar)
        self.btnExit.place(relx=0.956, rely=0.12, height=32, width=32)
        self.btnExit.configure(activebackground="#f9f9f9")
        self.btnExit.configure(command=cbv3Main_support.on_btnExit)
        self.btnExit.configure(font="-family {DejaVu Sans} -size 10 -weight bold -slant italic")
        photo_location = os.path.join(prog_location,"./images/32/app-exit.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.btnExit.configure(image=_img0)
        self.btnExit.configure(text='''Exit''')

        self.btnAdd = tk.Button(self.frameToolbar)
        self.btnAdd.place(relx=0.22, rely=0.06, height=38, width=38)
        self.btnAdd.configure(activebackground="#f9f9f9")
        self.btnAdd.configure(command=cbv3Main_support.on_btnAdd)
        photo_location = os.path.join(prog_location,"./images/32/list-add.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.btnAdd.configure(image=_img1)
        self.btnAdd.configure(text='''Button''')
        tooltip_font = "-family {DejaVu Sans} -size 9"
        ToolTip(self.btnAdd, tooltip_font, '''Add a new recipe''', delay=0.5)

        self.btnDelete = tk.Button(self.frameToolbar)
        self.btnDelete.place(relx=0.264, rely=0.08, height=38, width=38)
        self.btnDelete.configure(activebackground="#f9f9f9")
        self.btnDelete.configure(command=cbv3Main_support.on_btnDelete)
        photo_location = os.path.join(prog_location,"./images/32/list-remove.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.btnDelete.configure(image=_img2)
        self.btnDelete.configure(text='''Button''')
        tooltip_font = "-family {DejaVu Sans} -size 9"
        ToolTip(self.btnDelete, tooltip_font, '''Delete the current recipe''', delay=0.5)

        self.btnEdit = tk.Button(self.frameToolbar)
        self.btnEdit.place(relx=0.326, rely=0.06, height=38, width=38)
        self.btnEdit.configure(activebackground="#f9f9f9")
        self.btnEdit.configure(command=cbv3Main_support.on_btnEdit)
        photo_location = os.path.join(prog_location,"./images/32/edit-paste.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.btnEdit.configure(image=_img3)
        self.btnEdit.configure(text='''Button''')
        tooltip_font = "-family {DejaVu Sans} -size 9"
        ToolTip(self.btnEdit, tooltip_font, '''Edit the current recipe''', delay=0.5)

        self.btnScrape = tk.Button(self.frameToolbar)
        self.btnScrape.place(relx=0.15, rely=0.1, height=38, width=38)
        self.btnScrape.configure(activebackground="#f9f9f9")
        self.btnScrape.configure(command=cbv3Main_support.on_btnScrape)
        photo_location = os.path.join(prog_location,"./images/32/internet.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.btnScrape.configure(image=_img4)
        self.btnScrape.configure(text='''Button''')
        tooltip_font = "-family {DejaVu Sans} -size 9"
        ToolTip(self.btnScrape, tooltip_font, '''Scrape a web page''', delay=0.5)

        self.frameStatus = tk.Frame(top)
        self.frameStatus.place(relx=0.002, rely=0.941, relheight=0.058
                , relwidth=0.997)
        self.frameStatus.configure(relief='ridge')
        self.frameStatus.configure(borderwidth="3")
        self.frameStatus.configure(relief="ridge")

        self.lblTimeDisplay = tk.Label(self.frameStatus)
        self.lblTimeDisplay.place(relx=0.916, rely=0.2, height=29, width=86)
        self.lblTimeDisplay.configure(activebackground="#f9f9f9")
        self.lblTimeDisplay.configure(text='''Label''')
        self.lblTimeDisplay.configure(textvariable=cbv3Main_support.TimeDisp)

        self.frameNavigate = tk.Frame(top)
        self.frameNavigate.place(relx=0.002, rely=0.06, relheight=0.879
                , relwidth=0.276)
        self.frameNavigate.configure(relief='ridge')
        self.frameNavigate.configure(borderwidth="3")
        self.frameNavigate.configure(relief="ridge")

        self.Frame2 = tk.Frame(self.frameNavigate)
        self.Frame2.place(relx=0.006, rely=0.729, relheight=0.271
                , relwidth=0.989)
        self.Frame2.configure(relief='ridge')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="ridge")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.029, rely=0.049, height=21, width=81)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(font="-family {DejaVu Sans} -size 10 -weight bold -slant italic")
        self.Label1.configure(text='''Search:''')

        self.rbTitle = tk.Radiobutton(self.Frame2)
        self.rbTitle.place(relx=0.116, rely=0.244, relheight=0.102
                , relwidth=0.266)
        self.rbTitle.configure(activebackground="#f9f9f9")
        self.rbTitle.configure(anchor='w')
        self.rbTitle.configure(command=cbv3Main_support.on_rbClick)
        self.rbTitle.configure(justify='left')
        self.rbTitle.configure(text='''Title''')
        self.rbTitle.configure(value="0")
        self.rbTitle.configure(variable=cbv3Main_support.selectedButton)

        self.rbCategories = tk.Radiobutton(self.Frame2)
        self.rbCategories.place(relx=0.116, rely=0.39, relheight=0.102
                , relwidth=0.324)
        self.rbCategories.configure(activebackground="#f9f9f9")
        self.rbCategories.configure(anchor='w')
        self.rbCategories.configure(command=cbv3Main_support.on_rbClick)
        self.rbCategories.configure(justify='left')
        self.rbCategories.configure(text='''Category''')
        self.rbCategories.configure(value="2")
        self.rbCategories.configure(variable=cbv3Main_support.selectedButton)

        self.rbIngredients = tk.Radiobutton(self.Frame2)
        self.rbIngredients.place(relx=0.116, rely=0.537, relheight=0.102
                , relwidth=0.399)
        self.rbIngredients.configure(activebackground="#f9f9f9")
        self.rbIngredients.configure(anchor='w')
        self.rbIngredients.configure(command=cbv3Main_support.on_rbClick)
        self.rbIngredients.configure(justify='left')
        self.rbIngredients.configure(text='''Ingredients''')
        self.rbIngredients.configure(value="1")
        self.rbIngredients.configure(variable=cbv3Main_support.selectedButton)

        self.Checkbutton1 = tk.Checkbutton(self.Frame2)
        self.Checkbutton1.place(relx=0.523, rely=0.244, relheight=0.102
                , relwidth=0.327)
        self.Checkbutton1.configure(activebackground="#f9f9f9")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(command=cbv3Main_support.on_chkClick)
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Show All''')
        self.Checkbutton1.configure(variable=cbv3Main_support.che46)
        tooltip_font = "-family {DejaVu Sans} -size 9"
        ToolTip(self.Checkbutton1, tooltip_font, '''Show Deleted Records as well''', delay=0.5)

        self.Entry1 = tk.Entry(self.Frame2)
        self.Entry1.place(relx=0.116, rely=0.732,height=21, relwidth=0.685)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="-family {DejaVu Sans Mono} -size 9")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(state='disabled')
        self.Entry1.configure(textvariable=cbv3Main_support.EntryText)
        self.Entry1.bind('<KeyRelease>',lambda e:cbv3Main_support.on_Entry_Return(e))

        self.Frame3 = tk.Frame(self.frameNavigate)
        self.Frame3.place(relx=0.006, rely=0.004, relheight=0.725
                , relwidth=0.989)
        self.Frame3.configure(relief='ridge')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="ridge")

        self.style.configure('Treeview',  font=font16)
        self.Scrolledtreeview1 = ScrolledTreeView(self.Frame3)
        self.Scrolledtreeview1.place(relx=0.0, rely=0.0, relheight=0.998
                , relwidth=0.997)
        self.Scrolledtreeview1.configure(columns="Col1")
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0",text="Tree")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="165")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Col1")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="166")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.276, rely=0.06, relheight=0.88, relwidth=0.722)
        self.Frame1.configure(relief='ridge')
        self.Frame1.configure(borderwidth="3")
        self.Frame1.configure(relief="ridge")

        self.Scrolledtext1 = ScrolledText(self.Frame1)
        self.Scrolledtext1.place(relx=0.441, rely=0.541, relheight=0.455
                , relwidth=0.556)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=font9)
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(wrap="none")

        self.Scrolledlistbox1 = ScrolledListBox(self.Frame1)
        self.Scrolledlistbox1.place(relx=0.004, rely=0.54, relheight=0.451
                , relwidth=0.432)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font=font10)
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")

        self.lblTitle = tk.Label(self.Frame1)
        self.lblTitle.place(relx=0.022, rely=0.04, height=39, width=556)
        self.lblTitle.configure(activebackground="#f9f9f9")
        self.lblTitle.configure(font="-family {DejaVu Sans} -size 14 -weight bold -slant italic")
        self.lblTitle.configure(relief="ridge")
        self.lblTitle.configure(text='''Label''')
        self.lblTitle.configure(textvariable=cbv3Main_support.RecipeTitle)

        self.lblImage = tk.Label(self.Frame1)
        self.lblImage.place(relx=0.654, rely=0.026, height=300, width=300)
        self.lblImage.configure(activebackground="#f9f9f9")
        self.lblImage.configure(borderwidth="2")
        self.lblImage.configure(relief="ridge")
        self.lblImage.configure(text='''Label-Image''')

        self.lblSource = tk.Label(self.Frame1)
        self.lblSource.place(relx=0.131, rely=0.106, height=29, width=456)
        self.lblSource.configure(activebackground="#f9f9f9")
        self.lblSource.configure(font="-family {DejaVu Sans} -size 11 -weight bold -slant italic")
        self.lblSource.configure(relief="ridge")
        self.lblSource.configure(text='''Label''')
        self.lblSource.configure(textvariable=cbv3Main_support.RecipeSource)

        self.lblServings = tk.Label(self.Frame1)
        self.lblServings.place(relx=0.131, rely=0.158, height=29, width=456)
        self.lblServings.configure(activebackground="#f9f9f9")
        self.lblServings.configure(font="-family {DejaVu Sans} -size 10 -weight bold -slant italic")
        self.lblServings.configure(relief="ridge")
        self.lblServings.configure(text='''Label''')
        self.lblServings.configure(textvariable=cbv3Main_support.RecipeServings)

        self.msgNotes = tk.Message(self.Frame1)
        self.msgNotes.place(relx=0.131, rely=0.224, relheight=0.202
                , relwidth=0.496)
        self.msgNotes.configure(relief="ridge")
        self.msgNotes.configure(text='''Message''')
        self.msgNotes.configure(textvariable=cbv3Main_support.RecipeNotes)
        self.msgNotes.configure(width=455)

        self.msgCategories = tk.Message(self.Frame1)
        self.msgCategories.place(relx=0.098, rely=0.462, relheight=0.057
                , relwidth=0.878)
        self.msgCategories.configure(relief="ridge")
        self.msgCategories.configure(text='''Message''')
        self.msgCategories.configure(textvariable=cbv3Main_support.RecipeCategories)
        self.msgCategories.configure(width=805)

        self.lblID = tk.Label(self.Frame1)
        self.lblID.place(relx=0.022, rely=0.475, height=19, width=46)
        self.lblID.configure(text='''Label''')
        self.lblID.configure(textvariable=cbv3Main_support.IdLableShow)

# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





