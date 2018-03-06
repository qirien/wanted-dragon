#################################################
# Niir Route endings
#

# Definitely True Love
label niir_free_epilogue:
    scene bg kingdom with fade
    show niir neutral at center, basicfade with moveinright
    p surprised "Oh, Niir. You're back."
    show niir smirk at basicfade
    n "Yessss, I deccccided to gracce you with my pressenccce."
    p smile "I'd hardly call {b}that{/b} landing graceful."
    show niir smile at basicfade
    n "Did you misss me?"
    p friendly "Miss you? It has been several months...I was wondering when you'd come around again. You're supposed to bow to the Queen, you know."
    show niir neutral at squatting with move
    show niir neutral at standing with move
    n "Of courssse, your Majesssty."
    p smile "Well! Is it possible you've learned some manners during your journeys? Impressive!"
    show niir smirk at basicfade
    n "Only for you, your Majesssty."
    p tsk "Now, now, I don't believe a word of that. What's her name?"
    show niir mischief at basicfade
    n "There issss only one I would fly to ssspend time with."
    p smile "Awww, how sweet of you! You at least know how to tell me what I like to hear."
    show niir concerned at basicfade
    n "Asss long as I ssstill have a placcce here."
    p friendly "Of course! Sit down; I'll send for some stewed rabbit and you can tell me all about your travels."
    show niir mischief at basicfade
    n "I’d rather ssshow you about my travelsss."
    p laugh "Oh, Niir, you're all talk. You wouldn't dare-"
    "But I didn't get to say any more as he reached back and retrieved something feathery and floppy and plopped it into my arms."
    p surprised "What is this?!"
    show niir smirk at basicfade
    n "It'ssss called a \"duck\"."
    p shocked "What...does it do? Is it good to eat?"
    show niir neutral at basicfade
    n "Perhapssss, but not thisss one.  Thiss isss Chryssie."
    p surprised "You named this bird. After me."
    n "..."
    p smile "Well. "
    extend "I'm not sure whether to be jealous or flattered."
    n "Sssso, how many people have you sssentenced to the dungeons thisss passt month?"
    p tsk "Not nearly enough. Everyone's too scared to misbehave around here."
    n "I’m not ssscared to misssbehave.  Perhapsss I ssshould make up for the lack of misssbehavior around here."
    p smile "That's what I'm counting on."
    
    $persistent.DefinitelyTrueLove = True
    scene black with veryslowfade
    return 
    
# Never Too Late    
label niir_asleep_epilogue:
    scene bg woods with fade
    "I jabbed Niir again, but all I got out of him was the soft sound of him breathing."
    p angry "Niir!  I’m warning you.  You have been asleep for two weeks!  You have made me miss my sister’s coronation.  You will pay for that, I assure you."
    p tsk "And what’s worse is that I’ve been out here.  Miserable.  Having to get food for myself!"  
    p shout "Foraging, Niir.  Foraging!  All because you are a useless dragon who won’t WAKE UP!"
    p angry "I can’t believe I even freed you, you know.  To think that I almost deluded myself that I lo-"
    p surprised "Wait.  You’re moving?"
    show niir frown at center,squatting with moveinbottom
    p "Niir?"
    show niir sad at standing with move
    n "Ughhhhh."
    p tsk "You have to make up for this, Niir.  We have lost time to gain back.  Time in which I should have been Queen."
    show niir determined at basicfade
    n "My head.  It hurtsssss."
    p angry "Do stop your complaining.  You left me out here to starve." 
    p tsk "A princess is not supposed to do everything herself; that's why I brought you along! But I guess at least I survived."
    p shout "Now turn into your dragon form so we can go and storm my father’s castle!"
    show niir concerned at basicfade
    n "Eggghh."
    p shout "Quickly now.  Time awaits!"
    show niir smirk at basicfade
    n "I need to resssst.  I think I’ll jusssst lay here a little longer."
    p tsk "Oh, no Niir.  Enough resting.  It’s time for you to get moving." with hpunch
    show niir frown at basicfade
    n "If I could, Princessss.  But I need to resssst."
    show niir frown
    p angry "If I have to go one more day without my-"
    hide niir with moveoutbottom
    n "{i}Zzzzz{/i}."
    p shout "Niir!  NIIR!  I will not stand for this, Niir.  You must serve your Queen!"
    p tsk "You owe me for this, dragon."
    scene cg2 with veryslowfade
    $ renpy.pause()
    
    $persistent.NeverTooLate = True
    scene black with veryslowfade
    return
