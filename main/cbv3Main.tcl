#############################################################################
# Generated by PAGE version 5b
#  in conjunction with Tcl version 8.6
#  Jan 28, 2020 03:29:49 AM CST  platform: Linux
set vTcl(timestamp) ""


set image_list { \
    app_exit_png "./images/32/app-exit.png" \
    edit_paste_png "./images/32/edit-paste.png" \
    internet_png "./images/32/internet.png" \
    list_add_png "./images/32/list-add.png" \
    list_remove_png "./images/32/list-remove.png" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


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
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1270x861+281+109
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
    wm title $top "Greg's Cookbook v3"
    vTcl:DefineAlias "$top" "formCookbookMain" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure Frame -background $vTcl(actual_gui_bg)
    ttk::style configure Frame -foreground $vTcl(actual_gui_fg)
    ttk::style configure Frame -font "$vTcl(actual_gui_font_dft_desc)"
    frame $top.fra44 \
        -borderwidth 3 -relief ridge -background $vTcl(actual_gui_bg) \
        -height 50 -highlightcolor black -width 1265 
    vTcl:DefineAlias "$top.fra44" "frameToolbar" vTcl:WidgetProc "formCookbookMain" 1
    set site_3_0 $top.fra44
    button $site_3_0.but48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnExit \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image app_exit_png -text Exit 
    vTcl:DefineAlias "$site_3_0.but48" "btnExit" vTcl:WidgetProc "formCookbookMain" 1
    button $site_3_0.but43 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnAdd \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image list_add_png -text Button 
    vTcl:DefineAlias "$site_3_0.but43" "btnAdd" vTcl:WidgetProc "formCookbookMain" 1
    bind $site_3_0.but43 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Add a new recipe}
    }
    button $site_3_0.but44 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnDelete \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image list_remove_png -text Button 
    vTcl:DefineAlias "$site_3_0.but44" "btnDelete" vTcl:WidgetProc "formCookbookMain" 1
    bind $site_3_0.but44 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Delete the current recipe}
    }
    button $site_3_0.but45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnEdit \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image edit_paste_png -text Button 
    vTcl:DefineAlias "$site_3_0.but45" "btnEdit" vTcl:WidgetProc "formCookbookMain" 1
    bind $site_3_0.but45 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Edit the current recipe}
    }
    button $site_3_0.but46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnScrape \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image internet_png -text Button 
    vTcl:DefineAlias "$site_3_0.but46" "btnScrape" vTcl:WidgetProc "formCookbookMain" 1
    bind $site_3_0.but46 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Scrape a web page}
    }
    button $site_3_0.but47 \
        -background $vTcl(actual_gui_bg) -command on_btnPrint \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text Button 
    vTcl:DefineAlias "$site_3_0.but47" "btnPrint" vTcl:WidgetProc "formCookbookMain" 1
    place $site_3_0.but48 \
        -in $site_3_0 -x 1210 -y 8 -width 32 -relwidth 0 -height 32 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but43 \
        -in $site_3_0 -x 117 -y 8 -width 38 -relwidth 0 -height 38 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but44 \
        -in $site_3_0 -x 170 -y 8 -width 38 -relwidth 0 -height 38 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 240 -y 8 -width 38 -relwidth 0 -height 38 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 504 -y 8 -width 38 -relwidth 0 -height 38 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 630 -y 8 -width 38 -relwidth 0 -height 38 \
        -relheight 0 -anchor nw -bordermode ignore 
    vTcl:copy_lock $top.fra44
    frame $top.fra45 \
        -borderwidth 3 -relief ridge -background $vTcl(actual_gui_bg) \
        -height 50 -highlightcolor black -width 1265 
    vTcl:DefineAlias "$top.fra45" "frameStatus" vTcl:WidgetProc "formCookbookMain" 1
    set site_3_0 $top.fra45
    label $site_3_0.lab44 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Label \
        -textvariable TimeDisp 
    vTcl:DefineAlias "$site_3_0.lab44" "lblTimeDisplay" vTcl:WidgetProc "formCookbookMain" 1
    place $site_3_0.lab44 \
        -in $site_3_0 -x 0 -relx 0.916 -y 0 -rely 0.2 -width 0 \
        -relwidth 0.068 -height 0 -relheight 0.58 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $top.fra45
    frame $top.fra46 \
        -borderwidth 3 -relief ridge -background $vTcl(actual_gui_bg) \
        -height 755 -highlightcolor black -width 350 
    vTcl:DefineAlias "$top.fra46" "frameNavigate" vTcl:WidgetProc "formCookbookMain" 1
    set site_3_0 $top.fra46
    frame $site_3_0.fra49 \
        -borderwidth 2 -relief ridge -background $vTcl(actual_gui_bg) \
        -height 205 -highlightcolor black -width 345 
    vTcl:DefineAlias "$site_3_0.fra49" "Frame2" vTcl:WidgetProc "formCookbookMain" 1
    set site_4_0 $site_3_0.fra49
    label $site_4_0.lab54 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Search: 
    vTcl:DefineAlias "$site_4_0.lab54" "Label1" vTcl:WidgetProc "formCookbookMain" 1
    radiobutton $site_4_0.rad43 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -command on_rbClick \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -justify left -text Title -value 0 
    vTcl:DefineAlias "$site_4_0.rad43" "rbTitle" vTcl:WidgetProc "formCookbookMain" 1
    radiobutton $site_4_0.rad44 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -command on_rbClick \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -justify left -text Category -value 2 
    vTcl:DefineAlias "$site_4_0.rad44" "rbCategories" vTcl:WidgetProc "formCookbookMain" 1
    radiobutton $site_4_0.rad45 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -command on_rbClick \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -justify left -text Ingredients -value 1 
    vTcl:DefineAlias "$site_4_0.rad45" "rbIngredients" vTcl:WidgetProc "formCookbookMain" 1
    checkbutton $site_4_0.che46 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -command on_chkClick \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -justify left -state disabled -text {Show All} \
        -variable che46 
    vTcl:DefineAlias "$site_4_0.che46" "Checkbutton1" vTcl:WidgetProc "formCookbookMain" 1
    bind $site_4_0.che46 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Show Deleted Records as well}
    }
    entry $site_4_0.ent47 \
        -background white -font $vTcl(actual_gui_font_fixed_desc) \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -state disabled -textvariable EntryText \
        -width 236 
    vTcl:DefineAlias "$site_4_0.ent47" "Entry1" vTcl:WidgetProc "formCookbookMain" 1
    bind $site_4_0.ent47 <KeyRelease> {
        lambda e: on_Entry_Return(e)
    }
    place $site_4_0.lab54 \
        -in $site_4_0 -x 0 -relx 0.029 -y 0 -rely 0.049 -width 0 \
        -relwidth 0.234 -height 0 -relheight 0.102 -anchor nw \
        -bordermode ignore 
    place $site_4_0.rad43 \
        -in $site_4_0 -x 0 -relx 0.116 -y 0 -rely 0.244 -width 0 \
        -relwidth 0.266 -height 0 -relheight 0.102 -anchor nw \
        -bordermode ignore 
    place $site_4_0.rad44 \
        -in $site_4_0 -x 0 -relx 0.116 -y 0 -rely 0.39 -width 0 \
        -relwidth 0.324 -height 0 -relheight 0.102 -anchor nw \
        -bordermode ignore 
    place $site_4_0.rad45 \
        -in $site_4_0 -x 40 -y 110 -width 138 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.che46 \
        -in $site_4_0 -x 0 -relx 0.523 -y 0 -rely 0.244 -width 0 \
        -relwidth 0.327 -height 0 -relheight 0.102 -anchor nw \
        -bordermode ignore 
    place $site_4_0.ent47 \
        -in $site_4_0 -x 0 -relx 0.116 -y 0 -rely 0.732 -width 0 \
        -relwidth 0.685 -height 0 -relheight 0.102 -anchor nw \
        -bordermode ignore 
    frame $site_3_0.fra50 \
        -borderwidth 2 -relief ridge -background $vTcl(actual_gui_bg) \
        -height 545 -highlightcolor black -width 345 
    vTcl:DefineAlias "$site_3_0.fra50" "Frame3" vTcl:WidgetProc "formCookbookMain" 1
    set site_4_0 $site_3_0.fra50
    ttk::style configure Treeview \
         -font  "$vTcl(actual_gui_font_treeview_desc)"
    vTcl::widgets::ttk::scrolledtreeview::CreateCmd $site_4_0.scr51 \
        -background $vTcl(actual_gui_bg) -height 15 -highlightcolor black \
        -width 30 
    vTcl:DefineAlias "$site_4_0.scr51" "Scrolledtreeview1" vTcl:WidgetProc "formCookbookMain" 1

    .top43.fra46.fra50.scr51.01 configure -columns Col1 \
        -height 4
        .top43.fra46.fra50.scr51.01 configure -columns {Col1}
        .top43.fra46.fra50.scr51.01 heading #0 -text {Tree}
        .top43.fra46.fra50.scr51.01 heading #0 -anchor center
        .top43.fra46.fra50.scr51.01 column #0 -width 165
        .top43.fra46.fra50.scr51.01 column #0 -minwidth 20
        .top43.fra46.fra50.scr51.01 column #0 -stretch 1
        .top43.fra46.fra50.scr51.01 column #0 -anchor w
        .top43.fra46.fra50.scr51.01 heading Col1 -text {Col1}
        .top43.fra46.fra50.scr51.01 heading Col1 -anchor center
        .top43.fra46.fra50.scr51.01 column Col1 -width 166
        .top43.fra46.fra50.scr51.01 column Col1 -minwidth 20
        .top43.fra46.fra50.scr51.01 column Col1 -stretch 1
        .top43.fra46.fra50.scr51.01 column Col1 -anchor w
    place $site_4_0.scr51 \
        -in $site_4_0 -x 0 -y 0 -width 345 -relwidth 0 -height 548 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra49 \
        -in $site_3_0 -x 0 -relx 0.006 -y 0 -rely 0.729 -width 0 \
        -relwidth 0.989 -height 0 -relheight 0.271 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra50 \
        -in $site_3_0 -x 0 -relx 0.006 -y 0 -rely 0.004 -width 0 \
        -relwidth 0.989 -height 0 -relheight 0.725 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $top.fra46
    frame $top.fra47 \
        -borderwidth 3 -relief ridge -background $vTcl(actual_gui_bg) \
        -height 755 -highlightcolor black -width 915 
    vTcl:DefineAlias "$top.fra47" "Frame1" vTcl:WidgetProc "formCookbookMain" 1
    set site_3_0 $top.fra47
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_3_0.scr52 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_3_0.scr52" "Scrolledtext1" vTcl:WidgetProc "formCookbookMain" 1

    $site_3_0.scr52.01 configure -background white \
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
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_3_0.scr53 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_3_0.scr53" "Scrolledlistbox1" vTcl:WidgetProc "formCookbookMain" 1

    $site_3_0.scr53.01 configure -background white \
        -font font10 \
        -foreground black \
        -height 3 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    label $site_3_0.lab43 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 12 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable RecipeTitle 
    vTcl:DefineAlias "$site_3_0.lab43" "lblTitle" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab44 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label-Image 
    vTcl:DefineAlias "$site_3_0.lab44" "lblImage" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 9 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable RecipeSource 
    vTcl:DefineAlias "$site_3_0.lab45" "lblSource" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable RecipeServings 
    vTcl:DefineAlias "$site_3_0.lab46" "lblServings" vTcl:WidgetProc "formCookbookMain" 1
    message $site_3_0.mes43 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Message -textvariable RecipeCategories -width 805 
    vTcl:DefineAlias "$site_3_0.mes43" "msgCategories" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Label \
        -textvariable IdLableShow 
    vTcl:DefineAlias "$site_3_0.lab47" "lblID" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {Ubuntu} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Source: 
    vTcl:DefineAlias "$site_3_0.lab48" "Label2" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {Ubuntu} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Servings: 
    vTcl:DefineAlias "$site_3_0.lab49" "Label3" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {Ubuntu} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Description: 
    vTcl:DefineAlias "$site_3_0.lab50" "Label4" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable RecipeTotalTime 
    vTcl:DefineAlias "$site_3_0.lab51" "lblTotalTime" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {Ubuntu} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Total Time:} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label5" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {Ubuntu} -size 11 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable RecipeRating 
    vTcl:DefineAlias "$site_3_0.lab53" "Label6" vTcl:WidgetProc "formCookbookMain" 1
    label $site_3_0.lab54 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) \
        -font {-family {Ubuntu} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Rating: 
    vTcl:DefineAlias "$site_3_0.lab54" "Label7" vTcl:WidgetProc "formCookbookMain" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_3_0.scr43 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_3_0.scr43" "stNotes" vTcl:WidgetProc "formCookbookMain" 1

    $site_3_0.scr43.01 configure -background white \
        -font font12 \
        -foreground black \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap word
    place $site_3_0.scr52 \
        -in $site_3_0 -x 404 -y 410 -width 510 -relwidth 0 -height 345 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr53 \
        -in $site_3_0 -x 10 -y 410 -width 396 -relwidth 0 -height 342 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab43 \
        -in $site_3_0 -x 20 -y 9 -width 556 -relwidth 0 -height 39 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab44 \
        -in $site_3_0 -x 600 -y 20 -width 300 -relwidth 0 -height 300 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 120 -y 53 -width 456 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 120 -y 86 -width 456 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes43 \
        -in $site_3_0 -x 90 -y 350 -width 805 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 20 -y 360 -width 46 -relwidth 0 -height 19 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 23 -y 58 -width 86 -relwidth 0 -height 19 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 33 -y 92 -width 76 -relwidth 0 -height 19 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 30 -y 186 -width 82 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 119 -y 119 -width 456 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 22 -y 123 -width 89 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 120 -y 152 -width 456 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 30 -y 155 -width 79 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr43 \
        -in $site_3_0 -x 120 -y 184 -width 472 -relwidth 0 -height 145 \
        -relheight 0 -anchor nw -bordermode ignore 
    vTcl:copy_lock $top.fra47
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra44 \
        -in $top -x 0 -relx 0.002 -y 0 -rely 0.002 -width 0 -relwidth 0.997 \
        -height 0 -relheight 0.058 -anchor nw -bordermode ignore 
    place $top.fra45 \
        -in $top -x 0 -relx 0.002 -y 0 -rely 0.941 -width 0 -relwidth 0.997 \
        -height 0 -relheight 0.058 -anchor nw -bordermode ignore 
    place $top.fra46 \
        -in $top -x 0 -relx 0.002 -y 0 -rely 0.06 -width 0 -relwidth 0.276 \
        -height 0 -relheight 0.88 -anchor nw -bordermode ignore 
    place $top.fra47 \
        -in $top -x 351 -y 52 -width 917 -relwidth 0 -height 758 -relheight 0 \
        -anchor nw -bordermode ignore 

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

