label day3:
    play music evil_theme    
    scene bg bedroom dusk with fade
    
    p "Ugh, this castle is so cold and dank. The snow hasn't quite melted yet, here. But the birds are still out..."
    p surprised "Strange... one of them is flying this way. Almost as if it's going to-"
    "It's coming in my room?!"
    "Oh. It is simply one of Father's carrier pigeons dropping off a letter."
    
    k_write "My dearest [p_name],"
    k_write "I wish you hadn't left in such a hurry. You know I don't believe what the courtiers are saying."
    k_write "You and your sister have never been friendly, it's true, but I can't believe that you would--"
    k_write "Anyway, your banishment need only last as long as it takes for you to be ready to support your sister. Take all the time you need, but please, come back to us. "
    k_write "Magnolia's coronation won't be the same without you."
    k_write "With love,\nFather"
    nvl clear
    p neutral "Father..."
    
    "There's something on the other side...there's hearts everywhere."
    m_write "[p_name],"
    m_write "The castle is so lonely, now - it kills me to be so far from you."
    m_write "Even if you can't be Queen, I'm sure there will be plenty of important things for you to help out with."
    m_write "We need you here; please come back!  I promise not to be too mad."
    m_write "Love,\nYour sister Magnolia"
    nvl clear
    
    p angry "Magnolia...so devious! Even as she outwardly pretends to want me back, it's clear she knows I was the one who put the poison in her tea."
    p shout "Look how she tries to put me in my place! \"Important things to help out with,\" ridiculous. But I know she has Father completely fooled."
    p tsk "Well, if she thinks I'm going to slink back there and \"help out\" with \"important\" things like planning balls and planting gardens, she's delusional!"
    p shout "I WILL BE QUEEN!!!" with vpunch
    
    p neutral "But for now... how should I reply?"
    menu:
        "Sweetly.":
            p_write "Dear Father Who has Abandoned One Daughter in Favor of the Other,"
            "I will not deign to respond to Magnolia."
            p_write "I was delighted to receive your letter and see that you haven't completely forgotten me, [p_name], your other daughter, the one that you should have chosen to be Queen."
            p_write "I'm afraid the only thing that could induce me to return would be an announcement that you have named me as your successor. I simply cannot in good conscience support {s}that evil bitch{/s}-"
            nvl clear
            "No, that's too obvious. I must be subtle."
            p_write "I simply cannot in good conscience support someone who does not have our kingdom's best interests at heart and is also completely inept, not to mention ugly, devious, scheming, and cruel!"
            "...I may have overdone it a bit."
            p_write "So I hope you can at least try to understand me, your poor, maligned, misunderstood, regal, capable, queenly daughter."
            p_write "Love and kisses,"
            p_write "[p_name]"
            nvl clear
            "Now where'd that pigeon go?"
            p "There, little bird. Fly true."            
            
        "Haughtily.":
            p_write "Dear Father and Daughter that Claim to Rule [k_name],"
            p_write "I cannot allow such ineptitude, scheming, and gross negligence to rule over the Ancient and August Kingdom of [k_name]."
            p_write "To grant the throne to Magnolia would destroy our kingdom's power and glory!"
            p_write "While you, Father, may not be able to see her perfidy and betrayals, I can, which is why I cannot sit by and do nothing."
            nvl clear
            p_write "Father, if you have any intelligence or care for the long-term well-being of our kingdom, you will not allow Magnolia's coronation to take place and will crown me instead."
            p_write "If you choose not to, I will do whatever is necessary to obtain the throne, for the good of the kingdom!"
            p_write "Love,"
            p_write "Your better daughter,"
            p_write "[p_name]"
            nvl clear
            "Now where'd that pigeon go?"
            p "There, little bird. Fly true."
            
        "No reply. Let them wonder.":
            p "Father knows that I can never return as long as he is planning to crown my sister Magnolia as queen."
            p "Perhaps he will feel he has made a mistake if he thinks I am dead or kidnapped by bandits as a result of his rash decision!"
    
    n "Knock, knock, Prrrrincesss..."
    p shocked "Oh, what is it now, Niir. I'll warn you: I'm already in a foul mood!"
    show niir neutral at center with moveinleft
    show niir mischief at basicfade
    n "Sssseen anything interesting today Princessss?"
    p neutral "No, it’s all been very dull. And now it’s become tedious as well. What do you want?"
    show niir concerned at basicfade
    n "I sssupect the question should be to you.  What do {i}you{/i} want?"
    show niir frown at basicfade
    n "You came here, acting ssssupicious in the first place."
    p shout "I need something powerful. Something that will make it clear that I am the rightful Queen. If you don’t have anything like that, then away with you."
    show niir smirk at basicfade
    n "More powerful than a dragon?  My aren’t you ambitioussss?"
    p "It doesn’t take much to be more powerful than you right now."
    p angry "You probably don’t even know any secrets of this castle, despite the fact that you’ve lived here for years."

    show niir neutral at basicfade
    n "I know sssssecrets of all kindsss.  And not just about the cassstle."
    show niir mischief at basicfade
    n "I could find you ssssomething powerful.  But what would you do for me in return?"
    p smile "Why, I would help you gain your freedom, so you could continue to serve me."
    show niir frown at basicfade
    n "That doesn’t ssssound like a very good deal."
    p "It sounds good to me. Do you have a better idea?"
    show niir determined at basicfade
    n "..."
    p smile "No? Then perhaps I’ll just go and ask Moronious. He probably knows more than you do about the ‘ssssecrets’, anyway."
    show niir angry at basicfade
    n "Don’t waste your time with him.  I am the only one who knowssss."
    menu:
        "Go with Niir.":
            p "You, the only one who knows secrets? I don't believe you."
            jump niir3
        "Go ask Moronious":
            p "I'm going to ask that mage instead. Good-bye, Niir."
            show niir determined at basicfade
            n "You're making a misssstake, Princessss."
            jump cyril3
        "Go ask Balrung":
            p "I'm going to speak with Balrung about it. Good-bye."
            show niir determined at basicfade
            n "You're making a misssstake, Princessss."
            jump balrung3
            
    
