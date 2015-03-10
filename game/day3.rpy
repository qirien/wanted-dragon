label day3:
    scene bg bedroom with fade
    
    p "Ugh, this castle is so cold and dank. The snow hasn't quite melted yet, here. But the birds are still out..."
    p "Strange... one of them is flying this way. Almost as if it's going to-"
    "(It's coming in my room?!)"
    "(Oh. It is simply one of Father's carrier pigeons dropping off a letter.)"
    
    k_write "My dearest [p_name],"
    k_write "I wish you hadn't left in such a hurry. You know I don't believe what the courtiers are saying."
    k_write "You and your sister have never been friendly, it's true, but I can't believe that you would--"
    k_write "Anyway, your banishment need only last as long as it takes for you to be ready to support your sister. Take all the time you need, but please, come back to us. "
    k_write "Magnolia's coronation won't be the same without you."
    k_write "With love,\nFather"
    nvl clear
    p "Father..."
    
    "(There's something on the other side...there's hearts everywhere.)"
    m_write "[p_name],"
    m_write "The castle is so lonely, now - it kills me to be so far from you."
    m_write "Even if you can't be Queen, I'm sure there will be plenty of important things for you to help out with."
    m_write "We need you here; please come back!  I promise not to be too mad."
    m_write "Love,\nYour sister Magnolia"
    nvl clear
    
    p "Magnolia...so devious! Even as she outwardly pretends to want me back, it's clear she knows I was the one who put the poison in her tea."
    p "Look how she tries to put me in my place! \"Important things to help out with,\" ridiculous. But I know she has Father completely fooled."
    p "Well, if she thinks I'm going to slink back there and \"help out\" with \"important\" things like planning balls and planting gardens, she's delusional!"
    p "I WILL BE QUEEN!!!"
    
    p "But for now... how should I reply?"
    menu:
        "Sweetly.":
            p_write "Dear Father Who has Abandoned One Daughter in Favor of the Other,"
            "(I will not deign to respond to Magnolia.)"
            p_write "I was delighted to receive your letter and see that you haven't completely forgotten me, [p_name], your other daughter, the one that you should have chosen to be Queen."
            p_write "I'm afraid the only thing that could induce me to return would be an announcement that you have named me as your successor. I simply cannot in good conscience support {s}that evil bitch{/s}-"
            nvl clear
            "(No, that's too obvious. I must be subtle.)"
            p_write "I simply cannot in good conscience support someone who does not have our kingdom's best interests at heart and is also completely inept, not to mention ugly, devious, scheming, and cruel!"
            "(...I may have overdone it a bit.)"
            p_write "So I hope you can at least try to understand me, your poor, maligned, misunderstood, regal, capable, queenly daughter."
            p_write "Love and kisses,"
            p_write "[p_name]"
            nvl clear
            "(Now where'd that pigeon go?)"
            p "There, little bird. Fly true."            
            
        "Haughtily.":
            p_write "Dear Father and Daughter that Claim to Rule [k_name],"
            p_write "I cannot allow such ineptitude, scheming, and gross negligence to rule over the Ancient and August Kingdom of [k_name]."
            p_write "To grant the throne to Magnolia would destroy our kingdom's power and glory!"
            p_write "While you, Father, may not be able to see her perfidy and betrayals, I can, which is why I cannot sit by and do nothing."
            p_write "Father, if you have any intelligence or care for the long-term well-being of our kingdom, you will not allow Magnolia's coronation to take place and will crown me instead."
            p_write "If you choose not to, I will do whatever is necessary to obtain the throne, for the good of the kingdom!"
            p_write "Love,"
            p_write "Your better daughter,"
            p_write "[p_name]"
            "(Now where'd that pigeon go?)"
            p "There, little bird. Fly true."
            
        "No reply. Let them wonder.":
            p "Father knows that I can never return as long as he is planning to crown my sister Magnolia as queen."
            p "Perhaps he will feel he has made a mistake if he thinks I am dead or kidnapped by bandits as a result of his rash decision!"
    
    n "Knock, knock, Prrrrincesss..."
    p "Oh, what is it now, Niir. I'll warn you: I'm already in a foul mood!"
    show niir at quarterright with moveinleft
    n "Sssseen anything interesting today Princessss?"
    p "No, it’s all been very dull. And now it’s become tedious as well. What do you want?"
    n "I sssupect the question should be to you.  What do {i}you{/i} want?"
    n "You came here, acting ssssupicious in the first place."
    p "I need something powerful. Something that will make it clear that I am the rightful Queen. If you don’t have anything like that, then away with you."
    n "More powerful than a dragon?  My aren’t you ambitioussss?"
    p "It doesn’t take much to be more powerful than you right now."
    p "You probably don’t even know any secrets of this castle, despite the fact that you’ve lived here for years."

    n "I know sssssecrets of all kindsss.  And not just about the cassstle."
    n "I could find you ssssomething powerful.  But what would you do for me in return?"
    p "Why, I would help you gain your freedom, so you could continue to serve me."
    n "That doesn’t ssssound like a very good deal."
    p "It sounds good to me. Do you have a better idea?"
    n "..."
    p "No? Then perhaps I’ll just go and ask Moronious. He probably knows more than you do about the ‘ssssecrets’, anyway."
    n "Don’t waste your time with him.  I am the only one who knowssss."
    menu:
        "Go with Niir.":
            p "You, the only one who knows secrets? I don't believe you."
            jump niir3
        "Go ask Moronious":
            p "I'm going to ask that mage instead. Good-bye, Niir."
            jump cyril3
        "Go ask Balrung":
            p "I'm going to speak with Balrung about it. Good-bye."
            jump balrung3
            
    
