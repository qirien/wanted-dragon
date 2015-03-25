# DAY 6
# She does something nice for whoever's route she's on
# Of course, it's only to ensure their loyalty...

label day6:
    # She goes around eavesdropping to find out how well her plans have been working.
    scene bg bedroom dusk with fade
    play music evil_theme
    p "Ugggh, that moldy smell again. I must {b}still{/b} be in [castle_name]."
    p "But I believe I'm finally making some progress. Although... they could be deceiving me."
    p "Unfortunately, all my spies are back at the palace. I shall just have to do a little information gathering on my own!"
    
    if (route == "Niir"):
        "I snuck down to the dungeon to spy on the dragons."
        scene bg dungeon with fade
        show niir neutral at midright, basicfade
        show balrung neutral at midleft, basicfade
        show balrung angry at basicfade
        b "I do hope you haven't fallen in love with the tempestuous temptress that has entered our realm."
        n "Now why would you ssssssay that?"
        show balrung determined at basicfade
        b "I have seen it happen many times before. Many dragons and princesses have come and gone since I arrived."
        show balrung smirk at basicfade
        b "I can discern the signs."
        n "Love is not ssssomething that I am acquainted with, old dragon."
        n "Ssstop your posssstulating."
        show balrung determined at basicfade
        b "I'm no more happy about this than you are, Niir.  You provide what little distraction I have in this dreary place."
        show balrung smirk at basicfade
        b "If I could keep you here, I would."
        n "Your fearssss are ridiculousssss."
        n "I am sssstaying here, old dragon."
        show balrung angry at basicfade
        b "Stubborn fool!  What life is there for you here?!"
        show balrung determined at basicfade
        b "What other princesses are there?"
        "Could Balrung be right?  Could Niir actually be... {i}in love{/i}?"
        "The thought makes my stomach roil."
        "Though I have to admit, I do feel some... animal magnetism towards Niir."
        "Even if it is only physical."
        n "Sssshut up.  I am done conversssssing."
        show balrung neutral at basicfade
        b "I'd tell you to follow your heart. But that would require you to possess one in the first place."
        "This is what I wanted, wasn't it?"
        "A dragon at my disposal.  Willing to leave, all for the delusion of love."
        "But somehow, it doesn't feel as good as I thought it would."
        "Well, as long as Niir and I both get what we want, what's the harm? In fact... I have the perfect treat to reward Niir for his progress so far."
        jump niir6
    elif (route == "Cyril"):
        "I snuck over to the library to spy on Moronious."
        scene bg library with fade
        show cyril hat neutral at center, basicfade
        c "I just can’t do it."
        show cyril hat neutral at midleft with move
        c "It wouldn’t be right."
        show cyril hat neutral at midright with move
        c "I’d dedicated my life to this post, so I couldn’t just... give it up.  Could I?"
        "Give up his post? That would ruin everything I’ve been working for! No one else would be so eager to please and gullible."
        show cyril hat neutral at center with move
        c "Preposterous."
        c "No.  I could not.  Dyconis left me in charge and surely the dragons still need a guard."
        c "I just... oh, Master.  How I wish you were still around to sort out all this mess."
        c "It would be quite the opportunity to study again under the tutelage of Master Grivvorn.  But- I am still bound to my duty."
        c "To Dyconis."
        c "I’m not even sure why I do this anymore to be honest."
        c "But no.  Duty comes first."
        c "It’s rather foolish that I’d even be considering it."
        c "Isn’t it?"
        c "If only the walls could talk, Cyril.  What would they say?"
        c "Hmm, perhaps that is musing for another day."
        "Is it possible he’s that credulous? It’s worth a try, I suppose."
        menu:
            "Make the walls speak!":
                $ cyril_insanity += 1
                p "{i}Stayyyyyyyy.  Staaaaaaay, Cyril.{/i}"
                c "What was that?  "
                extend "Who’s there?"
                p "{i}staaaaayyyy.....{/i}"
                c "..."
                c "Could it be?  Could the walls actually have been listening to entire time?"
                c "I know your tricks, wall!  You just want to keep me here for your own company!"
                c "Well, it is not my doing if you are lonely.  There will be someone else to come and occupy you, surely.  But I must follow my heart."
                c "If only I knew what my heart was saying."

            "Keep quiet.":
                    "He’s not {b}that{/b} gullible."

        c "Perhaps the Princess could help me.  I have grown rather fond of her in this short stay.  But she does not know the council."
        c "No.  This is my decision.  And no walls, nor princesses can make it for me."

        c "Perhaps, I just need to run a warm bath and think about it for a while."
        c "Yes, that’ll do the trick."
        hide cyril at center with moveoutleft

        "While he’s occupied, I’ll just slip out and see that letter he was reading..."

        m_write "To Cyril Merlonious of the order of Dyconis:"
        m_write "We are pleased to inform you that an opening has arisen at the Academy in the House of Master Grivvorn, Third Star."
        m_write "Although your previous application was rejected, due to your recent service and experience, we would like to welcome you to the Academy as a second-tier student."
        nvl clear
        m_write "We await your speedy reply,"
        m_write "Sincerely,"
        m_write "Jillian Teslin"
        m_write "Undersecretary to Master Grivvorn, Third Star"
        m_write "Academy of Master Enchanters"
        nvl clear

        "Well, he’d be a fool not to accept and learn more powerful magic... but, then, he {b}is{/b} quite a fool, so anything’s possible."
        "I’ll just have to make sure he has plenty of reasons to stay here."
        scene black with fade
        jump cyril6
        
    elif (route == "Balrung"):
        "I snuck down to the dungeons to spy on the dragons."
        scene bg dungeon
        show niir neutral at midright
        show balrung neutral at midleft
        with fade
        show balrung smile blush at basicfade
        b "That Princess is really quite...something."
        show balrung smirk at basicfade
        b "Do you know, Niir, she beat me at Queens and Pawns yesterday? Nobody has done that since..."
        n "Ssssince Myriah?"
        show balrung neutral at basicfade
        b "Yes...she accomplished it mostly by distracting me with questions, but even so... Clever, for a human!"
        n "Sssso what?"
        show balrung smirk at basicfade
        b "Well, I don't wish to get your hopes up in vain, but it seems my long imprisonment may soon be over."
        n "How niccce for {b}you{/b}."
        show balrung determined at basicfade
        b "If we can count on your aid as well, then perhaps it's time to end this preposterous tradition of imprisoning ambitious dragons."
        n "I'm lissstening."
        show balrung neutral at basicfade
        b "I need you to go to Merlonious later today. Play one of your tricks on him or whatever it is you normally do. And then mention that the Princess and I are down here alone."
        n "But then he'll come and interrrupt you."
        show balrung smirk at basicfade
        b "Yes, that's the idea."
        n "How does thissss help me?"
        show balrung determined at basicfade
        b "When I'm a free dragon, I'll come back for you."
        n "That'sss what Firgol said, and he hasn't even come to visssit since marrying Princessss Dianthus."
        show balrung neutral at basicfade
        b "And you were a fool to believe him. But you know you can trust me, Niir. I've been like a father to you."
        n "The fatherrr I never wanted."
        show balrung smirk at basicfade
        b "Exactly. I look after you even though you show no gratitude or respect and give me nothing in return."
        n "...I supposssse I could do this for you."
        show balrung smile at basicfade
        b "Thank you, Niir. I always knew Merlonious was wrong about you."
        n "I'm not doing it to be niccce! I'm doing it becausssse that mage will hate it."
        hide niir at midright with moveoutleft
        "I pressed myself to the wall as Niir left going the other direction."
        "After a few moments of quiet, I entered the dungeon."
        jump balrung6
    return
        
