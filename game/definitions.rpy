init -1:

    #
    # VARIABLES
    #
    define balrung_affection = 0
    define niir_affection = 0
    define cyril_affection = 0
    define cyril_insanity = 0
    define p_name = "Chrysandra"
    define k_name = "Novaria"
    define castle_name = _("the Castle of the Banished")
    define asked_scepter = "no one"
    define route = None
    define HIGH_AFFECTION = 7
    define MEDIUM_AFFECTION = 3
    define INSANE = 3
    define cyril_dead = False
    define book_flipped = False

    #
    # CHARACTERS
    #
    define p = DynamicCharacter("p_name", image="princess", show_two_window=True)
    define b = Character('Balrung', image="balrung", show_two_window=True, show_side_image="GUI/side.png")
    define c = Character('Cyril', image="cyril", show_two_window=True, show_side_image="GUI/side.png")
    define n = Character('Niir', image="niir", show_two_window=True, show_side_image="GUI/side.png")
    define narrator = Character(' ', show_two_window=True, show_side_image="GUI/side.png")

    define p_write = Character("Princess", kind=nvl)
    define k_write = Character("King", kind=nvl)
    define m_write = Character("Magnolia", kind=nvl)
    define b_write = Character("Balrung", kind=nvl)
    define book = Character("Book", kind=nvl)

    #
    # BACKGROUNDS
    #
    # TODO: delete backgrounds we end up not using.
    image bg library = "bg/library.jpg"
    image bg bedroom day = "bg/bedroom_day.jpg"
    image bg bedroom dusk = "bg/bedroom_dusk.jpg"
    image bg bedroom candle = "bg/bedroom_candle.jpg"
    image bg dungeon = "bg/dungeon_day.jpg"
    image bg dungeon night = "bg/dungeon_night.jpg"
    image bg corridor = "bg/corridor.jpg"
    image bg corridor flip = im.Flip("bg/corridor.jpg", horizontal = True)
    image bg exterior dusk = "bg/exterior_dusk.jpg"
    image bg exterior day = "bg/exterior_day.jpg"
    image bg gate day = "bg/gate_day.jpg"
    image bg gate dusk = "bg/gate_dusk.jpg"
    image bg hall = "bg/hall_day.jpg"
    image bg kitchen = "bg/kitchen.jpg"
    image bg kingdom = "bg/kingdom.jpg"
    image bg ruins = "bg/ruins.jpg"
    image bg stairs day = "bg/stairs_day.jpg"
    image bg stairs = "bg/stairs_dusk.jpg"
    image bg stairs night = "bg/stairs_night.jpg"
    image bg storage = "bg/closet.jpg"
    image bg sunset = "bg/sunset.jpg"
    image bg woods = "bg/woods.jpg"
    image cg1 = "bg/dragon cg.png"
    image cg2 = "bg/dragon cg2.png"
    image logo = "gui/logo.png"

    #
    # VISUAL EFFECTS
    #
    image rain:
        "bg/rain1.png"
        0.1
        "bg/rain2.png"
        0.1
        "bg/rain3.png"
        0.1
        repeat

    #
    # SPRITES
    #
    # For some reason, side images don't automatically import.
    # Maybe they would if they were side princess whatever (instead of princess side whatever), but I'm just defining them manually
    image side princess = "sprites/princess neutral.png"
    image side princess angry = "sprites/princess angry.png"
    image side princess friendly = "sprites/princess friendly.png"
    image side princess laugh = "sprites/princess laugh.png"
    image side princess laugh eyes closed = "sprites/princess laugh eyes closed.png"
    image side princess neutral = "sprites/princess neutral.png"
    image side princess shocked = "sprites/princess shocked.png"
    image side princess shout = "sprites/princess shout.png"
    image side princess smile = "sprites/princess smile.png"
    image side princess surprised = "sprites/princess surprised.png"
    image side princess tsk = "sprites/princess tsk.png"
    image side princess smile eyes closed = "sprites/princess smile eyes closed.png"


    define config.automatic_images = None
    # Automatically import all sprites in the 'sprites' subdirectory
    # Thanks JinzouTamashii, http://www.renpy.org/wiki/renpy/doc/cookbook/Automatically_Defining_Images
init python:
    for fname in renpy.list_files():
        if fname.startswith('sprites/'):
            if fname.endswith(('.jpg', '.png')):
                name = fname.replace('sprites/','').replace('/', ' ').replace('.png','')
                renpy.image(name, im.FactorScale(fname, .667))

                # add green cyril images
                if (name.startswith("cyril")):
                    renpy.image(name + " green", im.FactorScale(im.MatrixColor(fname, im.matrix.desaturate() * im.matrix.tint(0.7, 1.0, 0.7)), .667))

                # add zoomin images at original size
                name += " zoomin"
                renpy.image(name, fname)

    #
    # POSITIONS
    #
    define.move_transitions('move', 0.5)
    define.move_transitions('quickmove', 0.25)
init -1:
    define midleft = Position(xpos=0.35, xanchor=0.5)
    define midright = Position(xpos=0.65, xanchor=0.5)
    define quarterleft = Position(xpos=0.22, xanchor=0.5)
    define quarterright = Position(xpos=0.78, xanchor=0.5)
    define farleft = Position(xpos=-0.30, xanchor=0)
    define farright = Position(xpos=1.0, xanchor=0)
    define sitting = Position(ypos=0.45, yanchor=0)
    define squatting = Position(ypos=0.25, yanchor=0)
    define standing = Position(ypos= 1.0, yanchor = 1.0)

    #
    # TRANSITIONS
    #
    define punch_long = Move((20, 15), (-20, -15), .10, bounce=True, repeat=True, delay=1.5)
    define vpunch_long = Move((0, 15), (0, -15), .10, bounce=True, repeat=True, delay=1.5)
    define hpunch_long = Move((20, 0), (-20, 0), .10, bounce=True, repeat=True, delay=1.5)

    define fade = Fade(0.3, 0.3, 0.3) # TODO: Tweak these times for our game?
    define slowfade = Fade(0.5, 0.5, 0.5)
    define veryslowfade = Fade(2.0, 0.5, 2.0)
    define flash = Fade(.25, 0, .75, color="#fff")
    define magic_flash = Fade(.25, 0, .75, color="#acf")
    define red_flash = Fade(.25, 0, .75, color="#a90000")
    define golden_flash = Fade(.25, 0, .75, color="#f9a900")
    define blood = Fade(.25, 0, .25, color="#f00")
    define dissolve = Dissolve(0.4, alpha=True)
    transform come_closer:
        #zoom 1.5
        yalign 0.0

    transform reset_zoom:
        zoom 1.0
        yalign 1.0

    transform exit_left:
        linear 3.0 xpos -600

    transform exit_right:
        linear 3.0 xpos +600

    transform hop:
        yalign 0.0
        linear 0.5 ypos +30
        pause 0.5
        linear 0.5 ypos 0
        repeat

    transform basicfade:
        on show:
            linear 0.5 alpha 1.0
#        on hide:
#            linear 0.5 alpha 0.0
#        on replace:
#            linear 0.5 alpha 1.0
        on replaced:
            linear 0.5 alpha 0.0

    #
    # MUSIC
    #
    define balrung_theme = "music/Cello.ogg"
    define niir_theme = "music/OniValse.ogg"
    define evil_theme = "music/Malos.ogg"
    define princess_theme = "music/EvilPrincessMarch.ogg"
    define cyril_theme = "music/AwkwardMageWaltz.ogg"
    define happy_ending = "music/SettingTheSails.ogg"
    define intro_music = "music/Pompous.ogg"