label cyril3:
    scene bg library with fade
    show cyril at center with dissolve
    $ cyril_affection += 1
    p "Ohhhh Moroooonious!"
    p "What progress have you made with obtaining that scepter for me?"
    c "Oh!  You disturbed me!  I didn't notice you there for a second."
    c "About the what now?"
    p "The Scepter of Lavendorm."
    p "The one purportedly hidden around these grounds."
    c "Oh yes, right."
    c "Well, your majesty. I have drawn up a map of the castle."
    c "And crossed off all the little places that I know most certainly that it isn't."
    c "And..."
    c "Wait just a moment here.  How did I get roped into doing your bidding again?"
    p "Because you have such a generous spirit."
    p "Oh, and if you don't I will be sure that your head is on a chopping block somewhere."
    c "Ah yes.  Very good reasons indeed!  I will return to the task at hand then!"
    p "Good, I see that we're on the same page then."
    c "I do wonder what it is that you plan to do with such a scepter, however, because I'm sure that it can only be wielded by someone with magical knowledge." 
    p "Then you will become more useful to me than ever."
    p "Wouldn't you want that?"
    c "I-I suppose it wouldn't be the worst thing, your majesty."
    return
     
label balrung3:
    scene bg dungeon with fade
    show balrung at center with dissolve
    b "Princess. What a pleasure it is to see your face. But, of course, you didn't come here to talk with me. Are you looking for Niir?"
    p "No, I wanted to talk to you."
    b "Really? I imagine you're looking for some gullible fool that you can trick into using their powers for your benefit? A thrall, a lackey, a minion?"
    p "No, no of course not!"
    "(Is it that obvious?!)"
    b "Oh really? My apologies, then. What {b}does{/b} bring you here?"
    if (asked_scepter == "Balrung"):
        p "Have you found out more about the location of that scepter I asked you about?"
        b "No, I'm afraid not. Its powers must be dormant at the moment."
        p "You are beginning to seem useless to me."
    else:
        p "Do you know anything about the Scepter of Lavendorm?"
        call balrung_scepter
    b "Well, as I cannot offer you a scepter at the moment, perhaps you would stay and talk with me for a bit? Your company would be much appreciated."
    menu:
        "\"I will join you.\"":
            p "Yes, I can spare you a few moments of my time."
            $ balrung_affection += 1
        "\"No, I must ask Cyril about it.\"" if (asked_scepter != "Cyril") :
            jump cyril3
        "\"I will look for it myself.\"" if (asked_scepter != "no one"):
            p "I will go and look for it myself."
            # TODO: Add exploration in here.
            
    b "What do you do? When you don't have a kingdom to reclaim, that is."
    p "I have many pursuits. Reading, hunting, music, alchemy, scheming, plotting."
    b "Ha! The usual royal activities, then."
    p "And what about you?"
    b "I sometimes read from the library, though human books are so maudlin and predictable."
    p "Are there dragon books?"
    b "Most dragons don't take time to read... so I'm afraid there aren't many. But the few books that have been written are masterpieces. We dragons don't do anything by halves. I only have one of my books here - this book of poetry."
    p "Dragon poetry? What is it like?"
    b "It's not nearly as powerful in translation, but there's one here that still speaks to me. Would you care to read it?"
    
    book "Fly:"
    book "Wings soar,"
    book "roar, writhe."
    book "Thy yearning groweth."
    book "This skin: nude, deft."
    book "Two sinuous serpents"
    book "soar rapturous."  #TODO: is this too...sexy? or something?
    nvl clear
    b "No, no, not that one. The one on the other side of the page."
    p "Oh! Of-of course!"
    
    book "Freedom:"
    book "Mastery you obtain,"
    book "Kneeling never."
    book "Remember reverie eternal,"
    book "Like circling glorious summits-"
    book "Soaring, graceful, limber-"
    book "Revel, love, vanquish."
    nvl clear
    
    b "What do you think?"
    menu:
        "\"Words, words, words. Boring!\"":
            p "Words, words, and more words. Boring and useless."
            b "I wouldn't underestimate their power. Sometimes ten words can accomplish what ten armies cannot."
            p "I'd prefer the armies."
            b "For your purposes, perhaps armies would work better."
        "\"I like the 'vanquish' part.\"":
            $ balrung_affection += 1
            p "I like the part about vanquishing. Why do you like this poem so much?"
            b "It speaks to me of freedoms I have all but forgotten. Of a life so far in the past it feels like history. Of the possibilities of the future."
    p "What form of poetry is this? I see no rhymes, no pattern of syllables."
    b "This is an example of the 7-chain form. There are seven lines in the poem. The first is a single word that introduces the topic of the poem. The next five elaborate, and the last line restates the topic in a different way."
    p "That's it?"
    b "And, the ending sound of each word must be the starting sound of the next word. This is much easier in our language because of the simpler conjugation of verbs and greater variety of- Forgive me, Princess. I'm afraid I'm boring you."
    p "Yes, you are. Goodbye."
    b "Another time, perhaps."
    return
    
