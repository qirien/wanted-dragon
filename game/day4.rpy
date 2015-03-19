label day4:
    scene bg bedroom dusk with fade
    p "The Sceptre of Lavendorm sounds powerful, if we can find it."
    p "But it could be just a legend, or it could have been moved. I should pursue other avenues as well."
    p "That mage has magical powers, if I could get him to use them the way I wanted."
    p "Or perhaps the dragons would aid me in exchange for their freedom?"
    p "They are all capable, but they certainly have faults. Every minion does, of course, but I need to decide who is the most likely to do what I want."
    p "Whose aid should I enlist?"
    menu:
        "The mage.":
            $ cyril_affection += 1
            jump cyril4
        "The dragons.":
            jump dragons4
        "I don't need help!":
            jump alone4
        
label alone4:
    p "In the end, the only person I can count on is myself."
    p "Perhaps I should research some more potions? That poison would have worked if it weren't for that clumsy serving maid."
    scene bg library with fade
    p "Hmm, {i}Theory of Alchemy{/i}, sounds dull. {i}Fifty Five-Minute Potions{/i}? If they only take five minutes they can't be very good. {i}Puissant Potions for Pleasure and Profit{/i}, now {b}that{/b} sounds interesting!"
    p "Ooh, they have a whole section on poisons... Slow-Acting Poison, Reversible Poison, Temporary Poison, Quasi-Death Draught..."
    p "Hmm, these ingredients aren't too rare..."
    jump cyril4
    
        
label cyril4:
    $ route = "Cyril"
    show cyril hat neutral at center with moveinleft
    c hat surprised "Ah, Princess!  I had been looking for you."
    p "Well, you clearly didn't look very hard because I've been here."
    c hat smile eyes closed blush "Ah, well, this was one of the first places that I found myself looking."
    p "What is it, mage?"
    c hat smile "Well, I have an update for you.  On the artefact."
    c hat laugh "It seems there were some notes that Dykonis left for me and those notes, they specify a location."
    c hat neutral "Not pinpoint exactly, but where we should start looking."
    p "And you're just thinking of this now?"
    c hat concerned "I've been here so long that I'd forgotten about those notes."
    p "Well, where is it?!"
    c hat surprised "As I said, it isn’t an exact location.  But it should be somewhere around the east wing.  At least that narrows our search.  Though it doesn’t help too much."
    p "Then begin searching!"
    c hat concerned blush "It’s not that simple.  We need all hands on deck, so to speak.  Well, more hands than I have presently.  And I do not trust the hands of those dragons - slippery creatures that they are.  So yes, we are short-handed when it comes to searching.  It might take months to canvas the whole area!"
    p "...I need more minions. Or perhaps simply more powerful minions. But, as there is just you, I will also search for this artifact. Direct me to the east wing!"
    c hat smile blush "That is- that is most gracious of you.  The east wing is this way, but I wouldn’t want you to do too much hard work.  If there is any lifting you need, just call me over and with a wave of my wand, I will remove the item obstructing your search."
    window hide
    scene bg corridor with slowfade
    scene bg storage with slowfade
    scene bg hall with slowfade
    scene bg closet with slowfade
    window show
    "We searched through bedrooms, storerooms, halls, and closets."
    p "This is pointless! We are no closer than we were three hours ago!"
    show cyril hat neutral at center with moveinleft
    c hat concerned "Well, now we know several hundred places the scepter is not."
    p "And several million places it still could be. Find a better way to search! Isn’t this what magic is for?!"
    c hat surprised "Magic can’t- well, there {b}are{/b} summoning spells, but I do not think we know enough about this scepter for those to work."
    p "Then find out more! While I am perfectly willing to waste your time, mine is much more valuable. I am done here."
    
    return