# She does something nice for Balrung.
label balrung6:
    $ balrung_affection += 1
    scene bg dungeon with fade
    show balrung neutral at center, basicfade
    play music balrung_theme
    show balrung smirk at basicfade
    b "My dear lady..."
    "He carefully took my hand and brought it to his lips, watching my reaction with the barest hint of smugness."
    "I smirked in return. Playing at love was more fun than I had imagined. No wonder ordinary people spend so much time on it."
    p "You may call me Chrysandra."
    show balrung neutral at basicfade
    b "Chrysandra...golden flower? Fitting... lovely as a blossom, tenacious as metal, yet malleable enough to thrive in any situation."
    p "That's what my father says. Though if I was really so precious to him, he'd have made me Queen."
    p "Anyway, I brought you something."
    show balrung smirk at basicfade
    b "Princess, the brilliance of your presence is gift enough to soften this stone heart of mine. What more could I ask?"
    p "How about a Hibernation Libation?"
    "I handed him a flask containing the gloopy, dark green potion I had made. It was one of the few whose ingredients were commonplace enough to be found in and around the Castle [castle_name]."
    show balrung smile blush at basicfade
    b "I...I'm touched. How did you know I had insomnia?"
    p "Oh! I assumed you would use it on Niir when you wanted some peace and quiet. Or on that fool mage. I know you're not foolish enough to use it on me."
    show balrung neutral at basicfade
    b "It has many uses, I see.  How many doses are in here?"
    p "That's enough to make a human sleep for two days. I'm not sure how it would affect a dragon."
    show balrung smirk at basicfade
    b "Well...thank you. I'm afraid I don't have anything for you."
    p "You will, I'm sure. For now, let us play another game together. I expect you'll have arranged for Moronious to drop by later, so he can witness our 'true love'?"
    show balrung smile at basicfade
    b "Yes, indeed... how did you know?"
    p "I have resources of my own."
    show balrung smile eyes closed at basicfade
    b "Splendid. Why don't you go first this time?"
    p "Yes, I will...there."
    show balrung smirk at basicfade
    b "That's an interesting opening move."
    p "I know All the Queen's Men is usually derided as transparent and inefficient, but it does have its uses."
    show balrung neutral at basicfade
    b "It is one way to control the board early."
    p "It sets up certain...expectations."
    show balrung determined at basicfade
    b "And illusions."
    p "Illusions? Why, what do you think I'm up to?"
    show balrung smirk at basicfade
    b "It's obvious. But I don't mind playing along with you."
    p "Well, of course the first plot is obvious. But that's only to distract you from uncovering the second, third, and fourth plots."
    show balrung smile at basicfade
    b "How amusing it is to watch people who think they are cleverly manipulating you, when in reality you have already predicted their every move."
    p "Ha! Did you predict this move?!"
    show balrung smile eyes closed at basicfade
    b "Yes, that's why I had this setup here waiting for you."
    p "No! Ohhh, you! You're distracting me with all your talk of plots and illusions!"
    show balrung smirk at basicfade
    b "A valiant effort, but you should know that I won't be tricked by the Distressed Princess Bluff."
    p "And I won't be misled by your Brooding Old Man Feint!"
    show balrung smile at basicfade
    b "You don't have to fall for it in order for it to be effective. There goes your last Queen."
    p "Ohhhh... I suppose you win, this time."
    show cyril hat neutral at left with moveinleft
    c "Princess?"
    p "Moronious! How long have you been lurking over there?"
    show cyril hat neutral at midleft
    show balrung smile at midright
    with move
    c "I ju-just came to check on you, make sure you were safe..."
    p "Oh yes, Balrung is quite the gentleman. I'm not sure why you're so worried about him; the most dangerous thing he's done is arouse my temper by beating me at Queens and Pawns."
    c "You two do seem to- to get along."
    c "But it's not enough! A person, no, a {b}dragon{/b}, cannot change so easily!"
    show balrung determined at basicfade
    b "Do you think allowing myself to love is {b}easy{/b}? It is not! I learned from Myriah the price of loving a human!"
    c "And...do you, do you feel the same way, Princess?"
    p "Balrung is charming and useful, so of course I love him."
    c "...Y-you don't even know! You two can't fathom what true l-love is!"
    hide cyril at midleft with moveoutleft
    show balrung determined at center with move
    
    show balrung angry at basicfade
    b "I'm afraid it may not be possible to convince him, Chrysandra."
    p "Don't give up, yet. Perhaps we just need to give him some time..."
    show balrung neutral at basicfade
    b "Perhaps..."
    return
    