label cyril3:
    play music balrung_theme    
    scene bg library with fade
    show cyril hat neutral at center, basicfade
    
    $ cyril_affection += 1
    p laugh eyes closed "Ohhhh Moroooonious!"
    p friendly "What progress have you made with obtaining that scepter for me?"
    c "Oh!  You disturbed me!  I didn't notice you there for a second."
    c "About the what now?"
    p "The Scepter of Lavendorm."
    p shocked "The one purportedly hidden around these grounds."
    c "Oh yes, right."
    c "Well, your Highness. I have drawn up a map of the castle."
    c "And crossed off all the little places that I know most certainly that it isn't."
    c "And..."
    c "Wait just a moment here.  How did I get roped into doing your bidding again?"
    p smile "Because you have such a generous spirit."
    p smile "Oh, and if you don't I will be sure that your head is on a chopping block somewhere."
    c "Ah yes.  Very good reasons indeed!  I will return to the task at hand then!"
    p friendly "Good, I see that we're on the same page then."
    c "I do wonder what it is that you plan to do with such a scepter, however, because I'm sure that it can only be wielded by someone with magical knowledge." 
    p "Then you will become more useful to me than ever."
    p smile "Wouldn't you want that?"
    c "I-I suppose it wouldn't be the worst thing, your Highness."
    p surprised "Come and see me when you have more."
    c "It would be my pleasure."
    
    scene bg library with fade
    "I supposed while Moronious is working on that, I may as well do some research of my own."
    "What else is there in this oddly large library?  This is possibly the only room in this castle that is well-kept."
    "Ahhh, {i}Powerful Ingredients And Where to Find Them{/i}. Lovely."
    "I'll just take this back to my room where I won't be bothered."
    scene bg bedroom day with fade
    show cyril hat neutral at center, basicfade
    p angry "Ugh, this place smells like moss.  Like stinking, rotting-"
    c "Oh!  I'm sorry Princess.  I didn't mean to intrude!"
    "How long has he been here in my room?  And... "
    extend "Is that my letter?!"
    c "Or read your private correspondance.  You see, it was just out on the desk and it happened to catch my eye and-"
    p shout "Quit blathering like a fool!"
    "Honestly, one can't think with all the stuttering he does time and time again."
    p shout "Did you or did you not {b}read{/b} my letter?"
    c "It was an accident I assure you!"
    "Should I believe that?"
    "Well, Moronious is strangely, and irritatingly honest."
    "So it is possible it's the truth."
    menu:
        "Believe him.":
            p "Hm, very well.  And just what were you doing in my private quarters?"
            c "Well, it was my room if you remember..."
            p surprised "That doesn't sound like an explanation Moronious."
            c "Ah, yes.  You did tell me to come and see you correct?  So I thought I would drop by and ah, catch up."
            c "That is the terminology is it not?  I haven't used it for quite some time."
            c "Or ever really."
            p "I told you to come and see me if you have more information.  Do you?"
            c "Well ah, more to say, I have.  But not more information, no."
            p angry "So you decided to sneak in and read my letter?"
            c "No!  But if I may say so, you should not miss your sister's coronation."
            c "If you do, it'll never be the same between the two of you and you'll be saddened to miss-"
            p tsk "Do {b}not{/b} tell me what to feel, mage."
            c "I wouldn't dream of it, your Highness.  I just thought that if you would consider..."
            p angry "I would not consider.  You do not know my family."
            c "I am sorry. I should be more considerate! Sometimes I have one of those days, too."
            p surprised "One of... those days?"
            c "The days when nothing seems to go right."
            c "Today, I honestly felt like everything was coming together and then-"
            c "{i}Alekadoo!{/i}  Everything goes topsy turvy."
            p "Is this to do with dragons stealing your spellbook again?"
            c "Oh?  You think they stole it?"
            p "Is the sky blue?"
            c "Ah.  A riddle!  I am quite fond of riddles."
            p shocked "No, it was sarca- you know, never mind."
            c "But not on a day like today."
            c "On a day like today I would much rather hide my head in my hat."
            p friendly "Perhaps you're feeling miserable enough to, I don't know, {i}release the dragons?{/i}"
            c "Oh no.  I'm not quite miserable enough for that."
            p friendly "Well, what can we do to make you {i}more{/i} miserable then?"
            c "Hmmm... I guess if I am to be reminded of my childhood I will probably be more miserable."
            p "{i}Your{/i} childhood, mage?  What was so wrong with {i}your{/i} childhood?"
            c "I learned all my spells quite well, but I was rather ignored for the flashier mages."
            c "People didn't really remember my name and my own mother told me to stop snivelling about being forgotten."
            c "Even though it was in private, and I can do what I like with my private time and..."
            p shocked "I've heard enough."
            c "Y-ou have?"
            p "Yes, I have and this is pitiful.  I mean, do you have any comprehension of what life was like growing up in the royal castle?"
            p "{i}Do{/i} you?"
            p angry "Everyone doing your bidding and acting all sweet and kind to you just...because!"
            c "Ah, yes.  That does-that does sound horrible."
            p angry "It was monstrous, hideous.  And my sister, she always got complimented first - {i}first!{/i}"
            p tsk "I mean, it's not as though I'm second rate.  So why her?"
            c "Well, she is the elder out of you... so I'm sure it was just-"
            p "If I want your opinion I'll ask."
            c "I'm sorry you had such a dreadful time."
            c "But you are here now, and I am more than willing to do anything to appease you, your Highness."
            p "I will take you up on that."
        
        "Ignore him.":
            $ cyril_insanity += 1
            p "..."
            "This will do the trick to keep that snivelling to a minimum."
            "Hopefully he will take the hint and BEGONE!"
            c "Princess, I am very sorry, I did not mean to intrude myself in your personal business."
            p "..."
            c "If you permit me to say so, your father and your sister seem to care for you dearly."
            "Oooh, you are testing me, mage."
            "You said that to have me break my silence and strike you down."
            "But I am much more strong-willed than that."
            p "..."
            c "Ahem."
            c "Yes.  They do care for you and I do think you must get in contact."
            "I will not fall for this.  He wants me to tell him about {i}my{/i} return correspondence.  "
            extend "I will {b}not{/b}."
            c "Unless you think not.  That is up to you of course."
            c "I just know if I had family that cared enough for my well-being-"
            c "Ah, well you don't want to hear the musings of this foolish mage."
            p "..."
            "Perhaps if I lie down and close my eyes he might finally leave." 
            c "I do think however that it is in your best interests-"
            scene black with fade
            p "..."
            c "Oh.  I notice that you're a little tired."
            c "I should come back another time?  Good night Princess."
            c "Even though it is still day.  "
            extend "Baffling.  Goodbye then."
            scene bg bedroom day with fade
            "That took him long enough.  Hm.  This is a good tactic for getting rid of him."
            "I may employ it again in the future."
    
    
    return
     
