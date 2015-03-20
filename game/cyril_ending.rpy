############################################################
# Cyril route ending
#
label cyril_ending:
        # TODO: calculate ignoring times to check for insane ending

    
label mage_insane:
    scene bg dungeon with fade
    show cyril hat neutral at midleft
    show balrung neutral at midright
    show niir neutral at right
    with dissolve
    b "It took only a few short years of solitude to lose your mind."
    b "Are you sure she's even real?"
    c "Yes!  Of course I am!"
    n "Sssshe's interested in you.  Ssshe must not be real."
    c "She is real.  She is the real princess.  Just look at her."
    b "Are you sure about that?"
    n "I can't ssssee a thing."
    p "You blithering fool, Cyril.  They're playing you."
    p "Of course I'm real."
    c "She says she's real!"
    b "Exactly what a false princess would say, don't you think?"
    n "Exacccctly."
    p "Cyril the Clueless.  You astound me.  I came here for a dragon."
    p "But despite your many inadequacies - and there are many - I found myself drawn to you."
    c "I do find it highly unlikely that an apparition would call me inadequate and clueless."
    b "Unless you were making her up to be realistic."
    c "I am!  I am!  So true!  I just wanted it to be true!"
    "Is he for real?"
    p "Oh for the love of..."
    menu:
        "Kiss him.":
            jump mage_insane_kiss
        "Step on his toes.":
            jump mage_insane_step
            
label mage_insane_kiss:
    "..."
    c "Ah, sweet, sweet apparition."
    c "I'm afraid this is the closest that we're going to get to being together for real."
    p "Cyril the Crazy, I just kissed you."
    c "And I'm going to spend all my years in this castle imagining you."
    p "You are completely insane."
    c "Insane with love, my dear."
    p "No, insane with insanity.  I'm leaving."
    c "But you can never leave, as you are in my mind."
    p "Watch me."
    p "Dragons, sorry it didn't work out."
    p "Cyril, this has been a complete waste of my time. Adieu."
    return
    #MAGE INSANE END
    
    
label mage_insane_step:
    c "Ouch!  You trod on me!"
    p "Would an imaginary person do this?" with hpunch
    p "Or this?" with hpunch
    c "Ow!  Ow!  Ow!"
    c "I suppose not.  You must be real after all."
    p "Yes and I was hoping that a certain foolish mage and I might go to the council of mages to get someone else to do this job."
    p "It seems I'm going to need you in the immediate future."
    c "I'm yours my majesty, I mean {i}your{/i} majesty of course."
    p "You had it right the first time."
    


label cyril_scepter_epilogue:
    p_write "To Cyril Merlonious,"
    p_write "The Academy of Mages, House of Master Grivvorn\n"

    p_write "I hope that half-wit you're studying under realizes your potential."
    p_write "Otherwise you can direct him to me."
    p_write "Queen of [k_name],\nChrysandra"
    nvl clear
    return

label cyril_dragon_epilogue:
    c neutral "It’s for the best, Chrysandra.  I know you don’t want to take this potion but I travelled a long way and met up with many, many members of the council in order to get it."
    c smile "So if you would just drink the potion and then rest for a while, I am sure you will be back to normal in no time."
    p "I still think that if I lit enough pants on fire, they might change the law to allow a dragon to be Queen. But… I'll drink it."
    #TODO: some magical VFX
    c smile blush "Thank you, my-your majesty.  I do think it’s best for everyone.  It was quite extraordinary that you became a dragon at all.  It’s good that scepter is now locked away securely so no one else can have the same fate."
    p "Securely? Where exactly did you hide it?"
    c surprised "You mustn’t worry about that my Queen.  But do trust me that it is securely away at the top of the cas- Oh dear.  I must work on holding my tongue more in the future."
    "The top of the castle?! I wondered if I might get it back… but perhaps it was better to stay here, as a human, but a Queen. Well, if I ever tire of being Queen, I know just where to go!"
    p "Don't worry about it, dear. Come here and rub my shoulders; they feel so cramped now that I'm human again. No wings! It's simply dreadful."
    c smile blush eyes closed "Y-yes, your majesty."
    p "That's a good boy.  Mmmmm.  Yeeees."
    p "You certainly are my favorite minion."
    return