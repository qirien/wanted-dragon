label day1:
    p "Another day and I’m still no closer to regaining my throne… what would be the best approach?"
    menu:
    "see if the dragons have any ideas":
       #they tell you some stuff, then maybe you decide whether to stay with Niir or ask Balrung something, call niir_next_conversation or balrung_next_conversation
    "research powerful artifacts":
            jump library1
        #(at the library, where Cyril hangs out)
#            after finding some interesting fact in a book:
#                share it with Cyril
#                    talk about it, then call cyril_next_conversation
#                keep researching on your own
    "Explore the castle":
        #(finds something secret?)
         #may also lead to some character’s next_conversation?


label library1:
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
