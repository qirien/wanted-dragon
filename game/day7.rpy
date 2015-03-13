# DAY 7
label day7:
    # Whoever's route she didn't choose hinders her
    if (route == "Cyril"):
        call cyril7
        
    elif (route == "Balrung"):
        call balrung7
        
    elif (route == "Niir"):
        call niir7

label niir7:
    return
    
label cyril7:
    return

label balrung7:
    scene bg dungeon with fade
    show balrung at center with dissolve
    p "Is that a scroll? Are you writing a letter?"
    b "Princess! I was not aware you had joined me. I'd better put this away..."
    p "Not so fast! Let me see that."
    b "Oh, Princess, you don't want to read this old man's ramblings..."
    p "Is this... Dragon poetry? Did you write this?"
    b "It's not worthy of your attention, please don't..."
    p "Too late! Oh ho ho!"
    b_write "She:{vspace=-10}Eyes shine noble, latent traps{vspace=-10}Supreme mischief."
    b_write "Face sly, young, grand{vspace=-10}Defang grand dragons’ scheme."
    b_write "Map pulse’s sussurus,{vspace=-10}sweet tyrant."
    "This is... about me?! No one's ever written a poem in my honor before..."
    p "I--"
    b "It's terrible, I apologize that you had to see that. I'll just dispose of this awful drivel--"
    p "No. No, I'll keep this."
    b "Indeed? Well... I'm sure you didn't come here to read the musings of an old dragon. Or did you come just to keep me company?"
    # TODO: finish this, add transition
    c "Don't let him ensnare you, Princess, I implore you!"
    p "I am not ensnared by anybody. I love him of my own free will."
    b "You would allow your personal hatred of me to mar the Princess's happiness?"
    b "Mage, of all the hearts in this room, I fear yours is the coldest. You know how long I've languished here. Yet you would deny me forgiveness, even after I've paid the price many times over?"
    c "It's- but the Princess- she can't...I know you're plotting something!"
    p "It is your plot that we are discussing, Moronious. Your plot to keep the dragons here forever."
    
    
    return