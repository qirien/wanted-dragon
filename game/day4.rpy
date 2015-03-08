label day4:
    scene bg bedroom with fade
    show princess at center with dissolve
    p "The Sceptre of Lavendorm sounds powerful, if we can find it."
    p "But it could be just a legend, or it could have been moved. I should pursue other avenues as well."
    p "Cyril has magical powers, if I could get him to use them the way I wanted."
    p "Or perhaps the dragons would aid me in exchange for their freedom?"
    p "Whose aid should I enlist?"
    menu:
        "Cyril.":
            jump cyril4
        "The dragons.":
            jump dragons4
        "I don't need help!":
            jump alone4
        
# TODO: Something about how Cyril could help her even if he can't find the scepter.        
label cyril4:
    p "Mage! Moronious!"

label dragons4:
    scene bg dungeon with fade
    show balrung at midright
    show niir at right
    with dissolve
    show princess at midleft with moveinleft
    
    b "Good morning, Princess. I trust you slept well?"
    p "That seems a silly thing to trust in. How can I sleep well when my kingdom is in the hands of a usurper?!"
    b "Well, you looked so radiant that I must have assumed it."
    p "Well, I haven't come to discuss my radiance. I've come to offer you a proposal."
    b "Really? Please continue."
    p "Cyril will release you from your curse if you fall in love, right?"
    b "And have demonstrated reform, yes."

    menu:
        "\"We can fool him.\"":
            p "We should be able to fool him easily."
            b "Yes... you may be just what we've been waiting for. "
            extend "So, how shall we convince him that you and Niir are in love, and he will trouble the other ladies no more?"
            
        "\"It won't be hard for you to love me.\"":
            p "Well, aren't you half-mad with love for me already, Niir?"
            n "What?! Love!"
            b "No, I'm afraid Niir always acts this way. But, perhaps he could learn to love you, given time."
            
    menu:
        "\"Niir, you must act as though you are in love with me.\"":
            jump niir4
                
        "\"Actually, I meant you, Balrung.\"":
            p "I think you would make a better vassal, Balrung. I have little hope that Niir could appear civilized."
            b "Princess! I'm flattered. Though I'll admit, I assumed you'd want someone..."
            n "Lessss ssscarred? Lesss ancient? More agile? More sssensual?"
            b "Yes, all of those things. I am not young, Princess."
            menu:
                "\"You're right. Niir it is.\"":
                    jump niir4
                "\"I prefer you.\"":
                    p "I am the princess!  {b}I{/b} decide who shall be my minion, and I have chosen you! Do not question my decisions."
                    b "Interesting. "
                    extend "Perhaps you would care to join me in a game of Queens and Pawns?"
                    jump balrung4
          
label balrung4:
    $ balrung_affection += 1
    p "Queens and Pawns? Is this a joke?"
    b "I can hardly think of a game more fit for someone who wishes to retake a kingdom."
    n "You should play ssstrip Queensss and Pawnssss."
    b "Niir, perhaps you would like to play against the Princess?"
    n "I do have a fine opening move... but not for Queensss and Pawnssss. I shall ssseeek better entertainment."
    hide niir with moveoutright
    b "He never was very good at this game. I thought I could teach him, but...he doesn't wish me to teach him anything."
    p "I used to play against my father; he wasn't very good, though, for I would always win. Are you any good?"
    b "I've had so few people to play against, lately, and Merlonious won't play with me anymore."
    p "Why not?"
    b "He claims he can't concentrate when Niir's around, so of course whever I challenge him to play, Niir comes to distract him."
    p "Well, I will play against you. I will go first."
    b "As you wish."
    p "There's only one thing I don't understand about this game."
    b "Only one thing?"
    p "Why are there so many queens? There should only be one queen!"
    b "Well, at the end there {b}is{/b} only one queen, yes? And whatever pawns she manages to bring with her."
    p "Still...if there's more than one, they aren't really queens. Just princesses."
    b "It must be a hard lot to be a princess."
    p "I know! So close to power, and to have it ripped away..."
    b "You know, the part I find most interesting is that in this game, there are no wizards, or knights, or sages. Merely those with power, and those used by those in power."
    p "That part, at least is true to life. Take that!"
    b "But which are you, I wonder?"
    p "Ha ha ha! Who's in power now?!"
    b "That was a daring move. Reckless, but daring. Your turn."
    p "Hmph. You only have one queen left."
    b "But I have all my pawns. Your queens are quite unguarded."
    p "The pawns are insignificant."
    b "I disagree."
    p "I only need one queen!"
    b "No, I'm afraid it won't be enough. You have no moves left."
    p "..."
    b "Thank you so much, Princess, I can't express how much I've enjoyed the chance to play against a real opponent. Perhaps you'll consider this a warm-up match and we can play a real game some other time?"
    p "A warm-up, yes...perhaps. I'm leaving now."
    b "Until next time, Princess."
    hide princess with moveoutright
    return
    
