label day1:
    scene bg bedroom dusk with fade
    play music niir_theme
    p "What a terrible start to a day; I'm still not queen."
    p "But that's why I came here; to remedy that."
    p "Dragons are supposed to be powerful, and I need more power. I should talk to them without that mage around; maybe they can tell me more."
    scene bg dungeon with fade
    n "Ssssomething tasssty comes!"
    p "Ahem. Dragons? I wish to speak with you!"
    show niir neutral at midright
    show balrung neutral at midleft
    with moveinright
    show balrung smirk at basicfade
    b "Princess [p_name]. To what do we owe this great honor?"
    show niir mischief at basicfade
    n "Yesss, it's a pleasure..."
    p "I'm sure. Anyway, I am seeking loyal vassals to aid me in reclaiming my throne from my evil sister. Do you accept?"
    show niir angry at basicfade
    n "Vasssssals? We are no sssuch thing."
    show balrung neutral at basicfade
    b "Princess, our powers are extremely limited whilst we are held captive here."
    p "I thought all you had to do was kiss a human or something, and the spell would be broken."
    show niir mischief at basicfade
    n "If that were the casssse, I'd have kissssed you firssst and asked questionssss later."
    show balrung angry at basicfade
    b "Yes, it's not quite that simple. You see, Merlonious will only release a dragon from captivity if he proves that he has found \"love\" and is reformed."
    p "Couldn't we overpower him? He doesn't seem that formidable..."
    show balrung smirk at basicfade
    b "He possesses powerful magic, and our powers are dormant because of the curse. So, unless you are a sorceress...?"
    p "I am not. But I am interested in powerful magical objects and alchemical recipes. Do you know of any?"
    show balrung neutral at basicfade
    b "There are many arcane tomes in the library that might describe such things. I have not read them, as they would be of little use to dragons."
    p "Then I will seek out the library."
    jump library1
    
    
label library1:
    scene bg library with fade
    play music cyril_theme
    show cyril hat concerned at center, basicfade
    "It appears the library is already occupied..."
    show cyril hat concerned eyes closed at basicfade
    c "I know this was you Niir!"
    "{i}He he he, ha ha ha...{/i}"
    show cyril hat angry at basicfade
    c "And you mark my words!  I will stop you, I will!"
    show cyril hat concerned at basicfade
    c "As soon as I find that proper spellbook!"
    "This completely ruins my plans.  But perhaps I could turn it to my advantage?"
    p "Doing some reading?"
    show cyril hat surprised with hpunch
    c "Yah!"
    "He dropped the book like it was a hot potato."
    c "Princess.  Yes, well I..."
    p "Let me get that."
    p "{i}15 Erotic Tales by Twilight{/i}."
    p "You were reading {i}this{/i}?"
    "I know he wasn't really, but sometimes he makes it too easy."
    p "You'll have to read me the good parts, I'm ever so curious."
    show cyril hat concerned blush at basicfade
    c "No, no.  Niir.  "
    extend "He's just having a joke."
    show cyril hat concerned at basicfade
    c "We joke together all the time.  Ha ha ha."
    show cyril hat angry at basicfade
    c "Hilarious dragon that he is."
    show cyril hat concerned at basicfade
    c "Well, anyway.  I must find my spellbook.  My real spellbook."
    show cyril hat concerned blush at basicfade
    c "Not.. this."
    p "I'm not sure, I think {i}15 Erotic Tales by Twilight{/i} could cast a completely different kind of spell."
    show cyril hat concerned eyes closed blush at basicfade
    c "..."
    show cyril hat concerned blush at basicfade
    c "Have you been talking with {i}him{/i} perchance?  Is this all part of the joke?"
    p "Of course it is.  This life is all one big joke at your expense, Moronious."
    show cyril hat angry at basicfade
    c "Merlonious.  Cyril Merlonious."
    p "Anyways, I came by for a some research, but if you are busy reading erotic tales, I will let you be."
    show cyril hat smile at basicfade
    c "I'm not busy- not at all!"
    show cyril hat laugh at basicfade
    c "Please, do spend time with me.  I mean, what are you looking for?  I will always be a helpful librarian."
    show cyril hat smile blush at basicfade
    c "Err, mage.  Librarian-mage type person."
    p "You {i}are{/i} odd Moronious."
    p "I suppose I will let you help me, if you promise not to be irritating."
    show cyril hat neutral at basicfade
    c "I think I can manage."
    p "Good.  Now direct me to a book outlining powerful artifacts in this vicinity."
    show cyril hat surprised at basicfade
    c "In this vicinity?  Whyever would you-"
    p "You're starting to irritate me."
    show cyril hat neutral at basicfade
    c "Oh, of course - of course.  The book.  Well, there has been something around here.  Old and dusty and-"
    show cyril hat laugh at basicfade
    c "Quite like the dragons in fact!"
    p "Are you trying to be witty, mage?"
    show cyril hat concerned blush at basicfade
    c "Not very hard.  It only just came to me really."
    p "Well, don't."
    show cyril hat smile at basicfade
    c "This is what I was looking for.  {i}Long-Hidden Powerful Objects: an abridged edition{/i}."
    show cyril hat concerned at basicfade
    c "It's really the best I could do at such short notice."
    p "While it is quite pitiful that you don't have more research materials in this castle of yours, I suppose this will have to do."
    show cyril hat laugh at basicfade
    c "Great! Now if I can be of any-"
    p "Begone!"
    show cyril hat smile blush at basicfade
    c "Alright, I'll just gather up my-"
    p "Begone with you!"
    show cyril hat concerned blush eyes closed at basicfade
    c "Good day Princess, I will just be seeing myself out."
    hide cyril with moveoutleft
    "I thought he'd never leave.  Now, what have we here..."
    play sound "sfx/flippage.ogg"
    "A hedge-trimming sword? Useless. Sleeping perfume? Possibly useful, but not what I'm looking for. Elixir of Youth? I'm already young and beautiful; I don't need that."
    "This one is quite curious.  This part here."
    stop sound fadeout 1.0
    book "{size=50}The Scepter of Lavendorm{/size}"
    book "Though it has not been located in centuries, this powerful artifact is rumored to reside in [castle_name].\n"
    book "Some claim it has the power to break enchantments, while others point to its use by royal families as a symbol of authority, and perhaps protection from assassination.\n"
    book "Ancient texts describe it as being encrusted with emeralds and emanating a palpable magical aura."
    nvl clear
    p "How... curious."
    p "Well, I may as well find out more about it."
    p "The Scepter of Lavendorm."
    p "Hmmm..."
    
    menu:
        "Ask Moronious about it.":
            $ asked_scepter = "Cyril"
            jump sharecyril
        "Ask Balrung about it.":
            $ asked_scepter = "Balrung"
            jump sharebalrung
        "Search for it on your own":
            jump explore1
       
