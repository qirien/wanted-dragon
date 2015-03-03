label day1:
    p "Another day and I’m still no closer to regaining my throne… what would be the best approach?"
    menu:
    "see if the dragons have any ideas":
        jump dragons1
       #they tell you some stuff, then maybe you decide whether to stay with Niir or ask Balrung something, call niir_next_conversation or balrung_next_conversation
    
    "research powerful artifacts":
        jump library1

    "Explore the castle":
        jump explore1

label dragons1:
    p "Dragons are powerful. I need more power. The most logical thing to do would be to enlist their aid."
    scene bg dungeon with fade
    n "Ssssomething tasssty comes!"
    show princess at midright with moveinright
    p "Ahem. Dragons? I wish to speak with you!"
    show niir at midleft
    show balrung at left
    with moveinleft
    b "Princess [name]. To what do we owe this great honor?"
    n "Yesss, it's a pleasure..."
    p "I'm sure. Anyway, I am seeking loyal vassals to aid me in reclaiming my throne from my evil sister. Do you accept?"
    n "Vasssssals?" #TODO: Trying to think of a naughty pun here...
    b "Princess, our powers are extremely limited whilst we are held captive here."
    p "I thought all you had to do was kiss a human or something, and the spell would be broken."
    n "If that were the casssse, I'd have kissssed you firssst and asssked questions later."
    b "Yes, it's not quite that simple. You see, Merlonious will only release a dragon from captivity if he proves that he has found love and is reformed."
    p "Love?"
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
                    jump niir_pretend_love
                "\"I prefer you.\"":
                    $ balrung_affection += 1
                    p "I am the princess!  {b}I{/b} decide who shall be my minion, and I have chosen you! Do not question my decisions."
                    b "As you wish, princess."
                    extend "Perhaps you would care to join me in a game of Queens and Pawns?"
                    jump balrung1
                "\"Isn't there another way?\"":
                    p "Couldn't we overpower him? He doesn't seem that formidable..."
                    b "He possesses powerful magic, and our powers are dormant because of the curse. So, unless you possess some powerful magic...?"
                    p "I do not. But perhaps there is something in the castle that would allow us to fight him."
                    n "He iss alwaysss reading. The bookssss might aid you..."
                    p "Then I will seek out the library."
                    jump library1

label balrung1:
    p "Queens and Pawns? Is this a joke?"
    b "I can hardly think of a game more fit for someone who wishes to retake a kingdom."
    n "You should play ssstrip Queensss and Pawnssss."
    b "Niir, perhaps you would like to play against the Princess?"
    n "I do have a fine opening move... but Queensss and Pawnsss is boring. I shall ssseeek better entertainment."
    # TODO: FInish this scene

label niir_pretend_love:
    $ niir_affection += 1
    n "Should I drool over you like thissss?"
    p "No, that just makes you look like a half-wit and soils my dress."
    n "You could alwaysss take off the dresss...."
    b "Niir, remember, you're trying to act as though you are in love, as though you are a reformed gentleman of a dragon who would never even think of princesses without their dresses on."
    p "Niir, you should..."
    # TODO: Let's roleplay this part?
    menu:
        "\"Write me poetry\"":
            p "You should write a poem suitable to discuss the multitude of reasons why I should be Queen."
        "Give me presents":
            p "You should bring me a gift suitable for my royal station."
        "Sing to me":
            p "You should sing a sonnet fit to describe my beauty, wit, and charm."
    
    
label library1:
    # TODO: against the dragons? Do you mean, against her sister or to free the dragons?
    p "Going to the library would be the perfect way to find a tidbit of knowledge to use against the dragons."
    c "I know this was you Niir!"
    "{i}He he he, ha ha ha...{/i}"
    p "If it wasn't already occupied..."
    c "And you mark my words!  I will stop you, I will!"
    c "As soon as I find that proper spellbook!"
    "(This completely ruins my plans.  But I guess I should make the best of a bad situation?)"
    p "Doing some reading?"
    c "Yah!"
    "He dropped the book like it was a hot potato."
    c "Princess.  Yes, well I..."
    p "Let me get that."
    p "{i}15 Erotic Tales by Twilight{/i}."
    p "You were reading {i}this{/i}?"
    "(I know he wasn't really, but sometimes he makes it too easy.)"
    p "You'll have to read me out the good parts, I'm ever so curious."
    c "No, no.  Niir.  "
    extend "He's just having a joke."
    c "We joke together all the time.  Ha ha ha."
    c "Hilarious dragon that he is."
    c "Well, anyway.  I must find my spellbook.  My real spellbook."
    c "Not.. this."
    p "I'm not sure, I think {i}15 Erotic Tales by Twilight{/i} could cast a completely different kind of spell."
    c "..."
    c "Have you been talking with {i}him{/i} perchance?  Is this all part of the joke?"
    p "Of course it is.  This life is all one big joke at your expense, Moronious."
    c "Merlonious.  Cyril Merlonious."
    p "Anyways, I came by for a particular book, but if you are busy reading erotic tales, I will let you be."
    c "I'm not busy- not at all!"
    c "Please, do spend time with me.  I mean, what book was it?  I will always be a helpful librarian."
    c "Err, mage.  Librarian-mage type person."
    p "You {i}are{/i} odd Moronious."
    p "I suppose I will let you help me, if you promise not to be irritating."
    c "I think I can manage."
    p "Good.  I'm glad.  Now if you could direct me on a book outlining powerful artefacts in this vicinity."
    c "In this vicinity?  Whyever would you-"
    p "You're starting to irritate me."
    c "Oh, of course - of course.  The book.  Well, there has been something around here.  Old and dusty and-"
    c "Quite like the dragons in fact!"
    p "Are you trying to be witty mage?"
    c "Not very hard.  It only just came to me really."
    p "Well don't."
    c "This is what I was looking for.  {i}Long Hidden Powerful Objects: an abridged edition{/i}."
    c "It's really the best I could do at such short notice."
    p "While it is quite pitiful that you don't have more research materials in this castle of yours, I suppose this will have to do."
    c "Great now if I can be of any-"
    p "Begone!"
    c "Alright, I'll just gather up my-"
    p "Begone with you!"
    c "Good day Princess, I will just be seeing myself out."
    p "(I thought he'd never leave.  Now what have we here...)"
    p "This is quite curious.  This part here."
    p "There is a scepter with emeralds that has not been located in centuries."
    p "I think that it says it has ties to this very castle."
    p "How... curious."
    p "Although no one is sure what it does, they do presume it has magical powers."
    p "Well, I may as well find out more about it."
    p "The Scepter of Lavendorm."
    p "Hmmm..."
    