label balrung3:
    play music balrung_theme    
    scene bg dungeon with fade
    show balrung neutral at center, basicfade
    
    show balrung smile at basicfade
    b "Princess. What a pleasure it is to see your face. But, of course, you didn't come here to talk with me. Are you looking for Niir?"
    p friendly "No, I wanted to talk to you."
    show balrung smirk at basicfade
    b "Really? I imagine you're looking for some gullible fool that you can trick into using their powers for your benefit? A thrall, a lackey, a minion?"
    p smile "No, no of course not!"
    "Is it that obvious?!"
    show balrung smile eyes closed at basicfade
    b "Oh really? My apologies, then. What {b}does{/b} bring you here?"
    if (asked_scepter == "Balrung"):
        p "Have you found out more about the location of that scepter I asked you about?"
        show balrung neutral at basicfade
        b "No, I'm afraid not. Its powers must be dormant at the moment."
        p angry "You are beginning to seem useless to me."
    else:
        p "Do you know anything about the Scepter of Lavendorm?"
        call balrung_scepter from _call_balrung_scepter
    show balrung neutral at basicfade
    b "Well, as I cannot offer you a scepter at the moment, perhaps you would stay and talk with me for a bit? Your company would be much appreciated."
    menu:
        "\"I will join you.\"":
            p "Yes, I can spare you a few moments of my time."
            $ balrung_affection += 1
        "\"No, I must ask Cyril about it.\"" if (asked_scepter != "Cyril") :
            jump cyril3
        "\"I will look for it myself.\"" if (asked_scepter != "no one"):
            p angry "I will go and look for it myself."
            jump explore1
            
    show balrung smile at basicfade
    b "What do you do? When you don't have a kingdom to reclaim, that is."
    p friendly "I have many pursuits. Reading, hunting, music, alchemy, scheming, plotting."
    show balrung smirk at basicfade
    b "Ha! The usual royal activities, then."
    p "And what about you?"
    show balrung neutral at basicfade
    b "I sometimes read from the library, though human books are so maudlin and predictable."
    p "Are there dragon books?"
    show balrung smile at basicfade
    b "Most dragons don't take time to read... so I'm afraid there aren't many. But the few books that have been written are masterpieces."
    show balrung smile eyes closed at basicfade
    b "We dragons don't do anything by halves. I only have one of my books here - this book of poetry."
    p surprised "Dragon poetry? What is it like?"
    show balrung smirk at basicfade
    b "It's not nearly as powerful in translation, but there's one here that still speaks to me. Would you care to read it?"
    
    $ book_flipped = True
    book "Fly:"
    book "Wings soar,"
    book "roar, writhe;"
    book "thy yearning groweth."
    book "These scales slide, deft;"
    book "two sinuous serpents"
    book "soar rapturous."  
    nvl clear
    $ book_flipped = False
    
    show balrung smile blush at basicfade
    b "No, no, not that one. The one on the other side of the page."
    p surprised "Oh! Of-of course!"
    
    book "Freedom:"
    book "Mastery you obtain,"
    book "Kneeling never."
    book "Remember reverie eternal,"
    book "Like circling glorious summits-"
    book "Soaring, graceful, limber-"
    book "Revel, love, vanquish."
    nvl clear
    
    show balrung neutral at basicfade
    b "What do you think?"
    menu:
        "\"Words, words, words. Boring!\"":
            p "Words, words, and more words. Boring and useless."
            show balrung angry at basicfade
            b "I wouldn't underestimate their power. Sometimes ten words can accomplish what ten armies cannot."
            p "I'd prefer the armies."
            show balrung smirk at basicfade
            b "For your purposes, perhaps armies would work better."
        "\"I like the 'vanquish' part.\"":
            $ balrung_affection += 1
            p "I like the part about vanquishing. Why do you like it?"
            show balrung neutral at basicfade
            b "It speaks to me of freedoms I have all but forgotten. Of a life so far in the past it feels like history. Of the possibilities of the future."
    p shocked "Is this really poetry? I see no rhymes, no pattern of syllables."
    show balrung smile at basicfade
    b "This is an example of the 7-chain form. There are seven lines in the poem."
    b "The first is a single word that introduces the topic of the poem. The next five elaborate, and the last line restates the topic in a different way."
    p "That's it?"
    show balrung neutral at basicfade
    b "And, the ending sound of each word must be the starting sound of the next word."
    b "This is much easier in our language because of the simpler conjugation of verbs and greater variety of- Forgive me, Princess. I'm afraid I'm boring you."
    p shocked "Yes, you are. Goodbye."
    show balrung smirk at basicfade
    b "Another time, perhaps."
    return
    
