# DAY 6
# She does something nice for whoever's route she's on
# Of course, it's only to ensure their loyalty...

label day6:
    # She goes around eavesdropping to find out how well her plans have been working.
    scene bg bedroom with fade
    p "Ugggh, that moldy smell again. I must {b}still{/b} be in the old [castle_name]."
    p "But I believe I'm finally making some progress. Although... they could be deceiving me."
    p "Unfortunately, all my spies are back at the palace. I shall just have to do a little information gathering on my own!"
    
    if (route == "Niir"):
        "I snuck down to the dungeon to spy on the dragons."
        scene dungeon with fade
        show niir at midright
        show balrung at midleft
        with dissolve
        b "I do hope you haven't fallen in love with the tempestuous temptress that has entered our realm."
        n "Now why would you ssssssay that?"
        b "I have seen it happen many times before. Many dragons and princesses have come and gone since I arrived."
        b "I can discern the signs."
        n "Love is not ssssomething that I am acquainted with, old dragon."
        n "Ssstop your posssstulating."
        b "I'm no more happy about this than you are, Niir.  You are all what little distraction I have in this dreary place."
        b "If I could keep you here, I would."
        n "Your fearssss are ridiculousssss."
        n "I am sssstaying here, old dragon."
        b "Stubborn fool!  What life is there for you here?!"
        b "What other princesses are there?"
        "Could Balrung be right?  Could Niir actually be... {i}in love{/i}?"
        "The thought makes my stomach roil."
        "Though I have to admit, I do feel some... animal magnetism towards Niir."
        "Even if it is only animal."
        n "Sssshut up.  I am done conversssssing."
        b "I'd tell you to follow your heart. But that would require you to possess one in the first place."
        "This is what I wanted, wasn't it?"
        "A dragon at my disposal.  Willing to leave, all for the delusion of love."
        "But somehow, it doesn't feel as good as I thought it would."
    elif (route == "Cyril"):
        "I snuck over to the library to spy on Moronious."
        #TODO: She overhears him talking with someone or spies on a letter he wrote or something?!
        
    elif (route == "Balrung"):
        "I snuck down to the dungeons to spy on the dragons."
        scene dungeon with fade
        show niir at midright
        show balrung at midleft
        with dissolve
        b "That Princess is really quite...something."
        b "Do you know, Niir, that she beat me at Queens and Pawns yesterday? Nobody has done that since..."
        n "Ssssince Myriah?"
        b "Yes...she distracted me by asking about my imprisonment. Clever human!"
        n "Sssso what?"
        b "Well, I don't wish to get your hopes up in vain, but it seems my long imprisonment may soon be over."
        n "How niccce for {b}you{/b}."
        b "If we can count on your aid as well, then perhaps it's time to end this preposterous tradition of imprisoning ambitious dragons."
        n "I'm lissstening."
        
    return
        
