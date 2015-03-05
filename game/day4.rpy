label day4:
    scene bg bedroom with fade
    show princess at center with dissolve
    p "The Sceptre of Lavendorm sounds powerful, if we can find it."
    p "But it could be just a legend, or it could have been moved. I should pursue other avenues as well."
    p "Cyril has some power, if I could get him to use it the way I wanted."
    p "Perhaps the dragons would aid me in exchange for their freedom?"
    
    p "Whose aid should I enlist?"
    menu:
        "Cyril.":
            jump cyril4
        "The dragons.":
            jump dragons4
        "I don't need help!":
            jump alone4
        
        
label cyril4:
    p "Ohhhh Cyril!"
    p "How are you going at getting that scepter for me?"
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
    c "I do wonder what it is that you plan to do with such a scepter however, because I'm sure that it can only be wielded by a powerful mage."
    p "Then you will become more useful too me than ever."
    p "Wouldn't you want that?"
    c "I-I suppose it wouldn't be the worst thing, your majesty."
    
    

label dragons4:
    scene bg dungeon with fade
    show balrung at midleft
    show niir at left
    with dissolve
    show princess at midright with moveinright
    
    b "Good morning, Princess. I trust you slept well?"
    p "That seems a silly thing to trust in. How can I sleep well when my kingdom is in the hands of a usurper?!"
    b "Well, you looked so radiant that I must have assumed it."
    n "And by radiant, he meansss radiating a ssstench. Haven't you heard of bathing?"
    p "I have more important things to worry about. Though I do love a good bath."
    n "I know."
    p "!!"
    b "Most princesses do, is what he meant to say. Really, Niir, she might suspect you were engaged in untoward behavior."
    p "Well, I haven't come to discuss bathing. I've come to offer you a proposal."
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
        "\"Niir, you must act as though you are in love me.\"":
            jump niir_pretend_love
                
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
    b "He never was very good at this game. I thought I could teach him, but..."
    p "I used to play against my father; he wasn't very good, though, I would always win. Are you any good?"
    b "It's hard to say; I've had so few people to play against. Merlonious won't play with me anymore."
    p "Why not?"
    b "He claims he can't concentrate when Niir's around, so of course whever I challenge him to play, Niir comes to distract him."
    p "Well, I will play against you."
    b "Wonderful! Just a friendly game, of course."
    p "I don't do friendly games."
    b "Of course not! I merely meant that we don't need any stakes for winning or losing."
    p "Very well. You may go first."
    b "All right. There."
    p "There's only one thing I don't understand about this game."
    b "Only one thing?"
    p "Why are there so many queens? There should only be one queen!"
    b "Well, at the end there {b}is{/b} only one queen, yes? And whatever pawns she manages to bring with her."
    p "Still...if there's more than one, they aren't really queens. Just princesses."
    b "It must be a hard lot to be a princess."
    p "I know! So close to power, and to have it ripped away..."
    b "You know, the part I find most interesting is that in this game, there are no wizards, or knights, or sages. Merely those with power, and those used by those in power."
    p "That part, at least is accurate. Take that!"
    b "But which are you?That was a daring move. Reckless, but daring. Your turn."
    p "Who's in power now?!"
    b "We shall see."
    p "Hmph. You only have one queen left."
    b "But I have all my pawns. Your queens are quite unguarded."
    p "The pawns are insignificant."
    b "I disagree."
    p "I only need one queen!"
    b "No, I'm afraid it won't be enough. There."
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
    p "Niir, you should..."
    # TODO: Let's roleplay this part?  Niir is snide and bratty and doesn't want to participate, but Balrung says he'll come around?
    menu:
        "\"Write me poetry\"":
            p "You should write a poem suitable to discuss the multitude of reasons why I should be Queen."
        "Give me presents":
            p "You should bring me a gift suitable for my royal station."
        "Sing to me":
            p "You should sing a sonnet fit to describe my beauty, wit, and charm."

p "Niir, you need to act like you're in love with me. You should bring me flowers, write poetry, things like that."
n "Flowerssss in here?  We are not well stocked on flowerssss.”
p " Well, can you cook? Make something for me? We need something concrete to allow that Moronious to discover so he will believe our ruse."
n “Cook?  Hahahahaha.  I can… roassssst.  Hehe hahaha.”
p "Heh, heh...I'm serious."
n “Cooking?  Poetry?  Flowersss?  I’m out.”
b "Niir, isn't it with trying to regain your freedom? Surely there's some way you could show some semblance of love, or at least affection."
n “Affection, well why didn’t you sssssay so?”
#todo show Niir at center with move
[I could imagine him getting all up in her face here, however we want to put that in the script]
p "It doesn't help to do that now, you imbecile, it has to be when Cyril's watching!"
n “Soooo how much leeway to I get?” 
b "Remember, you need to appear in love, not in lust... Perhaps you should practice a passionate, yet chaste embrace."
n “Do you really think I can do that?”
n “I’m out.”
b "You must enjoy it here very much. Is it really that much of a sacrifice to embrace a beautiful princess?"
n “Perhapssss not.  But I do not promise chassste.  That is the mage’s game.”
#todo show embrace somehow
p "Yes, that was... That'll do. You may remove your hands now."
n “I wassss just getting ssstarted.”
p "Can you sing? Perhaps you could compose a sonnet."
n “Hahahaha.  You really have to sstop with these foolissssh suggestions!”
b "Yes... that may work. Not the sonnets; you can amuse each other and laugh together."
n “Grrr.  No one asssked for your input!”
b "Well, then perhaps I'll leave you two alone for a bit. Though, princess, should you need me, I will be nearby. Behave yourself, Niir."
#hide balrung with moveoutleft

