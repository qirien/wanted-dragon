#################################################
# Niir Route endings
#

# Definitely True Love
label niir_free_epilogue:
    scene bg kingdom with fade
    show niir neutral at center, basicfade with moveinright
    p "Oh, Niir. You're back."
    show niir smirk at basicfade
    n "Yessss, I deccccided to gracce you with my pressenccce."
    p "I'd hardly call {b}that{/b} landing graceful."
    show niir smile at basicfade
    n "Did you misss me?"
    p "Miss you? It has been several months...I was wondering when you'd come around again. You're supposed to bow to the Queen, you know."
    show niir neutral at basicfade
    n "Of courssse, your Majesssty."
    p "Well! Is it possible you've learned some manners during your journeys? Impressive!"
    show niir smirk at basicfade
    n "Only for you, your Majesssty."
    p "Now, now, I don't believe a word of that. What's her name?"
    show niir mischief at basicfade
    n "There issss only one I would fly to ssspend time with."
    p "Awww, how sweet of you! You at least know how to tell me what I like to hear."
    show niir concerned at basicfade
    n "Asss long as I ssstill have a placcce here."
    p "Of course! Sit down; I'll send for some stewed rabbit and you can tell me all about your travels."
    show niir mischief at basicfade
    n "I’d rather ssshow you about my travelsss."
    p "Oh, Niir, you're all talk. You wouldn't dare-"
    "But I didn't get to say any more as he reached back and retrieved something feathery and floppy and plopped it into my arms."
    p "What is this?!"
    show niir smirk at basicfade
    n "It'ssss called a \"duck\"."
    p "What...does it do? Is it good to eat?"
    show niir neutral at basicfade
    n "Perhapssss, but not thisss one.  Thiss isss Chryssie."
    p "You named this bird. After me."
    n "..."
    p "Well. "
    extend "I'm not sure whether to be jealous or flattered."
    n "Sssso, how many people have you sssentenced to the dungeons thisss passt month?"
    p "Not nearly enough. Everyone's too scared to misbehave around here."
    n "I’m not ssscared to misssbehave.  Perhapsss I ssshould make up for the lack of misssbehavior around here."
    p "That's what I'm counting on."
    
    $persistent.DefinitelyTrueLove = True
    scene black with veryslowfade
    return 
    
# Never Too Late    
label niir_asleep_epilogue:
    scene bg woods with fade
    play music niir_theme
    "I jabbed Niir again, but all I got out of him was the soft sound of him breathing."
    p "Niir!  I’m warning you.  You have been asleep for two weeks!  You have made me miss my sister’s coronation.  You will pay for that, I assure you."
    p "And what’s worse is that I’ve been out here.  Miserable.  Having to get food for myself!"  
    p "Foraging, Niir.  Foraging!  All because you are a useless dragon who won’t WAKE UP!"
    p "I can’t believe I even freed you, you know.  To think that I almost deluded myself that I lo-"
    p "Wait.  You’re moving?"
    show niir frown at center,squatting with moveinbottom
    p "Niir?"
    show niir sad at standing with move
    n "Ughhhhh."
    p "You have to make up for this, Niir.  We have lost time to gain back.  Time in which I should have been queen."
    show niir determined at basicfade
    n "My head.  It hurtsssss."
    p "Do stop your complaining.  You left me out here to starve." 
    p "A princess is not supposed to do everything herself; that's why I brought you along! But I guess at least I survived."
    p "Now turn into your dragon form so we can go and storm my father’s castle!"
    show niir concerned at basicfade
    n "Eggghh."
    p "Quickly now.  Time awaits!"
    show niir smirk at basicfade
    n "I need to resssst.  I think I’ll jusssst lay here a little longer."
    p "Oh, no Niir.  Enough resting.  It’s time for you to get moving." with hpunch
    show niir frown at basicfade
    n "If I could, Princessss.  But I need to resssst."
    show niir frown
    p "If I have to go one more day without my-"
    hide niir with moveoutbottom
    n "{i}zzz{/i}."
    p "Niir!  NIIR!  I will not stand for this, Niir.  You must serve your queen!"
    p "You owe me for this, dragon."
    
    $persistent.NeverTooLate = True
    scene black with veryslowfade
    return