# She does something nice for Balrung.
label balrung6:
    scene dungeon with fade
    show balrung at center with dissolve
    b "My dear lady..."
    "He carefully took my hand and brought it to his lips, watching my reaction with the barest hint of smugness."
    "I smirked in return. Playing at love was more fun than I had imagined. No wonder ordinary people spend so much time on it."
    p "You may call me Chrysandra."
    b "Chrysandra...golden flower? Fitting... lovely as a blossom, hard as metal, yet malleable enough to thrive in any situation."
    p "That's what my father says. Though if I was really so precious to him, he'd have made me Queen."
    p "Anyway, I brought you something."
    b "Princess, the brilliance of your presence is gift enough to soften this stone heart of mine. What more could I ask?"
    p "How about a Hibernation Libation?"
    "I handed him a flask containing the gloopy, dark green potion I had made. It was one of the few whose ingredients were commonplace enough to be found in and around the Castle [castle_name]."
    b "I...I'm touched. How did you know I had trouble sleeping?"
    p "Oh! I assumed you would use it on Niir when you wanted some peace and quiet. Or on that fool mage. I know you're not foolish enough to use it on me."
    b "It has many uses, I see.  How many doses are in here?"
    p "That's enough to make a human sleep for two days. I'm not sure how it would affect a dragon."
    b "Well...thank you. I'm afraid I don't have anything for you."
    p "You will, I'm sure. For now, let us play another game together. I hinted to Moronious that I would be down here, so he may drop by later and we can play with him some more."
    b "Splendid. Why don't you go first this time?"
    p "Yes, I will...there."
    b "That's an interesting opening move."
    p "I know All the Queen's Men is usually derided as transparent and inefficient, but it does have its uses."
    b "It is one way to control the board early."
    p "It sets up certain...expectations."
    b "And illusions."
    p "Illusions? Why, what do you think I'm up to?"
    b "It's obvious. But I don't mind playing along with you."
    p "Well, of course the first plot is obvious. But that's only to distract you from uncovering the second, third, and fourth plots."
    b "How amusing it is to watch people who think they are cleverly manipulating you, when in reality you have already predicted their every move."
    p "Ha! Did you predict this move?!"
    b "Yes, that's why I had this setup here waiting for you."
    p "No! Ohhh, you! You're distracting me with all your talk of plots and illusions!"
    b "A valiant effort, but you should know that I won't be tricked by the Distressed Princess Bluff."
    p "And I won't be misled by your Experienced Brooding Old Man Feint!"
    b "You don't have to fall for it in order for it to be effective. There goes your last Queen."
    p "Ohhhh... I suppose you win, this time."
    show cyril at left with moveinleft
    c "Princess?"
    p "Moronious! How long have you been lurking over there?"
    show cyril at midleft
    show balrung at midright
    with move
    c "I ju-just came to check on you, make sure you were safe..."
    p "Oh yes, Balrung is quite the gentleman. I'm not sure why you're so worried about him; the most dangerous thing he's done is arouse my temper by beating me at Queens and Pawns."
    c "You two do seem to- to get along."
    c "But it's not enough! A person, no, a {b}dragon{/b}, cannot change so easily!"
    p "I have many powers, mage; you'd do well not to underestimate me."
    b "Do you think allowing myself to love is {b}easy{/b}? It is not! I learned from Myriah the price of loving a human!"
    c "And...do you, do you feel the same way, Princess?"
    p "Balrung is charming and useful, so of course I love him."
    c "...Y-you don't even know! You two can't fathom what true l-love is!"
    hide cyril with moveoutleft
    
    b "I'm afraid it may not be possible to convince him, Chrysandra."
    p "Don't give up, yet. Perhaps we just need to give him some time..."
    b "Perhaps..."
    return
    
label niir6:
    scene bg library with fade
    show cyril at center with dissolve
    p "Moronious, are you competent enough to pull a rabbit out of your hat?"
    c "Interesting request.  Hmmm, parlor magic.  I do remember some of that from my earlier days... What was it again?  Explodus Rabititious?  No.  That can’t be right..."
    p "..."
    c "Let me see.  Accerso Leoparda!"
    extend "Oh dear."
    p "I did not ask for a large cat."
    c "That is not, not, not what I was trying to do. Amitto!"
    c "Whew, now that we both escaped with our eyebrows intact, let’s try again."
    c "Accerso Leporidae!"
    p "I only need ONE rabbit, not a hundred of them!"
    c "Ah, yes.  I knew that.  I’ll just rectify that."
    c "Stop that rabbit from escaping!  We need them all in this room!"
    show cyril at left with move
    p "That’s your job, fool. Though, I am rather enjoying watching you run around and gather them up."
    show cyril at right with move
    c "Amitto! Amitto! Reddo amitto!"
    show cyril at midright with move
    c "Stay put for just one moment.   "
    extend "Ahh... that should be the last of them."
    c "One last time.  I’ve got it this time, Princess, don’t you worry."
    c "Accerso Leporida!"
    p "Thank you. Come with me, little bunny, I want you to meet my friend."
    c "Meet your...?  Not one of the dragons!"
    c "I just conjured that bunny!   "
    extend "I’d grown rather fond of him.  Princess?  Princess?"

    scene bg dungeon with fade
    show niir at center with dissolve
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
    hide niir with moveoutleft
    scene bg corridor with fade
    show niir at center with moveinleft
    n "Thissss way."
    hide niir with moveoutright

    scene bg hall with fade
    show niir at midleft with moveinleft
    n "Ssstop. He’s closssse."
    p "Under the statue!"
    n "Drrrive him thisss way."
    p "Oh little rabbit..."
    p "Come on out and play with Niir!"
    p "Get him!"
    "The rabbit burst out of hiding, darted right towards Niir, but then saw him and changed direction. I headed him off before he could leave the room, and he ran back towards Niir again."
    show niir at center with move
    n "Caught you!"
    "He caught it up in his hands, breathed on it, then sheepishly looked away."
    p "Did you just try to breathe fire? And it didn’t work?"
    n "That’sss how I usssed to eat them...I don’t rrreally want to eat thisss rrraw."
    p "Cook it, then. There is a kitchen here."
    n "Why don’t {b}you{/b} cook it?"
    p "Me? Cook?! That’s servants’ work."
    n "I’m no sssservant."
    p "Or just eat it raw, or hide in Moronious’ bed for him to find later, or drop it out a window and see if it bounces. I don’t care. Though, if you don’t appreciate your little gift, I may not feel inclined to express future generosity."
    hide niir with moveoutright
    p "Niir? Where you going?! Niir!"

    scene bedroom with fade
    p "Ungrateful serpent."
    p "..."
    p "I bet he’s in the kitchen right now, cooking. Ha. I bet he’s making a mess of it."
    menu:
        "Stay here.":
            p "I have better things to do than search for Niir. I found these delightful alchemy books in the library..."
            return
        "Go and see.":
                
            scene bg kitchen with fade
            show niir at midright with dissolve
            "I caught him in the middle of taking a huge bite. Juices dribbled down his chin, and he had closed his eyes to savor the taste."
            p "I thought I might find you here. Not that I was looking for you. Just curious"
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
    
