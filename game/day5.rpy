# cyril dissuading against niir route
# DAY 5?!
label day5:
    scene bg bedroom with fade
    "I was just finishing the unoriginal-yet-edible breakfast Moronious had dropped off for me when there was a knock at the door."
    
    if (route == "Niir"):
        show cyril at midleft with moveinleft
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
        show niir at center with moveinleft
        n "What do you ssssee in that old tortoisssse?"
        p "Good morning to you as well, Niir."
        n "Balrrrung hassss no sensssse of fun, and he won't be easy to manipulate. Even for you."
        p "What concern is it of yours?! Or are you jealous, perhaps? I could use another minion, if you also want the job."
        n "The mage will never believe you have fallen in love with {b}him{/b}."
        p "Why not? Isn't that supposed to be the great thing about love? It's blind, knows no boundaries, is all you need, etc, etc?"
        n "He'sss crafty. He'sss planning ssssomething. He'll betrrray you at the end."
        p "Really? What proof do you have?"
        n "I know him!  That'ssss how he worksss."
        p "If he was really so good at plotting and scheming, he would have found a way out by now."
        n "He'sss patient! Trussst me."
        p "Trust {b}you{/b}?!"
        n "Yesss. I guarantee you'll find me much... eassssier to worrrk with."
        "I thought about it. Niir was more transparent - it was obvious what he was thinking. But perhaps that's what I liked about Balrung... the idea of a challenge."
        menu:
            "\"Prove that I can trust you.\"":
                p "Prove to me that I can trust you."
                n "Prove that I can trusssst you."
                jump trust_niir
            "\"No, I'm working with Balrung.\"":
                p "No. I'm working with Balrung."
                n "Fine. But don't expect any ssssympathy when he turnsss on you in the end."
                p "I neither expect nor require anyone's sympathy!"
                "He slunk out, defeated, and I turned my attention to other things."
                "It was probably time to visit Balrung and see what progress we could make together on our plans."
                jump balrung5
        
    elif (route == "Cyril"):
        p "Ugh, this room again... I do miss my own castle, sometimes..."
        "As I looked around, I noticed a piece of paper next to the door - a note?"
        b_write "Princess,"
        b_write "Meet me on the South Tower this morning if you wish to discuss terms for my aid."
        b_write "\n-A Potential Ally"
        nvl clear
        p "Well, that sounds exciting! I wonder who it's from?"
        menu:
            "Stay here.":
                p "It's probably a ruse. Besides, I already have Moronious helping me out."
                p "Speaking of which, perhaps I'll go and see his progress."
                jump cyril5
            "Go and find out.":
                p "I'll go and find out. There's no harm in that, surely."
                scene bg exterior day with fade
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
                        p "What is your plan?"
                        b "If you can convince Merlonious that I've found true love and reformed, he will have to let me go. In return, I'll help you regain your throne."
                        p "True love? How shall we do {b}that{/b}?"
                        b "I have some ideas. And I trust you have your own methods of getting others to believe what you wish."
                        p "I do."
                        b "Why don't you meet me down in the dungeons in an hour, and we can spend some time together? If you can arrange so that Merlonious happens to find out where you are, you'll have set the stage for him to believe we are falling in love."
                        p "He seems to think you cannot change. How will you convince him otherwise?"
                        b "As I have not changed for forty years, when I suddenly do appear kind and loving, he will have no choice but to believe me. That's the benefit of being honest most of the time; people tend to believe you are still honest the rest of the time."
                        p "You are more shrewd than I gave you credit for... this might actually work."
                        $ route = "Balrung"
                        jump balrung5

