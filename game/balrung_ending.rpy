############################################################
# Balrung route ending
#


label balrung_epilogue:
    scene black with fade
    show text "Epilogue"
    $ renpy.pause(1.6)
    scene bg kingdom with fade
    show balrung smile at center with dissolve
    b smirk "Your kingdom is indeed beautiful, my dear Queen."
    p "Yes... it's a good thing we didn't completely burn it to the ground. Though the fact that their new King could do so at any moment is a wonderful motivator."
    p "I think half the courtiers soiled themselves when you transformed into dragon form at our wedding."
    b smile "Yes... that was quite the scene, wasn't it?"
    p "I only wish Magnolia could have seen it, too, and quivered in terror while you threatened to devour her whole... that would have been so nice."
    b neutral "I think your sister will enjoy the Academy."
    p "Yes... but that's the dark lining hiding behind this silver cloud. If she gains enough power... she could be a danger to us."
    b smirk "She could. But I have plans for that."
    p "Really? Like what?"
    b smile eyes closed "If I tell you, it'll spoil all the fun you could have unraveling it for yourself."
    p "Hmph. Well then, I'm not telling you my plans, either."
    b smirk "I wouldn't have it any other way."
    show balrung smile blush at come_closer with dissolve
    b "Queen:"
    b "Nigh, how wonderful!"
    b "Lost, tragic course!"
    b "Soft tresses, silken neck, quick kisses,"
    b "Savory yon nuptial love vexes,"
    b "Sibilant treasure rhapsodically enchants,"
    b "Sing, glorious sovereign!"
    p "...I don't sing."
    p "But I do kiss, when the mood strikes me."
    show balrung smile eyes closed with dissolve
    $ renpy.pause(1.6)    
    scene black with fade
    return 


label balrung_ending:
    "Now that Moronious was not about to attack us, I wrapped up my arm in a dishtowel and turned to look at Balrung. He lay still, but was breathing."
    "Slowly, he opened his eyes, and I helped him sit up."
    show balrung neutral at center with moveinbottom
    b determined "Such a fool..."
    p "Yes, I shall be glad to be rid of him."
    b angry "I meant you."
    p "How dare you speak to your future Queen so disrespectfully?!"
    b smirk "Is it still disrespectful if I am your King?"
    p "King?!"
    b smile "You freed me, Princess, and I want to aid you. What better way to help you maintain your kingdom than to serve by your side?"
    "He would be useful...but could I trust him?"
    p "You claim to have great power as a dragon. Moronious' spell is now broken, so show me!"
    b smirk "I will."
    hide balrung with red_flash
    scene bg kitchen with punch_long
    "He shook his head and stretched, and stretched, and stretched, skin shimmering into deep red scales. Wings emerged from his back and beat the air like waves crashing against a ship."
    "Balrung breathed a ball of fire at one of the chairs, turning it instantly to ash. His reptilian eyes looked at me for my response."
    play sound "sfx/fireball.ogg"    
    scene bg kitchen with red_flash
    # TODO: fireball vfx?
    menu:
        "Marry Balrung." if (balrung_affection >= HIGH_AFFECTION): #TODO: only if balrung_affection high enough?
            p "Balrung, your patient ruthlessness, and powers over flight and fire, will help you serve me well as my King. Now, let me climb on your back and take us to [k_name]."
            b "What an excellent future we shall have together. None will dare to defy our reign!"
            p "Mwah ha ha ha ha!"
            b "Bwah ha ha ha ha!"
            scene bg sunset with fade            
            "With a rush of wings and dust, we flew out of the dungeon and into the wide evening sky. Balrung let fly a fireball at the gates of his old prison, just for fun."
            play sound "sfx/fireball.ogg"
            "With a dragon on my side, my father would {b}have{/b} to make me Queen... and if not, well, I'd make sure there was no other choice."
            "And Balrung would be an valuable ally to have as we ruled together."
            "I reached down to pat his scaly cheek and could tell from the gleam in his eye that he was thinking the exact same thing. I'd never lack a worthy opponent again."
            p "You're such an ambitious schemer!"
            b "And you're dreadfully ruthless."
            p "Mwah ha ha ha ha!"            
            b "Bwah ha ha ha!"
            call credits
            jump balrung_epilogue
        "Make him an advisor.":
            p "While I admire your patient ruthlessness, you are not fit to be my King. You may be an advisor."
            b "Oh ho ho, I don't think so. A pity. If you change your mind, I am going to go raze the kingdom of [k_name]. You'll be able to find me on the throne by tomorrow afternoon."

        "Leave him here.":
            p "I don't need any King telling me what to do!"
            b "A pity. I rather enjoyed our time together. But I won't try to force you to change your mind. I've learned that lesson, at any rate."
            
    "In a whoosh of wings, he was gone." 
    scene bg kitchen with hpunch    
    if (cyril_dead):
        "Leaving several shiny red scales behind."
        p "With these, I can make as many Potions of Persuasion as I want! I'll become Queen all on my own! Mwah ha ha ha ha!"
        # TODO: kidnapped by Niir, who is now free? Or rules on her own?
        return
    else:
        p "..."
        show cyril neutral hat at center with moveinleft
        c "...Princess! I found it! The Scepter! It was under Balrung's bed the whole time!"
        p "Mwah ha ha ha... he left behind the Scepter of Lavendorm?! The fool! Moronious!"
        c "Y-yes your highness?"
        p "Shall we attack that evil dragon?"
        c "We shall!"
        play sound "sfx/electricity.ogg"
        # TODO lightning crackles.
        # TODO: jump to a Cyril ending?
        call credits
        #TODO jump some epilogue?
        return
    