label niir3:
    $ niir_affection += 1
    n "Follow me and I’ll sssshow you something."
    p "Very well. Lead on, Niir."
    n "Thissss way."
    hide niir
    with moveoutleft
    scene bg corridor with fade
    show niir at midright
    with moveinright
    n "Why do you care about the kingdom anyway?  What hasss the kingdom done for you?"
    p "Nothing, yet. That’s why I need to be Queen."
    p "Surely you can understand wanting greater power and recognition?"
    n "There are other wayssss of getting power.  Much more amusing ways, than dealing with royalty." 
    p "The throne should be mine! It {b}is{/b} mine! My sister is not fit to rule! If my father can’t see that--"
    n "Ssso you just want to take it?"
    p "It is my {b}right{/b}! I was born to be QUEEN!!"
    n "I don’t care about that.  But I am interessssted in you jussst taking it."
    hide niir
    with moveoutleft
    scene bg kitchen with fade
    show niir at midright
    with moveinright
    p "By the way, isn’t this the kitchen? Where are you taking me?"
    n "We have to go through the kitchen.  Patiencccce."
    p "Now you’re starting to sound like my father! You don’t usually sound like my father, though. He doesn’t seem to care what I wear or what I do or what I want at all."
    n "Ssssounds heartbreaking, princessss.  I don’t care either.  But I want to find out what your plansss are, as it seems like you don’t have any."
    n "Watching you fail could be entertaining."
    p "Hmph. That’s no way to talk to your future Queen."
    n "My queen?  Ha ha ha ha.  I am a dragon.  I have no queen."
    p "{b}Moronious{/b} might as well be your queen, since he controls where you can go and keeps you in human form. I wouldn’t be so cruel."
    n "He is rather pretty."
    n "But you, are ssslightly more becoming.  Just ssslightly."
    hide niir
    with moveoutleft
    scene bg storage with fade
    show niir at midright
    with moveinright
    p "Yes, well, it is a queenly duty to look becoming... though my presence would certainly be improved if I had my full royal wardrobe. Are we there yet?"    
    n "Ssssoon.  Hmmm.  Where is this royal wardrobe of yoursss?"
    p "Back at {b}my{/b} castle, which I must say is in much better repair than this one. Why, did you want to try something on?"
    n "I will if you do."
    p "I think you would look fabulous inside a wardrobe."
    n "Perhapsss.  Why leave sssuch a lovely wardrobe behind? " 
    p "I left in a bit of a...hurry."
    n "And you may never go back."
    p "Of course I’m going back! But when I go back, it shall be with such power and magnificence that they will have no choice but to accept me as Queen! I had thought to find something useful here, but it seems there’s only dusty old rooms and dusty old dragons."
    n "Leaving issss not alwaysss an option.  Not just for dragonsss either.  I might make it my misssion to keep you here."
    p "Hmph. Well, then your mission will need to include renovating this castle, finding me a new wardrobe, making me a queen, and making yourself...less of a nuisance. I’m not sure you can handle all that, particularly the last requirement. Though, if you could...hmmm..."
    n "Ahhh, ssseems it took less persuasion than I originally thought."
    p "I am not persuaded of anything, yet. Show me you are capable, however, and then I will decide."
    n "It would make things a little more entertaining.  I think I’ve worn Balrung down to the bone.  He isss less interesssting company than he initially wassss."
    hide niir
    with moveoutleft
    scene bg corridor flip with fade
    show niir at midright
    with moveinright    
    n "What is your cassstle like?  Better than thisss?"
    p "Obviously. Though, this castle does have a certain... gravity that is hard to find in a castle these days. My castle was- {b}is{/b} full of beauty, with stained glass scenes of my ancestors’ achievements, and every comfort a queen deserves."
    n "Perhapsss I will consider helping you take that one inssstead.  But you ssstill haven’t made me a good enough deal.  What will we do with thissss father of yourss if I help you take it?"
    p "Father? Well, I...he... what do you care what I do with my father?!"
    n "Oh, a sssore spot.  Fathersss usually are.  At leassst you have not had to deal with a dragon father."
    p "What is your father like?"
    n "I don’t remember, usss dragonsss do not have strong paternal bondsss.  But ever since I arrived here Balrung hasss acted like my father.  And every time I try to be rid of him, it sssseems I am ssstuck with him, in this form.  We dragonsss would rather not have such submisssion to parental figures."
    p "He wants you to be something you’re not."
    n "It sssseems in two dayss you understand me more than he."
    p "We do have a few things in common."
    n "..."
    hide niir
    with moveoutleft
    scene bg stairs with fade
    show niir at midright
    with moveinright
    p "What will you do once you’re free? Besides serve my every whim, of course."
    n "I’ll pretend you didn’t ssssay that."
    n "..."
    n "I don’t remember tasssting true freedom.  It hasss been too long."
    p "..."
    p "Surely you can think of {b}something{/b}? Flying around a volcano, or devouring a herd of sheep, or decimating an enemy castle? Actually, you’ll need to leave the castle in good enough condition that I can inherit it; just do enough damage to scare everyone out of it."
    n "Who {b}are{/b} you Princessss?  You ssssurely do not act like any princess that I have ssseen."
    p "Let me guess; all the princesses you’ve met were the demure, gentle type that pretend they wouldn’t hurt a fly, but actually scheme behind their sister’s back to steal away their kingdom?"
    n "The princessesss did not tell me to devour ssssheep or decimate a cassstle.  If that isss the type.  I thought it wasssn’t ‘regal’ to sssugest such thingsss.  Won’t your people be displeasssed with your hearty appetite for destruction?"
    p "It’s not destruction I crave, but the throne! And if a little poison fails to do the trick, then perhaps I’ll try a little dragon fire."
    "(Oops! Did I mention the poison?!)"
    n "Poissson?  I will keep it in mind the next time you put a tasssty morsssel in front of my nossse."
    p "A-a-anyway, is this the place you wanted to show me?"
    n "Not yet!  Princesss!  We are almossst there.  I just got… dissstracted."
    n "Thisss way."
    n "Here."
    hide niir
    with moveoutleft
    scene bg exterior with fade
    show niir at midright
    with moveinright
    p "This...is a tower."
    n "Nicccce up here, isn’t it?"
    n "It’ssss where I come sometimesss. "
    p "I thought you were going to show me something powerful?!"
    n "Sssomething that makesss me feel powerful."
    p "That’s not what I meant! I need something that can make me Queen!"
    n "Have you ever flown before Princesss?"
    p "Of course not. Do I look like a dragon to you?"
    n "Then you do not truly know what power issss."
    n "Maybe sssome day..."
    p "It is nice up here, though. I suppose it wasn’t a complete waste of time."
    n "It’sss not the sssame."
    n "Sssee you around, Princesss."
    hide niir with moveoutright
    p "W-w-wait, how do I get back?! Niir! You mustn’t leave your queen stranded!"
    "(He left me stranded.)"
    "(People will be hearing about this.  Perhaps that useless mage will keep him in line.)"
    return