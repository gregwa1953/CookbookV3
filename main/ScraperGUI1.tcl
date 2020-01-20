#############################################################################
# Generated by PAGE version 4.27o
#  in conjunction with Tcl version 8.6
#  Jan 20, 2020 09:52:07 AM CST  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans} -size 9"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 9"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 9"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 9"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set desc "-family {Liberation Sans} -size 9 -weight bold"
set vTcl(actual_gui_font_treeview_desc) $desc
set vTcl(actual_gui_font_treeview_name) [font create {*}$desc]
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    menu .pop43 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont -foreground black \
        -tearoff 1 
    vTcl:DefineAlias ".pop43" "Popupmenu1" vTcl:WidgetProc "" 1
    .pop43 add command \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command {#on_popPaste} \
        -font {-family {DejaVu Sans} -size 9} \
        -foreground $vTcl(pr,menufgcolor) -label Paste 
    .pop43 add separator \
        -background $vTcl(actual_gui_bg) 
    .pop43 add command \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command {#on_popCopy} \
        -font {-family {DejaVu Sans} -size 9} \
        -foreground $vTcl(pr,menufgcolor) -label Copy 
    .pop43 add separator \
        -background $vTcl(actual_gui_bg) 
    .pop43 add command \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command {#on_popClear} \
        -font {-family {DejaVu Sans} -size 9} \
        -foreground $vTcl(pr,menufgcolor) -label Clear 

proc vTclWindow.top43 {base} {
    global vTcl
    if {$base == ""} {
        set base .top43
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1211x822+372+122
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Greg's Recipe Website Scraper Test"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    button $top.but44 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnExit \
        -font {-family {Ubuntu} -size 11 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Exit 
    vTcl:DefineAlias "$top.but44" "btnExit" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Website: 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent46 \
        -background white -font $vTcl(actual_gui_font_fixed_desc) \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable EntryWebsite -width 596 
    vTcl:DefineAlias "$top.ent46" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable sRecipeTitle 
    vTcl:DefineAlias "$top.lab47" "lblTitle" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable sTotalTime 
    vTcl:DefineAlias "$top.lab48" "lblTotalTime" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable sYields 
    vTcl:DefineAlias "$top.lab49" "lblYields" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr50 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.scr50" "Scrolledlistbox1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr50.01 configure -background white \
        -font font10 \
        -foreground black \
        -height 3 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr51 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr51" "Scrolledtext1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr51.01 configure -background white \
        -font font9 \
        -foreground black \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap word
    label $top.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable sImageURL -wraplength 450 
    vTcl:DefineAlias "$top.lab53" "lblImageURL" vTcl:WidgetProc "Toplevel1" 1
    button $top.but54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnGo \
        -font {-family {Ubuntu} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Scrape 
    vTcl:DefineAlias "$top.but54" "btnGo" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab55 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Title: 
    vTcl:DefineAlias "$top.lab55" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab56 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Total Time:} 
    vTcl:DefineAlias "$top.lab56" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Yields: 
    vTcl:DefineAlias "$top.lab57" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Image URL:} 
    vTcl:DefineAlias "$top.lab58" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label 
    vTcl:DefineAlias "$top.lab59" "lblImage" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab60 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Ingredients: 
    vTcl:DefineAlias "$top.lab60" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab61 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Instructions: 
    vTcl:DefineAlias "$top.lab61" "Label8" vTcl:WidgetProc "Toplevel1" 1
    button $top.but43 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnSaveToDB \
        -font {-family {Ubuntu} -size 11 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Save To Database} 
    vTcl:DefineAlias "$top.but43" "btnSaveToDB" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Categories: 
    vTcl:DefineAlias "$top.lab44" "Label8_1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra45 \
        -borderwidth 3 -relief sunken -background $vTcl(actual_gui_bg) \
        -height 305 -width 295 
    vTcl:DefineAlias "$top.fra45" "frameCustomWidget" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra45
    vTcl::widgets::ttk::custom::CreateCmd $site_3_0.cus46 \
        -background $vTcl(actual_gui_bg) -height 291 -highlightcolor black \
        -width 286 
    vTcl:DefineAlias "$site_3_0.cus46" "Custom1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.cus46 \
        -in $site_3_0 -x 0 -relx 0.01 -y 0 -rely 0.01 -width 0 \
        -relwidth 0.976 -height 0 -relheight 0.977 -anchor nw \
        -bordermode ignore 
    message $top.mes47 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Message -textvariable msgCategories -width 295 
    vTcl:DefineAlias "$top.mes47" "Message1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but44 \
        -in $top -x 0 -relx 0.865 -y 0 -rely 0.038 -width 87 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 0 -relx 0.038 -y 0 -rely 0.088 -width 0 -relwidth 0.102 \
        -height 0 -relheight 0.024 -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 0 -relx 0.154 -y 0 -rely 0.081 -width 596 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.154 -y 0 -rely 0.139 -width 0 -relwidth 0.505 \
        -height 0 -relheight 0.038 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.154 -y 0 -rely 0.189 -width 0 -relwidth 0.227 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.154 -y 0 -rely 0.239 -width 0 -relwidth 0.227 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
    place $top.scr50 \
        -in $top -x 0 -relx 0.273 -y 0 -rely 0.584 -width 0 -relwidth 0.277 \
        -height 0 -relheight 0.369 -anchor nw -bordermode ignore 
    place $top.scr51 \
        -in $top -x 0 -relx 0.562 -y 0 -rely 0.584 -width 0 -relwidth 0.41 \
        -height 0 -relheight 0.372 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.154 -y 0 -rely 0.29 -width 0 -relwidth 0.477 \
        -height 0 -relheight 0.088 -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 0 -relx 0.652 -y 0 -rely 0.082 -width 81 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 0 -relx 0.029 -y 0 -rely 0.145 -width 0 -relwidth 0.118 \
        -height 0 -relheight 0.025 -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 0 -relx 0.031 -y 0 -rely 0.195 -width 0 -relwidth 0.114 \
        -height 0 -relheight 0.025 -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.246 -width 0 -relwidth 0.092 \
        -height 0 -relheight 0.025 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.038 -y 0 -rely 0.297 -width 0 -relwidth 0.107 \
        -height 0 -relheight 0.024 -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.672 -y 0 -rely 0.139 -width 0 -relwidth 0.248 \
        -height 0 -relheight 0.365 -anchor nw -bordermode ignore 
    place $top.lab60 \
        -in $top -x 0 -relx 0.281 -y 0 -rely 0.556 -width 0 -relwidth 0.103 \
        -height 0 -relheight 0.023 -anchor nw -bordermode ignore 
    place $top.lab61 \
        -in $top -x 0 -relx 0.57 -y 0 -rely 0.556 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.027 -anchor nw -bordermode ignore 
    place $top.but43 \
        -in $top -x 0 -relx 0.471 -y 0 -rely 0.219 -width 159 -relwidth 0 \
        -height 29 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 0 -relx 0.025 -y 0 -rely 0.556 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.028 -anchor nw -bordermode ignore 
    place $top.fra45 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.584 -width 0 -relwidth 0.244 \
        -height 0 -relheight 0.371 -anchor nw -bordermode ignore 
    place $top.mes47 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.414 -width 0 -relwidth 0.244 \
        -height 0 -relheight 0.137 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top43 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

