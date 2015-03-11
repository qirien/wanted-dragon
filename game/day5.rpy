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
            "\"I can make up my own mind - Begone!.\"":
                c "I understand that, but I don't think you have all the facts."
                c "He is most surely using you."
                p "How do you know I'm not using him?"
                c "I... I hadn't thought of that."
                c "{b}Are{/b} you using him?"
                p "Oh no.  We're hopelessly in love.  No one is using anyone."
                p "Good day, Moronious."
                c "Errr, good day, Princess?"
                p "Begone!"
                c "{i}I do wish you would quit telling me that.{/i}"
            "\"Maybe you're right...\"":
                p "That is not completely false. He does not know the meaning of respect."
                p "You on the other hand..."
                p "Someone like you would understand when a lady is in need."
                p "And has demands on her that only power can fulfill."
                c "P-p-power?"
                p "You must have some measure of power, or these dragons would have escaped long ago. Use it to help me rid the throne of my scheming sister Magnolia!"
                p "If you won't, I'll find someone else who will."
                # TODO: Roleplay this
                #TO DO:  ideas on finishing this?
                # switch to mage route?
                # can you have both routes going at once? I think we need our endings to decide that.
                    
    elif (route == "Balrung"):
        #TODO: who would dissuade from this? Niir? Balrung himself?
        n "What do you ssssee in that old tortoisssse?"
        
    elif (route == "Cyril"):
        #TODO: Balrung/Niir try to convince her that he's wimpy. "but if he's so wimpy, why are you still imprisoned?"
        p "Ugh, this room again... I do miss my own castle, sometimes..."
        "As I looked around, I noticed a piece of paper next to the door - a note?"
        write_b "Princess,"
        write_b "Meet me on the South Tower this morning if you wish to discuss terms for my aid."
        write_b "\n-A Potential Ally"
        nvl clear
        p "Well, that sounds exciting! I wonder who it's from?"
        menu:
            "Stay here.":
                p "It's probably a ruse. Besides, I already have Moronious helping me out."
                p "Speaking of which, perhaps I'll go and see his progress."
                jump cyril5
            "Go and find out.":
                p "I'll go and find out. There's no harm in that, surely."
                scene bg exterior with fade
                show balrung at center with dissolve
                p "Oh! It's {b}you{/b}."
                b "Yes, it is I. I'm surprised at you, Princess."
                p "Why, because I followed your invitation?"
                b "No. I am astonished that you have chosen to ally yourself with that ridiculous mage. I assumed you were more canny than that."
                p "You think {b}Moronious{/b} will betray {b}me{/b}?"
                b "Cyril's intentions are certainly pure, but he may not be willing to do what you want. He is not capable of murder."
                p "And you are?"
                b "If necessary, yes. I've proved that; that's how I came to be cursed here."
                p "Who'd you do in?"
                b "Another time, perhaps. But here is the offer I will make to you - ally with me instead of that mage. Our interests align more closely, and I will not balk at your...more troublesome requests."
                p "How could you help me?"
                b "I'm a {b}dragon{/b}, Princess. If I were free, I could fly you anywhere you wished. I could set fire to anything you desired. I could obliterate any building or army that stood in our way."
                p "Well..."
                menu:
                    "\"No. I don't trust you.\"":
                        p "I don't trust you, Balrung. Nor Niir. You may have potential for great destruction, but I see no reason to believe you will choose to do my will instead of your own."
                        b "As you wish, Princess. What a shame we could not be allies."
                        p "Do not hinder me, Balrung. I shall leave you alone if you do the same for me."
                        b "I make no promises. I have my own plans that you have no part in, now."
                        hide balrung with moveoutleft
                        p "Hmph."
                        "I better go see what Moronious is up to."
                        jump cyril5
                    "\"Perhaps you would be a valuable ally.\"":
                        p "Perhaps you would be a valuable ally. But what assurance do I have that you will aid me?"
                        b "I have the same ambitions you do - to be free and have the power to control my own destiny. Aiding you will help me with those goals."
                        $ route = "Balrung"
                        jump balrung5

###### DAY 5
if (route == "Niir"):
    p "Could you stop disappearing on me Niir!"
    p "I wish to confer with you!"
    n "Confer?  On what?  Your choice of dresssss?"
    p "No! The pretence!  The acting like you're in love with me!"
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
            call trustfall
        "Offer to show him some thigh.":
            call somethigh 
            
    p "Now, Moronious usually spends his time in the library. So if we are in the hall near the library, professing our love to each other, he will hear us."
    c "Professsss love?!"
    p "Just pretend you're reading a book or something. You don't have to mean it; you just have to convince that fool mage."
    
    scene bg corridor with fade
    show niir at center with dissolve:
        zoom 2.0 #TODO: test this
        
    p "Hold me like this, with your hands here, in case he peeks out."
    n "I can do that, at leassssst."
    # TODO: finish this
    
            