label sharebalrung:
    play music evil_theme
    $ balrung_affection += 1
    p "Back down to the dungeons, again. This castle is much too large for the few people that live here."
    scene bg dungeon with fade
    show balrung neutral at center, basicfade
    show balrung smirk at basicfade
    b "Back so soon?"
    p "Yes, I've found something that might help. What do you know of the Scepter of Lavendorm?"
    
label balrung_scepter:
    show balrung determined at basicfade
    b "No one has been able to find it. It is presumed lost, and, as its powers are unknown, no one lately has looked very hard."
    p "Yes, the book said as much. Where is it?"
    show balrung angry at basicfade
    b "Perhaps that's why she chose this place..."
    p "What? She who?"
    show balrung neutral at basicfade
    b "Never mind. I believe it is still here. I've felt latent power within the walls of the castle, but assumed it was just the binding curse."
    p "Interesting...could you pinpoint a certain location where that feeling is strongest?"
    show balrung smirk at basicfade
    b "The feeling is not constant or consistent; but if I detect it again I shall inform you."
    p "Very good, Balrung."
    return
       
label sharecyril:
    play music evil_theme    
    $ cyril_affection += 1
    p "Oh, Moronious~."
    p "That foolish mage has to be around here somewhere."
    scene bg corridor with fade
    p "Where {i}are{/i} you, foolish mage?"
    show cyril hat neutral at center with flash #TODO: with some flash-bang transition
    play sound "sfx/lightning.ogg"
    show cyril hat surprised at basicfade
    c "You called, your highness?"
    p "I am already quite aware that you are a magic wielder. Please do not just appear like that in the future."
    show cyril hat neutral at basicfade
    c "Oh, I'm sorry.  I overheard that you were looking for me, and I just wanted to help-"
    p "But I do have something rather curious to share with you, so you must come with me."
    show cyril hat smile blush at basicfade
    c "I would come with you anywhere, your Highness."
    hide cyril with moveoutright
    scene bg library with fade
    show cyril hat neutral at center with moveinleft
    show cyril hat surprised at basicfade
    c "So what is it that you wish to show me?"
    p "This illustration of a scepter.  The Scepter of Lavendorm.  Is it real?"
    show cyril hat neutral at basicfade
    c "Oh yes, it was real.  Once.  No one has seen it in quite some time."
    p "And this mentor of yours that put you in charge, he must have been centuries old.  Did he ever see it?"
    show cyril hat surprised at basicfade
    c "Well, I don't know about centuries..."
    show cyril hat concerned at basicfade
    c "He {b}might{/b} have said there was a powerful but uncontrollable magic that I shouldn't go looking for."
    show cyril hat surprised at basicfade
    c "But I thought he was just joking with me.  Although come to think of it, he wasn't really the joking type."
    p "So did he say {i}where{/i} not to go looking for it?"
    show cyril hat concerned at basicfade
    c "Not specifically, but he did say it was bound up with special magic somewhere within these walls."
    p "And you didn't think to mention this earlier?"
    show cyril hat neutral at basicfade
    c "I thought your interest was with the dragons, not with any ancient artifacts that everyone has forgotten about."
    p "My {i}interest{/i} is in whatever will get me on that throne the quickest!"
    p "Don't you ever forget that."
    show cyril hat concerned blush at basicfade
    c "I can't make any promises there, but I will try to make your stay here both accomodating and useful."
    p "Making my stay useful means getting me that scepter."
    show cyril hat smile blush at basicfade
    c "I-I'll certainly do my best, Highness."
    p "It seems I've underestimated you, Moronious."
    show cyril hat concerned at basicfade
    c "Ah yes.  You wouldn't be the first and you are surely not the last."
    p "Now find me that scepter!"
    show cyril hat concerned blush at basicfade
    c "I will try to recall for you just where it was.  Don't worry, my maj- your highness."
    
    return
    
