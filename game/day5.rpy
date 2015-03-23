# cyril dissuading against niir route
# DAY 5?!
label day5:
    scene bg bedroom dusk with fade
    play music princess_theme
    "I was just finishing the unoriginal-yet-edible breakfast Moronious had dropped off for me when there was a knock at the door."
    
    if (route == "Niir"):
        show cyril hat neutral at center with moveinleft
        c "I saw you, I'm begging your pardon.  I didn't want to have to bring this up but I feel compelled."
        c "I saw you, your highness."
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
                hide cyril with moveoutleft
                "But now... I will see what progress I can make with Niir today."
                scene bg corridor with fade
                "If I can find him..."
                scene bg dungeon with fade
                jump niir5
            "\"Maybe you're right...\"":
                p "That is not completely false. He does not know the meaning of respect."
                p "You on the other hand..."
                p "Someone like you would understand when a lady is in need."
                p "And has demands on her that only power can fulfill."
                c "P-p-power?"
                p "You must have some measure of power, or these dragons would have escaped long ago. Use it to help me rid the throne of my scheming sister Magnolia!"
                p "If you won't, I'll find someone else who will."
                c "I do want to help me, I mean, to help you, but... I need time!"
                p "Show me what you can do, then! I expect something concrete when I check in with you later today!"
                c "Y-yes Princess! I'll start right away!"
                hide cyril with moveoutleft
                "Useless! Everyone here is useless!"
                "In the meantime, I've got a little light reading I want to catch up on. It may even prove useful. Ah, my old favorite, {i}Draughts of Death, Destruction, and Devastation{/i}."
                scene black with fade
                "I feel much better, now. But I think that mage may require some... motivation to accomplish anything substantial."
                jump cyril5
                    
    elif (route == "Balrung"):
        show niir neutral at center with moveinleft
        n "What do you ssssee in that old tortoisssse?"
        p "Good morning to you as well, Niir."
        n "Balrrrung hassss no sensssse of fun, and he won't be easy to contrrrol. Even for you."
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
        "When I opened the door, there was nothing - except a slip of paper."
        b_write "Princess,"
        b_write "Meet me on the south tower this morning if you wish to discuss terms for my aid."
        b_write "\n-A Potential Ally"
        nvl clear
        p "Well, that sounds exciting! I wonder who it's from?"
        menu:
            "Stay here.":
                p "It's probably a ruse. If I went up there, someone might shove me off the tower to my death. Besides, I already have Moronious helping me out."
                p "Speaking of which, perhaps I'll go and see his progress."
                jump cyril5
            "Go and find out.":
                p "I'll go and find out. There's no harm in that, surely."
                scene bg exterior day with fade
                show balrung neutral at center, basicfade
                p "Oh! It's {b}you{/b}."
                show balrung smirk at basicfade
                b "Yes, it is I. I'm surprised at you, Princess."
                p "Why, because I followed your invitation?"
                show balrung determined at basicfade
                b "No. I am astonished that you have chosen to ally yourself with that ridiculous mage. I assumed you were more canny than that."
                p "You think {b}Moronious{/b} will betray {b}me{/b}?"
                show balrung smirk at basicfade
                b "Cyril's intentions are certainly pure, but he may not be willing to do what you want. He is not capable of murder."
                p "And you are?"
                show balrung determined at basicfade
                b "If necessary, yes. I've proved that; that's how I came to be cursed here."
                p "Who'd you do in?"
                show balrung neutral at basicfade
                b "Another time, perhaps. But here is the offer I will make to you - ally with me instead of that mage. Our interests align more closely, and I will not balk at your...more troublesome requests."
                p "How could you help me?"
                show balrung smile at basicfade
                b "I'm a {b}dragon{/b}, Princess. If I were free, I could fly you anywhere you wished. I could set fire to anything you desired. I could obliterate any building or army that stood in our way."
                p "Well..."
                menu:
                    "\"No. I don't trust you.\"":
                        p "I don't trust you, Balrung. Nor Niir. You may have potential for great destruction, but I see no reason to believe you will choose to do my will instead of your own."
                        show balrung determined at basicfade
                        b "As you wish, Princess. What a shame we could not be allies."
                        p "Do not hinder me, Balrung. I shall leave you alone if you do the same for me."
                        show balrung angry at basicfade
                        b "I make no promises. I have my own plans that you have no part in, now."
                        hide balrung with moveoutleft
                        p "Hmph."
                        "I better go see what Moronious is up to."
                        jump cyril5
                    "\"Perhaps you would be a valuable ally.\"":
                        p "Perhaps you would be a valuable ally. But what assurance do I have that you will aid me?"
                        show balrung neutral at basicfade
                        b "I have the same ambitions you do - to be free and have the power to control my own destiny. Aiding you will help me with those goals."
                        p "What is your plan?"
                        show balrung determined at basicfade
                        b "If you can convince Merlonious that I've found true love and reformed, he will have to let me go. In return, I'll help you regain your throne."
                        p "True love? How shall we do {b}that{/b}?"
                        show balrung smirk at basicfade
                        b "I have some ideas. And I trust you have your own methods of getting others to believe what you wish."
                        p "I do."
                        show balrung smile at basicfade
                        b "Why don't you meet me down in the dungeons in an hour, and we can spend some time together? If you can arrange so that Merlonious happens to find out where you are, you'll have set the stage for him to believe we are falling in love."
                        p "He seems to think you cannot change. How will you convince him otherwise?"
                        show balrung smirk at basicfade
                        b "As I have acted the recalcitrant criminal for forty years, when I suddenly do appear kind and loving, it will be very convincing."
                        p "Hmph. We'll see."
                        $ route = "Balrung"
                        jump balrung5

