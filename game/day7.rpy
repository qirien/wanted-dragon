# DAY 7
label day7:
    # Another letter from home tells her that the Coronation is in three days!
    
    
    # Whoever's route she didn't choose hinders her?
    if (route == "Cyril"):
        call cyril7
        
    elif (route == "Balrung"):
        call balrung7
        
    elif (route == "Niir"):
        call niir7

label cyril7:
c "So, Princess.  I had something I wanted to discuss with you."
c "I think you'd make a rather good sounding board and I am terribly grateful for what you did yesterday."
c "I think Niir will think twice next time before he-"
p "Did you just compare me to a sounding board mage?"
c "Oh, well.  Not intentionally."
c "I don't think you're anything like a piece of board.  You're much more... lively than that."
p "Lively.  Yes.  One would {i}hope{/i} so."
c "Anyway, I know it is my duty to guard this castle and these dragons.  It is something I take most seriously, but recently I have been made an offer."
p "To study under ---.  Yes.  I am aware of that offer."
menu:
	"\"I think you should take it.\"":
	    $ cyril_affection += 1
		c "Oh really?  Do you really think so?"
		c "I was hoping that I wasn't just being presumptous."
		c "It was hard to imagine that they wanted {i}me{/i}.  But if you really think it would be worth taking and worth giving up my post for."
		p "Well, your magic is rather pathetic Cyril.  And if you don't get any better then how can you aide me?"
		p "It doesn't do us any favors to have you grow old here and forget spells for the rest of your days."
		c "So you see a future?"
		c "I mean, with us.  Between us.  Errr, together."
		p "Possibly.  But you would need to be more powerful.  "
		extend "And wear that ridiculous hat a lot less."		
		c "I feel quite unclothed without my hat.  But I mean, I could.  {i}For you{/i}."
		show cyril smile
		"And then he took off his hat and looked at me with those pathetic puppy dog eyes of his as if he was begging for some kind of approval from me."
		"Tsh.  Most unappealing.  Even though I know he would be loyal if I let him down, I feel as though I should at least bite my tongue."
		p "That's a start, Cyril.  And after you go away and make yourself useful then maybe we can take more steps forward."
		c "I- I'd like that your highness."
		
	
	"\"That offer is a complete waste of my-I mean your time.\"":	
		c "Well, yes.  It was rather perposterous come to think of it."
		c "I do have a duty, and I am a man of my duty and of my word."
		c "I couldn't just simply..."
		"It is sad to see him try to justify not going like this."
		"But if he goes, someone harder to manipulate will take his place."
		"And then where will I be?"	
		"Somebody had to make the hard choices around here and as usual that somebody had to be me."
		p "Yes, your loyalty is to the dragons.  Anyone with eyes can see that."
		p "You know their best interests and you put them above your own."
		p "That is what makes you such a good dragon keeper.  However, I could help you out if you only said the word."
		c "You would do that, for me?"
		p "Of course I would Cyril.  You can trust me with these crafty dragons."
		#MORE MANIPULATING?  IDEAS?

    
    return
    
