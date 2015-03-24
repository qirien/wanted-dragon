label day8:
    scene bg bedroom dusk with fade
    play music evil_theme
    "Time is running out; Magnolia's coronation will take place tomorrow, unless I can find a way to stop it!"
    "Careful plots would take too much time; I needed to act now."
    if (route == "Niir"):
        jump niir8
    elif (route == "Cyril"):
        jump cyril8
    elif (route == "Balrung"):
        jump balrung8
        
    return

label niir8:
    scene bg dungeon with fade
    show niir neutral at center, basicfade
    
    p "Niir, it is time."
    n "What sssurrrpise do you have forrr me today?"
    p "Come with me and find out."
    n "The suspensssse is delicioussss."
    
    scene bg library with fade
    show cyril hat neutral at midleft, basicfade
    show niir neutral at midright with moveinleft
    play music cyril_theme
    p "Moronious, we are ready."
    show cyril hat surprised at basicfade
    c "Wh-?  {i}Please{/i} don’t sneak up, Princess.  Oh.  Of course.  {b}Niir{/b}.  He must have put you up to it."
    p "I shall ignore your ridiculous insinuation that I would be \"put up\" to anything I did not wish to do. Try our love, mage. It is strong enough to overcome even your foolish \"test\"."
    show cyril hat laugh at basicfade
    c "Oh yes.  Your \"love\".  You’re still on with that charade, are you?"
    n "It'sss no charade! She'sss my ssssweet little... hamhocks."
    p "Yes, exactly. See, we're even holding hands."
    show cyril hat eyes closed smile at basicfade
    c "If you two insist."
    show cyril hat laugh at basicfade
    c "This will be my amusement for the day.  Let’s begin."
    show cyril hat concerned at basicfade
    c "Niir! What is the Princess's favorite breakfast?"
    n "Nothing you could make for her, that’s for sssssure."
    show cyril hat neutral at basicfade
    c "So that’s your answer then?  Too bad, Niir."
    n "Wait!"
    $ quiz_questions = 0
    if (niir_affection >= HIGH_AFFECTION):
        n "She likessss..."
        "I sidled over out of Cyril's line of sight and mouthed the word \"eggs\"."
        n "Eggssss!"
        c "Hmph. A lucky guess, I'm sure of it."
        $ quiz_questions += 1
    else:
        n "She likesss crispy bacon, ssssucculent ham, and juicy ssssausage with a sssside of undercooked ssssquirrel.." 
        show cyril hat neutral at basicfade
        c "Squirrel?  And you do realize that ham and bacon are the same animal don’t you?"
        p "I- yes, I like squirrel! Ham, bacon, mmmm!"
        c "I’ll serve it to you then and see how much you eat.  Unless you’d just like to submit to the truth and move on."
        p "You couldn't conjure it if you tried. I know how you've been feeding these dragons!"
        c "I don't need to; I can tell you're lying."

    c "Anyway! Next question!"
    c "Princess! Who were Niir's parents?"
    n "Why would I tell her about my parentssss, sssstupid mage?"
    menu:
        "He doesn't know them." if (niir_affection >= HIGH_AFFECTION):
            p "That is a trick question! Niir doesn't even remember his parents, but Balrung has been like an inconvenient father."
            show cyril hat concerned at basicfade
            c "Well, it seems you have been doing more in the castle than just causing a ruckus together."
            n "We haven't been doing nearrrly enough ruckussssing..."
            c "I guess that is something positive."
            $ quiz_questions +=1
        "Some really nice dragons":
            p "His parents were...both dragons...and they were... very kind and beautiful. For dragons."
            c "And I expect that Niir is the one that told you this?"
            n "..."
            c "As I thought."
        "Ghiulana and Zanbatar":
            p "Their names were Ghiulana and Zanbatar. They were heartbroken at Niir's imprisonment and hope and pray with all their hearts that the dishonorable mage who has him in custody will soon relent and return their beloved son."
            n "...did you ever lisssten to anything I sssaid?!"
            c "Obviously not!"
    
    c "Question Three!"
    c "What is the Princess' favorite pastime?"
    if (niir_affection >= HIGH_AFFECTION):
        n "Ssshe likes making potionsss. And scheming."
        c "I don’t know about the scheming.  But I’ll give you the point for the potions.  At least you said something somewhat believable."
        p "If you really don't believe him, I have a potion for that."
        $ quiz_questions += 1
    else:
        n "That’ssss easssy.  Knitting hass to be it." 
        p "What?! The only thing I'd knit is a noose for your asinine neck!"
        n "Ssssuch a lady."

    c "Last question!"
    c "What is Niir’s favorite thing to hunt?" 
    menu:
        "Women, and rabbits" if (niir_affection >= HIGH_AFFECTION):
            p "He pretends to enjoy seducing women, but the truth is he's never even kissed one. As for meals, rabbits would be his prey of choice." 
            show niir frown blush at basicfade
            n "..."
            show cyril hat blush smile at basicfade
            c "Is that so?"
            show niir angry at basicfade
            n "Liessss, Cccyril the Chaste.  Liesss."
            c "No, I’d have to side with the princess on this one.  Absolutely correct."
            n "..."
            $ quiz_questions += 1

        "Foolish mages":
            p "Foolish mages like yourself, Moronious."
            n "Ssssstart running Cccyril the Cowardly."
            c "Yes, very amusing.  But joke answers are not accepted as real answers.  We have already been through the rules."

        "Deer":
            p "Deer, of course. That's what I like to hunt."
            n "...yesss, I love to hunt those... deer."
            c "And what does a deer look like Niir?  The alive type, not the type that have already been roasted and served on a plate."
            n "It issss pink, and hassss a curly tail.  With spotssss.  Lotsss of spotsss."
            p "That's a pig. And you call yourself a carnivore..."

    c "And, one final bonus question!"
    n "That'sss not fair, you sssaid the other one was the lassst."
    show cyril hat smile at basicfade
    c "Princess, why is it that this lout of a dragon Niir has not yet left the castle?"
    menu:
        "He hadn't met me yet.":
            p "He hadn't met me yet. Obviously."
            c "Oh, well.  I guess you do have a point.  But I do find it hard to believe that despite your... uniqueness that Niir has really changed."
            n "Ssshe can do what no one elsssse can."
            n "Let her ssshow you."
            c "Erm, well yes.  I suppose some progress has been made already.  But is it really love?  That is the question."
        "You'll never let him go.":
            p "Even if he changed into a butterfly, you'd still see him as a menace."
            c "You don’t understand princess.  He {b}is{/b} a menace.  I let him go and then it will be my job to go out and round him up all over again for disturbing the peace!  It is much simpler this way."
            n "Peaccccce is overrated, Ccccyril."
            p "Well, you could trust me to keep a leash on him. I certainly wouldn't allow him to cause trouble in [k_name]."
        "He has too much loyalty to Balrung.":
            p "Can't you see? It's his sense of filial duty to his surrogate father, Balrung. As long as he is imprisoned here, Niir is loath to leave his side. My poor, noble, Niir..."
            c "Oh.  I didn’t even consider that possibility."
            n "That'sss because it's not a posssibility."
            c "I suppose the dragons are... close...  I am not really sure how dragons show filial affection but maybe that is what Niir has been doing all along."
            p "You see?  But now he has me, and so he must leave poor Balrung and begin a new glorious life in service to his queen.  Unless you’d permit Balrung to come with us..."
            c "Absolutely not!"
            p "I tried, Niir.  You tell Balrung that I tried."    

    c "Very well! The test is over!"
    if (quiz_questions >= 4):
        c "I-I'm not sure how you did it, but somehow you’ve managed to astound me with how in sync you are."
        c "But is it {i}love{/i}?  I cannot figure that out."
        n "Perhapssss you sssshould let usss figure that out ourselvessss."
        c "Very true, Niir.  Perhaps I should."
        c "I can’t believe I am saying this.  I thought I would have to deal with Niir’s childish taunts until the day I got old and died in this castle."
        n "Very sssad."
        c "Regardless, I suppose I can let you go."
        c "Don’t make me regret this, Niir.  I feel like I’m regretting it already.  If you are anything less than completely loyal to this lovely young princess..."
        p "I will string him up by his dragony sinews and boil his scales for my potions. Until he learns his lesson."
        n "Pleassse don’t."
        c "{font=fonts/ankecallig-fg.ttf}{size=+10}INCARCERUS TERMINE{/size}{/font}!"
        show cyril hat angry with magic_flash
        play music happy_ending
        "Niir shimmered a little, and there was a distant noise like breaking glass."
        n "It isss done?  I feel... {i}powerful{/i} again."
        n "I will not sssstay here one minute more."
        p "Then it's time for us to fly."
        hide niir with golden_flash
        "Niir closed his eyes, concentrating, and then shifted, his skin turning golden and scaly, his frame lengthening. Huge glimmering wings unfolded behind him, and he stamped the ground with clawed feet."
        n "Let’ssss."
        play sound "sfx/wings.ogg" loop
        "I climbed on his back, looping my arms around his neck. Cyril frowned up at us disapprovingly as the wind from Niir's wings swirled around him, but did nothing to stop our flight."
        n "He let ussss go."
        p "Less talking, more flying!"
        n "Would you like to try ssssomething... dangerousss?"
        p "Of course!"
        n "Then grrrip me tightly, Prrrincesssss..."
        "I dug in my heels and clutched his wings right where they met his back. He twisted into a barrel roll, then looped several times. I almost fell off, but had never felt so alive."
        n "Direct me to your casssstle."
        p "Onward!"
        stop sound fadeout 2.0
        call credits
        jump niir_free_epilogue
    else:
        c "As I thought! The only thing between you is lies and plots!"
        n "Not true.  There issss alsssso the mutual wish to sssee you ssssuffer."
        p "So, you won't let him go? You'll force me to find some other way to be with my true love?"
        c "Well, I suppose if your father agrees to have you stay here in the castle, it wouldn’t be too bad to have you around as extra company.  Though I would not like to have to the be constant chaperone to you and the dragon."
        p "Well, I can show you how that will go right now. Niir, come with me. Moronious, you may not come."
        c "Ah, yes.  I don’t think it’s a good idea to leave you two alone right now."
        p "Then follow us, if you dare."

        scene bg ruins with fade
        show niir neutral at center with fade
        play music niir_theme
        p "Is he following us?"
        n "Yesss, I can ssstill sssmell that mage around here."
        menu:
            "Let's take him by surprise.":
                p "You're no weakling; why not take him by surprise?"
                n "I ssssupossse he won’t be expecting that."
                hide niir at basicfade
                "We walked around a corner, and Niir hung back behind a pillar. Sure enough, soon Moronious came creeping by."
                show cyril hat surprised at center
                show cyril hat surprised at basicfade
                c "Princess? Where's Niir?"
                "Just then Niir swung out from behind the mage and knocked his feet out from under him."
                "That sleight of hand was just what I needed to take the mage’s wand."
                c "{font=fonts/ankecallig-fg.ttf}INCARCERATUS{/font}!"
                c "Why isn’t it-?  My hand seems to be empty."
                c "Niir, this is {b}no{/b} joke.’"    
                p "Tie him up, Niir. Here. Look familiar?"
                n "My rope.  I sssshould have known."
                p "Aren't you glad I didn't hang myself with it?"
                n "Yessss, now hold sssstill Ccccyril."
                c "I will do no such thing!  Let me go you brute, or I’ll have to-"
                p "We can't have you calling for help or casting spells, either. You didn't need the hem of this robe, right?"
                c "This is a special magical garment!  You cannot merely- I am warning you-"                
                play sound "sfx/rip.ogg"
                c "The council will be hearing about this.  A princess, in cahoots with a dragon!  It will not go overlooked."
                p "Good! Let them learn to fear me! Now, you will be silent."
                c "I hardly thi- Mmmffffhhh..."
                n "Nicccce work, Princesssss."
                jump secret_weapon
    
            "Let's get Balrung to help.":
                p "Let's get Balrung to help. If the three of us attack him, we should be able to overpower him."
                n "Give me a sssssecond."
                hide niir with moveoutright

                "I waited patiently, but I didn't realize that those two dragons had already started the attack without me until I heard the noise of spells being cast. I ran towards the source of the sound - by the castle gates."
                scene bg gate dusk with fade
                show balrung at quarterright, basicfade
                show cyril at center, basicfade
                show niir at quarterleft, basicfade
                n "Your sssspellsss can’t ssstop usss thisss time."
                c "Oh yes they can!  They have before and they will again.  You will answer to the council of- Oof!"
                show niir at center with quickmove
                show cyril surprised at squatting with quickmove
                "Niir tackled Cyril and his wand and hat went flying."
                show cyril angry at standing with move
                show cyril angry at basicfade
                c "I don't need my wand for this spell! IGNI-"
                "Balrung came up behind him and gagged him with a strip of cloth so he couldn't cast any more spells."
                show balrung at midright with quickmove
                p "Good work.  I don’t know why you two haven’t tried doing this more often.  Then he would have had to have let you go."
                b "The problem is, he can't break the spell unless I allow him to speak. But the moment I do that...well, I have little faith that he will do so."
                p "But I don’t need him to break the spell.  I can only take one of you, and I’ve already agreed to take Niir.  Certainly, you can understand Balrung."
                p "So you can enjoy your captivity, and the two of us will be off."
                b "Unacceptable. I will remove this gag and let him continue his spells if that is your course of action."
                n "Isss that the way you want to play it, old frrriend?"
                p "If you side with that mage, I will make sure you rot in here when I am queen." 
                b "How is that any different than if I let you go? Either way, I'm trapped here. alone."
                n "Yessss, perhapsss I will sssend sssome princessessss your way.  If I remember."
                b "I think we both know you have no intentions of aiding me unless you have to."
                n "Then let ussss fight.  Whoever winsss getsss to go with the princesss."
                b "I hardly dare agree to such an unfair arrangement. You have so little experience, and so meager intelligence, that your chances are defeating me are minimal."
                n "Experiencccce and intelligencccce are not everything, old fool." 
                p "This is ridiculous. I did not say I would help whoever won some sort of primeval dragon duel. I chose Niir, and that's whom I will aid!"
                b "Still... I suppose your death would be a small price to pay for my freedom."
                n "Then you ssshall have to kill me."
                "No one ignores me like that! That violent viper will have me to contend with as well!"
                "Balrung dropped Cyril and lunged at Niir, attempting a chokehold. But Niir slithered out of his grasp and tried to pin his arms from behind. Balrung flung his head back and hit Niir in the nose."
                "Blood gushed down Niir's face as the two circled each other warily. This time it was Niir who attacked first, aiming a punch at Balrung's face. But Balrung caught his fist and turned his own weight against him, throwing Niir to the ground."
                "The old dragon stepped on Niir's chest, pinning him to the ground, and was about to attack again when I called out."
                p "I've had enough of your bickering! I'm leaving!"
                "Balrung looked over at me long enough for Niir to twist his ankle and send him sprawling as well. I ran over to see if I could help, when suddenly we heard the mage's voice shout."
                c "CARCERATUS!" #TODO: VFX? Glowing magical bars?
                play music princess_theme
                p "What is this?! I am no dragon; you have no right to imprison me!"
                c "I am very sorry to have to do this, your Highness! But I cannot abide your wrongdoing any longer!"
                p "Impossible! I am a PRINCESS! I am your future QUEEN!"
                c "Now, now, that's enough yelling, Princess. You forced my hand.  Siding with the dragons like this.  You really are responsible for this."
                c "I’ve told you all along, you cannot trust these dragons.  They will only put themselves first." 
                n "Sssorry, Princessss...we were ssso clossse! But at leassst we can keep each other company."
                p "Shut up, you imbecile!  I can’t believe I agreed to help you!"
                n "...Sssso much for \"love\"..."  
                call credits
                jump imprisoned_epilogue

            "Kiss me.":
                p "Hmph. Very well then. Kiss me. It'll make him leave us alone."
                show niir frown blush at basicfade
                n "Princessss, I-"
                p "No words! Just kissing!"
                n "..."
                n "I sssshould not want to ssstart sssomething I cannot ssstop, princesss."
                p "Do you trust yourself so little? Fortunately, I trust you more."
                n "How sssstupid of you."
                show niir neutral at come_closer
                "I seized his ridiculous ears and brought our lips together.  He struggled a little at first but I made sure to put a stop to that by putting a foot in his shin."
                "He gingerly put his hands on my hips, then held me tighter as I ran my fingers through his hair. Not bad, for his first kiss." #TODO: this sounds off to me.
                p "Is he gone yet?"
                n "..."
                p "I’m talking to you, dragon.  Is.  He. Gone?"
                n "Yessss.  Yesss, he isss gone."
                show niir neutral at reset_zoom

    label secret_weapon:
        p "Now it's time for my secret weapon."
        n "Is it in your blousssse?"
        p "Yes, actually it is. Would you mind getting it for me?"
        n "..."
        p "Oh, very well, must I do everything myself?!"
        "I pulled out a glass vial full of a fizzy purple liquid."
        n "It really wasss in your bloussse.  Is it poissson?"
        p "Of course not. Drink it."
        n "Your inssssisstence that I drink doesss not reasssure me that it isss not poissson."
        p "Why would I go through all the trouble of seducing you and getting rid of that mage just to kill you? I want you free so you can aid me!"
        n "Not for amusssement?"
        p "What kind of evil princess do you think I am?!"
        n  "One lassst kissss before I drink.  If it isss poisssson, I want it to be worth it."
        p "Well, I suppose we have time for one-"
        show niir smirk at come_closer, basicfade
        "Well. This kiss was much more satisfactory. At least the dragon could learn quickly."
        show niir neutral at reset_zoom, basicfade
        show niir smirk at basicfade
        n "Bottomssss up."
        p "You have no idea."
        "He drank the entire vial in one gulp. Good, I was beginning to worry he wouldn't do it."
        p "Now, try not to belch."
        hide niir at basicfade
        play music princess_theme
        "I hoisted him up onto my shoulder. With the weight-reducing potion in effect, it was as easy as carrying a sack of potatoes. Not that I had ever carried sacks of potatoes. But I'd seen it done. It looked easy."
        n "Don’t ssstrain yoursssself, princessss."
        "I strode over to the barrier. It was barely visible as a slight haze in the air. I probably should have packed some provisions or tools or something, but I was done with this place."
        "Hopefully once Niir was out of the castle and had regained consciousness, he could turn into a dragon and fly us the rest of the way to [k_name]."
        p "Hold on, Niir, this may hurt a bit."
        "He didn't even scream as I walked through the barrier; just went limp. No alarms rang or mages popped out of the air."
        "It was easier than I expected.  Stopping my sister’s coronation was probably not going to be quite so easy."
        "But I {b}would{/b} be Queen. No matter what!"

        call credits
        jump niir_asleep_epilogue


