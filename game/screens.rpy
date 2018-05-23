# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            window:
                id "window"
                ypos 350

                has vbox:
                    style "say_vbox"

                text what id "what"

            if who:
                window:
                    style "say_who_window"
                    xpos 250
                    ypos -110

                    text who:
                        id "who"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image xpos 62 ypos 489
    else:
        add SideImage() xpos 66 ypos 530
        add "GUI/side frame.png" xpos 62 ypos 489

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action at choicefade
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear
        yalign 0.3
        hover_color "#400000"
        idle_color "#803b3b"

    style menu_choice_button is button:
        xminimum 573
        xmaximum 573
        background Frame("GUI/choice.png",28,9)
        yminimum 114
        ypadding 5
        xpadding 20

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):
    if (dialogue):
        # use the parchment background unless it's a book
        if (dialogue[0][0] == "Book"):
            use book_screen
        else:
            add "bg/scroll.jpg"

            window:
                style "nvl_window"

                has vbox:
                    style "nvl_vbox"

                # Display dialogue.
                for who, what, who_id, what_id, window_id in dialogue:
                    window:
                        id window_id

                        has hbox:
                            spacing 10

                        if who is not None:
                            if (who == "King"):
                                text what id what_id font "fonts/danielbd.ttf"
                            if (who == "Balrung"):
                                text what id what_id font "fonts/FREEBSC_.ttf" size 35
                            elif (who == "Magnolia"):
                                text what id what_id font "fonts/Kristi.ttf" size 40
                            elif (who == "Princess"):
                                text what id what_id font "fonts/Kristi.ttf" size 40

                        else:
                            text what id what_id

                # Display a menu, if given.
                if items:

                    vbox:
                        id "menu"

                        for caption, action, chosen in items:

                            if action:

                                button:
                                    style "nvl_menu_choice_button"
                                    action action

                                    text caption style "nvl_menu_choice"

                            else:

                                text caption style "nvl_dialogue"

    #add SideImage() xalign 0.0 yalign 1.0

    #use quick_menu

screen book_screen:
    default side_image = None

    if (book_flipped):
        add im.Flip("bg/book.jpg", horizontal = True)
    else:
        add "bg/book.jpg"
    window:
        style "nvl_window"
        xpadding 50
        ypadding 50

        yfill True
        xfill True

        has vbox:
            style "nvl_vbox"
        vbox:
            # Display dialogue.
            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id
                    vbox:
                        xpos 100
                        xmaximum 800
                        xalign 0.0
                        text what id what_id font "fonts/ankecallig-fg.ttf" size 30


##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    vbox:
        style_group "mm"
        ypos 30
        xpos 830
        textbutton _("Language") action ShowTransient("language_select") at buttonfade

    # The main menu buttons.
    vbox:
        style_group "mm"
        ypos 420
        xpos 730
#        textbutton ("Start") action Start() at buttonfade
#        textbutton ("Load") action ShowMenu("main_load") at buttonfade
#        textbutton ("Preferences") action ShowMenu("preferences") at buttonfade
#        textbutton ("Extras") action ShowMenu("extras") at buttonfade
#        textbutton ("Quit") action Quit(confirm=False) at buttonfade

        imagebutton idle "GUI/button_start.png" hover "GUI/button_start_hover.png" action Start() at buttonfade

        imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" action ShowMenu("main_load") at buttonfade

        imagebutton idle "GUI/button_preferences.png" hover "GUI/button_preferences_hover.png" action ShowMenu("main_preferences") at buttonfade

        imagebutton idle "GUI/button_extras.png" hover "GUI/button_extras_hover.png" action ShowMenu("princess_endings") at buttonfade

        imagebutton idle "GUI/button_quit.png" hover "GUI/button_quit_hover.png" action Quit(confirm=False) at buttonfade

    on "show" action Stop ("sound")


screen language_select:
    vbox:
        style_group "mm"
        ypos 100
        xpos 830
        textbutton _("English") style "lang_button" action [ Language(None), Hide("language_select") ]
        textbutton _("Spanish") style "lang_button" action [Language("spanish"), Hide("language_select") ]

style lang_button:
    xalign 1.0

style lang_button_text is prefs_button_text:
    size 30
    idle_color "#400000"
    hover_color "#ffc180"
    selected_color "ffc180"

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"
        background None

    style mm_button_text:
        idle_color "#400000"
        hover_color "#ffc180"
        selected_color "ffc180"
        xalign 0.5
        font "fonts/Anderson Thunderbirds Are GO!.ttf"
        size 50


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.