label niir7:
    n "Thissssss."
    p "What is it, Niir?  I am in a predicament and do not have time for riddles - from you or the mage."
    n "Take it."
    p "Did you wrap this? And put a...bow on it? ...Did Balrung put you up to this?"
    n "..."
    n "I’m waiting Princessss."
    p "I'm suspicious. It's probably lingerie or something equally tasteless."
    n "Only the besssst for you, Princess.  Open it."
    p "I'm warning you...if you try to toy with me, I'll- oh!"
    p "It's...mother's amulet."
    n "It’ssss yourssss."
    p "Where did you find this?! She lost it many years ago, when I was a child…"
    n "Who ssssaid I found it?"
    p "Where. Did. You. Get it?!"
    n "It wasss around, and I ssssnatched it up."
    n "Don’t worry, Princesss.  I did not ssssteal…. thissss."
    n "Ssssomething else perhaps."    
    p "Around where?!"
    n "Curiousss, aren’t we?"
    n "Don’t you like your gift.  You got one for me, ssso I returned the favor."
    p "I- thank you."
    n "In that casssse, perhapsss I have more thingsss hidden away that might be of interessst to you."
    p "Is there anything else of hers? Or with the royal seal?"
    n "That isss one of a kind."
    n "And not the only thing that issss one of it’sss kind."
    p "To what are you referring?"
    n "Issssn’t it obvioussss?"
    p "I haven't seen your hoard, so I don't know what you have in there."
    n "It’ssss not like you, Princessss, to be thissss denssse."
    p "And it's not like you to outright insult me. I don't have time for play; my sister will be crowned in three days unless I can find a way to stop her!"
    n "Your ssssisster hasss nothing on you, Princesss.  You are not like other princessesssss."
    p "Well, you wouldn't have fallen in love with just any old princess. Actually, perhaps you would have, now that I think about it."
    n "Fallen?  {I}Balrung, that sssscheming Balrung{/i}.  He issss to blame for putting ideassss into your head."
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
    n "Exccccept for that rabbit, nothing but tasssstelesssss ssstew."
    "I couldn't lift him at all; he seemed more dense than a normal human. I grabbed him under the arms and was able to slide him across the castle tiles down the hallway."
    n "That hurtsssss Princessss."
    p "Poor baby Niir; I thought you could take a little rough handling."
    n "I prefer to be the one giving the punissssshment."
    p "Don't give it if you can't take it- oof!"
    "I fell back and sat on the floor, Niir's head in my lap. He was probably enjoying this way too much..." with vpunch
    menu:
        "Shove him away.":
            p "Get off me, you salacious serpent!"

        "Tease him a bit.":
            $ niir_affection += 1
            p "You're enjoying this, aren't you?"
            n "I can make it more enjoyable if you wissssh. You did it on purpossssse, didn’t you?"
            p "I'm sure I don't know what you're talking about. Though, now that I look at you from this angle...your ears are very strange. What purpose does their strange shape serve?"
            n "Touch them and guessss if you prefer but my lipsss are sssealed."
            p "Hmph. Now I feel both curious and queasy. Not a mix of emotions I enjoy. Get up, now."
            n "What if I ssssay no?"

    "I stood up and his head hit the ground with a crack."
    n "You clumssssy princessss.  What did you do that forrrrr?"
    p "I need some way to make you lighter, or myself stronger…"
    n "Impossssible.  Perhapssss you need to learn magic."
    p "I don't need magic! Magic is for weaklings and sycophants."
    p "But there may be another way...I must do some research, alone. You may leave me now. But you have been an excellent test subject. And-"
    p "Thank you, for my mother's amulet. She was the only one who really understood me. If she was still alive-- But, she's not."
    n "I am sssssure ssshe was extraordinary, jusssst like you."
    p "There, you see, that wasn't so hard to flatter like a proper minion should."
    n "It wassss not flattery, and I am not yourrrr minion, Princesssss."
    p "I suppose we did agree to be partners."
    n "Yessss, I will hold you to… that.  I sssshall leave, as you asssked."
    n "Ssssee you ssssoon, Princessss."

    "Niir was so uncomplicated, I felt confident that I could control him once he was free. But, in some ways, I wished it wasn't so easy. Would he love me as well if I hadn't tricked him into doing so? Was it even love at all?"
    "...It was pointless to even think about it. He could help me regain the throne; everything else could wait until after that."
    return