label cyril8:
    scene bg library with fade
    show cyril hat neutral at center, basicfade
    p "Time is running out, Moro-, er, Cyril. Unless you have something for me today, I will be forced to pursue other...options."
    c "I know, I know.  Time is of the essence.  I have been staying awake at night thinking of what to do about it but to no avail."
    p "Hmph. Then I will find something on my own. How unfortunate that your power was not enough to bring me the one thing I truly need."
    c "W-wait! One more time!"

    c "There it is again! The scepter's magical echo! Before it fades, I must..."
    c "{font=fonts/ankecallig-fg.ttf}Resonantia Concretus{/font}!"
    p "I can see wisps of something in the air. What did you do, mage?" #TODO: vfx for this?
    c "That should solidify the resonance for a while. It's coming from...the dungeon. Princess, someone is using the scepter right now!"
    p "Then we must follow the resonance and take it! What are you waiting for?!"
    c "R-right!"

    scene bg dungeon night with fade
    show cyril hat neutral at center
    with moveinleft
    play music balrung_theme
    "When we got to the dungeon, Balrung and Niir were nowhere to be seen."
    show cyril hat concerned eyes closed at basicfade
    c "Ahhhh!"
    p "Cyril! Don't just stand there; we need to get the scepter!"
    show cyril hat angry at basicfade
    c "The dragons... the curse is broken! That is...not...RIGHT!"
    #TODO show dragon shadow/head at right with vpunch
    "The ground trembled, and a giant shadow emerged from the corner of the room. No, not a shadow-- a dragon. {b}Two{/b} dragons."
    b "It {b}is{/b} right! Your prejudice and arrogance have gone far beyond justice and on to revenge for crimes not yet committed!"
    n "Nicccce work, old tortoissse. But I'm leaving."
    show cyril hat concerned eyes closed at basicfade
    c "Niir! You must stay! You WILL-- oof!" 
    hide cyril with quickmoveoutleft
    "Balrung's tail came out of nowhere and knocked Cyril to the ground."
    b "I'll supervise Niir. That's what you mages should have done in the first place; let dragons discipline dragons."
    show cyril concerned at center with moveinleft   #he lost his hat
    c "That wouldn't work! Nobody can trust you!"
    show cyril concerned eyes closed at basicfade
    c "..."
    show cyril angry at basicfade
    c "And wait Balrung, WHERE IS THAT SCEPTER?!" 
    "As they talked, I scanned the room. Balrung had used it earlier to break the spell, but I didn't see it in his hands- er, talons. But traces of Cyril's spell still lingered and led me to it."
    p "You mean...this scepter? Really, Balrung, under the bed is such an obvious hiding place." 
    show cyril surprised at basicfade
    c "Of course, I should have seen it.  I am sorry, my highness."
    b "I put it there for you to find, Princess. I've already used the scepter for what I needed. And now I've passed it on to you. I know you'll put it to much better use than this fool."
    show cyril concerned blush eyes closed at basicfade
    c "No, don't! It's too powerful; you can't control it without magical training! It could kill you, {i}kill{/i} you, Princess!"
    menu:
        "Give the scepter to Cyril" if (cyril_affection >= HIGH_AFFECTION):
            p "Cyril, I'm trusting you with this. Don't fail me!"
            show cyril smile blush at basicfade
            c "I won’t, Princess."
            b "You're making a mistake!  I WILL not be imprisoned AGAIN!"
            show cyril angry at basicfade
            c "You were the one making the mistake. And now you will reap the consequences of such a mistake."
            play sound "sfx/electricity.ogg"
            "Cyril started to chant, preparing some kind of powerful magic, I hoped."
            "Balrung breathed a maelstrom of fire in our direction, but Cyril swiped it away with a gesture. The old dragon pounced forwards as Cyril brandished the scepter at him and shouted another spell."
            play sound "sfx/fireball.ogg"
            show cyril angry at basicfade
            c "{font=fonts/ankecallig-fg.ttf}{size=+10}DRACONIS PETROMUNDI{/size}{/font}!"
            play sound "sfx/lightning.ogg"
            show cyril angry with magic_flash
            "There was a puff of smoke that sped towards Balrung like an arrow, and when it cleared... he had turned to stone."
            p "You...stopped him. Cyril, that was...power!"
            show cyril smile blush at basicfade
            c "Ah, yes.  I suppose it was, mostly.  This scepter is very dangerous buisness.  "
            extend "I think I’ll hold on to it."
            p "And I'll hold on to {b}you{/b}."
            show cyril concerned blush at center,come_closer
            show cyril smile blush eyes closed
            "I grabbed the sleeves of his robe and kissed him thoroughly. He was too surprised to respond at first, and almost dropped the scepter, but soon he had his arms around me awkwardly and was attempting some sort of kiss in response. It was...adorable. Yes, perhaps now he was worthy to aid me."
            p "Yes...Cyril, I think it's time for you and I to stop a coronation. When my father sees the power we possess, he will certainly change his mind."

            call credits
            jump cyril_scepter_epilogue


        "Use the scepter on Balrung":
            p "Cyril is right about one thing, dragon. You should not be free; you'll cause me too much trouble."
            "I pointed the scepter at him and focused my will on it."
            p "Hyaaaaah!"
            b "..."
            show cyril surprised at basicfade
            c "..."
            "...Nothing happened."
            b "Ho, ho ho ho. I spent years practicing with that artifact, using it carefully for minutes at a time so Merlonious wouldn't detect anything! You think to use it on {b}me{/b} after holding it for mere moments?"
            "Balrung reared back, jaws gaping wide open. To breathe fire? To swallow us whole?"
            show cyril concerned blush eyes closed at basicfade
            c "Princess!  Hide!  Don’t let that beast have the scepter!  I beseech you!"
            "This was not a battle in which I wanted to risk my royal person; that's what minions are for. I dived out into the hallway, leaving Cyril and Balrung to fight it out on their own."
            "Balrung swiped at Cyril with his claws, but Cyril managed to roll out of the way."
            show cyril concerned at basicfade with hpunch
            c "She won’t give you the scepter, so we may as well stop this Balrung.  You must surrender yourself to me, and I will have the council decide what to do with you."
            b "I know what your Council would do with me. The same thing they've done for forty years!"
            b "I'd rather die a free dragon than live an enslaved half-existence as a human! Rrrraaaagh!"
            show cyril surprised at basicfade with vpunch
            "The room filled with a raging inferno of fire breath. A shimmering magic shield surrounded Cyril, and I stepped back to avoid getting my hair singed."
            show cyril angry at basicfade with red_flash
            c "You must stop, Balrung!  {font=fonts/ankecallig-fg.ttf}INCARCERO{/font}!"
            show cyril angry with magic_flash
            "I peeked around the corner to see chains snaked around the dragon, though it was only a moment later when Balrung lunged free of the chains."
            c "I didn’t want to have to do- STAY PUT, YOU DRAGON!"
            b "If you want me to stay put, you'll have to kill me. Are you {i}man{/i} enough to do that?!"
            show cyril concerned at basicfade
            c "Don’t-don’t test me.  You submit to my authority and to the authority of the council of mages or - or else."
            b "I didn't think so. You humans are so weak! Farewell!"
            play sound "sfx/crash.ogg" 
            "Balrung smashed a giant hole in the side of the dungeon and crouched, ready to spring out into the evening sky." with hpunch
            show cyril angry with magic_flash
            c "{font=fonts/ankecallig-fg.ttf}{size=+10}FULGURENTIA MAXIMA{/size}{/font}!" #with lightning?
            "Cyril’s wand dropped to the ground."
            show cyril surprised at basicfade
            "Balrung stopped mid-leap and crashed to the ground, dead. There was no time for last words or final taunts - it was over. Cyril just stood there, staring at the dragon's corpse."
            show cyril concerned eyes closed at basicfade
            c "{i}I-I... he was supposed to stop{/i}."
            p "That was...very competent of you, Cyril."
            show cyril concerned at basicfade
            c "He didn’t give me a choice.  "
            extend "I hope the council of mages understand."
            show cyril concerned at basicfade
            c "You will, tell them, won’t you?"
            p "Of course I will. After you help me."
            show cyril angry at basicfade
            c "Oh yes.  You need the scepter, and you have it.  Quite... marvelous."
            p "But...I can't use it! I just tried, and it did nothing. You must come with me!"
            show cyril concerned at basicfade
            c "I will Princess.  I will help you."
            show cyril concerned eyes closed at basicfade
            c "There is... nothing else for me here."

            call credits
            if (cyril_insanity >= INSANE):
                jump cyril_dark_epilogue
            else:
                jump cyril_scepter_epilogue

        "Use the scepter on yourself":
            "I turned the scepter toward myself, feeling the intense energy that came from it."
            show cyril surprised at basicfade
            c "Wh-wh-what are you doing Princess?"
            p "Stand back Moro-Cyril.  We had an agreement.  The scepter would be {b}mine{/b}."
            b "Outsmarted again, mage.  Oh, ho ho!"
            show cyril concerned eyes closed at basicfade
            c "Princess, please stop this! You don't know what it might do! You won't be able to control it!"
            p "I'll do whatever I have to! Hyaaah!"
            "I felt myself thrust backwards, and I hit the wall. Then the magic began to work."
            "My skin tingled and stretched, twisted and changed. I looked down at my hands and watched as they morphed into powerful claws. I tossed my head, and instead of hair, felt horns."
            "And, to either side, enormous leathery wings strained against the ceiling, yearning for the open air."
            b "Princess... you're... marvelous!"
            show cyril surprised at basicfade
            c "Chrysandra!  No!"
            show cyril angry at basicfade
            c "This cannot be.  We can fix you.  Give me that scepter!"
            p "No, no, no."
            show cyril concerned at basicfade
            c "Princess, it’s okay.  I have heard of this happening.  Well, I heard of it happening once.  We can fix this, I {b}can{/b}!  You must trust me."
            "My new voice sounded deep and strange. I growled, just for the fun of it, and my laugh was like rolling thunder."
            p "This is how I was meant to be! But I won't forget you, Cyril. In fact, I shall allow you to accompany me so that you might serve me further."
            show cyril concerned blush at basicfade
            c "And then I will fix you, right?"
            "I crushed one of the stones from the wall to powder in my claws, and swung my tail back and forth, knocking a door off its hinges. I could get used to this."
            p "Climb on, Cyril! And I will give my sister a coronation she'll never forget!"
            show cyril surprised at basicfade
            c "Ah, yes.  But Balrung- he will still be here.  And we need to find Niir.  I can’t have him causing trouble again."
            b "Leave Niir to me. And, Princess, if you ever tire of humans and their petty, insignificant squabbling... come and join us."
            play sound "sfx/crash.ogg" 
            "With one final nod to me, Balrung bashed a hole in the dungeon wall and leapt out through it."
            "Cyril gingerly stepped onto my hind leg, and then clambered up onto my back. His weight felt like that of a small child, barely even registering."
            show cyril concerned at basicfade
            c "There's nothing to hold on to! Shouldn't there be reins or something?!"
            p "Never!"
            play music happy_ending
            play sound "sfx/wings.ogg" loop
            "With a running start, I surged out of the castle walls and out into the glowing evening. Cyril shrieked and almost fell off, but I leveled out just in time."
            "Flying felt so natural, it was hard to believe I had only been capable of it for mere minutes."
            scene bg sunset with fade

            c "I don’t believe I’m doing this.  I don’t believe I’m doing this.  I’m not sure if we should be doing this, Princess."
            p "I wonder if I can breathe fire? ...Oh, look, I can! Did you see that, Cyril?!"
            c "Please don’t.  Don’t do that, Princess.  At least not without due warning."
            p "I'm warning you right now, Cyril, there will be a lot more fire and destruction before the night is over! Mwah ha ha ha ha!"
            stop sound fadeout 2.0
            call credits
            jump cyril_dragon_epilogue

    return