screen load_save_slot:
    #tag menu
    #modal True
    $ file_text = "%2s. %s\n  %s" % (
                        FileSlotName(number, 4),
                        FileTime(number, empty=_("Empty Slot.")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 1 ypos 1
    text file_text xalign .5 yalign 0.1 size 16 color "#000000"

screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        alpha False
        ground "GUI/save_slots.png"
        idle "GUI/idle.png"
        hover "GUI/save_slots.png"
        insensitive "GUI/idle.png"

        hotspot (451, 140, 138, 104) at slotfade clicked FileAction(1):
            use load_save_slot(number=1)
        hotspot (608, 140, 138, 104) at slotfade clicked FileAction(2):
            use load_save_slot(number=2)
        hotspot (451, 263, 138, 104) at slotfade clicked FileAction(3):
            use load_save_slot(number=3)
        hotspot (608, 263, 138, 104) at slotfade clicked FileAction(4):
            use load_save_slot(number=4)



    imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" xpos 80 ypos 195 action ShowMenu("load") at buttonfade

    imagebutton idle "GUI/button_preferences.png" hover "GUI/button_preferences_hover.png" xpos 80 ypos 243 action ShowMenu("preferences") at buttonfade

    imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" xpos 80 ypos 295 action MainMenu() at buttonfade

    imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" xpos 80 ypos 345 action Return() at buttonfade

    imagebutton idle "GUI/button_a.png" hover "GUI/button_a_hover.png" selected_idle "GUI/button_a_hover.png" selected_hover "GUI/button_a_hover.png" xpos 500 ypos 440 focus_mask True action FilePage("auto")  at buttonfade
    imagebutton idle "GUI/button_1.png" hover "GUI/button_1_hover.png" selected_idle "GUI/button_1_hover.png" selected_hover "GUI/button_1_hover.png" xpos 550 ypos 440 focus_mask True action FilePage("1")  at buttonfade
    imagebutton idle "GUI/button_2.png" hover "GUI/button_2_hover.png" selected_idle "GUI/button_2_hover.png" selected_hover "GUI/button_2_hover.png" xpos 600 ypos 440 focus_mask True action FilePage("2")  at buttonfade
    imagebutton idle "GUI/button_3.png" hover "GUI/button_3_hover.png" selected_idle "GUI/button_3_hover.png" selected_hover "GUI/button_3_hover.png" xpos 650 ypos 440 focus_mask True action FilePage("3")  at buttonfade


screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        alpha False
        ground "GUI/load_slots.png"
        idle "GUI/idle.png"
        hover "GUI/load_slots.png"
        insensitive "GUI/idle.png"

        hotspot (451, 140, 138, 104) at slotfade clicked FileAction(1):
            use load_save_slot(number=1)
        hotspot (608, 140, 138, 104) at slotfade clicked FileAction(2):
            use load_save_slot(number=2)
        hotspot (451, 263, 138, 104) at slotfade clicked FileAction(3):
            use load_save_slot(number=3)
        hotspot (608, 263, 138, 104) at slotfade clicked FileAction(4):
            use load_save_slot(number=4)



    imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" xpos 80 ypos 195 action ShowMenu("save") at buttonfade

    imagebutton idle "GUI/button_preferences.png" hover "GUI/button_preferences_hover.png" xpos 80 ypos 243 action ShowMenu("preferences") at buttonfade

    imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" xpos 80 ypos 295 action MainMenu() at buttonfade

    imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" xpos 80 ypos 345 action Return() at buttonfade

    imagebutton idle "GUI/button_a.png" hover "GUI/button_a_hover.png" selected_idle "GUI/button_a_hover.png" selected_hover "GUI/button_a_hover.png" xpos 500 ypos 440 focus_mask True action FilePage("auto")  at buttonfade
    imagebutton idle "GUI/button_1.png" hover "GUI/button_1_hover.png" selected_idle "GUI/button_1_hover.png" selected_hover "GUI/button_1_hover.png" xpos 550 ypos 440 focus_mask True action FilePage("1")  at buttonfade
    imagebutton idle "GUI/button_2.png" hover "GUI/button_2_hover.png" selected_idle "GUI/button_2_hover.png" selected_hover "GUI/button_2_hover.png" xpos 600 ypos 440 focus_mask True action FilePage("2")  at buttonfade
    imagebutton idle "GUI/button_3.png" hover "GUI/button_3_hover.png" selected_idle "GUI/button_3_hover.png" selected_hover "GUI/button_3_hover.png" xpos 650 ypos 440 focus_mask True action FilePage("3")  at buttonfade

screen main_load:

    # This ensures that any other menu screen is replaced.
    tag menu
    add "GUI/sun.png"
    imagemap:
        alpha False
        ground "GUI/load_slots.png"
        idle "GUI/idle.png"
        hover "GUI/load_slots.png"
        insensitive "GUI/idle.png"

        hotspot (451, 140, 138, 104) at slotfade clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (608, 140, 138, 104) at slotfade clicked FileLoad (2):
            use load_save_slot(number=2)
        hotspot (451, 263, 138, 104) at slotfade clicked FileLoad (3):
            use load_save_slot(number=3)
        hotspot (608, 263, 138, 104) at slotfade clicked FileLoad (4):
            use load_save_slot(number=4)



    imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" xpos 80 ypos 195 action ShowMenu("save") at buttonfade

    imagebutton idle "GUI/button_preferences.png" hover "GUI/button_preferences_hover.png" xpos 80 ypos 243 action ShowMenu("main_preferences") at buttonfade

    imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" xpos 80 ypos 295 action Return() at buttonfade

    imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" xpos 80 ypos 345 action Return() at buttonfade

    imagebutton idle "GUI/button_a.png" hover "GUI/button_a_hover.png" selected_idle "GUI/button_a_hover.png" selected_hover "GUI/button_a_hover.png" xpos 500 ypos 440 focus_mask True action FilePage("auto")  at buttonfade
    imagebutton idle "GUI/button_1.png" hover "GUI/button_1_hover.png" selected_idle "GUI/button_1_hover.png" selected_hover "GUI/button_1_hover.png" xpos 550 ypos 440 focus_mask True action FilePage("1")  at buttonfade
    imagebutton idle "GUI/button_2.png" hover "GUI/button_2_hover.png" selected_idle "GUI/button_2_hover.png" selected_hover "GUI/button_2_hover.png" xpos 600 ypos 440 focus_mask True action FilePage("2")  at buttonfade
    imagebutton idle "GUI/button_3.png" hover "GUI/button_3_hover.png" selected_idle "GUI/button_3_hover.png" selected_hover "GUI/button_3_hover.png" xpos 650 ypos 440 focus_mask True action FilePage("3")  at buttonfade


init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

init -2 python:
    config.thumbnail_width = 136
    config.thumbnail_height = 102
    config.quit_action = Quit(confirm=False)

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    add "GUI/preferences.png"

    # Include the navigation.
#    use navigation

    # Put the navigation columns in a three-wide grid.

    vbox:
        xpos 600
        ypos 145
        style_group "prefs"

        textbutton _("Window") action Preference("display", "window") at buttonfade
        textbutton _("Fullscreen") action Preference("display", "fullscreen") at buttonfade


        textbutton _("Seen Messages") action Preference("skip", "seen") at buttonfade
        textbutton _("All Messages") action Preference("skip", "all") at buttonfade

    vbox:
        xpos 550
        ypos 275
        style_group "prefs"

        bar value Preference("auto-forward time")


    vbox:
        xpos 550
        ypos 315
        style_group "prefs"
        bar value Preference("sound volume")


    vbox:
        xpos 550
        ypos 355
        style_group "prefs"
        bar value Preference("music volume")

    imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" xpos 80 ypos 195 action ShowMenu("save") at buttonfade

    imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" xpos 80 ypos 245 action ShowMenu("load") at buttonfade

    imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" xpos 80 ypos 295 action MainMenu() at buttonfade

    imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" xpos 80 ypos 345 action Return() at buttonfade

screen main_preferences():

    tag menu
    add "GUI/sun.png"
    add "GUI/preferences.png"

    # Include the navigation.
#    use navigation

    # Put the navigation columns in a three-wide grid.

    vbox:
        xpos 600
        ypos 145
        style_group "prefs"

        textbutton _("Window") action Preference("display", "window") at buttonfade
        textbutton _("Fullscreen") action Preference("display", "fullscreen") at buttonfade


        textbutton _("Seen Messages") action Preference("skip", "seen") at buttonfade
        textbutton _("All Messages") action Preference("skip", "all") at buttonfade

    vbox:
        xpos 550
        ypos 275
        style_group "prefs"

        bar value Preference("text speed")


    vbox:
        xpos 550
        ypos 315
        style_group "prefs"
        bar value Preference("sound volume")


    vbox:
        xpos 550
        ypos 355
        style_group "prefs"
        bar value Preference("music volume")

    imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" xpos 80 ypos 195 action ShowMenu("save") at buttonfade

    imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" xpos 80 ypos 245 action ShowMenu("main_load") at buttonfade

    imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" xpos 80 ypos 295 action Return() at buttonfade

    imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" xpos 80 ypos 345 action Return() at buttonfade



init -2:
    style prefs_frame:
        xfill False

    style prefs_vbox:
        xfill False

    style prefs_button:
        size_group "pref"
        xalign 0.0
        background None
        ypadding 0
        ymargin 0

    style prefs_button_text:
        hover_color "#400000"
        idle_color "#803b3b"
        selected_hover_color "#400000"
        selected_idle_color "#400000"
        xalign 0.0

    style prefs_slider:
        xminimum 284
        xmaximum 284
        yminimum 30
        xalign 1.0
        left_bar "GUI/bar.png"
        right_bar "GUI/bar.png"
        thumb "GUI/thumbnail.png"




##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):
    modal True
    add "GUI/base.png"

    vbox:
        style_group "yesno"
        xalign .5
        yalign .3
        spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            imagebutton idle "GUI/button_yes.png" hover "GUI/button_yes_hover.png" action yes_action  at buttonfade
            imagebutton idle "GUI/button_no.png" hover "GUI/button_no_hover.png" action no_action  at buttonfade

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        color "#400000"

##############################################################################

screen princess_endings:
    tag menu
    add "GUI/sun.png"
    add "GUI/extras.png"

    vbox:
        xalign 0.5
        yalign 0.3
        if (persistent.PrincessInPrison):
            text _("Princess in Prison")
        else:
            text _("LOCKED")


    hbox:
        xalign 0.5
        yalign 0.75
        imagebutton idle "GUI/button_princess_idle.png" hover "GUI/button_princess_hover.png" selected_idle "GUI/button_princess.png" selected_hover "GUI/button_princess_hover.png" focus_mask True action ShowMenu("princess_endings") at buttonfade2
        imagebutton idle "GUI/button_cyril_idle.png" hover "GUI/button_cyril_hover.png" selected_idle "GUI/button_cyril.png" selected_hover "GUI/button_cyril_hover.png" focus_mask True action ShowMenu("cyril_endings") at buttonfade2
        imagebutton idle "GUI/button_balrung_idle.png" hover "GUI/button_balrung_hover.png" selected_idle "GUI/button_balrung.png" selected_hover "GUI/button_balrung_hover.png" focus_mask True action ShowMenu("balrung_endings") at buttonfade2
        imagebutton idle "GUI/button_niir_idle.png" hover "GUI/button_niir_hover.png" selected_idle "GUI/button_niir.png" selected_hover "GUI/button_niir_hover.png" focus_mask True action ShowMenu("niir_endings") at buttonfade2

    hbox:
        yalign 0.99
        xalign 0.98
        imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" action Return() at buttonfade

screen cyril_endings:
    tag menu
    add "GUI/sun.png"
    add "GUI/extras.png"

    vbox:
        xalign 0.5
        yalign 0.3
        if (persistent.DarkQueen):
            text _("Dark Queen")
        else:
            text _("LOCKED")

        if (persistent.DragonQueen):
            text _("Dragon Queen")
        else:
            text _("LOCKED")

        if (persistent.QueensHero):
            text _("Queen's Hero")
        else:
            text _("LOCKED")

        if (persistent.ImaginaryQueen):
            text _("Imaginary Queen")
        else:
            text _("LOCKED")

    hbox:
        xalign 0.5
        yalign 0.75
        imagebutton idle "GUI/button_princess_idle.png" hover "GUI/button_princess_hover.png" selected_idle "GUI/button_princess.png" selected_hover "GUI/button_princess_hover.png" focus_mask True action ShowMenu("princess_endings") at buttonfade2
        imagebutton idle "GUI/button_cyril_idle.png" hover "GUI/button_cyril_hover.png" selected_idle "GUI/button_cyril.png" selected_hover "GUI/button_cyril_hover.png" focus_mask True action ShowMenu("cyril_endings") at buttonfade2
        imagebutton idle "GUI/button_balrung_idle.png" hover "GUI/button_balrung_hover.png" selected_idle "GUI/button_balrung.png" selected_hover "GUI/button_balrung_hover.png" focus_mask True action ShowMenu("balrung_endings") at buttonfade2
        imagebutton idle "GUI/button_niir_idle.png" hover "GUI/button_niir_hover.png" selected_idle "GUI/button_niir.png" selected_hover "GUI/button_niir_hover.png" focus_mask True action ShowMenu("niir_endings") at buttonfade2

    hbox:
        yalign 0.99
        xalign 0.98
        imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" action Return() at buttonfade

screen balrung_endings:
    tag menu
    add "GUI/sun.png"
    add "GUI/extras.png"

    vbox:
        xalign 0.5
        yalign 0.3
        if (persistent.QueensGambit):
            text _("Queen's Gambit")
        else:
            text _("LOCKED")

        if (persistent.RevengeNeverEnds):
            text _("Revenge Never Ends")
        else:
            text _("LOCKED")

    hbox:
        xalign 0.5
        yalign 0.75
        imagebutton idle "GUI/button_princess_idle.png" hover "GUI/button_princess_hover.png" selected_idle "GUI/button_princess.png" selected_hover "GUI/button_princess_hover.png" focus_mask True action ShowMenu("princess_endings") at buttonfade2
        imagebutton idle "GUI/button_cyril_idle.png" hover "GUI/button_cyril_hover.png" selected_idle "GUI/button_cyril.png" selected_hover "GUI/button_cyril_hover.png" focus_mask True action ShowMenu("cyril_endings") at buttonfade2
        imagebutton idle "GUI/button_balrung_idle.png" hover "GUI/button_balrung_hover.png" selected_idle "GUI/button_balrung.png" selected_hover "GUI/button_balrung_hover.png" focus_mask True action ShowMenu("balrung_endings") at buttonfade2
        imagebutton idle "GUI/button_niir_idle.png" hover "GUI/button_niir_hover.png" selected_idle "GUI/button_niir.png" selected_hover "GUI/button_niir_hover.png" focus_mask True action ShowMenu("niir_endings") at buttonfade2

    hbox:
        yalign 0.99
        xalign 0.98
        imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" action Return() at buttonfade

screen niir_endings:
    tag menu
    add "GUI/sun.png"
    add "GUI/extras.png"

    vbox:
        xalign 0.5
        yalign 0.3
        if (persistent.DefinitelyTrueLove):
            text "Definitely True Love"
        else:
            text "LOCKED"

        if (persistent.NeverTooLate):
            text "Never Too Late"
        else:
            text "LOCKED"


    hbox:
        xalign 0.5
        yalign 0.75
        imagebutton idle "GUI/button_princess_idle.png" hover "GUI/button_princess_hover.png" selected_idle "GUI/button_princess.png" selected_hover "GUI/button_princess_hover.png" focus_mask True action ShowMenu("princess_endings") at buttonfade2
        imagebutton idle "GUI/button_cyril_idle.png" hover "GUI/button_cyril_hover.png" selected_idle "GUI/button_cyril.png" selected_hover "GUI/button_cyril_hover.png" focus_mask True action ShowMenu("cyril_endings") at buttonfade2
        imagebutton idle "GUI/button_balrung_idle.png" hover "GUI/button_balrung_hover.png" selected_idle "GUI/button_balrung.png" selected_hover "GUI/button_balrung_hover.png" focus_mask True action ShowMenu("balrung_endings") at buttonfade2
        imagebutton idle "GUI/button_niir_idle.png" hover "GUI/button_niir_hover.png" selected_idle "GUI/button_niir.png" selected_hover "GUI/button_niir_hover.png" focus_mask True action ShowMenu("niir_endings") at buttonfade2

    hbox:
        yalign 0.99
        xalign 0.98
        imagebutton idle "GUI/button_return.png" hover "GUI/button_return_hover.png" action Return() at buttonfade

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
        xpos 866
        ypos 710
        imagebutton idle "GUI/button_auto.png" hover "GUI/button_auto_hover.png" selected_idle "GUI/button_auto_hover.png" focus_mask True action Preference("auto-forward", "toggle") at buttonfade
    hbox:
        style_group "quick"
        xpos 914
        ypos 695
        imagebutton idle "GUI/button_skip.png" hover "GUI/button_skip_hover.png" selected_idle "GUI/button_skip_hover.png" focus_mask True action Skip() at buttonfade
    hbox:
        style_group "quick"
        xpos 943
        ypos 656
        imagebutton idle "GUI/button_options.png" hover "GUI/button_options_hover.png" focus_mask True action ShowMenu("preferences") at buttonfade

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