menu:
          "share it with Cyril."
                jump sharecyril
        "keep researching on your own"
            jump researchown

label sharecyril:
    p "Oh Cyrilllll."
    p "That foolish mage has to be around here somewhere."
    p "Where {i}are{/i} you foolish mage?"
    show cyril #TODO: with some flash-bang transition
    c "You called, your majesty?"
    p "I am already quite aware that you are a magic wielder."
    p "Please do not just appear like that in the future."
    c "Oh, I'm sorry.  I overheard that you were looking for me, and I just wanted to..."
    p "But a burden?  I see that."
    p "But I do have something rather curious to share with you, so if you would like to come with me."
    c "I would come with you anywhere, your majesty."
    p "..."
    p "I'd rather you didn't."
    c "So what is it that you wish to show me?"
    p "This scepter.  The Scepter of Lavendorm.  Is it real?"
    c "Quite real.  Once.  No one has seen it in quite some time."
    p "And this mentor of yours that put you in charge, he must have been centuries old.  Did he ever see it?"
    c "Well, I don't know about centuries..."
    c "He might have said there was a powerful but uncontrollable magic that I shouldn't go looking for."
    c "But I thought he was just joking with me.  Although come to think of it, he wasn't really the joking type."
    p "So did he say {i}where{/i} not to go looking for it?"
    c "Not specifically, but he did say it was bound up with special magic somewhere within these walls."
    p "And you didn't think to mention this earlier?"
    c "I thought your interest was with the dragons, not with any ancient artefacts that everyone has forgotten about."
    p "My {i}interest{/i} is in whatever will get me on that throne the quickest."
    p "Don't you ever forget that."
    c "I can't make any promises there, but I will try to make your stay here both accomodating and useful."
    p "Even if it means getting me that scepter?"
    c "Oh well.  Perhaps it means that too."
    p "It seems I've underestimated you, Moronious."
    c "Ah yes.  You wouldn't be the first and you are surely not the last."
    c "Although my name {i}is{/i} Merlonious, I do quite appreciate the kind words."
    p "I wasn't being kind.  I was being truthful.  I have no time for {i}kindness{/i}, mage."
    c "Appreciated all the same."
    p "Now find me that scepter!"
    c "I will try to recall for you just where it was.  Don't worry, my maj- your majesty."
    "(Let's see if the bumbling mage can get something right this time.  I suppose I can give him a chance.)"
    
label explore1:
    p "I don't need any help! I will scour this place myself!"
    p "And if I find something I can use to my advantage then it won't be a pathetic waste of a day."
    p "I just wish something would fall out of the sky that would be the answer to all my problems."
    # rope drops
    # niir drops down
    p "Well, what do we have here?"
    n "The ansssswer to all your problemsss."
    p "A piece of rope?"
    n "Look clossser."
    p "A noose.  How very... "
    extend "thoughtful of you."
    n "Thoughtful is not ussssually one of the words used to describe the great dragon Niir."
    p "You don't say?"
    p "Well, Niir.  I am very busy with things."
    p "So if you'd please be on your way, I can get to my explorations."
    n "Need an esssscort?"
    n "You mussst.  Pretty young thing like you.  {i}Alone{/i}.  In the casssstle."
    n "I'd advisssse you to be more careful."
    p "In case what?  There's some dragon lurking around above me and spying on me?"
    p "How ever will I cope?"
    n "Careful.  Or you might make a dragon mad."
    p "How do you know that wasn't what I intended?"
