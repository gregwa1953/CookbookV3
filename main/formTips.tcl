#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Mar 31, 2020 11:42:06 AM CDT  platform: Linux
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
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
}




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
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 1072x782+344+145
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
    wm title $top "Tips"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra44 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 55 -width 1075 
    vTcl:DefineAlias "$top.fra44" "frameToolbar" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra44
    button $site_3_0.but45 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Button 
    vTcl:DefineAlias "$site_3_0.but45" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnExit \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text Exit 
    vTcl:DefineAlias "$site_3_0.but46" "btnExit" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but45 \
        -in $site_3_0 -x 40 -y 10 -width 40 -relwidth 0 -height 40 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 995 -y 7 -width 40 -height 40 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $top.fra44
    frame $top.fra47 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 55 -highlightcolor black -width 1075 
    vTcl:DefineAlias "$top.fra47" "frameToolbar_2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra47
    label $site_3_0.lab48 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -relief sunken -text Label \
        -textvariable lblTime 
    vTcl:DefineAlias "$site_3_0.lab48" "lblTime" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab48 \
        -in $site_3_0 -x 920 -y 8 -width 146 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.fra49 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 605 -width 665 
    vTcl:DefineAlias "$top.fra49" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra49
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_3_0.scr50 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 595 -highlightcolor black -width 652 
    vTcl:DefineAlias "$site_3_0.scr50" "Scrolledtext1" vTcl:WidgetProc "Toplevel1" 1

    $site_3_0.scr50.01 configure -background white \
        -font font9 \
        -foreground black \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    place $site_3_0.scr50 \
        -in $site_3_0 -x 2 -y 2 -width 658 -relwidth 0 -height 595 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.fra51 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 625 -width 385 
    vTcl:DefineAlias "$top.fra51" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra51
    frame $site_3_0.fra52 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 505 -width 375 
    vTcl:DefineAlias "$site_3_0.fra52" "frameTreeView" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra52
    ttk::style configure Treeview \
         -font  "$vTcl(actual_gui_font_treeview_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $site_4_0.scr54 \
        -background $vTcl(actual_gui_bg) -height 15 -highlightcolor black \
        -width 30 
    vTcl:DefineAlias "$site_4_0.scr54" "Scrolledtreeview1" vTcl:WidgetProc "Toplevel1" 1

    .top43.fra51.fra52.scr54.01 configure -columns Col1 \
        -height 4
        .top43.fra51.fra52.scr54.01 configure -columns {Col1}
        .top43.fra51.fra52.scr54.01 heading #0 -text {Tree}
        .top43.fra51.fra52.scr54.01 heading #0 -anchor center
        .top43.fra51.fra52.scr54.01 column #0 -width 183
        .top43.fra51.fra52.scr54.01 column #0 -minwidth 20
        .top43.fra51.fra52.scr54.01 column #0 -stretch 1
        .top43.fra51.fra52.scr54.01 column #0 -anchor w
        .top43.fra51.fra52.scr54.01 heading Col1 -text {Col1}
        .top43.fra51.fra52.scr54.01 heading Col1 -anchor center
        .top43.fra51.fra52.scr54.01 column Col1 -width 183
        .top43.fra51.fra52.scr54.01 column Col1 -minwidth 20
        .top43.fra51.fra52.scr54.01 column Col1 -stretch 1
        .top43.fra51.fra52.scr54.01 column Col1 -anchor w
    place $site_4_0.scr54 \
        -in $site_4_0 -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore 
    frame $site_3_0.fra53 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 105 -width 385 
    vTcl:DefineAlias "$site_3_0.fra53" "frameSearch" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.fra52 \
        -in $site_3_0 -x 2 -y 0 -width 380 -relwidth 0 -height 511 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra53 \
        -in $site_3_0 -x 2 -y 510 -width 380 -relwidth 0 -height 112 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra44 \
        -in $top -x 0 -y 0 -width 1075 -relwidth 0 -height 55 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra47 \
        -in $top -x 0 -y 727 -width 1075 -relwidth 0 -height 55 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra49 \
        -in $top -x 400 -y 100 -width 665 -relwidth 0 -height 605 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.fra51 \
        -in $top -x 0 -y 100 -width 385 -relwidth 0 -height 625 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

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