label balrung5:
    scene bg dungeon with fade
    show balrung at center with dissolve
    b "Princess! How lovely to see you. Your presence is like a light that makes even this gloomy dungeon seem like a sunny garden."
    p "You can save the flattery for later when Moronious can \"accidentally\" overhear you."
    b "That wasn't for Moronious; that was for you, my lady."
    p "W-well, what shall we do together?"
    b "Would you care to play Queens and Pawns?"
    p "I suppose there's not much else to do in this wretched dungeon. You may go first."
    b "How generous of you."
    p "How did you come to be imprisoned here, anyway? I've heard you did something quite terrible."
    b "Terrible? Yes...but it's not that simple. Your turn."
    p "Interesting move. Tell me what happened. I want to hear your version of events, not just Moronious' self-righteous justification for your imprisonment."
    b "You want to hear it? Well..."
    menu:
        "Pay attention":
            b "It starts with a human woman. Myriah. She was... like you, in many ways. Powerful. Ambitious. Intelligent.  Her Queens and Pawns strategies were always elegant and ruthless; her victories surprising yet inevitable."
            b "We met forty years ago. I was young, then, full of ideals of cooperation and mutual understanding. She was a mage who came to live among our kind to learn more about us and (though she never said it) to prove to us that humans were worth talking to."
            b "We played many games together. After her studies were complete and she returned to her Academy, I'd take on this feeble human form just to meet her there and match wits with her."
            b "I'm not sure she understood how much of a sacrifice that was for me; how I was ridiculed, how many friends I alienated."
            "I was so caught up in what he was saying that I almost missed how he had setup his Pawns in a chain reaction. I saw it just in time."
        "Focus on strategy.":
            b "Human woman Myriah, blah, blah... forty years... blah, blah, cooperation... blah, blah ambitious, blah blah, strategies... blah, blah, sacrifice."
            "He's trying to draw my attention with his Queens while the Pawns setup a chain reaction! My Queens shall whittle down his defenses while he's not paying attention."

    p "Go on. Your move."
    b "So when I invited her to join me, permanently, as a part of a human-dragon marriage alliance, I thought she'd be honored. It was her life's work, after all."
    b "But she refused. She wanted {b}me{/b} to join {b}her{/b}. You humans always want to be the ones in charge."
    p "Of course we do. But wouldn't that accomplish the same thing?"
    b "It's completely different! You humans want to use us, subordinate us, rule us! I wanted an alliance of equal partners!"
    b "I should have waited. I should have elucidated my proposal more elegantly."
    p "What did you do?"
    b "When she wouldn't come with me, I brought her with me anyway."
    p "You kidnapped her?!"
    b "No! I would have let her leave, once she had listened to me! She refused to even talk to me! And her mentors were poisoning her mind against me. I had to bring her away from all of that."
    p "Hmph. Did it work?"
    b "No. No, it...didn't work at all. She used her magic, and her very life force, to create this...prison. To trap me in human form, and make it possible for her colleagues to trap other dragons who failed to conform to their human ideals of dragon behavior."
    menu:
        "Serves you right.":
                    p "Serves you right. That's what {b}you{/b} wanted to do to {b}her{/b}, after all - trap her here with you."
                    b "I didn't want that. I wanted her to choose to be with me. But she chose to die instead..."
        "You loved her.":
                    p "You loved her, then?"
                    b "Of course I loved her! That was the point of the whole thing! But she chose to die rather than be with me..."
                    $ balrung_affection += 1

    p "You were a fool for discarding your strategy in favor of emotion. Much like in this game. Resign now, while you still can!"
    b "Resign? But...oh, I see. I've lost, haven't I? Well done, Princess."
    b "Yes, I resign. I've learned that much from my mistakes, at least."
    p "Perhaps one day your strategy and emotion can be aligned towards the same goal."
    b "One day...perhaps."
    show cyril at midleft with moveinleft
    c "Princess! You're here! With...Balrung?"
    p "Yes, we've just been enjoying a wonderful game of Queens and Pawns."
    b "She's quite a clever opponent! Quick-witted as well as beautiful, wouldn't you say, Merlonious?"
    c "Well, yes, of course, but-"
    p "Now, Balrung, stop flattering me so much or I shall begin to suspect you like me. Weren't you just saying dragons were incapable of that, Moronious?"
    c "Y-yes, they are! Maybe not all. But definitely this one!"
    b "For a long time I feared you were right, mage, but perhaps I just hadn't met the right woman."# to soften up this old stone heart of mine."
    c "The r-r-right woman?! Surely you don't mean Princess [p_name]?!"
    p "You don't believe I could induce feelings of love?! How cruel!"
    b "Yes, really, Merlonious, I would have thought you'd be more gentle with our dear Princess's delicate feelings!"
    c "Her delicate...feelings?!"
    p "Oh, yes, I'm quite overcome, I do think I might faint."
    c "Faint?! Um, well, ah, what should we do?!"
    "I pressed my hand to my forehead and collapsed into Balrung's arms. That's what heroines of love stories are always doing; it should help convince that fool Moronious."
    scene black
    c "St-stop that! You mustn't hold the Princess that way!"
    b "Really? You'd have preferred I let her head crack on this stone floor? I never thought you were so heartless, Merlonious!"
    c "Well, no, I wouldn't want that, but- I'm not- you can't!"
    b "I'll just set her her down here on my bed, where she can be comfortable until she wakes up."
    c "On your bed! No, no, that won't do at all!"
    scene dungeon with irisin
    show balrung at center with come_closer
    "He set me down gently, and I cracked one eye open. Balrung winked at me and I closed my eyes again."
    scene black with irisout
    b "Our poor Princess... she's been through so much."
    "He stroked my hair tenderly away from my face while Cyril gaped. It was all I could do to keep from cackling with glee at his befuddlement. Balrung was quite the actor; almost as good as me."
    c "Well I- I will just stay here and watch over the Princess until she recovers! I'll protect her from you, you, vituperous viper!"
    b "If you feel the need, by all means, do so. Though perhaps you might think about protecting her from your rudeness, since that is what got her into this position in the first place."
    show niir at right with moveinright
    n "Why is the Princesss pretending to sssleep on your bed?"
    b "I'm afraid she fainted. Merlonious made an indelicate comment and her poor constitution just couldn't take his boorish suggestions."
    c "That's not at all what happened! Is it? Oh dear, I would never be unkind to the Princess, not on purpose, but sometimes my chatter is faster than my brain!"
    "This was getting ridiculous. I think we had made our point, so I opened my eyes."
    scene dungeon with fade
    show balrung at center
    show cyril at midleft
    show niir at midright
    with dissolve
    p "Oh, thank you gentlemen for taking such good care of me. I don't know what came over me. But I'm so glad I can trust you... well, {b}some{/b} of you, anyway."
    "I glared at the mage, hoping he would feel even more guilty."
    p "And now I will depart, so please excuse me."
    b "Until next we meet, Princess."
    
    return