label explore1:
    play music evil_theme
    scene bg corridor with fade
    play music princess_theme
    p "I don't need any help! I will scour this place myself!"
    p "And if I find something I can use to my advantage then it won't be a pathetic waste of a day."
    p "I just wish something would fall out of the sky that would be the answer to all my problems."
    show rope at midright with moveintop
    play sound "sfx/stab.ogg"
    p "Well, what do we have here?"
    show niir neutral at center with moveinright
    show niir mischief at basicfade
    n "The ansssswer to all your problemsss."
    p "A piece of rope?"
    show niir smile at basicfade
    n "Look clossser."
    p "A noose.  How very... "
    extend "thoughtful of you."
    show niir frown at basicfade
    n "Thoughtful is not ussssually one of the words used to describe the great dragon Niir."
    p "You don't say?"
    p "Well, Niir.  I am very busy with things."
    p "So if you'd please be on your way, I can get to my explorations."
    show niir neutral at basicfade
    n "Need an esssscort?"
    show niir mischief at basicfade
    n "You mussst.  Pretty young thing like you.  {i}Alone{/i}.  In the casssstle."
    show niir smirk at basicfade
    n "I'd advisssse you to be more careful."
    p "In case what?  There's some dragon lurking around above me and spying on me?"
    p "How ever will I cope?"
    show niir determined at basicfade
    n "Careful.  Or you might make a dragon mad."
    p "How do you know that wasn't what I intended?"
    show niir concerned at basicfade
    n "You are not sssscared?"
    show niir neutral at basicfade
    n "..."
    show niir frown at basicfade
    n "Curiousss."
    p "And could you stop sniffing me like that, I {i}have{/i} recently bathed!"
    show niir happy at basicfade
    n "Oh of that, I'm well aware."
    p "So I guess that's why you're in here."
    p "Any proper lady would be repulsed by such loathsome habits."
    show niir frown at basicfade
    p "But it's a good thing I'm not so proper, because I'm the only shot you have at getting out of here."
    show niir angry at basicfade
    n "You need to get your facts sssstraight nexxxt time."
    show niir smirk at basicfade
    n "Prrrrrincessssss."
    hide niir with moveoutright
    p "I have got my- Niir!  Where did you get to, you sneaky dragon!"
    p "Oh, well.  I didn't want you around anyway, you ridiculous reptile!"
    "..."
    scene bg stairs with fade
    p "This castle just has endless steps!"
    "Hours of searching... and nothing. Well, except for these delicious dried apples from the kitchens. And this rope...? So I supposed it wasn't a complete waste of time."
    return