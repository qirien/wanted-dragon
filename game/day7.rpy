# DAY 7
label day7:
    # Whoever's route she didn't choose hinders her
    if (route == "Cyril"):
        call cyril7
        
    elif (route == "Balrung"):
        call balrung7
        
    elif (route == "Niir"):
        call niir7

label niir7:
    return
    
label cyril7:
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
    b_write "She:{vspace=-10}Eyes shine noble, latent traps{vspace=-10}Supreme mischief."
    b_write "Face sly, young, grand{vspace=-10}Defang grand dragons’ scheme."
    b_write "Map pulse’s sussurus,{vspace=-10}sweet tyrant."
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
    
    b determined "There are many dragons who I once numbered among my allies. But they have been deceived by you humans, trading their power and heritage to pacify your panicky masses. They marry humans, live as humans, and their offspring are barely distinguishable from ordinary humans."
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

    c "P-princess! There you are! When I couldn't find you, I was so worried that some nasty dragon had done something terrible to you!"
    p "Moronious, you've just ruined our lovely walk. We were conversing deeply, and then walking together in silence, as people who are in love often do."
    c "In- in love?! It's not possible! Don't let him ensnare you, Princess, I implore you!"
    p "I am not ensnared by anybody. I love him of my own free will."
    b smirk "Yes, despite your best efforts, we are in love. Will you deny it?"
    c "D-deny...I- you- Yes! You cannot be in love! Can. Not. I know you, dragon; you {b}cannot{/b} love!"
    b determined "You would allow your personal hatred of me to mar the Princess's happiness?"
    c "Sh-she would not be happy! Not with you. Impossible!"
    b angry "Mage, of all the hearts in this castle, I fear yours is the coldest. You know how long I've languished here. Yet you would deny me forgiveness, even after I've paid the price many times over?"
    c "It's- but the Princess- she can't...I know you're plotting something!"
    p "It is {b}your{/b} plot that we are discussing, Moronious. Your plot to keep the dragons here forever."
    b determined "What would it take, Merlonious? Is there anything, {b}anything{/b} that could convince you I no longer deserve this suffering, this abuse?!"
    c "...No. It's not possible; it's impossible. You can't! You. Can't. Love."
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
            
    c "No! Love is kind; it helps people be better, it makes people happy! You two just want, just want power!"
    p "And who says you can't have both?!"
    b neutral "Princess-"
    p "No, really! I want both! And I WILL get what I want! You won't dare to try and stop me!!!"
    
label our_enemy:    
    c "Yes, I- will, I am. I don't want to be your enemy, Princess, but if you side with him against me, th-then, I'll have no choice."
    p "What will you do? Banish me from this castle, too?"
    c "No! I...I don't want to hurt you!"
    b angry "You claim to be all about love, and yet you've hurt more people than anyone else here. Come, Princess, let's discuss our new plans privately."
    c "New plans?! I knew it! I told you he had plans! You can't trust him, Princess!"
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
    "I wanted more."
    "I grabbed his vest and pulled his head down to my level."
    show balrung determined with dissolve
    p "You will kiss your queen goodnight."
    b smirk "Goodnight, my Queen."
    
    scene black with fade
    return