label balrung5:
    scene bg dungeon with fade
    show balrung neutral at center, basicfade
    play music balrung_theme
    show balrung smile at basicfade
    b "Princess! How lovely to see you. Your presence is like a light that makes even this gloomy dungeon seem like a sunny garden."
    p "You can save the flattery for later when Moronious can \"accidentally\" overhear you."
    show balrung smile blush at basicfade
    b "That wasn't for Moronious; that was for you, my lady. "
    show balrung smile at basicfade
    b "Would you care to play Queens and Pawns?"
    p "I suppose there's not much else to do in this wretched dungeon. You may go first."
    show balrung smirk at basicfade
    b "How generous of you."
    p "How did you come to be imprisoned here, anyway? I've heard you did something quite terrible."
    show balrung neutral at basicfade
    b "Terrible? Yes...but it's not that simple. Your turn."
    p "Interesting move. Tell me what happened. I want to hear your version of events, not just Moronious' self-righteous justification for your imprisonment."
    show balrung smirk at basicfade
    b "You want to hear it? Well..."
    menu:
        "Pay attention":
            show balrung determined at basicfade
            b "It starts with a human woman. Myriah. She was... like you, in many ways. Powerful. Ambitious. Intelligent.  Her Queens and Pawns strategies were always elegant and ruthless; her victories surprising yet inevitable."
            show balrung neutral at basicfade
            b "We met forty years ago. I was young, then, full of ideals of cooperation and mutual understanding. She was a mage who came to live among our kind to learn more about us and, though she never said it, to prove to us that humans were worth talking to."
            show balrung smirk at basicfade
            b "We played many games together. After her studies were complete and she returned to her Academy, I'd take on this feeble human form just to meet her there and match wits with her."
            show balrung angry at basicfade
            b "I'm not sure she understood how much of a sacrifice that was for me; how I was ridiculed, how many friends I alienated."
            "I was so caught up in what he was saying that I almost missed how he had setup his pawns in a chain reaction that was about to decimate my queens. But now that I had seen through his scheme it would be easy to unravel."
        "Focus on strategy.":
            show balrung determined at basicfade
            b "Human woman Myriah, blah, blah... forty years... blah, blah, cooperation... blah, blah ambitious, blah blah, strategies... blah, blah, sacrifice."
            "He's trying to draw my attention with his Queens while the Pawns setup a chain reaction! My Queens shall whittle down his defenses while he's not paying attention."

    p "Go on. Your move."
    show balrung neutral at basicfade
    b "So when I invited her to join me, permanently, as a part of a human-dragon marriage alliance, I thought she'd be honored. It was her life's work, after all."
    show balrung determined at basicfade
    b "But she refused. She wanted {b}me{/b} to join {b}her{/b}. You humans always want to be the ones in charge."
    p "Of course we do. But wouldn't that accomplish the same thing?"
    show balrung angry at basicfade
    b "It's completely different! You humans want to use us, subordinate us, rule us! I wanted an alliance of equal partners!"
    show balrung neutral at basicfade
    b "I should have waited. I should have elucidated my proposal more elegantly."
    p "What did you do?"
    show balrung smirk at basicfade
    b "When she chose not to come with me, I brought her anyway."
    p "You kidnapped her?!"
    show balrung angry at basicfade
    b "No! I would have let her leave, once she had listened to me! She refused to even talk to me! And her mentors were poisoning her mind against me. I had to bring her away from all of that."
    p "Hmph. Did it work?"
    show balrung neutral at basicfade
    b "No. No, it...didn't work at all. She used her magic, and her very life force, to create this...prison. To trap me in human form, and make it possible for her colleagues to trap other dragons who failed to conform to their human ideals of dragon behavior."
    menu:
        "Serves you right.":
                    p "Serves you right. That's what {b}you{/b} wanted to do to {b}her{/b}, after all - trap her with you."
                    show balrung angry at basicfade
                    b "I didn't want that. I wanted her to choose to be with me. But she chose to die instead..."
        "You loved her.":
                    p "You loved her, then?"
                    show balrung angry at basicfade
                    b "Of course I loved her! That was the point of the whole thing! But she chose to die rather than be with me..."
                    $ balrung_affection += 1

    p "You were a fool for discarding your strategy in favor of emotion. Much like in this game. Resign now, while you still can!"
    show balrung determined at basicfade
    b "Resign? But...oh, I see. I've lost, haven't I? Well done, Princess."
    show balrung neutral at basicfade
    b "Yes, I resign. I've learned that much from my mistakes, at least."
    p "Perhaps one day your strategy and emotion can be aligned towards the same goal."
    show balrung smile at basicfade
    b "One day...perhaps."
    show cyril hat neutral at midleft with moveinleft
    show balrung at midright with move
    play music cyril_theme
    c "Princess! You're here! With...Balrung?"
    p "Yes, we've just been enjoying a wonderful game of Queens and Pawns."
    show balrung smirk at basicfade
    b "She's quite a clever opponent! Quick-witted as well as beautiful, wouldn't you say, Merlonious?"
    c "Well, yes, of course, but-"
    p "Now, Balrung, stop flattering me so much or I shall begin to suspect you like me. Weren't you just saying dragons were incapable of that, Moronious?"
    c "Y-yes, they are! Maybe not all. But definitely this one!"
    show balrung smile at basicfade
    b "For a long time I feared you were right, mage, but perhaps I just hadn't met the right woman."
    c "The r-r-right woman?! Surely you don't mean Princess [p_name]?!"
    p "You don't believe I could induce feelings of love?! How cruel!"
    show balrung neutral at basicfade
    b "Yes, really, Merlonious, I would have thought you'd be more gentle with our dear Princess's delicate feelings!"
    c "Her delicate...feelings?!"
    p "Oh, yes, I'm quite overcome, I do think I might faint."
    c "Faint?! Um, well, ah, what should we do?!"
    show balrung smile blush at basicfade
    "I pressed my hand to my forehead and collapsed into Balrung's arms. That's what heroines of love stories are always doing; it should help convince that fool Moronious."
    scene black with fade
    c "St-stop that! You mustn't hold the Princess that way!"
    show balrung smirk at basicfade
    b "Really? You'd have preferred I let her head crack on this stone floor? I never thought you were so heartless, Merlonious!"
    c "Well, no, I wouldn't want that, but- I'm not- you can't!"
    show balrung smile eyes closed at basicfade
    b "I'll just set her her down here on my bed, where she can be comfortable until she wakes up."
    c "On your bed! No, no, that won't do at all!"
    scene bg dungeon 
    show balrung smile at center, come_closer
    with fade
    "He set me down gently, and I cracked one eye open. Balrung winked at me and I closed my eyes again."
    scene black with fade
    show balrung smile at basicfade
    b "Our poor Princess... she's been through so much."
    "He stroked my hair tenderly away from my face while Cyril sputtered. It was all I could do to keep from cackling with glee at his befuddlement. Balrung was quite the actor. Almost as good as me."
    c "Well I- I will just stay here and watch over the Princess until she recovers! I'll protect her from you, you, vituperous viper!"
    show balrung smirk at basicfade
    b "If you feel the need, by all means, do so. Though perhaps you might think about protecting her from your rudeness, since that is what got her into this position in the first place."
    n "Why is the Princesss pretending to sssleep on your bed?"
    show balrung smile eyes closed at basicfade
    b "I'm afraid she fainted. Merlonious made an indelicate comment and her poor constitution just couldn't take his boorish suggestions."
    c "That's not at all what happened! Is it? Oh dear, I would never be unkind to the Princess, not on purpose, but sometimes my batter is faster than my train! I mean, my chatter is faster than my brain..."
    "This was getting ridiculous. I think we had made our point, so I opened my eyes."
    scene bg dungeon with fade
    show cyril hat neutral at midleft, basicfade
    show niir neutral at midright, basicfade
    show balrung smirk at come_closer, basicfade   
    p "Oh, thank you, Balrung, for taking such good care of me. I don't know what came over me. But I'm so glad I can trust {b}you{/b}, at least."
    "I glared at the mage, hoping he would feel even more guilty."
    p "And now I will depart, so please excuse me."
    show balrung smile eyes closed at basicfade
    b "Until next we meet, Princess."
    
    return