label balrung7:
    scene bg dungeon with fade
    show balrung neutral at center with dissolve
    p "Is that a scroll? Are you writing a letter?"
    b smile "Princess! I was not aware you had joined me. I'd better put this away..."
    p "Not so fast! Let me see that."
    b smile blush "Oh, Princess, you don't want to read this old man's ramblings..."
    p "Is this... Dragon poetry? Did you write this?"
    b neutral "It's not worthy of your attention, please don't..."
    p "Too late! Oh ho ho!"
    b_write "She:"
    b_write "Eyes shine noble, latent traps"
    b_write "Supreme mischief."
    b_write "Face sly, young, grand"
    b_write "Defang grand dragons’ scheme."
    b_write "Map pulse’s sussurus,"
    b_write "sweet tyrant."
    "This is... about me?! No one's ever written a poem in my honor before..."
    p "I--"
    b smile blush "It's terrible, I apologize that you had to see that. I'll just dispose of this awful drivel--"
    p "No. No, I'll keep this."
    b smirk "Indeed? Well... I'm sure you didn't come here to read the musings of an old dragon. Or did you come just to keep me company?"
    p "No, I am going to explore the castle, looking for powerful secrets, and you may join me."
    b neutral "How generous of you. "
    extend smile "But, perhaps I can take you someplace that you will enjoy. A part of the castle I'm sure Cyril didn't show you."
    p "Yes, perfect. But we need to make sure he finds us lost in deep conversation at some point in our walk."
    b smirk "That can certainly be arranged."
    hide balrung with moveoutleft
    
    scene bg gate day with fade
    show balrung neutral at center with moveinleft
    b "It's outside the castle proper, but still within the walls. Fortunately, it is also still within Merlonious' wards."
    p "Wards?"
    b determined "The wards that keep us from simply walking away."

    hide balrung with moveoutright
    scene bg ruins with fade    
    show balrung neutral with moveinleft
    p "What would happen if you tried to walk through the wards?"
    b angry "The last time I attempted to do so, I fell unconscious for two weeks."
    p "How long ago was that?"
    b determined "When Merlonious first arrived here. As he was new, I thought perhaps he would not be as strong as some of the previous guardians. But I underestimated him. A mistake I don't intend to repeat."  #TODO: how many years ago was that?
    p "So that's why he doesn't trust you?"
    b neutral "That, and the fact that I've been here so long. He believes that if I could have changed, I would have done so already."
    p "Where are the wards?"
    b determined "Right...here. You may go through them; they only affect dragons. Sadly, they also prevent any of my comrades from coming to my aid."
    menu:
        "But you promised Niir you would come back for him.":
            $ balrung_affection += 1
            p "So you lied to Niir, when you told him you would come back for him."
            b smile "No, I-- ah. You've been spying on me, have you?"
            p "Of course. Haven't you been spying on me as well?"
            b smirk "Perhaps. But, no, I didn't lie to Niir; I would come back for him, though I would need either humans I could trust or many other dragons to break the barrier."
            p "Are there many other dragons you could count on?"
        "Comrades? You mean other dragons?":
            p "You have dragon... friends? Out there?"
    
    b determined "There are many dragons whom I once numbered among my allies. But they have been deceived by you humans, trading their power and heritage to pacify your panicky masses. They marry humans, live as humans, and their offspring are barely distinguishable from ordinary humans."
    b angry "Most of them don't even take dragon form anymore. Your kind finds it too frightening."
    menu:
        "I would not be frightened.":
            p "I would not find it frightening."
            b smile "No? No, you would not. You should be a dragon, Princess; you're unafraid, aggresive, and more than a little arrogant."
            p "Yes, you understand me perfectly. There's not a way, is there?"
            b neutral "A way for what?"
            p "A way for me to become a dragon. It would be quite useful."
            b smile eyes closed "Ha! I'd like to see that! No, there's no way I know of. Unless Merlonious knows of some esoteric transmogrification, or there's been some new alchemical advances."
            p "Hmmm, an interesting area of study."
        "What is your dragon form like?":
            p "What do you look like? As a dragon, I mean?"
            b neutral "What do I look like? Hmmmm... It's been so long, and I wasn't even full-grown when I was trapped here. But I do remember long limbs covered with burgundy scales, long teeth sharp enough to pierce a deer's heart in one bite, and, oh, the wings!"
            b smile "I remember the wings most of all; the feeling of beating upon the wind, a battle every time I'd take to the air, and the surge of victory with every new voyage."
            p "How can they keep you from such power? I could not imagine a worse punishment."
            b determined "Yes. Well, that was the idea."
       
    "We walked in silence after that, until we arrived back at the castle gates. The mage was there waiting for us."
    scene bg gate dusk with fade
    show cyril hat neutral at midleft with dissolve
    show balrung neutral at midright with moveinright

    c hat surprised "P-princess! There you are! When I couldn't find you, I was so worried that some nasty dragon had done something terrible to you!"
    p "Moronious, you've just ruined our lovely walk. We were conversing deeply, and then walking together in silence, as people who are in love often do."
    c hat concerned blush "In- in love?! It's not possible! Don't let him ensnare you, Princess, I implore you!"
    p "I am not ensnared by anybody. I love him of my own free will."
    b smirk "Yes, despite your best efforts, we are in love. Will you deny it?"
    c hat angry "D-deny...I- you- Yes! You cannot be in love! Can. Not. I know you, dragon; you {b}cannot{/b} love!"
    b determined "You would allow your personal hatred of me to mar the Princess's happiness?"
    c hat concerned "Sh-she would not be happy! Not with you. Impossible!"
    b angry "Mage, of all the hearts in this castle, I fear yours is the coldest. You know how long I've languished here. Yet you would deny me forgiveness, even after I've paid the price many times over?"
    c hat concerned blush "It's- but the Princess- she can't...I know you're plotting something!"
    p "It is {b}your{/b} plot that we are discussing, Moronious. Your plot to keep the dragons here forever."
    b determined "What would it take, Merlonious? Is there anything, {b}anything{/b} that could convince you I no longer deserve this suffering, this abuse?!"
    c hat concerned eyes closed "..."
    c hat angry "...No. It's not possible; it's impossible. You can't! You. Can't. Love."
    b angry "..."
    menu:
        "You're wrong, Moronious.":
            $ balrung_affection += 1
            p "You're wrong, Moronious. You don't get to decide who can love and who can't."
            b determined "Apparently he does."
        "You're right; Balrung cannot love.":
            p "You're right, Moronious; Balrung will do anything to get his power back. Much like I will. And if you will not help us, then you are our enemy."
            jump our_enemy
        "It's a different kind of love.":
            $ balrung_affection += 1
            p "Just because we're not all lovey-dovey and senseless with passion, does that mean it's not love? Or is it just a different kind than you're used to?"
            b determined "I don't think he knows what love is at all, outside of a fairy tale."
            
    c hat concerned "No! Love is kind; it helps people be better, it makes people happy! You two just want, just want power!"
    p "And who says you can't have both?!"
    b neutral "Princess-"
    p "No, really! I want both! And I WILL get what I want! You won't dare to try and stop me!!!"
    