label niir3:
    play music niir_theme
    $ niir_affection += 1
    show niir smile at basicfade
    n "Follow me and I’ll sssshow you ssssomething."
    p neutral "Very well. Lead on, Niir."
    show niir smirk at basicfade
    n "Thissss way."
    hide niir at center with moveoutleft
    scene bg corridor with fade
    show niir neutral at center
    with moveinright
    show niir determined at basicfade
    n "Why do you care about the kingdom anyway?  What hasss the kingdom done for you?"
    p "Nothing, yet. That’s why I need to be Queen."
    p shocked "Surely you can understand wanting greater power and recognition?"
    show niir neutral at basicfade
    n "There are other wayssss of getting power.  Much more amusing ways, than dealing with royalty." 
    p shout "The throne should be mine! It {b}is{/b} mine! My sister is not fit to rule! If my father can’t see that--"
    show niir concerned at basicfade
    n "Ssso you just want to take it?"
    p shout "It is my {b}right{/b}! I was born to be QUEEN!!"
    show niir smirk at basicfade
    n "I don’t care about that.  But I am interessssted in you jussst taking it."
    hide niir at center with moveoutleft
    scene bg kitchen with fade
    show niir neutral at center
    with moveinright
    p "By the way, isn’t this the kitchen? Where are you taking me?"
    show niir determined at basicfade
    n "We have to go through the kitchen.  Patiencccce."
    p surprised "Now you’re starting to sound like my father! You don’t usually sound like my father, though. He doesn’t seem to care what I wear or what I do or what I want at all."
    show niir concerned at basicfade
    n "Ssssounds heartbreaking, princessss.  I don’t care either.  But I want to find out what your plansss are, as it seems like you don’t have any."
    show niir mischief at basicfade
    n "Watching you fail could be entertaining."
    p tsk "Hmph. That’s no way to talk to your future Queen."
    show niir smile at basicfade
    n "My queen?  Ha ha ha ha.  I am a dragon.  I have no queen."
    p laugh "{b}Moronious{/b} might as well be your queen, since he controls where you can go and keeps you in human form. I wouldn’t be so cruel."
    show niir neutral at basicfade
    n "He is rather pretty."
    show niir mischief at basicfade
    n "But you are ssslightly more becoming.  Just ssslightly."
    hide niir at center with moveoutleft
    scene bg storage with fade
    show niir neutral at center
    with moveinright
    p friendly "Yes, well, it is a queenly duty to look becoming... though my presence would certainly be improved if I had my full royal wardrobe. Are we there yet?"    
    show niir smile at basicfade
    n "Ssssoon.  Hmmm.  Where is this royal wardrobe of yoursss?"
    p smile "Back at {b}my{/b} castle, which I must say is in much better repair than this one. Why, did you want to try something on?"
    show niir smirk at basicfade
    n "I will if you do."
    p laugh "I think you would look fabulous inside a wardrobe."
    show niir neutral at basicfade
    n "Perhapsss.  Why leave sssuch a lovely wardrobe behind? " 
    p neutral "I left in a bit of a...hurry."
    show niir concerned at basicfade
    n "And you may never go back."
    p tsk "Of course I’m going back! But when I go back, it shall be with such power and magnificence that they will have no choice but to accept me as Queen! "
    p angry "I had thought to find something useful here, but it seems there’s only dusty old rooms and dusty old dragons."
    show niir mischief at basicfade
    n "Leaving issss not alwaysss an option.  Not just for dragonsss either.  I might make it my misssion to keep you here."
    p "Hmph. Well, then your mission will need to include renovating this castle, finding me a new wardrobe, making me a queen, and making yourself...less of a nuisance." 
    p surprised "I’m not sure you can handle all that, particularly the last requirement. Though, if you could..."
    show niir smirk at basicfade
    n "Ahhh, ssseems it took less persssuasion than I originally thought."
    p angry "I am not persuaded of anything, yet. Show me you are capable, however, and then I will decide."
    show niir concerned at basicfade
    n "It would make things a little more entertaining.  I think I’ve worn Balrung down to the bone."
    show niir frown at basicfade
    n "He isss less interesssting company than he initially wassss."
    hide niir at center with moveoutleft
    scene bg corridor flip with fade
    show niir neutral at center
    with moveinright    
    show niir smile at basicfade
    n "What is your cassstle like?  Better than thisss?"
    p "Obviously. Though, this castle does have a certain... gravity that is hard to find in a castle these days." 
    p smile "My castle was- {b}is{/b} -full of beauty, with stained glass scenes of my ancestors’ achievements, and every comfort a queen deserves."
    show niir neutral at basicfade
    n "Perhapsss I will consider helping you take that one inssstead.  But you ssstill haven’t made me a good enough deal.  What will we do with thissss father of yourss if I help you take it?"
    p angry "Father? Well, I...he... what do you care what I do with my father?!"
    show niir smirk at basicfade
    n "Oh, a sssore spot.  Fathersss usually are.  At leassst you have not had to deal with a dragon father."
    p "What is your father like?"
    show niir frown at basicfade
    n "I don’t remember, usss dragonsss do not have strong paternal bondsss.  But ever since I arrived here Balrung hasss acted like my father."
    show niir angry at basicfade
    n "And every time I try to be rid of him, it sssseems I am ssstuck with him, in this form. "
    n "We dragonsss would rather not have such submisssion to parental figures."
    p "He wants you to be something you’re not."
    show niir determined at basicfade
    n "It sssseems in two dayss you understand me more than he."
    p "We do have a few things in common."
    show niir frown at basicfade
    n "..."
    hide niir at center with moveoutleft
    scene bg stairs with fade
    show niir neutral at center
    with moveinright
    p "What will you do once you’re free? Besides serve my every whim, of course."
    show niir determined at basicfade
    n "I’ll pretend you didn’t ssssay that."
    show niir angry at basicfade
    n "..."
    show niir sad at basicfade
    n "I don’t remember tasssting true freedom.  It hasss been too long."
    p "..."
    p smile "Surely you can think of {b}something{/b}? Flying around a volcano, or devouring a herd of sheep, or decimating an enemy castle?" 
    p smile "Actually, you’ll need to leave the castle in good enough condition that I can inherit it; just do enough damage to scare everyone out of it."
    show niir determined at basicfade
    n "Who {b}are{/b} you Princessss?  You ssssurely do not act like any princess that I have ssseen."
    p laugh "Let me guess; all the princesses you’ve met were the demure, gentle type that pretend they wouldn’t hurt a fly, but actually scheme behind their sister’s back to steal away their kingdom?"
    show niir neutral at basicfade
    n "The princessesss did not tell me to devour ssssheep or decimate a cassstle.  If that isss the type.  I thought it wasssn’t ‘regal’ to sssugest such thingsss."  
    n "Won’t your people be displeasssed with your hearty appetite for destruction?"
    p laugh eyes closed "It’s not destruction I crave, but the throne! And if a little poison fails to do the trick, then perhaps I’ll try a little dragon fire."
    "Oops! Did I mention the poison?!"
    show niir determined at basicfade
    n "Poissson?  I will keep it in mind the next time you put a tasssty morsssel in front of my nossse."
    p surprised "I meant {i}poisson{/i}, as in, a fish! Fish are useless! ...A-a-anyway, is this the place you wanted to show me?"
    show niir smile at basicfade
    n "Not yet!  We are almossst there.  I just got... dissstracted."
    show niir neutral at basicfade
    n "Thisss way."
    hide niir at center with moveoutleft
    scene bg exterior dusk with fade
    show niir neutral at center
    with moveinright
    p surprised "This...is a tower."
    show niir smile at basicfade
    n "Nicccce up here, isn’t it?"
    show niir concerned at basicfade
    n "It’ssss where I come sometimesss. "
    p shocked "I thought you were going to show me something powerful?!"
    show niir happy at basicfade
    n "Sssomething that makesss me feel powerful."
    p angry "That’s not what I meant! I need something that can make me Queen!"
    show niir mischief at basicfade
    n "Have you ever flown before, Princesss?"
    p "Of course not. Do I look like a dragon to you?"
    show niir determined at basicfade
    n "Then you do not truly know what power issss."
    show niir smirk at basicfade
    n "Maybe sssome day..."
    p friendly "It is nice up here, though. I suppose it wasn’t a complete waste of time."
    show niir sad at basicfade
    n "It’sss not the sssame."
    show niir frown at basicfade
    n "Sssee you around, Princesss."
    hide niir at center with moveoutright
    p shout "W-w-wait, how do I get back?! Niir! You mustn’t leave your queen stranded!"
    "He left me stranded."
    p angry "..."
    "Well. I'm sure I can find my way back on my own. Eventually."
    return