label niir5:
    play music niir_theme
    $ niir_affection += 1
    p "Could you stop disappearing on me Niir!"
    p "I wish to confer with you!"
    show niir neutral at center with moveinright    
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
    show niir neutral at center, come_closer, basicfade

    p "Hold me like this, with your hands here, in case he peeks out."
    n "I can do that, at leassssst."
    p "Now, say things you like about me, and I will do the same for you. I've heard that's what lovers often talk about."
    n "I suppossse."
    n "Oh, Princessss, your...dresss is ssssooo...shiny. And your earsss are ssso...sstrange. How can you even hearrr with those tiny things?"
    c "Is that...Niir?! I've never heard him talk in such a positive manner."
    p "I suppose that's a start. Don't just compliment my body, though, or he won't believe it's true love!"
    n "You're sssoo deviousss, when I ssseee your scheming grin I jussst want to eat you up!"
    show niir with vpunch
    n "I mean, I jussst want to be good! And not kidnap any one elsssse."
    n "And only ssssteal you away if you assssk me to."
    "He bent his head close to my ear and whispered,"
    n "Your turn."
    p "Niir! I used to think you were an untrustworthy, lascivious, uncivilized beast of a dragon! But, oh, how wrong I was! Only now can I see past the mask you wear to hide your pain. Now, I can see the true, sweet, caring Niir underneath!"
    n "I'm not ssssweeet or carrring!"
    p "You've worn this mask for so long, even you have started to believe it! But I know that you've changed. You've learned your lesson, and now you would never hurt anyone or offend a Princess's delicate sensibilities!"
    "He hissed in my ear,"
    n "Delicate sensibilitiessss? Ssssurely you mussst mean some {b}other{/b} Princessss?"
    "I gripped his shoulders and whispered,"
    p "Your turn, Niir! Make it good; he has to believe you!"
    n "Yesss, how I've changed. If only I were frrreee, we'd live happily everrr afterrr!"
    p "If only you were free!"
    "I turned my face up to him and whispered,"
    p "Now kiss me!"
    n "..."
    "What was he hesitating for? Obviously he wanted to; it was practically all he could talk about."
    n "Thissss will not work."
    p "You've never actually kissed anyone, have you?! Well, we simply must remedy that right away." 
    "But before I could execute my plan, Cyril came running towards us. Niir's education would have to wait until later." 
    show cyril hat neutral at midleft, come_closer with moveinleft
    c "Princess! You can't! Y-You mustn't believe him!"
    show niir neutral at midright, reset_zoom, basicfade
    show cyril hat neutral at midleft, reset_zoom, basicfade
    p "Moronious! What a... surprise to see you here, interrupting our completely private conversation!"
    c "I warned you about him, Princess.  And I don’t believe any of this for a second!  You won’t fool old Cyril the Clever.  Errr, young Cyril.  I do quite forget my age some times."
    n "Nobody calls you Cccccyril the Cleverrr."
    c "I’m sure someone has called me that once.  I’m sure some time..."
    p "Cyril, I consider you somewhat of a friend. Niir is my friend, too, and it would be so dreadful if my friends couldn't get along. Can't you see how different he is now, how he's changed?!"
    c "Friend?  I do say!  I am glad that you see us like that Princess.  But I cannot say this dragon has your best interests at heart."
    n "My hearrrt is ssso full of love, I have no room for missschief." 
    p "There now, you see? Amazing, isn't it, what love can do in such a short time?"
    c "Well, I suppose there is no arguing with love.  But no.  "
    extend "It must be a trick."
    p "Moronious, you are dreadfully mistaken. But I will be generous and allow you a few days to change your mind."
    c "I propose a test if this is to go on.  Niir, you must prove this to me.  And then at the end I will test you both to see how well you know one another and how deep your commitment is to one another.  I do not let dragons leave willy-nilly you know."
    p "Our love is strong enough to pass your silly tests! I have no doubts about that."
    show niir smirk at basicfade
    n "Give us a few dayssss, and I'll know her well enough to passs any tessst..."
    show niir determined with vpunch
    "I kicked Niir in the shins. Was he truly so foolish?!"
    c "There is more to love than knowing, so don’t think the test will be that easy to pass."
    p "I am not concerned with your tests. "
    extend "Come, Niir, let us spend what little time we have together."
    
    return
            
