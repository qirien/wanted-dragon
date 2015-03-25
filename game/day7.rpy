# DAY 7
label day7:
    # Another letter from home tells her that the Coronation is in two days!
    scene bg bedroom dusk with fade
    play music princess_theme
    "I've certainly made some progress here, even if things are moving rather slowly. Mother always said the best plans take time..."
    "She always had such beautiful schemes... but even they weren't enough to save her, in the end..."
    p "I will not end up like her! Dying peacefully, in my sleep, for no reason at all?! Ridiculous!"
    "I stomped over to the washbasin and scrubbed my face. The water was icy cold, but it felt refreshing."
    "I opened the window for some fresh air, and a pigeon swooped in carrying a scroll. I dreaded opening it; I was in no mood to hear from Father or Magnolia."
    p "Better get it over with..."
    k_write "\nMy sweet golden blossom Chrysandra,"
    k_write "I hope you can find it in your heart to forgive me for choosing Magnolia, but it was what your Mother wanted."
    k_write "We're holding the Coronation in two days; I hope you can come support your sister."
    k_write "[k_name] needs you; we need you!"
    k_write "All my love,"
    k_write "Your Father"
    nvl clear
    p "Mother wanted... Magnolia to be Queen?! No, no, no; it's impossible! I can't believe; I won't believe it!"
    p "It's true, she's more beautiful and more kind and smiles more and doesn't poison people... but Mother always said I was intelligent!" 
    p "She said a Queen needed to be clever, and always one step ahead of everyone else. Was she lying? Was she just humoring me?!"
    p "No... Magnolia must have tainted Father's mind, twisted Mother's words to her own advantage!"
    p "It's all {b}her{/b} fault!"
    p "..."
    p "Well. She will find out just how clever a Queen needs to be! I have my own plans! I'll need to work a bit faster if the coronation is in two days, however."
    
    p "I need to think. I'll think better while I walk."
    scene bg corridor with fade
    p "This castle is so huge..."
    
    if (route == "Cyril"):
        scene bg library with fade
        if (cyril_insanity >= INSANE):
            "I ought to ask Cyril if he has anything new to report."
            jump mage_insane
    
        p "If I had time, I'd read all these books and uncover all their secrets. But instead..."
        call cyril7
        
    elif (route == "Balrung"):
        scene bg stairs day with fade
        p "If I had time, I'd search it day and night for secrets. But instead..."       
        call balrung7
        
    elif (route == "Niir"):
        scene bg stairs day with fade
        p "If I had time, I'd search it day and night for secrets. But instead..."    
        
        call niir7
        
    return

    
label mage_insane:
    p "Cyril? CYRIL! Hmmm.  Usually he responds to my summons right away. Where can he be?"
    scene bg stairs day with fade
    "I hear noises coming from the dungeon..."
    scene bg dungeon with fade
    show balrung neutral at center, basicfade
    show niir neutral at quarterright, basicfade
    show cyril hat neutral at quarterleft, basicfade
    play music cyril_theme
    
    b "It took only a few short years of solitude to lose your mind."
    b "Are you sure she's even real?"
    c "Yes!  Of course I am!"
    n "Sssshe's interested in you.  Ssshe must not be real."
    c "She is real.  She is the real princess.  Here she is; just look at her!"
    b "Are you sure about that?"
    n "I can't ssssee a thing."
    p "You blithering fool, Cyril.  They're playing you."
    p "Of course I'm real."
    c "She says she's real!"
    b "Exactly what a false princess would say, don't you think?"
    n "Exacccctly."
    p "Cyril the Clueless.  You astound me.  I came here for a dragon."
    p "But despite your many inadequacies - and there are many - I found myself drawn to you."
    c "I do find it highly unlikely that an apparition would call me inadequate and clueless."
    b "Unless you were making her up to be realistic."
    c "I am!  I am!  So true!  I just wanted it to be true!"
    "Is he for real?"
    p "Oh for the love of..."
    menu:
        "Kiss him.":
            call mage_insane_kiss
        "Step on his toes.":
            call mage_insane_step
            
    return
            