label niir4:
    $ niir_affection += 1
    n "Should I drool over you like thissss?"
    p "No, that just makes you look like a half-wit and soils my dress."
    n "You could alwaysss take off the dresss...."
    b "Niir, remember, you're trying to act as though you are in love, as though you are a reformed gentleman of a dragon who would never even think of princesses without their dresses on."

    p "Niir, you need to act like you're in love with me. You should bring me flowers, write poetry, things like that."
    n "Flowerssss in here?  We are not well stocked on flowerssss."
    p "Well, can you cook? Make something for me? We need something concrete to allow that Moronious to discover so he will believe our ruse."
    n "Cook?  Hahahahaha.  I can… roassssst.  Hehe hahaha."
    p "Heh, heh...I'm serious."
    n "Cooking?  Poetry?  Flowersss?  I’m out."
    b "Niir, isn't it worth {b}trying{/b} to regain your freedom? Surely there's some way you could show some semblance of love, or at least affection."
    n "Affection, well why didn’t you sssssay so?"
    show niir at center with move
    p "It doesn't help to do that now, you imbecile, it has to be when Cyril's watching!"
    show niir at midright
    show balrung at quarterright with move
    n "Soooo how much leeway do I get?" 
    b "Remember, you need to appear in love, not in lust... Perhaps you should practice a passionate, yet chaste embrace."
    n "Do you really think I can do that?"
    b "You must enjoy it here very much. Is it really that much of a sacrifice to embrace a beautiful princess?"
    n "Perhapssss not.  But I do not promise chassste.  That is the mage’s game."
    #todo show embrace somehow
    p "Yes, that was... That'll do. You may remove your hands now."
    n "I wassss just getting ssstarted."
    p "Can you sing? Perhaps you could compose a sonnet."
    n "Hahahaha.  You really have to sstop with these foolissssh suggestions!"
    b "Yes... that may work. Not the sonnets; you can amuse each other and laugh together."
    n "Grrr.  No one asssked for your input!"
    b "Well, then perhaps I'll leave you two alone for a bit. Though, princess, should you need me, I will be nearby. Behave yourself, Niir."
    hide balrung with moveoutleft

    n "Don’t lisssten to that crussty old dragon."
    p "Don't you have any hobbies? I mean, what do you normally do all day? Do you paint? Play sports?"
    n "Playing with the mage isss enough of a hobby for me."
    p "Well, just think of this façade as another way to trick him... But no wonder you're such a nuisance; we need to find you something else to do! Gardening? Novel reading? Hunting?"
    n "I don’t need a hobby, Princessss.  Essspecially not one of those."
    n "Though if I wasss free I would be hunting again.  Jussst not the kind of prey mossst would approve of."
    p "I suppose you'll just have to spend time with me, then. You can tell me how wonderful I am and perhaps we'll even enjoy another \"chaste embrace\"."
    n "Are you bribing me Princess?"
    p "It's not bribery if we both get something out of it. It's just a...negotiation."
    n "What ssssort of thing do {b}you{/b} like to be bribed with Princessss?"
    p "Oh, what a charming question! Powerful artifacts are always good, though I also enjoy oaths of fealty and rare poisons."
    n "I think I have ssssomething in mind."
    n "You make it too eassssy."
    p "I make what easy?"
    n "..."
    p "Niir.  I demand you- where are you going?"
    hide niir with moveoutright
    p "Niir!  Niir!"
    p "I will never understand that dragon!  Not that dragons are {i}ever{/i} to be understood."
    p "Used, yes.  But not understood."
    p "But still...  "
    extend "I wish I knew what that infernal dragon meant."
        
        
    