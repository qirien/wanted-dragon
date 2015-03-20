label day8:
    scene bg bedroom dusk with fade
    "Time is running out; Magnolia's coronation will take place tomorrow, unless I can find a way to stop it!"
    "Careful plots would take too much time; I needed to act now."
    if (route == "Niir"):
        jump niir8
    elif (route == "Cyril"):
        jump cyril8
    elif (route == "Balrung"):
        jump balrung8
        
    return

#TODO: she carries him across dragon barrier? 
label niir8:

label cyril8:
    if (cyril_insanity >= INSANE):
        jump mage_insane
    p "Time is running out, Moro-, er, Cyril. Unless you have something for me today, I will be forced to pursue other...options."
    c "I know, I know.  Time is of the essence.  I have been staying awake at night thinking of what to do about it but to no avail."
    p "Hmph. Then I will find something on my own. How unfortunate that your power was not enough to bring me the one thing I truly need."
    c "W-wait! One more time!"

    c "There it is again! The scepter's magical echo! Before it fades, I must..."
    c "Resonantia Concretus!"
    p "I can see wisps of something in the air. What did you do, mage?"
    c "That should solidify the resonance for a while. It's coming from...the dungeon. Princess, someone is using the scepter right now!"
    p "Then we must follow the resonance and take it! What are you waiting for?!"
    c "R-right!"

    scene bg dungeon night with fade
    show cyril hat neutral at midleft
    with moveinleft
    "When we got to the dungeon, Balrung and Niir were nowhere to be seen."
    c hat concerned eyes closed "Ahhhh!"
    p "Cyril! Don't just stand there; we need to get the scepter!"
    c hat angry "The dragons... the curse is broken! That is...not...RIGHT!"
    #TODO show dragon shadow/head at right with vpunch
    "The ground trembled, and a giant shadow emerged from the corner of the room. No, not a shadow-- a dragon. {b}Two{/b} dragons."
    b "It {b}is{/b} right! Your prejudice and arrogance have gone far beyond justice and on to revenge for crimes not yet committed!"
    n "Nicccce work, old tortoissse. But I'm leaving."
    c hat concerned eyes closed "Niir! You must stay! You WILL-- oof!" 
    hide cyril with quickmoveoutleft
    "Balrung's tail came out of nowhere and knocked Cyril to the ground."
    b "I'll supervise Niir. That's what you mages should have done in the first place; let dragons discipline dragons."
    show cyril concerned at midleft with moveinleft   #he lost his hat
    c "That wouldn't work! Nobody can trust you!"
    c concerned eyes closed "..."
    c angry "And wait Balrung, WHERE IS THAT SCEPTER?!" 
    "As they talked, I scanned the room. Balrung had used it earlier to break the spell, but I didn't see it in his hands- er, talons. But traces of Cyril's spell still lingered and led me to it."
    p "You mean...this scepter? Really, Balrung, under the bed is such an obvious hiding place." 
    c surprised "Of course, I should have seen it.  I am sorry, my highness."
    b "I put it there for you to find, Princess. I've already used the scepter for what I needed. And now I've passed it on to you. I know you'll put it to much better use than this fool."
    c concerned blush eyes closed "No, don't! It's too powerful; you can't control it without magical training! It could kill you, {i}kill{/i} you, Princess!"
    menu:
        "Give the scepter to Cyril" if (cyril_affection >= HIGH_AFFECTION):
            p "Cyril, I'm trusting you with this. Don't fail me!"
            c smile blush "I won’t, Princess."
            b "You're making a mistake!  I WILL not be imprisoned AGAIN!"
            c angry "You were the one making the mistake and now you will reap the consequences of such a mistake."
            play sound "sfx/electricity.ogg"
            "Cyril started to chant, preparing some kind of powerful magic, I hoped."
            "Balrung breathed a maelstrom of fire in our direction, but Cyril swiped it away with a gesture. The old dragon pounced forwards as Cyril brandished the scepter at him and shouted another spell."
            c angry "{font=fonts/ankecallig-fg.ttf}{size=+10}DRACONIS PETROMUNDI{/size}{/font}!"
            show cyril angry with magic_flash
            "There was a puff of smoke that sped towards Balrung like an arrow, and when it cleared... he had turned to stone."
            p "You...stopped him. Cyril, that was...power!"
            c smile blush "Ah, yes.  I suppose it was, mostly.  This scepter is very dangerous buisness.  "
            extend "I think I’ll hold on to it."
            p "And I'll hold on to {b}you{/b}."
            show cyril concerned blush at come_closer
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
            c surprised "..."
            "...Nothing happened."
            b "Ho, ho ho ho. I spent years practicing with that artifact, using it carefully for minutes at a time so Merlonious wouldn't detect anything! You think to use it on {b}me{/b} after holding it for mere moments?"
            "Balrung reared back, jaws gaping wide open. To breathe fire? To swallow us whole?"
            c concerned blush eyes closed "Princess!  Hide!  Don’t let that beast have the scepter!  I beseech you!"
            "This was not a battle in which I wanted to risk my royal person; that's what minions are for. I dived out into the hallway, leaving Cyril and Balrung to fight it out on their own."
            "Balrung swiped at Cyril with his claws, but Cyril managed to roll out of the way."
            c concerned "She won’t give you the scepter, so we may as well stop this Balrung.  You must surrender yourself to me, and I will have the council decide what to do with you."
            b "I know what your Council would do with me. The same thing they've done for forty years!"
            b "I'd rather die a free dragon than live an enslaved half-existence as a human! Rrrraaaagh!"
            "The room filled with a raging inferno of fire breath. A shimmering magic shield surrounded Cyril, and I stepped back to avoid getting my hair singed."
            c angry "You must stop, Balrung!  {font=fonts/ankecallig-fg.ttf}INCARCERO{/font}!"
            show cyril angry with magic_flash
            "I peeked around the corner to see chains snaked around the dragon, though it was only a moment later when Balrung lunged free of the chains."
            c angry "I didn’t want to have to do- STAY PUT, YOU DRAGON!"
            b "If you want me to stay put, you'll have to kill me. Are you {i}man{/i} enough to do that?!"
            c angry "Don’t-don’t test me.  You submit to my authority and to the authority of the council of mages or - or else."
            b "I didn't think so. You humans are so weak! Farewell!"
            "Balrung smashed a giant hole in the side of the dungeon and crouched, ready to spring out into the evening sky." with hpunch
            c angry "{font=fonts/ankecallig-fg.ttf}{size=+10}FULGURENTIA MAXIMA{/size}{/font}!" #with lightning?
            "Cyril’s wand dropped to the ground."
            "Balrung stopped mid-leap and crashed to the ground, dead. There was no time for last words or final taunts - it was over. Cyril just stood there, staring at the dragon's corpse."
            c concerned eyes closed "{i}I-I... he was supposed to stop{/i}."
            p "That was...very competent of you, Cyril."
            c concerned "He didn’t give me a choice.  "
            extend "I hope the council of mages understand."
            c concerned "You will, tell them, won’t you?"
            p "Of course I will. After you help me."
            c angry "Oh yes.  You need the scepter, and you have it.  Quite... marvelous."
            p "But...I can't use it! I just tried, and it did nothing. You must come with me!"
            c concerned "I will Princess.  I will help you."
            c concerned eyes closed "There is... nothing else for me here."

            call credits
            jump cyril_crazy_epilogue

        "Use the scepter on yourself":
            "I turned the scepter toward myself, feeling the intense energy that came from it."
            c surprised "Wh-wh-what are you doing Princess?"
            p "Stand back Moro-Cyril.  We had an agreement.  The scepter would be {b}mine{/b}."
            b "Outsmarted again, mage.  Oh, ho ho!"
            c concerned eyes closed "Princess, please stop this! You don't know what it might do! You won't be able to control it!"
            p "I'll do whatever I have to! Hyaaah!"
            "I felt myself thrust backwards, and I hit the wall. Then the magic began to work. My skin tingled and stretched, twisted and changed. I looked down at my hands and watched as they morphed into powerful claws. I tossed my head, and instead of hair, felt horns. And, to either side, enormous leathery wings strained against the ceiling, yearning for the open air."
            b "Princess... you're... marvelous!"
            c surprised "Chrysandra!  No!"
            c angry "This cannot be.  We can fix you.  Give me that scepter!"
            p "No, no, no."
            c concerned "Princess, it’s okay.  I have heard of this happening.  Well, I heard of it happening once.  We can fix this, I {b}can{/b}!  You must trust me."
            "My new voice sounded deep and strange. I growled, just for the fun of it, and my laugh was like rolling thunder."
            p "This is how I was meant to be! But I won't forget you, Cyril. In fact, I shall allow you to accompany me so that you might serve me further."
            c concerned blush "And then I will fix you, right?"
            "I crushed one of the stones from the wall to powder in my claws, and swung my tail back and forth, knocking a door off its hinges. I could get used to this."
            p "Climb on, Cyril! And I will give my sister a coronation she'll never forget!"
            c surprised "Ah, yes.  But Balrung- he will still be here.  And we need to find Niir.  I can’t have him causing trouble again."
            b "Leave Niir to me. And, Princess, if you ever tire of humans and their petty, insignificant squabbling... come and join us."
            "With one final nod to me, Balrung bashed a hole in the dungeon wall and leapt out through it. Cyril gingerly stepped onto my hind leg, and then clambered up onto my back. His weight felt like that of a small child, barely even registering."
            c concerned "There's nothing to hold on to! Shouldn't there be reins or something?!"
            p "Never!"
            "With a running start, I surged out of the castle walls and out into the glowing evening. Cyril shrieked and almost fell off, but I leveled out just in time. Flying felt so natural, it was hard to believe I had only been capable of it for mere minutes."
            scene bg sunset with fade
            c concerned eyes closed "I don’t believe I’m doing this.  I don’t believe I’m doing this.  I’m not sure if we should be doing this, Princess."
            p "I wonder if I can breathe fire? ...Oh, look, I can! Did you see that, Cyril?!"
            c concerned blush "Please don’t.  Don’t do that, Princess.  At least not without due warning."
            p "I'm warning you right now, Cyril, there will be a lot more fire and destruction before the night is over! Mwah ha ha ha ha!"

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
    b determined "Chrysandra? There you are! I have another plan, but I'm not satisfied with its chances for success. Tell me you have something better."
    p "Depends. Do you have any dragon scales?"
    b neutral "Perhaps; how many do you need?"
    p "Just one, and some other ingredients. I thought I saw berry grass on our walk the other day, and I know the kitchen has molasses, and I brought some nightshade."
    b angry "So many dragons have come and gone, here, we should be able to find at least one dragon scale. Firgol left several months ago from the top tower, so let's try there."
    hide balrung with moveoutleft
    
    scene bg stairs day with fade
    show balrung neutral at center with moveinright
    p "Tell me about Firgol."
    b determined "None too bright, but he was honest and sincere. That's what his Princess wanted, I suppose."
    p "She came here seeking a dragon?"
    b neutral "Yes, she was ruling with a regency, and they threatened to take over if she did not produce any heirs. She decided the quickest way to get married was to seek a dragon here."
    p "Why did she choose Firgol?"
    b smirk "Well...Niir wasn't interested, since she was a bit older and not particularly beautiful. I chatted with her several times, but she wanted someone guileless and pliable. Firgol was both."
       
    hide balrung with moveoutleft
    
    scene bg exterior day with fade
    show balrung neutral at center with moveinleft
    p "What color scales are we looking for?"
    b angry "I'm afraid I don't know. I couldn't bear to watch {b}him{/b} return to dragon form while I was incapable of doing so."
    b smile "But tell me...what potion are you planning on making, Chrysandra?"
    p "Persuasion. I wanted to make one to use on my father, but I had no dragon scales."
    b smirk "Ah-hah! Here's one. Once I'm free, you can have as many scales as you like. Perhaps using a potion on your father would be a better way to regain your kingdom than burning it to the ground?"
    p "Ohhhh, I suppose. I had such lovely visions of flames and rubble...but it is expensive to rebuild a castle."
    b neutral "Your pragmatism is delightful. I'm sure we can find something else to destroy together."
    p "Ha. Stop it, Balrung, now you're just teasing me."
    b smile "Not at all. Perhaps we should destroy {b}this{/b} castle? It would look nice as a pile of smoldering debris, wouldn't it? "
    show balrung smile blush at come_closer with dissolve
    b "You and I, soaring above, circling, conflagrating..."
    p "I- I have to start brewing this potion. Find me the rest of these ingredients, and meet me in the kitchen."
    show balrung smirk at reset_zoom with dissolve
    b smirk "Of course, Chrysandra."
    hide balrung with moveoutleft
    scene bg kitchen with fade
    play sound "sfx/boiling.ogg" loop
    "At least the scale only needs to boil in blood for an hour. But, it took more blood than I thought...I need to sit down."
    scene bg kitchen with vpunch
    "Oh. I'm already sitting down. On the floor."
    scene bg kitchen with fade
    stop sound fadeout 10.0
    show cyril hat neutral at quarterright with moveinleft
    c hat surprised "Princess! You're bleeding!"
    c hat concerned "Which dragon was it?! I'll make sure they can NEVER hurt anyone else again!"
    "I tried to stand up, but couldn't quite manage it."
    p "It was... it wasn't... Balrung...!"
    
    show balrung neutral at center with moveinleft
    b determined "Princess? I have the- oh. {b}You're{/b} here."
    c hat angry "It was YOU! YOU SHALL NOT HURT THE PRINCESS!!"
    play sound "sfx/electricity.ogg"
    b angry "I did nothing of the sort. Stop this ridiculous posturing and help her!"
    c hat concerned "You will regret calling me ridiculous!"
    c hat angry "{font=fonts/ankecallig-fg.ttf}{size=+10}FULGURENTIA MAXIMA{/size}{/font}!" #TODO: lots of lightning/
    play sound "sfx/lightning.ogg"
    show cyril hat angry with magic_flash
    hide balrung with quickmoveoutleft
    b angry "AHHHHH!"
    play sound "sfx/electricity.ogg"
    p "Stop it, you stupid mage! It wasn't even him, it was me!"
    c hat concerned "You're not making delirious, I mean, you're not making sense, Princess! No, no, I'm going to do what they should have done to this villain in the first place!"
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
            c hat surprised "He...didn't hurt you?"
            p "No, idiot! The only one in this castle who has been hurting people is {b}you{/b}!"
            # TODO: ? if (cyril_affection >= MEDIUM_AFFECTION):
            c hat concerned eyes closed "I...I'm not fit for this job. I never should have agreed to it..."
            "He dropped his hands, dejected, and turned to leave."
            c "You're free to leave, Balrung. You m-may not be perfect, but I am no butter. I mean, no better."
            hide cyril with moveoutleft
            jump balrung_ending
        "Shield Balrung" if (balrung_affection >= HIGH_AFFECTION):
            "I ran to stand in front of Balrung. I didn't think that mage would be foolish enough to attack me."
            p "Stop, stop, stop! You bumbling buffoon, I cut my own arm to make a potion! Balrung has been {b}helping{/b} me!"
            c hat surprised "He...didn't hurt you?"
            p "No, idiot! The only one in this castle who has been hurting people is {b}you{/b}!"
            c hat concerned eyes closed "I...I'm not fit for this job. I never should have agreed to it..."
            "He dropped his hands, dejected, and turned to leave."
            c "You're free to leave, Balrung. You m-may not be perfect, but I am no butter. I mean, no better."
            hide cyril with moveoutleft
            jump balrung_ending
        "Wait it out.":
            p "Hmmm, I must admit, I'm curious who would win if you two begin fighting. What better way to prove who is stronger and more fit to aid me?"
            "They looked at each other, surprised. Balrung stood up slowly, shaking, and shook his head."
            show balrung neutral at center with moveinbottom
            b determined "..."
            c hat surprised "..."
            p "Well? What are you waiting for? Commence battle!"
            b smirk "Cyril, you've seen the Princess. Who do you really think is a greater threat to the safety of this kingdom? Yes, I know she's a \"princess\", and quite an attractive one at that; but she's selfish, lustful for power, and will stop at nothing."
            b "She had even agreed to poison you in your sleep if it was necessary for our plan. Would you trust the future of this kingdom to someone like that?"
            p "Poisoning the mage was your idea!"
            b angry "You don't care whose life you have to destroy to get what you want. You don't care about the desires and goals of those around you. I know you, Princess, I've seen into your heart and it's dark with malice."
            c "You'd know all about malice, wouldn't you?!"
            b neutral "Yes. I would. I used to be the same. But, Cyril, after all this time, do you know what I really want to do?"
            c hat angry "Yes! You want revenge, and power!"
            b determined "No. I only want to be able to fly over the mountains and be left alone."
            show cyril hat surprised with dissolve
            p "He's lying! He was going to help me destroy [k_name]!"
            b smirk "Cyril, I hope you'll do the right thing and help the Princess see the error of her ways. You mages have helped me to, even though I disagree with the way it was done."
            p "Balrung! I will hunt you down! I will find you and DESTROY YOU!!!"
            # TODO: if her cyril_affection is high enough, send to cyril_attack instead?
            b smile "Farewell, Princess. I hope you find better things to consume your life than revenge."
            hide balrung with moveoutleft
            p "Moronious! Stop him! Why are you just standing there?! KILL HIM!"
            # TODO: Feel free to rewrite Cyril's lines better or end this differently
            c hat concerned "N-no, Princess, I don't th-think I will."
            p "Useless! Betrayed at every turn! When I am Queen, you will regret this!"
            c hat concerned eyes closed blush "You sh-shouldn't be Queen the way you are. I'm terribly sorry, my dear Princess [p_name], but..."
            p "Moronious, you fool, point that wand at the dragon! Not at me!"
            c hat concerned blush "Carceratus!!"
            p "What have you done to me?!"
            c hat neutral "Stay! You will stay here, until you learn to be good! I know, somewhere inside of you, there's goodness and love...please, find it quickly, Princess."
            p "You thought guarding dragons was bad? I {b}will{/b} make your life a hell of mental pain, psychological torture, and physical anguish until you LET. ME. GO!"
            c hat concerned eyes closed "I'm so sorry! It's for your own good...."
            # TODO: jump to a common ending where she ends up imprisoned?                    
     
            call credits
            jump imprisoned_epilogue