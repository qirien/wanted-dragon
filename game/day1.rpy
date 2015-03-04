label day1:
    scene bg bedroom with fade
    show princess at center with dissolve
    p "What a terrible start to a day; I'm still not queen."
    p "But that's why I came here; to remedy that."
    p "Dragons are powerful, and I need more power. I should talk to them without that mage around; maybe they can tell me more."
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
    n "Vasssssals? We are no sssuch thing." #TODO: Better Niir response?
    b "Princess, our powers are extremely limited whilst we are held captive here."
    p "I thought all you had to do was kiss a human or something, and the spell would be broken."
    n "If that were the casssse, I'd have kissssed you firssst and asssked questions later."
    b "Yes, it's not quite that simple. You see, Merlonious will only release a dragon from captivity if he proves that he has found love and is reformed."
    p "Couldn't we overpower him? He doesn't seem that formidable..."
    b "He possesses powerful magic, and our powers are dormant because of the curse. So, unless you are a sorceress...?"
    p "I am not. But I am interested in powerful magical objects. Do you know of any?"
    b "There are many arcane tomes in the library that might describe such things. I have not read them, as they would be of no use to dragons."
    p "Then I will seek out the library."
    jump library1
    
    
label library1:
    # TODO: against the dragons? Do you mean, against her sister or to free the dragons?
    scene bg library with fade
    show cyril at midright with dissolve
    "(It appears the library is already occupied...)"
    c "I know this was you Niir!"
    "{i}He he he, ha ha ha...{/i}"
    c "And you mark my words!  I will stop you, I will!"
    c "As soon as I find that proper spellbook!"
    "(This completely ruins my plans.  But perhaps I could turn it to my advantage?)"
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
    # TODO: write this on a book-screen to look like an old book?
    p "There is a scepter with emeralds that has not been located in centuries."
    p "I think that it says it has ties to this very castle."
    p "How... curious."
    p "Although no one is sure what it does, they do presume it has magical powers."
    p "Well, I may as well find out more about it."
    p "The Scepter of Lavendorm."
    p "Hmmm..."
    
    menu:
        "Share it with Cyril."
            jump sharecyril
        "Share it with Balrung.":
            jump sharebalrung
        "Search for it on your own":
            jump explore1
       
label sharebalrung:
    p "Back down to the dungeons, again. This castle is much too large for the few people that live here."
    scene bg dungeon with fade
    show balrung at midleft with dissolve
    show princess at midright with moveinright
    b "Back so soon?"
    p "Yes, I've found something that might help. What do you know of the Scepter of Lavendorm?"
    b "No one has been able to find it. It is presumed lost, and, as its powers are unknown, no one lately has tried very hard."
    p "Yes, the book said as much. Where is it?"
    b "Perhaps that's why she chose this place..."  #TODO: This assumes the mage who imprisoned the dragons did choose this place? Or was it the dragon castle originally?
    p "What? She who?"
    b "Never mind. I believe it is still here. I've felt latent power within the walls of the castle, but assumed it was just the binding curse."
    p "Interesting...could you pinpoint a certain location where that feeling is strongest?"
    b "The feeling is not constant or consistent; but if I detect it again I shall inform you."
    p "Very good, Balrung."
       
label sharecyril:
    p "Oh Cyrilllll."
    p "That foolish mage has to be around here somewhere."
    p "Where {i}are{/i} you foolish mage?"
    show cyril #TODO: with some flash-bang transition
    c "You called, your majesty?"
    p "I am already quite aware that you are a magic wielder. Please do not just appear like that in the future."
    c "Oh, I'm sorry.  I overheard that you were looking for me, and I just wanted to..."
    p "But a burden?  I see that." #TODO: This doesn't make sense to me.
    p "But I do have something rather curious to share with you, so if you would like to come with me."
    c "I would come with you anywhere, your majesty."
    p "..."
    p "I'd rather you didn't."
    c "So what is it that you wish to show me?"
    p "This illustration of a scepter.  The Scepter of Lavendorm.  Is it real?"
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
    # TODO: Finish this; does she ask about the scepter? Does he know anything?