label our_enemy:    
    c hat angry "Yes, I- will, I am. I don't want to be your enemy, Princess, but if you side with him against me, th-then, I'll have no choice."
    p "What will you do? Banish me from this castle, too?"
    c hat surprised "No! I...I don't want to hurt you!"
    b angry "You claim to be all about love, and yet you would devastate our Princess. Come, Chrysandra, let's discuss our new plans privately."
    c hat angry "New plans?! I knew it! I told you he had plans! You can't trust him, Princess!"
    p "I'll decide whom to trust, Moronious, and it certainly isn't you."
    hide balrung with moveoutleft
    
    scene bg bedroom candle with fade
    show balrung neutral at center with moveinleft
    p "In here. He won't dare come in without knocking."
    b angry "I apologize, Princess. Though I didn't underestimate Merlonious' power, this time I underestimated his vindictiveness."
    p "No, it's all right. We'll just plan something else."
    b smirk "We?"
    p "Yes, of course; who else would I trust?"
    b smile "Who else, indeed?"
    p "I could poison him, though he'll be suspicious of both of us, now. Perhaps that sleeping perfume? No, his spell must still be active while he's asleep, otherwise you could just escape at night. Hmmm..."
    b smirk "I wasn't lying, you know."
    p "Hmm? Wasn't lying about what?"
    b smile blush "About being in love with you. Of course I said it so he could hear me, but... well..."
    p "Oh that! Yes, of course you're in love with me. That's why I can trust you."
    b determined "..."
    p "So, it seems like the easiest way is going to be to kill Merlonious."
    b neutral "Perhaps. Let us meet again tomorrow; there is something that could help us that I must research alone."
    p "Yes, it is getting late, isn't it?"
    b smile blush "But for now, my lady..."
    show balrung at come_closer with dissolve
    "He bent down and kissed my forehead. Was this what it felt like to have someone be in love with you? It felt like...{b}power{/b}, delicious and thrilling."
    menu:
        "Kiss him back":
            $ balrung_affection += 1
            "I wanted more."
            "I grabbed his vest and pulled his head down to my level."
            show balrung determined with dissolve
            p "You will kiss your queen goodnight."            
        "Slap him":
            $ balrung_affection -= 1
            show balrung determined at reset_zoom with hpunch
            p "You presume too much, minion."
            
        "Say good night":
            p "Good night, Balrung."
    
    b smirk "Goodnight, my Queen."
    scene black with fade
    return