label somethigh:
    p "Alright.  Fine."
    p "I'll show you some of mine if you show me some of yours."
    p "Trust."
    n "I thought you'd never offer."
    play sound "sfx/lightning.ogg"
    scene black with magic_flash
    # TODO: add vfx for Cyril's protection spell that got activated?
    p "Happy now?"
    n "Happy wouldn't be the word that I would ussssse."
    p "Well, now I know how Moronious' protection spell works. I'm surprised you're still conscious after that much electricity."
    n "You are no fun Princesssss."
    scene bg dungeon with fade
    show niir neutral at center, basicfade
    p "So there we go, I trust you enough with that, and now you trust me. Say it."
    n "Sssstill not convincccccced."
    show niir determined with hpunch
    n "Agh!  What wasssss that?"
    p "Convincing.  Hurry up and trust me or I'll do it again."
    show niir angry with vpunch
    n "It doessss not work- {i}stop, human{/i}!"
    show niir angry with hpunch
    n "Desisst!"
    show niir at come_closer, basicfade
    "He grabbed my fist before I could punch him again. The protection spell didn't activate, this time, since I touched him first."
    p "Release your hands from my royal person immediately!"
    show niir smirk at basicfade
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
    show niir neutral at midleft with hpunch
    "He caught me awkwardly, almost dumping me backwards on my head before helping me stand upright. I smoothed my skirts and folded my arms."
    p "Good.  Then are we ready to go onto the next step in our diabolical plan to gain your freedom and my throne?"
    n "Perhapssss."
    p "Then let's do it and stop talking about it."    
    return