label balrung8:
    "That fool mage won't let Balrung go no matter what. I need a new plan..."
    "There are some good books on potions in the library. There must be something that can help!"
    scene bg library with fade
    "Good, it's empty. Now, where was that book...?"
    "Ah yes, {i}Draughts of Death, Destruction, and Devastation{/i}. Death is such an uninteresting solution, but if it's the one that works best..."
    play sound "sfx/flippage.ogg"
    "Hmmm, here's a Concotion of Confusion... but it takes griffon claws, and those aren't easy to find. And three-month dried kelp; I'm not waiting that long."
    "A Potion of Persuasion? That could work... it requires a dragon scale. Well, if we had any dragons in dragon form, that'd be no problem."
    "Transmogrification Tonic? If I could turn into a dragon... but then, I'd be stuck here as well. Unless I drank it after leaving... then I mightn't need help after all..."
    stop sound fadeout 2.0
    show balrung neutral at center with moveinleft
    play music balrung_theme
    show balrung determined at basicfade
    b "Chrysandra? There you are! I have another plan, but I'm not satisfied with its chances for success. Tell me you have something better."
    p "Depends. Do you have any dragon scales?"
    show balrung neutral at basicfade
    b "Perhaps; how many do you need?"
    p "Just one, and some other ingredients. I thought I saw berry grass on our walk the other day, and I know the kitchen has molasses, and I brought some nightshade."
    show balrung angry at basicfade
    b "So many dragons have come and gone, here, we should be able to find at least one dragon scale. Firgol left several months ago from the top tower, so let's try there."
    hide balrung with moveoutleft
    
    scene bg stairs day with fade
    show balrung neutral at center with moveinright
    p "Tell me about Firgol."
    show balrung determined at basicfade
    b "None too bright, but he was honest and sincere. That's what his Princess wanted, I suppose."
    p "She came here seeking a dragon?"
    show balrung neutral at basicfade
    b "Yes, she was ruling with a regency, and they threatened to take over if she did not produce any heirs. She decided the quickest way to get married was to seek a dragon here."
    p "Why did she choose Firgol?"
    show balrung smirk at basicfade
    b "Well...Niir wasn't interested, since she was a bit older and not particularly beautiful. I chatted with her several times, but she wanted someone guileless and pliable. Firgol was both."
       
    hide balrung with moveoutleft
    
    scene bg exterior day with fade
    show balrung neutral at center with moveinleft
    p "What color scales are we looking for?"
    show balrung angry at basicfade
    b "I'm afraid I don't know. I couldn't bear to watch {b}him{/b} return to dragon form while I was incapable of doing so."
    show balrung smile at basicfade
    b "But tell me...what potion are you planning on making, Chrysandra?"
    p "Persuasion. I wanted to make one to use on my father, but I had no dragon scales."
    show balrung smirk at basicfade
    b "Ah-hah! Here's one. Once I'm free, you can have as many scales as you like. Perhaps using a potion on your father would be a better way to regain your kingdom than burning it to the ground?"
    p "Ohhhh, I suppose. I had such lovely visions of flames and rubble...but it is expensive to rebuild a castle."
    show balrung neutral at basicfade
    b "Your pragmatism is delightful. I'm sure we can find something else to destroy together."
    p "Ha. Stop it, Balrung, now you're just teasing me."
    show balrung smile at basicfade
    b "Not at all. Perhaps we should destroy {b}this{/b} castle? It would look nice as a pile of smoldering debris, wouldn't it? "
    show balrung smile blush at come_closer, basicfade
    b "You and I, soaring above, circling, conflagrating..."
    p "I- I have to start brewing this potion. Find me the rest of these ingredients, and meet me in the kitchen."
    show balrung smirk at center, reset_zoom, basicfade
    b "Of course, Chrysandra."
    hide balrung with moveoutleft
    scene bg kitchen with fade
    play sound "sfx/boiling.ogg" loop
    "At least the scale only needs to boil in blood for an hour. But, it took more blood than I thought...I need to sit down."
    scene bg kitchen with vpunch
    "Oh. I'm already sitting down. On the floor."
    scene bg kitchen with fade
    stop sound fadeout 10.0
    show cyril hat neutral at quarterright with moveinleft
    play music cyril_theme
    show cyril hat surprised at basicfade
    c "Princess! You're bleeding!"
    show cyril hat concerned at basicfade
    c "Which dragon was it?! I'll make sure they can NEVER hurt anyone else again!"
    "I tried to stand up, but couldn't quite manage it."
    p "It was... it wasn't... Balrung...!"
    
    show balrung neutral at center with moveinleft
    show balrung determined at basicfade
    b "Princess? I have the- oh. {b}You're{/b} here."
    show cyril hat angry at basicfade
    c "It was YOU! YOU SHALL NOT HURT THE PRINCESS!!"
    play sound "sfx/electricity.ogg"
    show balrung angry at basicfade
    b "I did nothing of the sort. Stop this ridiculous posturing and help her!"
    show cyril hat concerned at basicfade
    c "You will regret calling me ridiculous!"
    show cyril hat angry at basicfade
    c "{font=fonts/ankecallig-fg.ttf}{size=+10}FULGURENTIA MAXIMA{/size}{/font}!" #TODO: lots of lightning/
    play sound "sfx/lightning.ogg"
    show cyril hat angry
    show balrung angry
    with magic_flash
    hide balrung with quickmoveoutleft
    b "AHHHHH!"
    play sound "sfx/electricity.ogg"
    p "Stop it, you stupid mage! It wasn't even him, it was me!"
    show cyril hat concerned at basicfade
    c "You're not making delirious, I mean, you're not making sense, Princess! No, no, I'm going to do what they should have done to this villain in the first place!"
    "He began muttering, trying to remember the words. I grabbed the bloody knife and managed to stand up."
    menu:
        "Attack Cyril":
            play sound "sfx/stab.ogg"
            $ cyril_dead = True
            show cyril hat surprised with blood
            "I brought the knife down and buried it into Cyril's back. He stopped chanting and fell forward, dead. The magical aura dissipated."
            hide cyril with moveoutbottom
            p "So this...is what it feels like. To have a plot work. To be victorious."
            p "...it's not as much fun as I thought."
            jump balrung_ending
            
        "Threaten to stab yourself":
            p "Stop it, Moronious, or I shall stab myself with this knife!"
            c "What?! Princess, no! What are you doing?!"
            p "You bumbling buffoon, I cut my own arm to make a potion! Balrung has been {b}helping{/b} me!"
            show cyril hat surprised at basicfade
            c "He...didn't hurt you?"
            p "No, idiot! The only one in this castle who has been hurting people is {b}you{/b}!"
            # TODO: ? if (cyril_affection >= MEDIUM_AFFECTION):
            show cyril hat concerned eyes closed at basicfade
            c "I...I'm not fit for this job. I never should have agreed to it..."
            "He dropped his hands, dejected, and turned to leave."
            c "You're free to leave, Balrung. You m-may not be perfect, but I am no butter. I mean, no better."
            hide cyril with moveoutleft
            jump balrung_ending
        "Shield Balrung" if (balrung_affection >= HIGH_AFFECTION):
            "I ran to stand in front of Balrung. I didn't think that mage would be foolish enough to attack me."
            p "Stop, stop, stop! You bumbling buffoon, I cut my own arm to make a potion! Balrung has been {b}helping{/b} me!"
            show cyril hat surprised at basicfade
            c "He...didn't hurt you?"
            p "No, idiot! The only one in this castle who has been hurting people is {b}you{/b}!"
            show cyril hat concerned eyes closed at basicfade
            c "I...I'm not fit for this job. I never should have agreed to it..."
            "He dropped his hands, dejected, and turned to leave."
            c "You're free to leave, Balrung. You m-may not be perfect, but I am no butter. I mean, no better."
            hide cyril with moveoutleft
            jump balrung_ending
        "Wait it out.":
            p "Hmmm, I must admit, I'm curious who would win if you two begin fighting. What better way to prove who is stronger and more fit to aid me?"
            "They looked at each other, surprised. Balrung stood up slowly, shaking, and shook his head."
            show balrung neutral at center with moveinbottom
            show balrung determined at basicfade
            b "..."
            show cyril hat surprised at basicfade
            c "..."
            p "Well? What are you waiting for? Commence battle!"
            show balrung smirk at basicfade
            b "Cyril, you've seen the Princess. Who do you really think is a greater threat to the safety of this kingdom? Yes, I know she's a \"princess\", and quite an attractive one at that; but she's selfish, lustful for power, and will stop at nothing."
            b "She had even agreed to poison you in your sleep if it was necessary for our plan. Would you trust the future of this kingdom to someone like that?"
            p "Poisoning the mage was your idea!"
            show balrung angry at basicfade
            b "You don't care whose life you have to destroy to get what you want. You don't care about the desires and goals of those around you. I know you, Princess, I've seen into your heart and it's dark with malice."
            c "You'd know all about malice, wouldn't you?!"
            show balrung neutral at basicfade
            b "Yes. I would. I used to be the same. But, Cyril, after all this time, do you know what I really want to do?"
            show cyril hat angry at basicfade
            c "Yes! You want revenge, and power!"
            show balrung determined at basicfade
            b "No. I only want to be able to fly over the mountains and be left alone."
            show cyril hat surprised at basicfade
            p "He's lying! He was going to help me destroy [k_name]!"
            show balrung smirk at basicfade
            b "Cyril, I hope you'll do the right thing and help the Princess see the error of her ways. You mages have helped me to, even though I disagree with the way it was done."
            p "Balrung! I will hunt you down! I will find you and DESTROY YOU!!!"
            # TODO: if her cyril_affection is high enough, send to cyril_attack instead?
            show balrung smile at basicfade
            b "Farewell, Princess. I hope you find better things to consume your life than revenge."
            hide balrung with moveoutleft
            p "Moronious! Stop him! Why are you just standing there?! KILL HIM!"
            # TODO: Feel free to rewrite Cyril's lines better or end this differently
            show cyril hat concerned at basicfade
            c "N-no, Princess, I don't th-think I will."
            p "Useless! Betrayed at every turn! When I am Queen, you will regret this!"
            show cyril hat concerned eyes closed blush at basicfade
            c "You sh-shouldn't be Queen the way you are. I'm terribly sorry, my dear Princess [p_name], but..."
            p "Moronious, you fool, point that wand at the dragon! Not at me!"
            show cyril hat concerned blush at basicfade
            c "CARCERATUS!!"
            p "What have you done to me?!"
            show cyril hat neutral at basicfade
            c "Stay! You will stay here, until you learn to be good! I know, somewhere inside of you, there's goodness and love...please, find it quickly, Princess."
            p "You thought guarding dragons was bad? I {b}will{/b} make your life a hell of mental pain, psychological torture, and physical anguish until you LET. ME. GO!"
            show cyril hat concerned eyes closed at basicfade
            c "I'm so sorry! It's for your own good...."

            call credits
            jump imprisoned_epilogue