label mage_insane_kiss:
    show cyril hat smile blush eyes closed at center, come_closer, basicfade
    "..."
    c "Ah, sweet, sweet apparition."
    show cyril hat smile blush at center, reset_zoom
    c "I'm afraid this is the closest that we're going to get to being together for real."
    p "Cyril the Crazy, I just kissed you."
    c "And I'm going to spend all my years in this castle imagining you."
    p "You are completely insane."
    c "Insane with love, my dear."
    p "No, insane with insanity.  I'm leaving."
    c "But you can never leave, as you are in my mind."
    p "Watch me."
    "That was no help at all!"
    return
    
    
label mage_insane_step:
    c "Ouch!  You trod on me!"
    p "Would an imaginary person do this?" with hpunch
    p "Or this?" with hpunch
    c "Ow!  Ow!  Ow!"
    c "I suppose not.  You must be real after all."
    p "Yes, and don't you forget it."
    p "Now, get back to work helping me find a way to reclaim my rightful throne!"
    return
  

label cyril7:
    show cyril hat neutral at center with moveinleft
    play music cyril_theme

    p "...I always find myself talking to you."
    c "So, Princess.  I had something I wanted to discuss with you."
    show cyril hat smile at basicfade
    c "I think you'd make a rather good sounding board and I am terribly grateful for what you did yesterday."
    c "I think Niir will think twice next time before he-"
    p "Did you just compare me to a sounding board, mage?"
    show cyril hat concerned blush at basicfade
    c "Oh, well.  Not intentionally."
    show cyril hat smile blush at basicfade
    c "I don't think you're anything like a piece of board.  You're much more... lively than that."
    p "Lively.  Yes.  One would {i}hope{/i} so."
    show cyril hat neutral at basicfade
    c "Anyway, I know it is my duty to guard this castle and these dragons.  It is something I take most seriously, but recently I have been made an offer-"
    p "To study under Grivvorn.  Yes.  I am aware of that offer."
    menu:
        "\"I think you should take it.\"":
            $ cyril_affection += 1
            show cyril hat surprised at basicfade
            c "Oh really?  Do you really think so?"
            show cyril hat laugh at basicfade
            c "I was hoping that I wasn't just being presumptous."
            c "It was hard to imagine that they wanted {i}me{/i}.  But if you really think it would be worth taking and worth giving up my post for."
            p "Well, your magic is rather pathetic Cyril.  And if you don't get any better, then how can you aid me?"
            p "It doesn't do us any favors to have you grow old here and forget spells for the rest of your days."
            show cyril hat smile at basicfade
            c "So you see a future?"
            show cyril hat smile blush at basicfade
            c "I mean, with us.  Between us.  Errr, together."
            p "Possibly.  But you would need to be more powerful.  "
            extend "And wear that ridiculous hat a lot less."                
            show cyril hat concerned blush at basicfade
            c "I feel quite unclothed without my hat.  But I mean, I could.  {i}For you{/i}."
            show cyril smile blush at basicfade
            "And then he took off his hat and looked at me with those pathetic puppy dog eyes of his as if he was begging for some kind of approval from me."
            "Tsh.  Most unappealing.  Even though I know he would be loyal if I let him down, I feel as though I should at least bite my tongue."
            p "That's a start, Cyril.  And after you go away and make yourself useful then maybe we can take more steps forward."
            c "I- I'd like that, your Highness."
            "He turned away, embarrassed, and put his hat back on."
            
        "\"That offer is a complete waste of my-I mean your time.\"":        
            c "Well, yes.  It was rather perposterous come to think of it."
            c "I do have a duty, and I am a man of my duty and of my word."
            c "I couldn't just simply..."
            "It is sad to see him try to justify not going like this."
            "But if he goes, someone harder to manipulate will take his place."
            "And then where will I be?"        
            "Somebody had to make the hard choices around here, and as usual, that somebody had to be me."
            p "Yes, your loyalty is to the dragons.  Anyone with eyes can see that."
            p "You know their best interests and you put them above your own."
            p "That is what makes you such a good dragon keeper.  However, I could help you out if you only said the word."
            c "You would do that, for me?"
            p "Of course I would Cyril.  You can trust me with these crafty dragons."
            
    show cyril hat laugh at basicfade
    c "I thank you Princess.  You have been a great sounding board.  Person.  Great sounding person."
    c "Oh! I almost forgot! I have something for you!"
    p "Hand it over, then! I am...fond of presents."
    "What could he possibly find here that is fit for a princess, I wonder?"
    c "It requires a spell… oh, what is it?! I practiced it just fine this morning!"
    c "Oh yes! Vitreo Calceatus!"
    p "..."
    c "I'm sorry; maybe that was inappropriate?"
    p "Where is it?!"
    c "Oh! On your feet, your Highness!"
    p "...you changed my shoes. Without asking."
    "I poked my feet out from under my skirts and peered down at them. They were encased in form-fitting shoes...made of glass? Oh no. He didn't."
    c "I'm sorry! I read this story once, and it sounded so elegant, but perhaps it's not to your liking?!"
    "I was wearing glass slippers."
    "My feet were getting sweaty already."
    menu:
        "They're lovely.":
            $ cyril_affection += 1
            p "No, no, it's...they're...lovely."
            "I'm not sure why I told him that. The soles of my feet were already starting to feel sore, and I could tell if I moved I would have blisters all over."
            c "Really?! Oh, I'm so comfortable you're glad. I mean, glad you're comfortable."
            p "What a...thoughtful gift."
            p "But...I would like to look at them more closely. Would it be possible for you to remove them and place them in my hands? I wouldn't want to break them."
            c "Right away!  I’ll just get down here and - "
            hide cyril at center with moveoutbottom 
            extend "Just one..."
            p "Please tell me they are not stuck."
            c "If you’d just bear with me...  "
            show cyril hat smile blush at center with moveinbottom
            extend "There we go.  You may observe your shoes, your Highness."
            "Whew. If I'd had to wear those any longer...But they did look lovely."
            p "I believe they would look best decorating my room. It still looks as though a reclusive wizard lives there, for some reason."
            c "Yes!  Your room!  I’m sorry I have yet to make it fit for a princess.  Perhaps later I can try to make it more accomodating."
            p "Yes, it certainly could use a thorough cleaning. And you may remove your dirty socks from under the bed."
            c hat blush "Oh my!  I’d forgotten about those!"

        "They're ridiculous.":
            p "This is the most ridiculous pair of footwear I've seen in my life. Not only are they a terrible tripping hazard to my royal person, but they will rub on my heel and give me blisters!" 
            p "Are you trying to injure me, Cyril?!"
            c "Errr, no.  That wasn’t my intention, I assure you!  Here, I’ll just ah, sit down please your Highness and I will remove these shoes for you."
            p "Yes, immediately!"
            hide cyril at center with moveoutbottom 
            c "They are a little tighter than expected.  Just wait a moment."
            p "They had better not be stuck!"
            show cyril hat concerned blush at center with moveinbottom
            c "And there.  I am dreadfully sorry."
            p "Whoever heard of shoes made of glass?! It sounds like an assassination weapon, if you ask me."
            c "Oh well.  I thought it was regular princess wear.  I suppose I was mistaken.  It won’t happen again, Princess."
            p "I won't count on that."

    "The door opened, revealing the other two denizens of the castle. Really, one would think I had invited everyone for a party or something."
    show balrung smirk at quarterleft, basicfade
    show niir neutral at quarterright, basicfade
    with moveinleft

    show cyril hat surprised at basicfade
    b "Oh ho ho.  What have we here?  A princess wasting her time with a mage?"
    c "Now, now.  The princess was only helping me come to a conclusion."
    show niir mischief at basicfade
    n "Sssso, when you have thisss delectable princesss all to yoursssself, the thing you care about getting isss advicccce?"
    n "Ssssuch a sssshame."
    show cyril hat concerned at basicfade
    c "Yes, well.  It is important.  There are so few trustworthy people around here."
    show balrung determined at basicfade
    b "Out of all the princesses, I didn't think you'd be the type to hold such incompetent company."
    p "He's holding {b}you{/b} here isn't he?  So I would think the mage isn't quite as useless as you would have everyone believe, Balrung."
    p "Not that your attitude does much for your reputation either Cyril.  You should really teach these dragons more of a lesson."
    show cyril concerned blush at basicfade
    c "Well, perhaps... thank you, Princess."
    return            
          
    
    return
    
