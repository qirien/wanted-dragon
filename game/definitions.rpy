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
    define castle_name = "the Castle of the Banished"
    define asked_scepter = "no one"
    define route = None
    define HIGH_AFFECTION = 7
    define MEDIUM_AFFECTION = 3
    define INSANE = 3
    define cyril_dead = False

    #
    # CHARACTERS
    #

    define p = DynamicCharacter("p_name", image="princess", color="#3390a4")
    define b = Character('Balrug', image="balrung", color="#a41c1c")
    define c = Character('Cyril Merlonious', image="cyril", color="#7b1f43")
    define n = Character('Niir', image="niir", color="#fec54d")
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
    image bg closet = "bg/closet.jpg"
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
    image bg storage = "bg/storage.jpg"
    image bg sunset = "bg/sunset.jpg"

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
    image side princess = Placeholder("girl")
    # Automatically import all sprites in the 'sprites' subdirectory 
    # Thanks JinzouTamashii, http://www.renpy.org/wiki/renpy/doc/cookbook/Automatically_Defining_Images    
init python:
    import os
    for fname in os.listdir(config.gamedir + '/sprites'):
        if fname.endswith(('.jpg', '.png')):
            tag = fname[:-4]
            fname =  'sprites/' + fname
            renpy.image(tag, fname)

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
    define punch_long = Move((20, 15), (-20, -15), .10, bounce=True, repeat=True, delay=2.0)
    define vpunch_long = Move((0, 15), (0, -15), .10, bounce=True, repeat=True, delay=2.0)
    define hpunch_long = Move((20, 0), (-20, 0), .10, bounce=True, repeat=True, delay=2.0)
    
    define fade = Fade(0.3, 0.3, 0.3) # TODO: Tweak these times for our game?
    define slowfade = Fade(0.5, 0.5, 0.5) # TODO: Tweak these times for our game?    
    define flash = Fade(.25, 0, .75, color="#fff")
    define magic_flash = Fade(.25, 0, .75, color="#acf")
    define red_flash = Fade(.25, 0, .75, color="#a90000")
    define blood = Fade(.25, 0, .25, color="#f00")
    define dissolve = Dissolve(0.4, alpha=True)
    transform come_closer:
        zoom 1.5
        yalign 0.0
        
    transform reset_zoom:
        zoom 1.0
        yalign 1.0

    transform basicfade:
        on show:
            linear 1.0 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0
        on replace:
            linear 1.0 alpha 1.0
        on replaced:
            linear 1.0 alpha 0.0        
    
    #
    # MUSIC
    # 
    define balrung_theme = "music/MephistoPolka.mp3"
    define niir_theme = "music/OniValse.mp3"
    define evil_theme = "music/Malos.mp3"
    define princess_theme = "music/EvilPrincessMarch.ogg"