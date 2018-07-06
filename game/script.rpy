# MAIN
#

label start:
    call intro from _call_intro
    $ i = 1
    while (i<9):
        stop music fadeout 2.0
        #scene black with fade
        $ current_day = "day" + str(i)
        show expression current_day + " zoomin" at top with slowfade
        #show text "{color=#fff}{size=+10}Day [i]{/size}{/color}"
        $ renpy.pause(1.6)
        call expression current_day from _call_expression
        $ i += 1

    return