label niir7:
    scene bg hall with fade
    play music niir_theme
    
    p "...I always run end up running into you."
    show niir neutral at center with moveinright
    n "Thissssss."
    p "What is it, Niir?  I am in a predicament and do not have time for riddles - from you or the mage."
    n "Take it."
    p "Did you wrap this? And put a...bow on it? ...Did Balrung put you up to this?"
    n "..."
    n "I’m waiting Princessss."
    p "I'm suspicious. It's probably lingerie or something equally tasteless."
    n "Only the besssst for you, Princess.  Open it."
    p "I'm warning you...if you try to toy with me, I'll- oh!"
    p "It's...mother's amulet!"
    n "It’ssss yourssss."
    p "Where did you find this?! She lost it many years ago, when I was a child..."
    "I fingered the necklace gently. This was proof that she wanted {b}me{/b} to be Queen."
    n "Who ssssaid I found it?"
    p "Where. Did. You. Get it?!"
    n "It wasss around, and I ssssnatched it up."
    n "Don’t worry, Princesss.  I did not ssssteal.... thissss."
    n "Ssssomething else perhaps."    
    p "Around where?!"
    n "Curiousss, aren’t we?"
    n "Don’t you like your gift?  You got one for me, ssso I returned the favor."
    p "I- thank you."
    n "In that casssse, perhapsss I have more thingsss hidden away that might be of interessst to you."
    p "Is there anything else of hers? Or with the royal seal?"
    n "That isss one of a kind."
    n "And not the only thing that issss one of itsss kind."
    p "To what are you referring?"
    n "Issssn’t it obvioussss?"
    p "I haven't seen your hoard, so I don't know what you have in there."
    n "It’ssss not like you, Princessss, to be thissss denssse."
    p "And it's not like you to outright insult me. I don't have time for play; my sister will be crowned in three days unless I can find a way to stop her!"
    n "Your ssssisster hasss nothing on you, Princesss.  You are not like other princessesssss."
    p "Well, you wouldn't have fallen in love with just any old princess. Actually, perhaps you would have, now that I think about it."
    n "Fallen?  {i}Balrung, that sssscheming Balrung{/i}.  He issss to blame for putting ideassss into your head."
    p "Well, it matters little what you think. What matters is stopping my sister! Will Moronious let you go, do you think?"
    n "... "
    n "Perhapssss, if he has amnessssia."
    p "We could try blunt head trauma, but if it didn't work then he certainly wouldn't let you go. What sort of spells does he have keeping you here?"
    n "If we try to esssscape, we fall unconscioussss.  And he takesss us back insssside the cassstle."
    p "What if he couldn't find you? Or when you woke up, you were outside his spell? How far does it go, anyway?"
    n "All around the entrancccce, the exitssss, the sidessss.  It isss all covered."
    n "Are you sssugessting you’ll hide me?"
    p "Yes...or perhaps I could move you past the spell. "
    n "Did you want to practicccce?"
    n "Perhapsss in your room.  With the door closssssed."
    p "Once I'm Queen, then I'll have time for such frivolous activities. But, you are right that we should practice. Lie down and pretend to be unconscious. I will see if I can move you."
    hide niir
    n "Thissss isss lesss fun than I expecccted."
    p "Hyaaah! What have you been eating, you enormous useless lump?!" with vpunch
    n "Exccccept for that rabbit, nothing but tasssstelesssss vegetable ssstew."
    "I couldn't lift him at all; he seemed more dense than a normal human. I grabbed him under the arms and was able to slide him across the castle tiles down the hallway."
    n "That hurtsssss Princessss."
    p "Poor baby Niir; I thought you could take a little rough handling."
    n "I prefer to be the one giving the punissssshment."
    p "Don't give it if you can't take it- oof!"
    show niir neutral at center,come_closer with vpunch
    "I fell back and sat on the floor, Niir's head in my lap. He was probably enjoying this way too much..."
    menu:
        "Shove him away.":
            p "Get off me, you salacious serpent!"

        "Tease him a bit.":
            $ niir_affection += 1
            p "You're enjoying this, aren't you?"
            n "I can make it more enjoyable if you wissssh. You did it on purpossssse, didn’t you?"
            p "I'm sure I don't know what you're talking about. Though, now that I look at you from this angle...your ears are very strange. What purpose does their strange shape serve?"
            n "Touch them and guessss if you prefer but my lipsss are sssealed."
            p "Hmph. Now I feel both curiousity and revulsion. Not a mix of emotions I enjoy. Get up, now."
            n "What if I ssssay no?"

    show niir angry at center,reset_zoom with vpunch
    "I stood up and his head hit the ground with a crack."
    n "You clumssssy princessss.  What did you do that forrrrr?"
    p "I need some way to make you lighter, or myself stronger..."
    n "Impossssible.  Perhapssss you need to learn magic."
    p "I don't need magic! Magic is for weaklings and sycophants."
    p "But there may be another way...I must do some research, alone. You may leave me now. But you have been an excellent test subject. And-"
    p "Thank you, for my mother's amulet. She was the only one who really understood me."
    p "If she was still alive- "
    extend "But, she's not."
    n "I am sssssure ssshe was extraordinary, jusssst like you."
    p "There, you see, that wasn't so hard to flatter like a proper minion should."
    n "It wassss not flattery, and I am not yourrrr minion, Princesssss."
    p "I suppose we did agree to be partners."
    n "Yessss, I will hold you to... that.  I sssshall leave, as you asssked."
    n "Ssssee you ssssoon, Princessss."

    "Niir was so uncomplicated, I felt confident that I could control him once he was free." 
    "But, in some ways, I wished it wasn't so easy. Would he love me as well if I hadn't tricked him into doing so? Was it even love at all?"
    "...It was pointless to even think about it. He could help me regain the throne; everything else could wait until after that."
    return