# Not using; keeping around for copy paste purposes
label old_balrung_ending:
    c "There it is again! The scepter's magical echo! Before it fades, I must..."
    c "Resonantia Concretus!"
    p "I can see wisps of something in the air. What did you do, mage?"
    c "That should solidify the resonance for a while. It's coming from...the dungeon. Princess, someone is using the scepter right now!"
    p "Then we must follow the resonance and take it!"
    
    scene bg dungeon with fade
    show cyril hat neutral at midleft
    with moveinleft
    "When we got to the dungeon, Balrung and Niir were nowhere to be seen."
    c "Ahhhh!"
    p "Moronious! Don't just stand there; we need to get the scepter!"
    c "The dragons... the curse is broken! That is...not...RIGHT!"
    #TODO show dragon shadow/head at right with vpunch
    "The ground trembled, and a giant shadow emerged from the corner of the room. No, not a shadow-- a dragon. Two dragons."
    b "It {b}is{/b} right! Your prejudice and arrogance have gone far beyond justice and on to revenge for crimes not yet committed!"
    #TODO: lightning crackle
    n "Nicccce work, old man. But I'm leaving."
    if (route == "Niir"):
        n "Coming, Princesssss?"
        p "Yes, now that I've freed you, we shall turn our attention to my kingdom."
        n "Let'sss fly."
        jump niir_end
    
    c "Niir! You must stay! You WILL-- oof!"
    "Balrung's tail came out of nowhere and knocked Cyril to the ground."
    b "I'll supervise Niir. That's what you mages should have done in the first place; let dragons discipline dragons."
    c "That wouldn't work! Nobody can trust you!"
    if (route == "Balrung"):
        b "So you say. But the Princess and I have managed to work out an arrangement. Princess?"
        menu:
            "Grab Cyril's wand.":
                p "Moronious, before I go, there's just one thing I need from you."
                c "Wh-what's that? Oh!"
                p "Your wand."
                c "My...wand? No! Princess! Without my wand, I cannot seal up the dragons again!"
                p "Yes, that was rather the point."
                b "Well done. Shall we depart?"
                p "Finally! Now that I've freed you, on to [k_name], where I will rule, and you may be my minion!"
                b "Oh, did I forget to mention? If you want me to help you with your kingdom, we will need to rule together."
                p "Together? There can be only one Queen!"
                b "But you may sometimes find it useful to have a King to help you. Don't you agree that we work well together?"
                c "Princess, no! He'll destroy your kingdom! All he knows is bitterness and destruction!"
                b "Merlonious, you don't understand in the slightest. There is no point in destroying a kingdom you intend to rule. That would be like ruling an empty castle... as you may do, with this castle, now."
                menu:
                    "Agree to marry Balrung.": #TODO: only if balrung_affection high enough?
                        p "Balrung, your patient ruthlessness will help you serve well as my King. Now, let me climb on your back and take us to [k_name]."
                        b "What an excellent future we shall have together. None will dare to defy our reign!"
                        p "Mwah ha ha ha ha!"
                        b "Bwah ha ha ha ha!"
                        c "Noooooooooo!"
                        "With a rush of wings and dust, we flew out of the dungeon and into the blue, blue sky. Balrung let fly a fireball at the gates of his old prison, just for fun."
                        "With a dragon on my side, my father would {b}have{/b} to make me Queen... and if not, well, if Magnolia was dead he'd have no choice."
                        "And Balrung would be an intelligent ally to have as we ruled together. If he crossed, me, though... I brought along some new poison recipes from the library."
                        "I reached down to pat his cheek and could tell from the gleam in his eye that he was thinking the exact same thing. I'd never lack a worthy opponent again. How exciting!"
                        p "You're such an ambitious schemer! I love that about you."
                        b "Is it evil of me if I love how dreadfully ruthless you are?"
                        p "Probably."
                        b "Bwah ha ha ha!"
                        p "Mwah ha ha ha ha!"
                        jump credits
                    "Offer to make him an advisor.":
                        p "While I admire your patient ruthlessness, you are not fit to be my King. You may be an advisor."
                        b "Oh ho ho, I don't think so. A pity. If you change your mind, I am going to go raze the kingdom of [k_name]. You'll be able to find me on the throne by tomorrow afternoon."
                        "In a whoosh of wings, he was gone."
                        p "..."
                        c "...Princess? Can I have my wand back, now?"
                        p "Mwah ha ha ha... he left behind the Scepter of Lavendorm! The fool! Moronious!"
                        c "Y-yes your highness?"
                        p "Shall we attack that evil dragon?"
                        c "We shall!"
                        # TODO lightning crackles.
                        # TODO: jump to a Cyril ending?
                    "Give Cyril back his wand.":
                        p "That wasn't our agreement, Balrung. I detest betrayal."
                        "As I moved closer, I stood in front of Cyril, handing him back his wand behind my back."
                        b "A pity. Well, if you change your mind, I'll be-"
                        jump cyril_attack
            "Try to help Cyril.":
                p "Balrung, it was rather foolish of you to trust me so easily."
                "As I talked, I scanned the room. Where was the scepter? Balrung had used it earlier to break the spell, but I didn't see it in his hands- er, talons."
                b "Oh, Princess, Princess. I let you win a few games of Queens and Pawns, and you imagine yourself some kind of master strategist. I don't need {b}you{/b} in order to claim your kingdom. It would have smoothed things over with the nobles, that's true, but your presence is certainly not necessary to my plans."
                p "My presence is certainly required for {b}MY{/b} plans! Moronious! Your princess is in danger!"
                "Balrung reared back, readying an attack."
                jump cyril_attack
            
                
                
