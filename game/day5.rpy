   
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
            jump other_route #TODO: Write this
            
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
    
    ###{I thought about a scene between Balrung and Niir that the princess overhears)
    
if niir_love:
    b "You have fallen in love with the tempestuous temptress that has entered our realm."
    n "Now why would you ssssssay that?"
    b "I have seen it happen many times before."
    b "I can tell the signs."
    n "Love is not ssssomething that I am acquainted with, old dragon."
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
    p "(Though I have to admit, there is some sort of animal magnetism toward Niir.)"
    p "(Even if it is only animal.)"
    n "Sssshut up.  I am done conversssssing."
    b "Think about what I said.  I'd say to follow your heart."
    b "But we both know that isn't possible."
    p "(This is what I wanted, wasn't it?)"
    p "(A dragon at my disposal.  Willing to leave, all for the delusion of love.)"
    p "(But somehow, I am not content.  What is this?)"
