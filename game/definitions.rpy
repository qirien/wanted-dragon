init -1:

    #
    # VARIABLES
    #
    define balrung_affection = 0
    define niir_affection = 0
    define cyril_affection = 0

    #
    # CHARACTERS
    #

    define p = Character('Princess', image="princess", color="#c8ffc8")
    define b = Character('Balrug', image="balrung", color="#c8ffc8")
    define c = Character('Cyril Merlonious', image="merlin", color="#c8ffc8")
    define n = Character('Niir', image="niir", color="#c8ffc8")

    #
    # BACKGROUNDS
    #
    image bg castle_exterior = Placeholder("bg")
    image bg hall = Placeholder("bg")
    image bg bedroom = Placeholder("bg")
    image bg dungeon = Placeholder("bg")


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