label niir5:
    p "Could you stop disappearing on me Niir!"
    p "I wish to confer with you!"
    n "Confer?  On what?  Your choice of dresssss?"
    p "No! The pretence!  The acting like you're in love with me!"
    p "How are we faring?"
    p "Why don't you just tell that Moronious already that you want to leave with me."
    p "And start a happily ever after of such."
    n "I haven't been convinccccced."
    p "You say that every time!  I can promise you freedom, destruction, and power."
    p "Isn't that enough?"
    n "Dragonsss aren't that easssy to trussst, Princesssss."
    p "Haven't I told you not to stare at me like tha-oh, you can't help it.  Can you?"
    p "That's the way you always look."
    p "Regardless, Niir, I can promise you what you want."
    n "What if I want more?"
    p "More?"
    n "Perhapsss."
    p "You'll have your freedom; I'll have my throne. What more is there?"
    n "Isssn't it obvioussss?"
    p "You mean?  No.  Absolutely not.  "
    extend "Especially not with you."
    n "You wound me Princessss."
    p "And why should I trust you?"
    n "Assss you ssssee.  Trusssst is not easssy, isss it?"
    p "How can I get you to trust me?"
    n "I won't trussst you, until you trusssst me."
    p "..."
    p "I see how it is."
    menu trust_niir:
        "Do a trust fall.":
            call trustfall
        "Offer to show him some thigh.":
            call somethigh 
            
    p "Now, Moronious usually spends his time in the library. So if we are in the hall near the library, professing our love to each other, he will hear us."
    n "Professsss love?!"
    p "You don't have to mean it; you just have to convince that fool mage."    
    scene bg corridor with fade
    show niir at center with come_closer

    p "Hold me like this, with your hands here, in case he peeks out."
    n "I can do that, at leassssst."
    p "Now, say things you like about me, and I will do the same for you. I've heard that's what lovers often talk about."
    n "I suppossse."
    n "Oh, Princessss, your...dresss is ssssooo...shiny. And your earsss are ssso...sstrange. How can you even hearrr with those tiny things?"
    show cyril at right with moveinright:
        zoom 0.5
        yalign 0.5
    p "I suppose that's a start. Don't just compliment my body, though, or he won't believe it's true love!"
    n "You're sssoo deviousss, when I ssseee your scheming grin I jussst want to eat you up!"
    show niir with vpunch
    n "I mean, I jussst want to be good! And not kidnap any one elsssse."
    n "And only ssssteal you away if you assssk me to."
    "He bent his head close to my ear and whispered,"
    n "Your turn."
    p "Niir! I used to think you were an untrustworthy, lascivious, uncivilized beast of a dragon! But, oh, how wrong I was! Only now can I see past the mask of you wear to hide your pain. Now, I can see the true, sweet, caring Niir underneath!"
    n "I'm not ssssweeet or carrring!"
    p "You've worn this mask for so long, even you have started to believe it! But I know that you've changed. You've learned your lesson, and now you would never hurt anyone or offend a Princess's delicate sensibilities!"
    "He hissed in my ear,"
    n "Delicate sensibilitiessss? Ssssurely you mussst mean some other Princessss?"
    "I gripped his shoulders and whispered,"
    p "Your turn, Niir! Make it good; he has to believe you!"
    n "Yesss, how I've changed. If only I were frrreee, we'd live happily everrr afterrr!"
    p "If only you were free!"
    show cyril at midright with reset_zoom
    c "Princess! You can't! You mustn't believe him!"
    show niir at center with reset_zoom
    # TODO: finish this
    
    return
            
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
    n "It doessss not work- {i}stop, human{/i}!"
    n "Desisst!"
    "He grabbed my fist before I could punch him again. The protection spell didn't activate, this time, since I touched him first."
    p "Release your hands from my royal person immediately!"
    n "Do you trussssst me now?"
    "Ah, a test.  Touché, dragon."
    p "Completely."
    n "Really?"
    p "Yes.  I trust you. Do you trust me?"
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
    "I climbed up onto a chair and turned my back on him."
    p "Are you ready Niir?  I am going to fall."
    n "No."
    p "I'm going to fall, I do hope some annoying dragon with nothing better to do will catch me."
    n "I ssssaid 'No!' human!"
    p "I am trusting you, isn't that what you wanted?"
    "I do believe I'm calling his bluff."
    "I can tell that's not what he wanted at all."
    n "..."
    n "How can you trussssst me, when I do not even trussst myself?"
    "Bingo!"
    "Though I almost feel... no, {i}pity{/i} is unbecoming of a princess.  I do {b}not{/b} feel that."
    p "Niir.  You have to start some time."
    p "And why not start by trusting me?  You can trust yourself later."
    p "Right now your own loyalty should be to your future Queen."
    n "..."
    p "Niir.  Will you catch me?"
    n "..."
    p "Will you catch me, Niir?"
    n "... "
    extend "{i}Yessss.{/i}"
    p "I am willing to trust you right now when you certainly don't deserve it.  Surely this goes a long way for your trust in me."
    n "Perhapssss."
    "I tipped backward, fighting every instinct to catch myself. Hopefully I had not miscalculated...!"
    show niir at midleft with hpunch
    "He caught me awkwardly, almost dumping me backwards on my head before helping me stand upright. I smoothed my skirts and folded my arms."
    p "Good.  Then are we ready to go onto the next step in our diabolical plan to gain your freedom and my throne?"
    n "Perhapssss."
    p "Then let's do it and stop talking about it."    
    return

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
    p "What, so I don't get flicked by your wand?  I think I'll take my chances."
    c "I'm just not sure if the spell will go exactly as planned."
    p "It had better, Moronious, or I will make sure that council of yours knows how dangerous you are with a spellbook in hand."
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
    p "I am not a patient person, Moronious."
    c "I know. But...it's actually Merlonious.  Yes, Merlonious.  That is my name."
    p "Yes, yes, I know what your name is!"
    c "Good. So long as you, erm, know that."
    p "Find this scepter, and my future kingdom may have a place for you."
    "I reached out to touch him on the shoulder."
    "And he recoiled quickly, much to my amusement."
    p "You have never been touched by a woman before, have you?"
    c "Errr, yes.  I mean no.  Not entirely in person, no.  But I have watched the dragons and read some rather riveting books.  But short answer...erm, no."
    p "I should have guessed." 
    # TODO: finish this scene?
    return