init -1:

    #
    # VARIABLES
    #
    define balrung_affection = 0
    define niir_affection = 0
    define cyril_affection = 0
    define p_name = "Chrysandra"
    define k_name = "Novaria"
    define asked_sceptre = "no one"
    define route = None

    #
    # CHARACTERS
    #

    define p = DynamicCharacter("p_name", image="princess", color="#c8ffc8")
    define b = Character('Balrug', image="balrung", color="#c8ffc8")
    define c = Character('Cyril Merlonious', image="merlin", color="#c8ffc8")
    define n = Character('Niir', image="niir", color="#c8ffc8")
    define p_write = Character("Princess", kind=nvl)
    define k_write = Character("King", kind=nvl)
    define m_write = Character("Magnolia", kind=nvl)
    
    #
    # BACKGROUNDS
    #
    # TODO: delete backgrounds we end up not using.
    image bg exterior = "bg/exterior_dusk.jpg"
    image bg library = "bg/library.jpg"
    image bg bedroom = "bg/bedroom_dusk.jpg"
    image bg dungeon = "bg/dungeon_day.jpg"
    image bg corridor = "bg/corridor.jpg"
    image bg corridor flip = im.Flip("bg/corridor.jpg", horizontal = True)
    image bg gate = "bg/gate_dusk.jpg"
    image bg hall = "bg/hall_day.jpg"
    image bg kitchen = "bg/kitchen.jpg" 
    image bg stairs = "bg/stairs_dusk.jpg"
    image bg storage = "bg/storage.jpg"


    #
    # SPRITES
    #

    image princess = Placeholder("girl")
    image balrung = Placeholder("boy")
    image cyril = Placeholder("boy")
    image niir = Placeholder("boy")

    #
    # POSITIONS
    #
    define fade = Fade(0.2, 0.2, 0.2) # TODO: Tweak these times for our game?
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
    # MUSIC
    # 
    define balrung_theme = "music/MephistoPolka.mp3"
    define niir_theme = "music/OniValse.mp3"
    define princess_theme = "music/Malos.mp3"