label somethigh:
    p "Alright.  Fine."
    p "I'll show you some of mine if you show me some of yours."
    p "Trust."
    n "I thought you'd never offer."
    scene black
    # TODO: add vfx for Cyril's protection spell that got activated?
    p "Happy now?"
    n "Happy wouldn't be the word that I would ussssse."
    p "Well, now I know how Moronious' protection spell works. I'm surprised you're still conscious after that much electricity."
    n "You are no fun Princesssss."
    scene castle
    p "So there we go, I trust you enough with that, and now you trust me. Say it."
    n "Sssstill not convincccccced."
    with hpunch
    n "Agh!  What wasssss that?"
    p "Convincing.  Hurry up and trust me or I'll do it again."
    n "It doessss not work- {i}stop human{/i}!"
    n "Desist!"
    "He grabbed me. Since I had just finished punching him, the protection spell didn't activate."
    p "(He's stronger than I thought...)"
    p "Release your hands from my royal person immediately!"
    n "Do you trussssst me now?"
    "Ah, a test.  Touché, dragon."
    p "Completely."
    n "Really?"
    p "Yes.  I trust you.  Do you trust me?"
    n "..."
    n "Yessss."
    p "I didn't quite hear you, what was that?"
    n "Yessss, don't make me repeat it Princessss."
    p "So let us fool the mage about our love."
    p "And I will make your trust worth it."
    n "Yessss.  Fool.  We sssshall."
    p "Then we are partners.  I want a full agreement Niir.  Nothing less will do."
    n "Partnerssss."
    return

label trustfall:
    p "I'll fall and you'll catch me."
    n "What will that prove?"
    p "That you can trust me because I'm trusting you with my very life."
    n "You are trussssting me with your life jusssst by being in this room."
    p "Well, let's make it more official then."
    p "I won't fight back; I trust that you will not hurt me."
    p "And that you will catch me."
    p "Are you ready Niir?  I am going to fall."
    n "No."
    p "I'm going to fall, I do hope some annoying dragon with nothing better to do will catch me."
    n "I ssssaid 'No!' human!"
    p "I am trusting you, isn't that what you wanted?"
    p "(I do believe I'm calling his bluff.)"
    p "(I can tell that's not what he wanted at all.)"
    n "..."
    n "How can you trussssst me, when I do not even trussst myself?"
    p "(Bingo!)"
    p "(Though I almost feel... no, {i}pity{/i} is unbecoming on a princess.  I do not feel that.)"
    p "Niir.  You have to start some time."
    p "And why not start by trusting me?  You can trust yourself later."
    p "Right now your own loyalty should be to your future Queen."
    n "..."
    p "Niir.  Will you catch me?"
    n "..."
    p "Will you catch me Niir?"
    n "... "
    extend "{i}Yessss.{/i}"
    p "I am willing to trust you right now when you certainly don't deserve it.  Surely this goes a long way for your trust in me."
    n "Perhapssss."
    p "Good.  Then are we ready to go onto the next step in our diabolical plan to gain your freedom and my throne?"
    n "Perhapssss."
    p "Then let's do it and stop talking about it."    
    return
    
    ###{I thought about a scene between Balrung and Niir that the princess overhears)
    
if (route == "Niir"):
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


label cyril5:
    
    # scepter progress
    # DAY 5
    scene bg library with fade
    show cyril at center with dissolve
    
    c "I found it."
    p "My scepter? You are not as infantile as you seem."
    p "I've actually been very impressed with the way you operate."
    p "Acting like you don't know a thing and then astounding us all with your competence."
    p "Keeps the dragons on their toes as well, I'd presume."
    c "Errr... no.  I found my spellbook."
    c "It was right under my nose the entire time."
    p "..."
    p "Don't think because I'm banished I can't bring about your death."
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
    p "{size=+2}Just do the spell already!{/size}"
    c "Ah yes."
    c "MAGIA LUXIS!" #TODO: should we have a special font for when he does magic?
    c "There.  I-"
    p "..."
    c "Do you see that?"
    p "Something is glowing..."
    c "... but it's gone."
    p "Bring it back!"
    c "Magia Luxis!"
    c "Something is blocking it... but the scepter is here, in this castle!"
    c "I'm so sorry, your majesty, but I need to study this more. Please be patient!"
    p "I am not a patient person."
    c "I know."
    return