n “Don’t lisssten to that crussty old dragon.”
p "Don't you have any hobbies? I mean, what do you normally do all day? Do you paint? Play sports?"
n “Playing with the mage isss enough of a hobby for me.”
p "Well, just think of this façade as another way to trick him... But no wonder you're such a nuisance; we need to find you something else to do! Gardening? Novel reading? Hunting?"
n “I don’t need a hobby Princessss.  Essspecially not one of those.”
n “Though if I wasss free I would be hunting again.  Jussst not the kind of prey mossst would approve of.”
p "I bet you would enjoy a good theatrical performance."
n “The theatre?  I’m not that bored.”
p "I suppose you'll just have to spend time with me, then. You can tell me how wonderful I am and perhaps we'll even enjoy another "chaste embrace"."
n “Are you bribing me Princess?”
p "Bribery is underrated."
n “It issss.  What ssssort of thing do you like to be bribed with Princessss?”
p "Oh, what a charming question! Powerful artifacts are always good, though I also enjoy oaths of fealty and rare poisons."
n “I think I have ssssomething in mind.”
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
    
    
    
    
    
###### DAY 5
if niir_love:
    p "Could you stop disappearing on me Niir!"
    p "I wish to confer with you!"
    n "Confer?  On what?  Your choice of dresssss?"
    p "No.  Let's get on the same page here."
    p "The pretence!  The acting like you're in love with me!"
    p "How are we faring?"
    p "Why don't you just tell that Moronious already that you want to leave with me."
    p "And start a happily ever after of such."
    n "I haven't been convinccccced."
    p "You say that every time!  I can promise you freedom, destruction and power."
    p "Isn't that enough?"
    n "Dragonsss aren't that easssy to trussst, Princesssss."
    p "Haven't I told you not to stare at me like tha-oh, you can't help it.  Can you?"
    p "That's the way you always look."
    p "Regardless Niir.  I can promise you what you want."
    n "What if I want more?"
    p "More?"
    n "Perhapsss."
    p "What more is there?"
    n "Isssn't it obvioussss?"
    p "You mean?  No.  Absolutely not.  "
    extend "Especially not to you."
    n "You wound me Princessss."
    p "And why should I trust you?"
    n "Assss you ssssee.  Trusssst is not easssy, isss it?"
    p "How can I get you to trust me?"
    n "I won't trussst you, until you trusssst me."
    p "..."
    p "I see how it is."
    menu:
        "Do a trust fall.":
            jump trustfall
        "Offer to show him some thigh.":
            jump somethigh 
        "Tell him you're just not that committed to getting him on board.":
            jump {other route?}
            
label somethigh:
    p "Alright.  Fine."
    p "I'll show you some of mine if you show me some of yours."
    p "Trust."
    n "I thought you'd never offer."
    scene black
    p "Happy now?"
    n "Happy wouldn't be the word that I would ussssse."
    
    
    
label cyril5:
    
    c "Ah, Princess!  I had been looking for you."
    p "Well, you clearly didn't look very hard because I've been here."
    c "Ah, well, this was one of the first places that I found myself looking."
    p "What is it mage?"
    c "Well, I have an update for you.  On the artefact."
    c "It seems there were some notes that --- left for me and those notes, they specify a location."
    c "Not pinpoint exactly, but where we should start looking."
    p "And you're just thinking of this now?"
    c "I've been here so long that I'd forgotten about those notes."
    #TO DO: TBC
    
    ALSO
    ###{I thought about a scene between Balrung and Niir that the princess overhears)
    
if niir_love:
    b "You have fallen in love with the tempestuous temptress that has entered our realm."
    n "Now why would you ssssssay that?"
    b "I have seen it happen many times before."
    b "I can tell the signs."
    n "Love is not ssssomething that I am aquainted with, old dragon."
    n "Ssstop your posssstulating."
    b "I'm no more happy about this than you are, Niir.  You are all what little entertainment I have in this dreary place."
    b "If I could keep you here, I would."
    n "Your fearssss are ridiculousssss."
    b "Ah, yes.  I could let her just leave and you be miserable."
    b "And then I'll will have you here, but no peace."
    n "I am sssstaying here, old dragon."
    b "Then you are foolish.  What is for you here?"
    b "What other princesses are there?"
    p "(Could Balrung be right?  Could Niir actually be... {i}in love{/i}?)"
    p "(The thought sickens me to my stomach.)"
    p "(Though I have to admit, there is some sort of animal magnatism toward Niir.)"
    p "(Even if it is only animal.)"
    n "Sssshut up.  I am done conversssssing."
    b "Think about what I said.  I'd say to follow your heart."
    b "But we both know that isn't possible."
    p "(This is what I wanted, wasn't it?)"
    p "(A dragon at my disposal.  Willing to leave, all for the delusion of love.)"
    p "(But somehow, I am not content.  What is this?)"
