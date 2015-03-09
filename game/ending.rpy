label ending:
    if (route == "Balrung"):
        jump balrung_ending
    elif (route == "Niir"):
        jump niir_ending
    else:
        jump cyril_ending

############################################################
# Cyril route ending
#
label cyril_ending:
    # TODO: She should finally call him by his real name!

############################################################
# Balrung route ending
#
label balrung_ending:
    c "There it is again! The scepter's magical echo! Before it fades, I must..."
    c "Resonantia Concretus!"
    p "I can see wisps of something in the air. What did you do, mage?"
    c "That should solidify the resonance for a while. It's coming from...the dungeon. Princess, someone is using the scepter right now!"
    p "Then we must follow the resonance and take it!"
    
    scene bg dungeon with fade
    show cyril at midleft
    with moveinleft
    
    c "Ahhhh!"
    p "Moronious! Don't just stand there; we need to get the scepter!"
    c "The dragons... the curse is broken! That is...not...RIGHT!"
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
                p "Cyril, before I go, there's just one thing I need from you."
                c "Wh-what's that? Oh!"
                p "Your wand." #TODO: foreshadow that he has a wand and uses it to do magic
                c "My...wand? No! Princess! Without my wand, I cannot seal up the dragons again!"
                p "Yes, that was rather the point."
                b "Well done. Shall we depart?"
                p "Finally! Now that I've freed you, on to [k_name], where I will rule, and you may be allowed to help!"
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
                        p "Mwah ha ha ha... he left behind the Scepter of Lavendorm! The fool! Cyril!"
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
                p "My presence is certainly required for {b}MY{/b} plans! Cyril! Your princess is in danger!"
                "Balrung reared back, readying an attack."
                jump cyril_attack
            "Wait it out.":
                p "Hmmm, I must admit, I'm curious who would win if you two begin fighting. What better way to prove who is stronger and more fit to aid me?"
                b "..."
                c "..."
                p "Well? What are you waiting for? Commence battle!"
                b "Cyril, you've seen the Princess. Who do you really think is a greater threat to the safety of this kingdom? Yes, I know she's a \"princess\", and quite an attractive one at that; but she's selfish, lustful for power, and will stop at nothing. She had even agreed to poison you in your sleep if it was necessary for our plan. Would you trust the future of this kingdom to someone like that?"
                p "Poisoning the mage was your idea!"
                b "I was curious how far you'd go. You don't care whose life you have to destroy to get what you want. You don't care about the desires and goals of those around you. I know you, Princess, I've seen into your heart and it's dark with malice."
                c "You'd know all about malice, wouldn't you?!"
                b "Yes. I would. I used to be the same. But, Cyril, after all this time, do you know what I really want to do?"
                c "Yes! You want revenge, and power!"
                b "No. I only want to be able to fly over the mountains and be left alone."
                p "He's lying! He was going to help me destroy [k_name]!"
                b "Cyril, I hope you'll do the right thing and help the Princess see the error of her ways. You mages have helped me to, even though I disagree with the way it was done."
                p "Balrung! I will hunt you down! I will find you and DESTROY YOU!!!"
                # TODO: if her cyril_affection is high enough, send to cyril_attack instead?
                b "Farewell, Princess. I hope you find better things to consume your life than revenge."
                p "Cyril! Stop him! Why are you just standing there?! KILL HIM!"
                # TODO: Feel free to rewrite Cyril's lines better or end this differently
                c "N-no, Princess, I don't th-think I will."
                "Balrung's flapping wings filled the dungeon with dusty gusts, and then he was gone."                
                p "Useless! Betrayed at every turn! When I am Queen, you will regret this!"
                c "You sh-shouldn't be Queen the way you are. I'm terribly sorry, my dear Princess [p_name], but..."
                p "Moronious, you fool, point that wand at the dragon! Not at me!"
                c "Carceratus!!"
                p "What have you done to me?!"
                c "Stay! You will stay here, until you learn to be good! I know, somewhere inside of you, there's goodness and love...please, find it quickly, Princess."
                p "You thought guarding dragons was bad? I {b}will{/b} make your life a hell of mental pain, psychological torture, and physical anguish until you LET. ME. GO!"
                c "I'm so sorry! It's for your own good...."
                # TODO: jump to a common ending where she ends up imprisoned?
                
                
label cyril_attack:                
    c "NOT. SO. FAST!"
    # TODO lightning crackles
    c "YOU WILL NEVER LEAVE HERE!!!!"
    "Balrung breathed a maelstrom of fire in our direction, but Cyril swiped it away with a gesture from his wand. The old dragon pounced forwards as Cyril shouted another spell."
    c "DRACONIS PETROMUNDI!"
    "There was a puff of smoke that sped towards Balrung like an arrow, and when it cleared... he had turned to stone." 
    # TODO: Finish this? Jump to a cyril ending?                