label niir6:
    scene bg library with fade
    show cyril hat neutral at center, basicfade
    play music cyril_theme
    
    p "Moronious, are you competent enough to pull a rabbit out of your hat?"
    c "Interesting request.  Hmmm, parlor magic.  I do remember some of that from my earlier days... What was it again?  Explodus Rabititious?  No.  That can’t be right..."
    p "..."
    c "Let me see.  {font=fonts/ankecallig-fg.ttf}Accerso Leoparda{/font}!  "
    show cyril hat angry with magic_flash
    extend "Oh dear."
    p "I did not ask for a large cat."
    c "That is not, not, not what I was trying to do. {font=fonts/ankecallig-fg.ttf}Amitto{/font}!"
    c "Whew, now that we both escaped with our eyebrows intact, let’s try again."
    c "{font=fonts/ankecallig-fg.ttf}Accerso Leporidae{/font}!" #TODO: can we show a bunny?!
    show cyril hat angry with magic_flash
    p "I only need ONE rabbit, not a hundred of them!"
    c "Ah, yes.  I knew that.  I’ll just rectify that."
    c "Stop that rabbit from escaping!  We need them all in this room!"
    show cyril hat neutral at left with move
    p "That’s your job, fool. Though, I am rather enjoying watching you run around and gather them up."
    show cyril hat neutral at right with move
    c "{font=fonts/ankecallig-fg.ttf}Amitto! Amitto! Reddo amitto{/font}!"
    show cyril hat neutral at midright with move
    c "Stay put for just one moment.   "
    extend "Ahh... that should be the last of them."
    show cyril hat concerned at center with move
    c "One last time.  I’ve got it this time, Princess, don’t you worry."
    c "{font=fonts/ankecallig-fg.ttf}Accerso Leporida{/font}!"
    show cyril hat angry with magic_flash
    p "Thank you. Come with me, little bunny, I want you to meet my friend."
    c "Meet your...?  Not one of the dragons!"
    c "I just conjured that bunny!   "
    extend "I’d grown rather fond of him.  Princess?  Princess?"

    scene bg dungeon with fade
    show niir neutral at center, basicfade
    play music niir_theme
    n "Come for a little game of hide-and-sssseek, Princessss?"
    p "Yes, actually, that’s exactly what I’ve come for."
    n "Rrrreally? You rrread my mind."
    p "You may play hide-and-seek with this bunny. Run and hide, bunny! Niir wants to find you and EAT YOU UP!!! Don’t you, Niir?"
    n "I’m almosssst disssssappointed.  But I do like the subsssstitute."
    n "Where did you find thissss... creature?"
    menu:
        "It doesn't matter where I found it.":
            n "It only matterssss if you can get more."
            p "I can get as many as is needed."
        "The mage has his uses after all.":
            $ niir_affection += 1
            n "Ah, perhapsss he resssspondsss better to your requesssts than to mine."
            n "Did you... have to sssacrifice much for it?"
            p "Only a few moments of my time.  Which could have been better spent.  But I thought you would like it."
    n "..."
    p "Well? Aren’t you going to hunt it down and eat it? That little thing could be halfway across the castle by now."
    n "Yesss. But I’ve never hunted in thisss form before. Not {b}thisss{/b} type of hunting."
    p "If you’re not going to hunt it, then I will. I brought a spear star, which is what we \"inferior humans\" use in my kingdom. Hunting is a popular royal pastime."
    n "Then let’sss hunt."
    "He licked his lips and sniffed the air. Then, without warning, he was off down the corridor, following its scent. I ran after him, my soft slippers making as little noise as his bare feet."
    hide niir at center with moveoutleft
    scene bg corridor with fade
    show niir neutral at center with moveinleft
    n "Thissss way."
    hide niir at center with moveoutright

    scene bg hall with fade
    show niir neutral at quarterleft with moveinleft
    n "Ssstop. He’s closssse."
    p "Under the statue!"
    n "Drrrive him thisss way."
    p "Oh little rabbit..."
    p "Come on out and play with us!"
    p "Get him!"
    "The rabbit burst out of hiding, darted right towards Niir, but then saw him and changed direction. I headed him off before he could leave the room, and he ran back towards Niir again."
    show niir neutral at center with quickmove
    n "Caught you!"
    "He caught it up in his hands, breathed on it, then sheepishly looked away."
    p "Did you just try to breathe fire? And it didn’t work?"
    n "That’sss how I usssed to eat them...I don’t rrreally want to eat thisss rrraw."
    p "Cook it, then. There is a kitchen here."
    n "Why don’t {b}you{/b} cook it?"
    p "Me? Cook?! That’s servants’ work."
    n "I’m no sssservant."
    p "Or just eat it raw, or hide in Moronious’ bed for him to find later, or drop it out a window and see if it bounces. I don’t care." 
    p "Though, if you don’t appreciate your little gift, I may not feel inclined to express future generosity."
    hide niir at center with moveoutright
    p "Niir? Where you going?! Niir!"

    scene bg bedroom candle with fade
    p "Ungrateful serpent."
    p "..."
    p "I bet he’s in the kitchen right now, cooking. Ha. I bet he’s making a mess of it."
    menu:
        "Stay here.":
            p "I have better things to do than search for Niir. I found these delightful alchemy books in the library..."
            return
        "Go and see.":
            $ niir_affection += 1
            scene bg kitchen with fade
            show niir neutral at midright, basicfade
            "I caught him in the middle of taking a huge bite. Juices dribbled down his chin, and he had closed his eyes to savor the taste."
            p "I thought I might find you here. Not that I was looking for you. Just slightly curious."
            "He opened his eyes, looking first guilty, then devious. He held out a skewer full of gristle, singed meat, and bones that was once Cyril’s rabbit. He watched my expression carefully, expecting me to recoil."
            n "Want ssssome?"
            p "Yes, actually, it’ll be nice to eat something not conjured up by that silly mage for once."
            n "Sssso, what’s the priccce?"
            p "Price?"
            n "Surely you didn’t give me that for frrree."
            p "I treat my minions well."
            n "I am not any ssssort of minion!"
            p "I treat my partners even better."
            n "Partnerssss, eh?"
            p "Though you're a little bit of both, honestly."
            n "Princesssss..."
            scene black with fade
    return
    
