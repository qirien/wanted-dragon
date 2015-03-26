############################################################
# Cyril route endings
#

# Dark Queen
label cyril_dark_epilogue:
    scene bg dungeon with fade
    show cyril concerned at center, basicfade
    p "I have a job for you."
    c "No, no, no, no.  {i}It can’t be.{/i}  You shouldn't be here, your Highness."
    p "That's \"your majesty\" now, thanks to you. I didn't think you had it in you to kill Magnolia, but you surprised me." 
    p "Pity my father had to get in the way, of course, but... well, that's in the past."
    show cyril angry at basicfade
    c "Well, I would do {i}anything{/i} for you, your majesty."  
    c "After killing that dragon, I don’t know why I spent so long not exacting a thorough comeuppance on those deserving it."  
    c "Your family were doing you a great disservice.  They did deserve it."
    p "Yes, there are many more that deserve justice. In fact, I have decided to allow you to work off some of your sentence by exacting that justice."
    p "You've proven yourself capable of greater things. There is a dragon, in a neighboring kingdom, who has amassed too much power. You know the kind?"
    show cyril concerned at basicfade
    c "I do. "
    p "Then ensure he doesn't cause any more trouble."
    show cyril angry at basicfade
    c "It would be my pleasure, your Majesty.  No longer will there be any dragons causing chaos as long as I am around."  
    c "I was wrong.  Imprisoning them was wrong.  They only deserve death."
    c "That is the only way."
    p "Good, good. You've come a long way since the stuttering, bumbling half-mage you used to be. I'm proud of you, Cyril."
    c "You have taught me much, your majesty."
    c "I owe it all to you."
    
    $persistent.DarkQueen = True
    scene black with veryslowfade
    return
      
# Queen's Hero
label cyril_scepter_epilogue:
    # since you can only get this ending if affection points are high and telling Cyril to go study gives you more points, it’s safe to say he’s away studying...  
    p_write "To Cyril Merlonious,"
    p_write "The Academy of Mages, House of Master Grivvorn\n"
    p_write "I hope that half-wit you're studying under realizes your potential."
    p_write "Otherwise you can direct him to me, the Queen of [k_name]."
    p_write "Also..."
    nvl clear
    scene bg kingdom with fade
    play music happy_ending
    p "Oh, this is ridiculous. I can't say everything in a letter!"
    p "Cyril Merlonious! I summon thee!"
    show cyril hat smile at center with magic_flash
    c "I am here, my Queen!"
    p "I do wish you would not do that, Cyril the- what are they calling you now, at the Academy?"
    c "Oh.  Well, it’s embarrassing.  I really don’t want all that kerfluffle made...."
    p "What is it then?"
    c "It’s Cyril the Courageous.  Quite a bit better than Cyril the Competent, but even still a rather hefty weight to bear."
    p "Oh, do stop with the false humility Cyril.  If the Queen sees worth in you, it’s only natural that others will."
    p "Now, make yourself useful and cast a spell to summon me some cinnamon cakes."
    c "Oh, yes.  Yes your majesty."
    p "After that, perhaps you'll have enough courage to ask to accompany me to the Coronation Ball this Saturday."
    c "Accompany you?  That would be... I would be with people?  I mean, with {i}you{/i} with people?"
    p "Are you Cyril the Courageous, or not?!"
    c "Oh, well, ah.  I suppose I am."
    p "... "
    extend "I'm waiting."
    c "Oh, the cakes!  Of course.  {font=fonts/ankecallig-fg.ttf}Dulcis Cottura{/font}!"
    p "No, you fool! Ask me! To accompany you!"
    c "Ah, your majesty, would you do me the honor of going to the ball... that’s in your honor.  But it would be {i}my{/i} honor to-"
    p "Go on!"
    c "Yes-ahem.  Please come with me to this ball, great Queen.  I would be privileged to accompany you."
    p "There, was that really so hard? Of course you may accompany me. And, have one of these cinnamon cakes; they're delicious."
    c "Thank you, your majesty."
    "I would make this mage worthy of a Queen yet."
    
    $persistent.QueensHero = True
    scene black with veryslowfade
    return

# Dragon Queen
label cyril_dragon_epilogue:
    scene bg woods with fade
    c "Stop, stop, {b}stop{/b}! Your Highness!"
    p "Oh, are you still here, Cyril? I'll land and you may depart. You have served me well."
    show cyril neutral at center, basicfade   
    c "Where are you going anyway?  The kingdom is back {b}that way{/b}!  We’re going to far from where you are to rule.  We must go back!"
    p "Why rule a tiny kingdom when I can rule the entire skies?! I've never seen what's beyond the Seven Kingdoms."
    c "Well I- I hadn’t quite thought of it like that."
    c "But who is going to rule the kingdom your Highness?  You can’t just up and leave!"
    c "There are responsibilities to be had..."
    p "Oh, I don't care. As long as it's not Magnolia...though, I don't think she'll dare return after the singing I gave her!"
    p "...in fact, why don't you take the throne? Keep it warm for me, in case I change my mind. I know {b}you{/b} at least would not betray me."
    c "Me?  Take the?  Oh, no no.  I am just a humble mage.  But perhaps-"
    c "But where would you go?  And when would you be back?"
    p "I shall fly wherever I want!  See everything that there is! Return whenever I please! I am a dragon, Cyril, a DRAGON!"
    c "But I- but… {size=-1}I’d miss you.{/size}"
    p "Oh, come, don't look so crestfallen. When I return I'll tell you all about my adventures and you can write a book about me."
    c "Well, yes, I guess I could write a book.  When you do return, whoever knows when that will be."
    p "Farewell, Cyril! I suppose I should thank you for the small part you played in my becoming more powerful than I had ever dreamed…"
    c "Wait!"
    p "...but, really, it's no less than I deserve."
    c "I-I can’t let you leave."
    p "Try and stop me, then!"
    "I stamped my feet and roared in his face."
    c "No- I mean I can’t let you leave without me."
    c "I do appreciate the offer to run the kingdom, but I-"
    p "I don't think you'll be able to keep up with me."
    c "But could you let me... try?"
    p "Ha! Try, then! Here I go!"
    c "Ah, yes.  Not so fast.  DRACONIS TRANSFORMA!"
    "I was almost ready to take off when his transformation caught my eye. In a flash of light, a blue, nervous-looking dragon appeared where Cyril had been."
    p "...Could you have done this at any time?! Why didn't you just transform me into a dragon in the first place?!"
    c "I didn’t-I didn’t think you’d {b}want{/b} to be a dragon!"
    p "Why {b}wouldn't{/b} someone want to be a dragon? Isn't it wonderful, Cyril?!"
    c "Ah-I don’t think I’m quite ready for this flying business."
    p "Keep up, or stay behind!"
    "I lunged into the air, wings beating faster and faster, and soared off to the south."
    c "Wait for me, my dragon Princess!"
    "I launched a ball of flame in his direction."
    c "I mean, my dragon Queen!"
    
    $persistent.DragonQueen = True
    scene black with veryslowfade
    return
