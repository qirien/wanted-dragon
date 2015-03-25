############################################################
# Cyril route endings
#


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
    p "Good, good. I'm so glad I can count on you, Cyril. You'll always be my favorite minion."
    scene black with veryslowfade
    return
      

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
    scene black with veryslowfade
    return


label cyril_dragon_epilogue:
    scene bg kingdom with fade
    show cyril neutral at center, basicfade
    c "It’s for the best, Chrysandra.  I know you don’t want to take this potion but I travelled a long way and met up with many, many members of the council in order to get it."
    show cyril smile at basicfade
    c "So if you would just drink the potion and then rest for a while, I am sure you will be back to normal in no time."
    p "I still think that if I lit enough pants on fire, they might change the law to allow a dragon to be Queen. But... I'll drink it."
    #TODO: some magical VFX
    show cyril smile blush at basicfade
    c "Thank you, my-your majesty.  It was quite extraordinary that you became a dragon at all.  It’s good that scepter is now locked away securely so no one else can have the same fate."
    p "Securely? Where exactly did you hide it?"
    show cyril surprised at basicfade
    c "You mustn’t worry about that my Queen.  But do trust me that it is securely away at the top of the cas- Oh dear.  I must work on holding my tongue more in the future."
    "The top of the castle?! I wondered if I might get it back... but perhaps it was better to stay here, as a human, but a Queen." 
    "Well, if I ever tire of being Queen, I know just where to go!"
    p "Don't worry about it, dear. Come here and rub my shoulders; they feel so cramped now that I'm human again. No wings! It's simply dreadful."
    show cyril smile blush eyes closed at basicfade
    c "Y-yes, your majesty."
    p "That's a good boy.  Mmmmm.  Yeeees."
    show cyril smile blush at basicfade
    p "You certainly are my favorite minion."
    scene black with veryslowfade
    return
