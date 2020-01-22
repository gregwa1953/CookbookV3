#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.27p
#  in conjunction with Tcl version 8.6
#    Jan 22, 2020 08:24:26 AM CST  platform: Linux

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

import formEditor_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    formEditor_support.set_Tk_var()
    top = formEditor (root)
    formEditor_support.init(root, top)
    root.mainloop()

w = None
# Modified this routine per Don Rozen 1/22/20
def create_formEditor(rt, *args, **kwargs):   # (root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    # global w, w_win, rt
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = rt            # Replaces commented statement above.
    w = tk.Toplevel (root)
    # rt = root
    # w = tk.Toplevel (root)
    formEditor_support.set_Tk_var()
    top = formEditor (w)
    formEditor_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_formEditor():
    global w
    w.destroy()
    w = None

class formEditor:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {DejaVu Sans} -size 9"
        font13 = "-family {DejaVu Sans Mono} -size 9"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1139x773+425+152")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#919191")
        top.configure(highlightcolor="black")

        self.btnExit = tk.Button(top)
        self.btnExit.place(relx=0.87, rely=0.039, height=49, width=119)
        self.btnExit.configure(activebackground="#f9f9f9")
        self.btnExit.configure(command=formEditor_support.on_btnExit)
        self.btnExit.configure(font="-family {Ubuntu} -size 11 -weight bold -slant italic")
        self.btnExit.configure(text='''Exit''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.702, rely=0.168, height=300, width=299)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(borderwidth="2")
        self.Label1.configure(relief="ridge")
        self.Label1.configure(text='''Label''')

        self.entryTitle = tk.Entry(top)
        self.entryTitle.place(relx=0.237, rely=0.116,height=31, relwidth=0.435)
        self.entryTitle.configure(background="white")
        self.entryTitle.configure(font="-family {DejaVu Sans Mono} -size 9")
        self.entryTitle.configure(selectbackground="#c4c4c4")
        self.entryTitle.configure(textvariable=formEditor_support.RecipeTitle)

        self.entrySource = tk.Entry(top)
        self.entrySource.place(relx=0.237, rely=0.168, height=31, relwidth=0.435)

        self.entrySource.configure(background="white")
        self.entrySource.configure(font="-family {DejaVu Sans Mono} -size 9")
        self.entrySource.configure(selectbackground="#c4c4c4")
        self.entrySource.configure(textvariable=formEditor_support.RecipeSource)

        self.entryServes = tk.Entry(top)
        self.entryServes.place(relx=0.237, rely=0.22,height=31, relwidth=0.435)
        self.entryServes.configure(background="white")
        self.entryServes.configure(font="-family {DejaVu Sans Mono} -size 9")
        self.entryServes.configure(selectbackground="#c4c4c4")
        self.entryServes.configure(textvariable=formEditor_support.RecipeServes)

        self.entryTotalTime = tk.Entry(top)
        self.entryTotalTime.place(relx=0.237, rely=0.272, height=31
                , relwidth=0.435)
        self.entryTotalTime.configure(background="white")
        self.entryTotalTime.configure(font="-family {DejaVu Sans Mono} -size 9")
        self.entryTotalTime.configure(selectbackground="#c4c4c4")
        self.entryTotalTime.configure(textvariable=formEditor_support.RecipeTotalTime)

        self.entryRating = tk.Entry(top)
        self.entryRating.place(relx=0.237, rely=0.323, height=31, relwidth=0.435)

        self.entryRating.configure(background="white")
        self.entryRating.configure(font="-family {DejaVu Sans Mono} -size 9")
        self.entryRating.configure(selectbackground="#c4c4c4")
        self.entryRating.configure(textvariable=formEditor_support.RecipeRating)

        self.stNotes = ScrolledText(top)
        self.stNotes.place(relx=0.237, rely=0.375, relheight=0.123
                , relwidth=0.345)
        self.stNotes.configure(background="white")
        self.stNotes.configure(font=font12)
        self.stNotes.configure(insertborderwidth="3")
        self.stNotes.configure(selectbackground="#c4c4c4")
        self.stNotes.configure(wrap="word")

        self.chkActive = tk.Checkbutton(top)
        self.chkActive.place(relx=0.026, rely=0.039, relheight=0.027
                , relwidth=0.072)
        self.chkActive.configure(activebackground="#f9f9f9")
        self.chkActive.configure(anchor='w')
        self.chkActive.configure(background="#919191")
        self.chkActive.configure(borderwidth="0")
        self.chkActive.configure(command=formEditor_support.on_chkActive)
        self.chkActive.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.chkActive.configure(highlightbackground="#919191")
        self.chkActive.configure(justify='left')
        self.chkActive.configure(offrelief="flat")
        self.chkActive.configure(text='''Active''')
        self.chkActive.configure(variable=formEditor_support.che49)

        self.lblRecNumber = tk.Label(top)
        self.lblRecNumber.place(relx=0.211, rely=0.034, height=31, width=78)
        self.lblRecNumber.configure(activebackground="#f9f9f9")
        self.lblRecNumber.configure(relief="ridge")
        self.lblRecNumber.configure(text='''Label''')
        self.lblRecNumber.configure(textvariable=formEditor_support.RecordNumber)

        self.frameCustom = tk.Frame(top)
        self.frameCustom.place(relx=0.018, rely=0.608, relheight=0.369
                , relwidth=0.212)
        self.frameCustom.configure(relief='groove')
        self.frameCustom.configure(borderwidth="2")
        self.frameCustom.configure(relief="groove")

        self.Custom1 = formEditor_support.Custom(self.frameCustom)
        self.Custom1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.frameIngredients = tk.Frame(top)
        self.frameIngredients.place(relx=0.246, rely=0.608, relheight=0.369
                , relwidth=0.32)
        self.frameIngredients.configure(relief='groove')
        self.frameIngredients.configure(borderwidth="2")
        self.frameIngredients.configure(relief="groove")

        self.Scrolledlistbox1 = ScrolledListBox(self.frameIngredients)
        self.Scrolledlistbox1.place(relx=0.0, rely=0.0, relheight=1.0
                , relwidth=1.0)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font=font13)
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")

        self.frameInstructions = tk.Frame(top)
        self.frameInstructions.place(relx=0.579, rely=0.608, relheight=0.369
                , relwidth=0.399)
        self.frameInstructions.configure(relief='groove')
        self.frameInstructions.configure(borderwidth="2")
        self.frameInstructions.configure(relief="groove")

        self.Scrolledtext1 = ScrolledText(self.frameInstructions)
        self.Scrolledtext1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=font12)
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(wrap="word")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.018, rely=0.446, relheight=0.149
                , relwidth=0.212)
        self.Message1.configure(borderwidth="2")
        self.Message1.configure(relief="ridge")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(textvariable=formEditor_support.SelectedCats)
        self.Message1.configure(width=241)

        self.btnSave = tk.Button(top)
        self.btnSave.place(relx=0.729, rely=0.039, height=49, width=119)
        self.btnSave.configure(activebackground="#f9f9f9")
        self.btnSave.configure(command=formEditor_support.on_btnSave)
        self.btnSave.configure(font="-family {Ubuntu} -size 11 -weight bold -slant italic")
        self.btnSave.configure(text='''Save''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.255, rely=0.569, height=19, width=96)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#919191")
        self.Label2.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label2.configure(text='''Ingredients:''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.588, rely=0.569, height=19, width=124)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#919191")
        self.Label3.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label3.configure(text='''Instructions:''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.105, rely=0.116, height=19, width=143)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='e')
        self.Label4.configure(background="#919191")
        self.Label4.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label4.configure(text='''Title:''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.105, rely=0.168, height=20, width=145)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='e')
        self.Label5.configure(background="#919191")
        self.Label5.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label5.configure(text='''Source:''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.105, rely=0.22, height=20, width=143)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='e')
        self.Label6.configure(background="#919191")
        self.Label6.configure(font="-family {Trebuchet MS} -size 10 -weight bold")
        self.Label6.configure(text='''Servings:''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.105, rely=0.273, height=20, width=143)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='e')
        self.Label7.configure(background="#919191")
        self.Label7.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label7.configure(text='''Total Time:''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.105, rely=0.321, height=20, width=143)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(anchor='e')
        self.Label8.configure(background="#919191")
        self.Label8.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label8.configure(text='''Rating:''')

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.105, rely=0.375, height=19, width=144)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(anchor='e')
        self.Label9.configure(background="#919191")
        self.Label9.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label9.configure(text='''Description/Notes:''')

        self.Label10 = tk.Label(top)
        self.Label10.place(relx=0.035, rely=0.414, height=20, width=107)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#919191")
        self.Label10.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label10.configure(text='''Categories:''')

        self.Label11 = tk.Label(top)
        self.Label11.place(relx=0.088, rely=0.039, height=20, width=128)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(anchor='e')
        self.Label11.configure(background="#919191")
        self.Label11.configure(font="-family {Ubuntu} -size 10 -weight bold")
        self.Label11.configure(text='''Record Number:''')

        self.btnDelete = tk.Button(top)
        self.btnDelete.place(relx=0.404, rely=0.556, height=34, width=34)
        self.btnDelete.configure(command=formEditor_support.on_btnDelete)
        photo_location = os.path.join(prog_location,"./images/32/list-remove.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.btnDelete.configure(image=_img0)
        self.btnDelete.configure(text='''Button''')
        tooltip_font = "-family {DejaVu Sans} -size 9"
        ToolTip(self.btnDelete, tooltip_font, '''Delete an ingredient''', delay=0.5)

        self.btnAdd = tk.Button(top)
        self.btnAdd.place(relx=0.36, rely=0.556, height=34, width=34)
        self.btnAdd.configure(command=formEditor_support.on_btnAdd)
        photo_location = os.path.join(prog_location,"./images/32/list-add.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.btnAdd.configure(image=_img1)
        self.btnAdd.configure(text='''Button''')
        tooltip_font = "-family {DejaVu Sans} -size 9"
        ToolTip(self.btnAdd, tooltip_font, '''Add an ingredient''', delay=0.5)

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