label cyril6:

    scene hall with fade
    show cyril at center with dissolve #TODO: make him green
    c "Niir!  Get back here you {i}dragon!{/i}  I’m not playing games this time!  I’m all green now.  Niir just stay in one place so I can- so I can...!"
    "He reached into the pocket of his robes, but his hands came out empty."
    c "...and my spell book's gone again. Oh, p'zuffle!" #TODO: replace if you don't like, or delete this if it's fine.
    p "Moronious, why do you allow Niir to play with you like that? You should use your magic to teach him a lesson. Show your strength and he will think twice before bothering you again!"
    c "The council doesn’t approve of magic used for frivolous things, such as getting even.  And besides, what can a green mage do, like this?"
    p "Can't you turn him into a squirrel, or paralyze him, or make him feel like he's fallen into poison nettle?"
    c "Paralyze? Poison? Squirrel?!  Absolutely not!  Positively absolutely assuredly not.  {i}It’s not as if I don’t want to...{/i} but I am under oath to protect these dragons!"
    p "But you shouldn't have to endure such humiliation! Surely the council would look the other way..."
    c "I thank you for your concern, highness.  I am grateful for that.  But what can I do?  I have my standing before the council to think of and do not think they would let the matter go lightly."
    p "Well, if you aren't going to do anything about it, perhaps I will!"
    c "I wouldn’t-they’re, they’re dragons milady!  And one should know better than to take on a dragon.  Though I do appreciate the sentiment I absolutely cannot allow it."
    p "You cannot {b}allow{/b} it? It sounds as though you were trying to command YOUR future Queen? Surely even you would not be so ludicrously unintelligent."
    c "Oh no.  That wasn’t what I was intending at all.  I was just-if anything were to happen to you over my own foolishness your majesty I would never be able to forgive myself."
    p "That’s your concern, not mine. Stay here. That is an {b}order{/b}!"

    scene library with fade
    p "I know I saw something around here... ah-hah! \"Perfect Potion Pranks\", just the sort of book every mage library needs! I’ll need something without too many complicated ingredients."

    scene kitchen with fade
    p "Carrot tops, rat droppings, broken glass... ohh, I've forgotten how much I love brewing potions!"

    scene bg dungeon with fade
    show niir at midright with dissolve
    n "Do I sssmell..?"
    p "Niir, meet me at the castle gates in five minutes. I have something I want to show you that you will find VERY interesting."
    n "Interessssssting.  I have been waiting for interesssting."
    hide niir with moveoutleft
    "Now, I’ll just sprinkle this in his sheets...Ahhh!"
    show balrung at midright with moveinright
    b "Princess? Can I assist you?"
    p "No, no, no assistance needed, thank you."
    "He glanced at the flask in my hands and smiled."
    b "I believe I feel quite tired. I will be asleep and shall not see or hear anything."
    "Hmph, well, so much for secrecy. Still, now’s my chance!"
    "There! He’ll have quite a surprise when he gets in bed next! \"Interesting\" indeed, mwah ha ha ha ha ha ha!"
    b "I suggest you return to your room before commencing with gleeful cackling, Princess."
    p "I shall return when I am ready! Oh, and Balrung, if Niir is looking for me, please tell him I’ll be in the hall."
    b "Very well. I wish you success in your...endeavors."

    scene hall with fade
    show cyril at midright with dissolve
    p "Well, that was the most fun I’ve had since poisoning my sis- I mean, passing my sister the ball in croquet!"
    c "Croquet you say?  I have always been meaning to play that..."
    p "Don’t bother. It’s dreadfully dull. Did you know you’re not supposed to hit the other players, only the balls? Who invented that game?!"
    c "Oh well, yes.  I think the purpose is to… how do you propose that it’s played?  Perhaps we can invent a new sport and name it after you [p_name]."
    p "An excellent idea. There should certainly be bludgeoning involved, and perhaps pilfering? Alchemy? Princess-worship?"
    c "Ah, that sounds like a very interesting sport ind-"
    n "Princesssssss.  It musssst have been you, Princessssss."
    p "Niir? Why are you dancing around like a festival girl? I don’t dance, you know, and it’s unbecoming to dance alone."
    n "I am not danccccccing.  Thissss isss magic.  Some of hissss magic."
    c "Don’t look at me!  Though it is quite amusing to see this side of you Niir."
    p "Yes, I take back what I said earlier. This dancing suits you, much like a fool’s motley suits him."
    n "Ahhh, what issss thisss?  I jusssst need to ssscratch!"
    n "End it!  End it now!"
    p "Well, I don’t know any magic, but Cyril is an absurdly kind magician...perhaps if you begged him, he might assist you?"
    p "Although... he might be a bit cross about the whole dyeing-him-green incident. You might have to grovel. Or you could continue your itching dance; I’m enjoying it."
    n  "Begged?  I will not- ahhh!  It itchessss.  I will get you for thissss, mage!"
    c "Just hold on.  I’ll think of something that can help you."
    c "If only I had my spellbook on hand..."
    p "If only we knew where it was."
    n "I’ll find your sssstupid ssspellbook if you get this sssspell off of me!"
    hide niir with moveoutleft

    p "Aha ha ha ha ha ha! Did you enjoy that as much as I did, Cyril?" 
    c "That was quite dev- wait.  Cyril?  You called me Cyril!"
    p "Of course I did. That’s your name, isn’t it?"
    c "Ah, yes you’re right, my-your majesty.  That is correct.  I am Cyril - to you - which I couldn’t be happier about.  So what did you do exactly?"
    p "Me? I don’t know what you’re talking about."
    c "Ah, that must have been some magic indeed.  I think someone, somewhere must be punishing that misbehaving dragon for his misdeeds."
    p "It’s all very mysterious."
    c "Well, to whomever did it, I would like to extend my gratitude."
    p "Yes, yes. Now, can’t you find some way to rid your skin of that disgusting green color? It’s making me ill."
    c "Ah yes.  As soon as that dragon brings me that spellbook of mine, that is the first thing I’ll do."
    c "And if he’s nice, perhaps I’ll help him out too."
    show niir
    n "I have your sssspellbook mage."
    n "Now sssstop this infernal sssscratching."
    c "I’ll just need to find a different spell first.  Something to rectify what was first wrong."
    p "Cyril! He didn’t beg. He should at least say \"please\"."
    c "Yes, very true.  I do think that is the least he can do after all this trouble."
    n "Pleassse?!  You mussst be jo-oh!   "
    extend "Pleassssse.  Pleassssse."
    c "Here it is! Dermis Claro!" #TODO: un-green CYril
    n "That doessssn’t help me, ussseless mage."
    p "Perhaps you should kneel."
    n "I will not {b}kneel{/b}.  I will NOT!"
    c "Okay, I think that’s enough.  I’m looking for the spell now.  It itches right?  Any rash anywhere?"
    n "Yesss, I need to sssratch.  Here.  Sssee for yoursssself."
    p "Ha ha ha, I will never forget this."
    c "This should do the trick - Pruritus Termine!"
    n "I will not forget thissss."
    c "I do believe you have learned your lesson, Niir.  And there will be no more of that stealing books business, or turning people green, or making them slip, or sneaking something under the door when they are sleeping.  No more of that."
    n "Ssssay what you like. I’ll do as I pleasssse."
    hide niir with moveoutleft
    c "It didn’t seem like he learned anything from all that.  Quite disappointing."
    p "You mean entertaining! Perhaps he’ll at least think twice before bothering people."
    c "That is true, Princess.  You always do know how to look on the bright side of things.  I do find your perspective like a breath of fresh air around here."
    p "Ha! I approve of your flattery. That is a skill I prize in all my minions."
    c "Minions?  Oh, yes.  Of course.  How could I have deluded myself into thinking anything but... I am honored to be anything to you, even a minion your majesty."
    p "Don’t look so disappointed. You are my favorite minion...at the moment."
    c "Favorite? I-I do say."
    p "You may kiss my cheek, if you wish."
    c "Oh, I wasn’t expect- thank you Princess.  It would be my honor."
    show cyril at center with come_closer
    "He stepped forward, and leaned his head in for the quickest kiss that could possibly still bear the name."
    "He's mine, now... mwah ha ha ha!"
    scene black with fade
    return