label balrung7:
    scene bg dungeon with fade
    show balrung neutral at center, basicfade
    play music balrung_theme
    
    p "...I always seem to find myself here."    
    p "Is that a scroll? Are you writing a letter?"
    show balrung smile at basicfade
    b "Princess! I was not aware you had joined me. I'd better put this away..."
    p "Not so fast! Let me see that."
    show balrung smile blush at basicfade
    b "Oh, Princess, you don't want to read this old man's ramblings..."
    p "Is this... Dragon poetry? Did you write this?"
    show balrung neutral at basicfade
    b "It's not worthy of your attention, please don't..."
    p "Too late! Oh ho ho!"
    b_write "She:"
    b_write "Eyes shine noble, latent traps"
    b_write "Supreme mischief."
    b_write "Face sly, young, gold"
    b_write "Defang grand dragons’ scheme."
    b_write "Map pulse’s sussurus,"
    b_write "sweet tyrant."
    "This is... about me?! No one's ever written a poem in my honor before..."
    p "I--"
    show balrung smile blush at basicfade
    b "It's terrible, I apologize that you had to see that. I'll just dispose of this awful drivel--"
    p "No. No, I'll keep this."
    show balrung smirk at basicfade
    b "Indeed? Well... I'm sure you didn't come here to read the musings of an old dragon. Or did you come just to keep me company?"
    p "No, I am going to explore the castle, looking for powerful secrets, and you may join me."
    show balrung neutral at basicfade
    b "How generous of you. "
    extend smile "But, perhaps I can take you someplace that you will enjoy. A part of the castle I'm sure Cyril didn't show you."
    p "Yes, perfect. But we need to make sure he finds us lost in deep conversation at some point in our walk."
    show balrung smirk at basicfade
    b "That can certainly be arranged."
    hide balrung at center with moveoutleft
    
    scene bg gate day with fade
    show balrung neutral at center with moveinleft
    b "It's outside the castle proper, but still within the walls. Fortunately, it is also still within Merlonious' wards."
    p "Wards?"
    show balrung determined at basicfade
    b "The wards that keep us from simply walking away."

    hide balrung at center with moveoutright
    scene bg ruins with fade    
    show balrung neutral with moveinleft
    p "What would happen if you tried to walk through the wards?"
    show balrung angry at basicfade
    b "The last time I attempted to do so, I fell unconscious for two weeks."
    p "How long ago was that?"
    show balrung determined at basicfade
    b "When Merlonious first arrived here. As he was new, I thought perhaps he would not be as strong as some of the previous guardians." 
    b "But I underestimated him. A mistake I don't intend to repeat."  #TODO: how many years ago was that?
    p "So that's why he doesn't trust you?"
    show balrung neutral at basicfade
    b "That, and the fact that I've been here so long. He believes that if I could have changed, I would have done so already."
    p "Where are the wards?"
    show balrung determined at basicfade
    b "Right...here. You may go through them; they only affect dragons. Sadly, they also prevent any of my comrades from coming to my aid."
    menu:
        "But you promised Niir you would come back for him.":
            $ balrung_affection += 1
            p "So you lied to Niir, when you told him you would come back for him."
            show balrung smile at basicfade
            b "No, I-- ah. You've been spying on me, have you?"
            p "Of course. Haven't you been spying on me as well?"
            show balrung smirk at basicfade
            b "Perhaps. But, no, I didn't lie to Niir; I would come back for him, though I would need either humans I could trust or many other dragons to break the barrier."
            p "Are there many other dragons you could count on?"
        "Comrades? You mean other dragons?":
            p "You have dragon... friends? Out there?"
    
    show balrung determined at basicfade
    b "There are many dragons whom I once numbered among my allies. But they have been deceived by you humans, trading their power and heritage to pacify your panicky masses." 
    b "They marry humans, live as humans, and their offspring are barely distinguishable from ordinary humans."
    show balrung angry at basicfade
    b "Most of them don't even take dragon form anymore. Your kind finds it too frightening."
    menu:
        "I would not be frightened.":
            p "I would not find it frightening."
            show balrung smile at basicfade
            b "No? No, you would not. You should be a dragon, Princess; you're unafraid, aggresive, and more than a little arrogant."
            p "Yes, you understand me perfectly. There's not a way, is there?"
            show balrung neutral at basicfade
            b "A way for what?"
            p "A way for me to become a dragon. It would be quite useful."
            show balrung smile eyes closed at basicfade
            b "Ha! I'd like to see that! No, there's no way I know of. Unless Merlonious knows of some esoteric transmogrification, or there's been some new alchemical advances."
            p "Hmmm, an interesting area of study."
        "What is your dragon form like?":
            p "What do you look like? As a dragon, I mean?"
            show balrung neutral at basicfade
            b "What do I look like? Hmmmm... It's been so long, and I wasn't even full-grown when I was trapped here." 
            b "But I do remember long limbs covered with burgundy scales, long teeth sharp enough to pierce a deer's heart in one bite, and, oh, the wings!"
            show balrung smile at basicfade
            b "I remember the wings most of all; the feeling of beating upon the wind, a battle every time I'd take to the air, and the surge of victory with every new voyage."
            p "How can they keep you from such power? I could not imagine a worse punishment."
            show balrung determined at basicfade
            b "Yes. Well, that was the idea."
       
    "We walked in silence after that, until we arrived back at the castle gates. The mage was there waiting for us."
    scene bg gate dusk with fade
    show cyril hat neutral at midleft, basicfade
    show balrung neutral at midright with moveinright

    show cyril hat surprised at basicfade
    c "P-princess! There you are! When I couldn't find you, I was so worried that some nasty dragon had done something terrible to you!"
    p "Moronious, you've just ruined our lovely walk. We were conversing deeply, and then walking together in silence, as people who are in love often do."
    show cyril hat concerned blush at basicfade
    c "In- in love?! It's not possible! Don't let him ensnare you, Princess, I implore you!"
    p "I am not ensnared by anybody. I love him of my own free will."
    show balrung smirk at basicfade
    b "Yes, despite your best efforts, we are in love. Will you deny it?"
    show cyril hat angry at basicfade
    c "D-deny...I- you- Yes! You cannot be in love! Can. Not. I know you, dragon; you {b}cannot{/b} love!"
    show balrung determined at basicfade
    b "You would allow your personal hatred of me to mar the Princess's happiness?"
    show cyril hat concerned at basicfade
    c "Sh-she would not be happy! Not with you. Impossible!"
    show balrung angry at basicfade
    b "Mage, of all the hearts in this castle, I fear yours is the coldest. You know how long I've languished here. Yet you would deny me forgiveness, even after I've paid the price many times over?"
    show cyril hat concerned blush at basicfade
    c "It's- but the Princess- she can't...I know you're plotting something!"
    p "It is {b}your{/b} plot that we are discussing, Moronious. Your plot to keep the dragons here forever."
    show balrung determined at basicfade
    b "What would it take, Merlonious? Is there anything, {b}anything{/b} that could convince you I no longer deserve this suffering, this abuse?!"
    show cyril hat concerned eyes closed at basicfade
    c "..."
    show cyril hat angry at basicfade
    c "...No. It's not possible; it's impossible. You can't! You. Can't. Love."
    show balrung angry at basicfade
    b "..."
    menu:
        "You're wrong, Moronious.":
            $ balrung_affection += 1
            p "You're wrong, Moronious. You don't get to decide who can love and who can't."
            show balrung determined at basicfade
            b "Apparently he does."
        "You're right; Balrung cannot love.":
            p "You're right, Moronious; Balrung will do anything to get his power back. Much like I will. And if you will not help us, then you are our enemy."
            jump our_enemy
        "It's a different kind of love.":
            $ balrung_affection += 1
            p "Just because we're not moping about with addled brains or senseless with passion, does that mean it's not love? Or is it just a different kind than you're used to?"
            show balrung determined at basicfade
            b "I don't think he knows what love is at all, outside of a fairy tale."
            
    show cyril hat concerned at basicfade
    c "No! Love is kind; it helps people be better, it makes people happy! You two just want, just want power!"
    p "And who says you can't have both?!"
    show balrung neutral at basicfade
    b "Princess-"
    p "No, Moronious! I want both! And I WILL get what I want! You won't dare to try and stop me!!!"
    