label cyril6:
    scene bg hall with fade
    show cyril neutral at center, basicfade #TODO: make him green
    play music niir_theme
    c "Niir!  Get back here you {i}dragon!{/i}  I’m not playing games this time!  I’m all green now.  Niir just stay in one place so I can- so I can...!"
    "He reached into the pocket of his robes, but his hands came out empty."
    c "...and my spell book's gone again. Oh, p'zuffle!" #TODO: replace if you don't like, or delete this if it's fine.
    p "Moronious, why do you allow Niir to play with you like that? You should use your magic to teach him a lesson. Show your strength and he will think twice before bothering you again!"
    c "The council doesn’t approve of magic used for frivolous things, such as getting even.  And besides, what can a green mage do, like this?"
    p "Can't you turn him into a squirrel, or paralyze him, or make him feel like he's fallen into poison nettle?"
    c "Paralyze? Poison? Squirrel?!  Absolutely not!  Positively absolutely assuredly not.  {i}It’s not as if I don’t want to...{/i} but I am under oath to protect these dragons!"
    p "But you shouldn't have to endure such humiliation! Surely the council would look the other way..."
    c "I thank you for your concern, Highness.  I am grateful for that.  But what can I do?  I have my standing before the council to think of and do not think they would let the matter go lightly."
    p "Well, if you aren't going to do anything about it, perhaps I will!"
    c "I wouldn’t-they’re, they’re dragons milady!  And one should know better than to take on a dragon.  Though I do appreciate the sentiment I absolutely cannot allow it."
    p "You cannot {b}allow{/b} it? It sounds as though you were trying to command YOUR future Queen? Surely even you would not be so ludicrously unintelligent."
    c "Oh no.  That wasn’t what I was intending at all.  I was just-if anything were to happen to you over my own foolishness, your Highness, I would never be able to forgive myself."
    p "That’s your concern, not mine. Stay here. That is an {b}order{/b}!"

    scene bg library with fade
    p "I know I saw something around here... ah-hah! \"Perfect Potion Pranks\", just the sort of book every mage library needs! I’ll need something without too many complicated ingredients."

    scene bg kitchen with fade
    p "Carrot tops, rat droppings, broken glass... ohh, I've forgotten how much I love brewing potions!"

    scene bg dungeon with fade
    show niir neutral at center, basicfade
    n "Do I sssmell...Princesssss?"
    p "Niir, meet me at the castle gates in five minutes. I have something I want to show you that you will find VERY interesting."
    n "Interessssssting.  I have been waiting for interesssting."
    hide niir at center with moveoutleft
    "Now, I’ll just sprinkle this in his sheets...Ahhh!"
    show balrung neutral at center with moveinright
    b "Princess? Can I assist you?"
    p "No, no, no assistance needed, thank you."
    "He glanced at the flask in my hands and smiled."
    show balrung smile eyes closed at basicfade
    b "I believe I feel quite tired. I will be asleep and shall not see or hear anything."
    hide balrung at center with moveoutright
    "Hmph, well, so much for secrecy. Still, now’s my chance!"
    "There! He’ll have quite a surprise when he gets in bed next! \"Interesting\" indeed, mwah ha ha ha ha ha ha!"
    b "I suggest you return to your room before commencing with gleeful cackling, Princess."
    p "I shall return when I am ready! Oh, and Balrung, if Niir is looking for me, please tell him I’ll be in the hall."
    b "Very well. I wish you success in your...endeavors."

    scene bg hall with fade
    show cyril neutral at center, basicfade
    p "Well, that was the most fun I’ve had since poisoning my sis- I mean, passing my sister the ball in croquet!"
    c "Croquet you say?  I have always been meaning to play that..."
    p "Don’t bother. It’s dreadfully dull. Did you know you’re not supposed to hit the other players, only the balls? Who invented that game?!"
    c "Oh well, yes.  I think the purpose is to... how do you propose that it’s played?  Perhaps we can invent a new sport and name it after you, [p_name]."
    p "An excellent idea. There should certainly be bludgeoning involved, and perhaps pilfering? Alchemy? Princess-worship?"
    c "Ah, that sounds like a very interesting sport ind-"
    show niir determined at midright with moveinright
    show cyril neutral at midleft with move
    n "Princesssssss.  It musssst have been you, Princessssss."
    p "Niir? Why are you dancing around like a festival girl? I don’t dance, you know, and it’s unbecoming to dance alone."
    show niir angry at standing, hop
    n "I am not danccccccing.  Thissss isss magic.  Some of hissss magic."
    c "Don’t look at me!  Though it is quite amusing to see this side of you Niir."
    show niir determined at right, hop with move
    p "Yes, I take back what I said earlier. This dancing suits you, much like a fool’s motley suits him."
    n "Ahhh, what issss thisss?  I jusssst need to ssscratch!"
    show niir at midright, hop with move
    n "End it!  End it now!"
    p "Well, I don’t know any magic, but Cyril is an absurdly kind magician...perhaps if you begged him, he might assist you?"
    p "Although... he might be a bit cross about the whole dyeing-him-green incident. You might have to grovel. Or you could continue your itching dance; I’m enjoying it."
    n "Beg?!  I will not- ahhh!  It itchessss.  I will get you for thissss, mage!"
    c "Just hold on.  I’ll think of something that can help you."
    c "If only I had my spellbook on hand..."
    p "If only we knew where it was!"
    n "I’ll find your sssstupid ssspellbook if you get this sssspell off of me!"
    hide niir at midright with moveoutleft

    p "Aha ha ha ha ha ha! Did you enjoy that as much as I did, Cyril?" 
    c "That was quite dev- wait.  Cyril?  You called me Cyril!"
    p "Of course I did. That’s your name, isn’t it?"
    c "Ah, yes you’re right, my-your Highness.  That is correct.  I am Cyril - to you - which I couldn’t be happier about.  So what did you do exactly?"
    p "Me? I don’t know what you’re talking about."
    c "Ah, that must have been some magic indeed.  I think someone, somewhere must be punishing that misbehaving dragon for his misdeeds."
    p "It’s all very mysterious."
    c "Well, to whomever did it, I would like to extend my gratitude."
    p "Yes, yes. Now, can’t you find some way to rid your skin of that disgusting green color? It’s making me ill."
    c "Ah yes.  As soon as that dragon brings me that spellbook of mine, that is the first thing I’ll do."
    c "And if he’s nice, perhaps I’ll help him out too."
    show niir determined at midright,hop with moveinright
    n "I have your sssspellbook mage."
    n "Now sssstop this infernal sssscratching."
    c "I’ll just need to find a different spell first.  Something to rectify what was first wrong."
    p "Cyril! He didn’t beg. He should at least say \"please\"."
    c "Yes, very true.  I do think that is the least he can do after all this trouble."
    n "Pleassse?!  You mussst be jo-oh!   "
    extend "Pleassssse.  Pleassssse."
    c "Here it is! {font=fonts/ankecallig-fg.ttf}Dermis Claro{/font}!" #TODO: un-green CYril
    show cyril angry with magic_flash
    n "That doessssn’t help me, ussseless mage."
    p "Perhaps you should kneel."
    n "I will not {b}kneel{/b}.  I will NOT!"
    c "Okay, I think that’s enough.  I’m looking for the spell now.  It itches right?  Any rash anywhere?"
    n "Yesss, I need to ssscratch.  Here.  Sssee for yoursssself."
    p "Ha ha ha, I will never forget this."
    c "This should do the trick - {font=fonts/ankecallig-fg.ttf}Prurius Termine{/font}!"
    show cyril angry
    show niir angry at midright
    with magic_flash
    
    n "I will not forget thissss."
    c "I do believe you have learned your lesson, Niir."  
    c "And there will be no more of that stealing books business, or turning people green, or making them slip, or sneaking something under the door when they are sleeping.  No more of that."
    n "Ssssay what you like. I’ll do as I pleasssse."
    hide niir at midright with moveoutleft
    show cyril neutral at center with move
    c "It didn’t seem like he learned anything from all that.  Quite disappointing."
    p "You mean entertaining! Perhaps he’ll at least think twice before bothering people."
    c "That is true, Princess.  You always do know how to look on the bright side of things.  I do find your perspective like a breath of fresh air around here."
    p "Ha! I approve of your flattery. That is a skill I prize in all my minions."
    c "Minions?  Oh. Yes.  Of course.  How could I have deluded myself into thinking anything but... I am honored to be anything to you, even a minion, your Highness."
    p "Don’t look so disappointed. You are my favorite minion...at the moment."
    c "Favorite? I-I do say."
    p "You may kiss my cheek, if you wish."
    c "Oh, I wasn’t expect- thank you Princess.  It would be my honor."
    show cyril smile blush eyes closed at come_closer
    "He stepped forward, and leaned his head in for the quickest kiss that could possibly still bear the name."
    "He's mine, now... mwah ha ha ha!"
    scene black with fade
    return