label cyril5:
    
    # scepter progress
    # DAY 5
    scene bg library with fade
    show cyril hat neutral at center, basicfade
    play music cyril_theme
    
    $ cyril_affection += 1
    c "I found it."
    p "My scepter? You are not as infantile as you seem."
    p "I've actually been very impressed with the way you operate."
    p "Acting like you don't know a thing, and then astounding us all with your competence."
    p "Keeps the dragons on their toes as well, I presume."
    c "Errr... no.  I found my spellbook."
    c "It was right under my nose the entire time."
    p "..."
    p "Don't think because I'm banished I can't bring about your death."
    c "I'm dreadfully sorry."
    c "But now that I have my spellbook I can find some sort of locating spell, surely."
    p "You'd better, because I grow tired of waiting."
    c "Let's see here... locater-locater... lo-"
    c "Here!"
    c "It's not a locating spell but it does bring deep, powerful magical items to glow incessantly until I stop the spell."
    p "Then try it already!"
    c "I will, I will."
    c "Stand back, your highness."
    p "What, so I don't get flicked by your wand?  I think I'll take my chances."
    c "I'm just not sure if the spell will go exactly as planned."
    p "It had better, Moronious, or I will make sure that council of yours knows how dangerous you are with a spellbook in hand."
    c "More threats.  Jolly good, Princess.  I do think we're communicating quite well."
    c "You do look me in the eye when you're threatening me which is lovely, and gives me tingles all-"
    p "{size=+2}Just do the spell already!{/size}"
    c "Ah yes."
    
    c "{font=fonts/ankecallig-fg.ttf}Magia Luxis{/font}!"
    show cyril hat angry with magic_flash
    c "Something is blocking it... but the scepter is here, in this castle!"
    c "I'm so sorry, your Highness, but I need to study this more. Please be patient!"
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
    p "So, no one has ever held your hand, like this?"
    c "Errr, not in recent memory."
    p "Do tell me, how does it feel? You seem uncomfortable; do you dislike it?"
    "Such an amusing plaything!"
    c "I wouldn’t- I wouldn’t say {i}that{/i}." 
    p "And if I lean on your shoulder, like this...?"
    c "Oh dear.  I-I- do believe you have me flustered, Princess."
    p "Well, we wouldn't want that. I suppose I'd better leave you alone for now, even though there's so many other things I'd like to show you."
    c "Ah yes."
    c "..."
    c "I mean no, no, that isn’t necessary.  You don’t-"
    p "Don't worry; I know exactly what you mean. You don't have to explain to me. So, until next time..."
    c "Good night, P-Princess."
    "It's still midafternoon..."
    p "...Good night."
    return