label dragons4:
    scene bg dungeon with fade
    show balrung neutral at midleft
    show niir neutral at midright
    with dissolve
    
    b smile "Good morning, Princess. I trust you slept well?"
    p "That seems a silly thing to trust in. How can I sleep well when my kingdom is in the hands of a usurper?!"
    b smirk "Well, you looked so radiant that I must have assumed it."
    p "Well, I haven't come to discuss my radiance. I've come to offer you a proposal."
    b neutral "Really? Please continue."
    p "That mage will release you from your curse if you fall in love, right?"
    b angry "And have demonstrated reform, yes."

    menu:
        "\"We can fool him.\"":
            p "We should be able to fool him easily."
            b smile "Yes... you may be just what we've been waiting for. "
            b smirk "So, how shall we convince him that you and Niir are in love, and he will trouble the other ladies no more?"
            
        "\"It won't be hard for you to love me.\"":
            p "Well, aren't you half-mad with love for me already, Niir?"
            n determined "Mad, yessss. Cccertainly not love!"
            b smile eyes closed "No, I'm afraid Niir always acts this way. But, perhaps he could learn to love you, given time."
            p "I don't have that much time."
            
    menu:
        "\"Niir, you must act as though you are in love with me.\"":
            p "Niir, you must act as though you are in love with me."
            jump niir4
                
        "\"Actually, I meant you, Balrung.\"":
            p "I think you would make a better vassal, Balrung. I have little hope that Niir could appear civilized."
            b smile blush "Princess! I'm flattered. Though I'll admit, I assumed you'd want someone..."
            n mischief "Lessss ssscarred? Lesss ancient? More agile? More sssensual?"
            b neutral "Yes, all of those things. I am not young, Princess."
            menu:
                "\"You're right. Niir it is.\"":
                    p "Perhaps you are right... Niir can you act as though you are in love with me?"
                    jump niir4
                "\"I prefer you.\"":
                    p "I am the princess!  {b}I{/b} decide who shall be my minion, and I have chosen you! Do not question my decisions."
                    show niir determined with dissolve
                    b smirk "Interesting. "
                    extend "Perhaps you would care to join me in a game of Queens and Pawns?"
                    jump balrung4
          
label balrung4:
    $ balrung_affection += 1
    $ route = "Balrung"
    p "Queens and Pawns? Is this a joke?"
    b smile "I can hardly think of a game more fit for someone who wishes to retake a kingdom."
    n mischief "You should play ssstrip Queensss and Pawnssss."
    b smile eyes closed "Niir, perhaps you would like to play against the Princess?"
    n smirk "I do have a fine opening move... but not for Queensss and Pawnssss. I shall ssseeek better entertainment."
    hide niir with moveoutright
    b neutral "He never was very good at this game. I thought I could teach him, but...he doesn't wish me to teach him anything."
    p "I used to play against my father; he wasn't very good, though, for I would always win. Are you any good?"
    b determined "I've had so few people to play against, lately, and Merlonious won't play with me anymore."
    p "Why not?"
    b smirk "He claims he can't concentrate when Niir's around, so of course whever I challenge him to play, Niir comes to distract him."
    p "Well, I will play against you. I will go first."
    b neutral "As you wish."
    p "There's only one thing I don't understand about this game."
    b smile "Only one thing?"
    p "Why are there so many queens? There should only be one queen!"
    b neutral "Well, at the end there {b}is{/b} only one queen, yes? And whatever pawns she manages to bring with her."
    p "Still...if there's more than one, they aren't really queens. Just princesses."
    b smirk "It must be a hard lot to be a princess."
    p "I know! So close to power, and to have it ripped away..."
    b determined "You know, the part I find most interesting is that in this game, there are no wizards, or knights, or sages. Merely those with power, and those used by those in power."
    p "That part, at least is true to life. Take that!"
    b smirk "But which are you, I wonder?"
    p "Ha ha ha! Who's in power now?!"
    b neutral "That was a daring move. Reckless, but daring. Your turn."
    p "Hmph. You only have one queen left."
    b smile "But I have all my pawns. Your queens are quite unguarded."
    p "The pawns are insignificant."
    b smile eyes closed "I disagree. Your move."
    p "I only need one queen!"
    b smirk "No, I'm afraid it won't be enough. You have no moves left."
    p "..."
    b smile eyes closed "Thank you so much, Princess, I can't express how much I've enjoyed the chance to play against a real opponent. Perhaps you'll consider this a warm-up match and we can play a real game some other time?"
    p "A warm-up, yes...perhaps. I'm leaving now."
    b smirk "Until next time, Princess."
    return
    
