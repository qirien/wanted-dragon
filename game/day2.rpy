label day2:
    scene bg bedroom with fade
    show princess at center with dissolve
    # TODO: Add intro thing in here? Receives a letter?

    
    show niir at quarterleft with moveinleft
    n "Ssssen anything interesting today Princessss?"
    p "No, it’s all been very dull. And now it’s become tedious as well. What do you want?"
    n "I sssupect the question should be to you.  What do {i}you{/i} want?"
    n "You came here, acting ssssupicious in the first place."
    p "I need something powerful. Something that will make it clear that I am the rightful Queen. If you don’t have anything like that, then away with you."
    n "More powerful than a dragon?  My aren’t you ambitioussss?"
    p "It doesn’t take much to be more powerful than you right now."
    if (niir_route):
        p "But if we can get that mage to believe love has reformed you, then perhaps I’ll allow you to demonstrate some of your supposedly awesome powers."
        p "In fact, why don’t you demonstrate your love by finding me something powerful?"
        n "Pretend to be in love with you?"
        n "I may be bored sssstuck in this form, but I'm not that bored."
        p "Fine. I’ll find some other way."
        n "I didn’t sssay I wouldn’t help.  I just need incccentive."
    else:
        p "You probably don’t even know any secrets of this castle, despite the fact that you’ve lived here for… what? Ten, twenty years?"

    n "I know sssssecrets of all kindsss.  And not just about the cassstle."
    n "I could find you ssssomething powerful.  But what would you do for me in return?"
    p "Why, I would help you gain your freedom, so you could continue to serve me."
    n "That doesn’t ssssound like a very good deal."
    p "It sounds good to me. Do you have a better idea?"
    n "..."
    p "No? Then perhaps I’ll just go and ask Cyril. He probably knows more than you do about the ‘ssssecrets’, anyway."
    n "Don’t waste your time with him.  I am the only one who knowssss."
    p "I don’t believe you."
    n "Follow me and I’ll sssshow you something."
    p "Very well. Lead on, Niir."
    n "Thissss way."
    # TODO: tour of the castle with lots of fun BGs

    n "Why do care about the kingdom anyway?  What hasss the kingdom done for you?"
    p "Nothing, yet. That’s why I need to be Queen."
    p "Surely you can understand wanting greater power and recognition?"
    n "There are other wayssss of getting power.  Much more amusing ways, than dealing with royalty." 
    p "The throne should be mine! It {b}is{/b} mine! My sister is not fit to rule! If my father can’t see that--"
    n "Ssso you just want to take it?"
    p "It is my {b}right{/b}! I was born to be QUEEN!!"
    n "I don’t care about that.  But I am interessssted in you jussst taking it."
    p "Good. By the way, isn’t this the way to the [insert boring place here]? Where are you taking me?"
    n "We have to go through the [place].  Patiencccce."
    p "Now you’re starting to sound like my father! You don’t usually sound like my father, though. He doesn’t seem to care what I wear or what I do or what I want at all."
    n "Ssssounds heartbreaking, princessss.  I don’t care either.  But I want to find out what your plansss are, as it seems like you don’t have any."
    n "Watching you fail could be entertaining."
    p "Hmph. That’s no way to talk to your future Queen."
    n "My queen?  Ha ha ha ha.  I am a dragon.  I have no queen."
    p "Cyril might as well be your queen, since he controls where you can go and keeps you in human form. I wouldn’t be so cruel."
    n "He is rather pretty."
    n "But you, are ssslightly more becoming.  Just ssslightly."
    p "Yes, well, it is a queenly duty to look becoming… though my presence would certainly be improved if I had my full royal wardrobe. Are we there yet?"