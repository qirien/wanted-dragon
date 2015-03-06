# cyril dissuading against niir route
# DAY 5?!
label day5:
    if (route == "Niir"):
        c "I saw you, I'm begging your pardon.  I didn't want to have to bring this up but I feel compelled."
        c "I saw you, your majesty."
        p "Saw me what?"
        c "Well, you see..."
        p "Spit it out mage!  I do not have all day."
        c "With Niir, that {i}dragon{/i}."
        c "Do not trust him.  There is a reason he is here.  He shall not be freed, milady!"
        c "Shall not.  Do you have any idea what he would be like out there?"
        c "You cannot trust him for a second.  Not one second!"
        menu:
            "\"You are mistaken about what you saw.\"":
                p "You are mistaken about what you saw."
                c "Oh, so then you were just being friendly?"
                p "Of course, I wouldn't be interested in that creature."
                p "He's despicable and does not know the meaning of respect."
                p "You on the other hand..."
                p "Someone like you would understand when a lady is in need."
                p "And has demands on her that only power can fulfill."
                c "P-p-power?"
                p "You must have some measure of power, or these dragons would have escaped long ago. Use it to help me rid the throne of my scheming sister Magnolia!"
                p "If you won't, I'll find someone else who will."
                
                #TO DO:  ideas on finishing this?
                # switch to mage route?
                # can you have both routes going at once? I think we need our endings to decide that.
            "\"I can make up my own mind - Begone!.\"":
                c "I understand that, but I don't think you have all the facts."
                c "He is most surely using you."
                p "How do you know I'm not using him?"
                c "I... I hadn't thought of that."
                c "{b}Are{/b} you using him?"
                p "Oh no.  We're hopelessly in love.  No one is using anyone."
                p "Good day Moronious."
                c "Errr, good day Princess?"
                p "Begone!"
                c "{i}I do wish you would quit telling me that.{/i}"
            "\"Maybe you're right...\"":
                p "That is not completely false. But whom do you suggest I trust?"
                c "Well, there's...you could...I mean..."
                c "Me. Trust me, my highness- your highness."
                menu:
                    "\"I do trust you.\"":
                        p "You are much more trustworthy...very well, if you will promise to aid me"
                        $ route = "Cyril"        
                    "\"I do trust you\" (Lie)."
                    "\"You don't have what I need.\""
                    
    elif (route == "Balrung"):
        #TODO: who would dissuade from this? Niir? Balrung himself?
        n "What do you ssssee in that old tortoisssse?"
        
    elif (route == "Cyril"):
        #TODO: Balrung/Niir try to convince her that he's wimpy. "but if he's so wimpy, why are you still imprisoned?"   
        b "Cyril's intentions are certainly pure, but he may not be willing to do what you want."

###### DAY 5
if (route == "Niir"):
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
    b "I can discern the signs."
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
    b "But that would require you to possess one in the first place."
    p "(This is what I wanted, wasn't it?)"
    p "(A dragon at my disposal.  Willing to leave, all for the delusion of love.)"
    p "(But somehow, I don't enjoy the feeling.  What is this?)"


label cyril6:
    
    # scepter progress
    # DAY 5 or 6?
    
    c "I found it."
    p "My scepter?  I knew you could do it.  You are not as infantile as you seem."
    p "I've actually been very impressed with the way you operate."
    p "Acting like you don't know a thing and then astounding us all with your competence."
    p "Keeps the dragons on their toes as well, I'd presume."
    c "Errr... no.  I found my spellbook."
    c "It was right under my nose the entire time."
    p "..."
    p "Don't think because I'm banished I can't order your death."
    p "I do have people, you know."
    c "I'm dreadfully sorry."
    c "But now that I have my spellbook I can find some sort of locating spell, surely."
    p "You'd better because I've grown tired of waiting."
    c "Let's see here... locater-locater... lo-"
    c "Here!"
    c "It's not a locating spell but it does bring deep, powerful magical items to glow incessantly until I stop the spell."
    p "Then try it already!"
    c "I will, I will."
    c "Stand back, your majesty."
    p "What?  So I don't get flicked by your wand.  I think I'll take my chances."
    c "I'm just not sure if the spell will go exactly as planned."
    p "It had better Moronious or I will make sure that council of yours knows how dangerous you are with a spellbook in hand."
    c "More threats.  Jolly good, Princess.  I do think we're communicating quite well."
    c "You do look me in the eye when you're threatening me which is lovely, and gives me tingles all-"
    p "JUST DO THE SPELL ALREADY!"
    c "Ah yes."
    #TO DO:  magic words?  Andrea?  Got anything?
    c "There.  I-"
    p "..."
    c "Do you see that?"
    p "Something is glowing..."
    # should the dragons get the scepter first?  what plot should we do here?
    

    
    
 