label niir4:
    $ niir_affection += 1
    $ route = "Niir"
    n mischief "Should I drool over you like thissss?"
    p "No, that just makes you look like a half-wit and soils my dress."
    n smirk "You could alwaysss take off the dresss...."
    b neutral "Niir, remember, you're trying to act as though you are in love, as though you are a reformed gentleman of a dragon who would never even think of princesses without their dresses on."

    p "Yes, you should bring me flowers, write poetry, things like that."
    n determined "Flowerssss in here?  We are not well stocked on flowerssss."
    p "Well, can you cook? Make something for me? We need something concrete to allow that Moronious to discover so he will believe our ruse."
    n mischief "Cook?  Hahahahaha.  I can... roassssst.  Hehe hahaha."
    p "Heh, heh...I'm serious."
    n angry "Cooking?  Poetry?  Flowersss?  I’m out."
    b determined "Niir, isn't it worth {b}trying{/b} to regain your freedom? Surely there's some way you could show some semblance of love, or at least affection."
    n smirk "Affection, well why didn’t you sssssay so?"
    show niir neutral at come_closer with dissolve
    p "It doesn't help to do that now, you imbecile, it has to be when Moronious is watching!"
    show niir neutral at reset_zoom with dissolve
    n mischief "Soooo how much leeway do I get?" 
    b smirk "Remember, you need to appear in love, not in lust... Perhaps you should practice a passionate, yet chaste embrace."
    n determined "Do you really think I can do that?"
    b determined "You must enjoy it here very much. Is it really that much of a sacrifice to embrace a beautiful princess?"
    n neutral "Perhapssss not.  But I do not promise chassste.  That is the mage’s game."
    show niir smirk at come_closer with dissolve
    #todo show embrace somehow
    p "Yes, that was... That'll do. You may remove your hands now."
    show niir determined at reset_zoom with dissolve
    n mischief "I wassss just getting ssstarted."
    p "Can you sing? Perhaps you could compose a sonnet."
    n happy "Hahahaha.  You really have to sstop with these foolissssh suggestions!"
    b smirk "Yes... that may work. Not the sonnets; you can amuse each other and laugh together."
    n determined "Grrr.  No one asssked for your input!"
    b smile eyes closed "Well, then perhaps I'll leave you two alone for a bit. Though, princess, should you need me, I will be nearby. Behave yourself, Niir."
    hide balrung with moveoutleft
    show niir at center with move
    n determined "Don’t lisssten to that crussty old dragon."
    p "Don't you have any hobbies? I mean, what do you normally do all day? Do you paint? Play sports?"
    n smirk "Playing with the mage isss enough of a hobby for me."
    p "Well, just think of this façade as another way to trick him... But no wonder you're such a nuisance; we need to find you something else to do! Gardening? Novel reading? Hunting?"
    n concerned "I don’t need a hobby, Princessss.  Essspecially not one of those."
    n neutral "Though if I wasss free I would be hunting again.  Jussst not the kind of prey mossst would approve of."
    p "I suppose you'll just have to spend time with me, then. You can tell me how wonderful I am and perhaps we'll even enjoy another \"chaste embrace\"."
    n mischief "Are you bribing me, Princess?"
    p "It's not bribery if we both get something out of it. It's just a...negotiation."
    n smile "What ssssort of thing do {b}you{/b} like to be bribed with Princessss?"
    p "Oh, what a charming question! Powerful artifacts are always good, though I also enjoy oaths of fealty and rare poisons."
    n smirk "I think I have ssssomething in mind."
    n mischief "You make it too eassssy."
    p "I make what easy?"
    n happy "..."
    p "Niir.  I demand you- where are you going?"
    hide niir with moveoutright
    p "Niir!  Niir!"
    p "I will never understand that dragon!  Not that dragons are {i}ever{/i} to be understood."
    p "Used, yes.  But not understood."
    p "But still...  "
    extend "I wish I knew what that infernal dragon meant."
    return
        
    