label our_enemy:    
    show cyril hat angry at basicfade
    c "Yes, I- will, I am. I don't want to be your enemy, Princess, but if you side with him against me, th-then, I'll have no choice."
    p "What will you do? Banish me from this castle, too?"
    show cyril hat surprised at basicfade
    c "No! I...I don't want to hurt you!"
    show balrung angry at basicfade
    b "You claim to be all about love, and yet you would devastate our Princess. Come, Chrysandra, let's discuss our new plans privately."
    show cyril hat angry at basicfade
    c "New plans?! I knew it! I told you he had plans! You can't trust him, Princess!"
    p "I'll decide whom to trust, Moronious, and it certainly isn't you."
    hide balrung at midright with moveoutleft
    
    scene bg bedroom candle with fade
    show balrung neutral at center with moveinleft
    p "In here. He won't dare come in without knocking."
    show balrung angry at basicfade
    b "I apologize, Princess. Though I didn't underestimate Merlonious' power, this time I underestimated his vindictiveness."
    p "No, it's all right. We'll just plan something else."
    show balrung smirk at basicfade
    b "We?"
    p "Yes, of course; who else would I trust?"
    show balrung smile eyes closed at basicfade
    b "Who else, indeed?"
    p "I could poison him, though he'll be suspicious of both of us, now. Perhaps that sleeping perfume?" 
    p "No, his spell must still be active while he's asleep, otherwise you could just escape at night. Hmmm..."
    show balrung smirk at basicfade
    b "I wasn't lying, you know."
    p "Hmm? Wasn't lying about what?"
    show balrung smile blush at basicfade
    b "About being in love with you. Of course I said it so he could hear me, but... well..."
    p "Oh that! Yes, of course you're in love with me. That's why I can trust you."
    show balrung determined at basicfade
    b "..."
    p "So, it seems like the next step in our plan will be to kill Merlonious."
    show balrung neutral at basicfade
    b "Perhaps. Let us meet again tomorrow; there is something that could help us that I must research alone."
    p "Yes, it is getting late, isn't it?"
    show balrung smile blush at basicfade
    b "But for now, my lady..."
    show balrung at come_closer, basicfade
    "He bent down and kissed my forehead. Was this what it felt like to have someone be in love with you? It felt like...{b}power{/b}, delicious and thrilling."
    menu:
        "Kiss him back":
            $ balrung_affection += 1
            "I wanted more."
            "I grabbed his vest and pulled his head down to my level."
            show balrung determined at basicfade
            p "You will kiss your queen goodnight."
            show balrung smile blush at basicfade
            "It was the perfect kiss; just long enough to ignite passion, just firm enough to imply strength, and just gentle enough to signify tenderness."
        "Slap him":
            "If he thought a little kiss on the forehead was going to turn me into a simpering pliable damsel, he was greatly mistaken."
            $ balrung_affection -= 3
            show balrung determined at reset_zoom with hpunch
            p "You presume too much, minion."
            show balrung neutral at basicfade
            b "Really? Hmmm... we shall see."
            
        "Say good night":
            "I needed to remain aloof enough to keep him under my control. I took a step back."
            show balrung at reset_zoom, basicfade
            p "Good night, Balrung."
    
    show balrung smirk at basicfade
    b "Goodnight, my Queen."
    scene black with fade
    return