label cyril_attack:                
    c "NOT. SO. FAST!"
    play sound "sfx/electricity.ogg"
    # TODO lightning crackles
    c "YOU WILL NEVER LEAVE HERE!!!!"
    "Balrung breathed a maelstrom of fire in our direction, but Cyril swiped it away with a gesture from his wand. The old dragon pounced forwards as Cyril shouted another spell."
    play sound "sfx/lightning.ogg"
    c "DRACONIS PETROMUNDI!"
    "There was a puff of smoke that sped towards Balrung like an arrow, and when it cleared... he had turned to stone." 
    # TODO: Finish this? Jump to a cyril ending?                
    

label imprisoned_epilogue:
    scene bg dungeon with fade
    show cyril hat concerned at midleft with moveinleft
    c "I've brought you your breakfast, your Highness."
    "I threw the bowl at his ridiculous face and it knocked off his ridiculous hat. Niir snatched it up and grinned."
    show cyril surprised with dissolve
    show niir at midright with moveinright
    n mischief "Oooh, you're a much more interesssting companion."
    c concerned blush "That was quite uncalled for.  I don’t think you’ve made any progress with your reform, you know."
    c concerned eyes closed "Your father expects me to keep him updated and at this rate I will have nothing to update him with!"
    p "My sister put you up to this, didn't she?! DIDN'T SHE?! She thinks she's won, but she's wrong! Eventually I will escape and PUNISH YOU ALL!!!!"
    c neutral "Now, now Princess.  It might have taken me a week, but you were always going to show your true colors at the end.  Just start reflecting on your own behavior and soon you will understand what it is you have to do."
    c smile "I do believe you can change.  I have seen it happen to dragons, why not you?"
    p "...I will kill you. I will rip off your fingers and toes one by one and feed them to your stupid dragons!"
    n frown "...that's disgusssting!"
    c concerned blush "I will let that slide because I know you don’t mean that, Princess.  I’ll tell your father that you’re starting to see the error of your ways."
    c neutral "See you at dinner, when I do hope you will be more agreeable."
    "It was impossible. How had it come to this?! I thought I had him wrapped around my finger, and then…"
    "...but I refused to be beaten. It wasn't too late to escape this hell and return to [k_name]. I'd just have to be more careful, lay better plans, put on my good-princess face, and THEN take my revenge. On all of them!"
    "Mwah ha ha ha ha!"
    