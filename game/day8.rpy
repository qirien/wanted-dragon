label day8:
    p "It's time."
    
label balrung8:
    scene bg bedroom day with fade
    "That fool mage won't let Balrung go no matter what. I need a new plan..."
    "There are some good books on potions in the library. There must be something that can help!"
    scene bg library with fade
    "Good, it's empty. Now, where was that book...?"
    "Ah yes, {i}Draughts of Death, Destruction, and Devastation{/i}. Death is such an uninteresting solution, but if it's the one that works best..."
    # TODO: page flipping sfx"
    "Hmmm, here's a Concotion of Confusion... but it takes griffon claws, and those aren't easy to find. And three-month dried kelp; I'm not waiting that long."
    "A Potion of Persuasion? That could work... it requires a dragon scale. Well, if we had any dragons in dragon form, that'd be no problem."
    "Transmogrification Tonic? If I could turn into a dragon... but then, I'd be stuck here as well. Unless I drank it after leaving... then I mightn't need help after all..."
    show balrung neutral at center with moveinleft
    b determined "Chrysandra? There you are! I have another plan, but I'm not satisfied with its chances for success. Tell me you have something better."
    p "Depends. Do you have any dragon scales?"
    b neutral "Perhaps; how many do you need?"
    p "Just one, and some other ingredients. I thought I saw berry grass on our walk the other day, and I know the kitchen has molasses, and I brought some nightshade."
    b angry "So many dragons have come and gone, here, we should be able to find at least one dragon scale. Firgol left several months ago from the top tower, so let's try there."
    hide balrung with moveoutleft
    
    scene bg stairs day with fade
    show balrung neutral at center with moveinright
    p "Tell me about Firgol."
    b determined "None too bright, but he was honest and sincere. That's what his Princess wanted, I suppose."
    p "She came here seeking a dragon?"
    b neutral "Yes, she was ruling with a regency, and they threatened to take over if she did not produce any heirs. She decided the quickest way to get married was to seek a dragon here."
    p "Why did she choose Firgol?"
    b smirk "Well...Niir wasn't interested, since she was a bit older and not particularly beautiful. I chatted with her several times, but she wanted someone guileless and pliable. Firgol was both."
       
    hide balrung with moveoutleft
    
    scene bg exterior day with fade
    show balrung neutral at center with moveinleft
    p "What color scales are we looking for?"
    b angry "I'm afraid I don't know. I couldn't bear to watch {b}him{/b} return to dragon form while I was incapable of doing so."
    b smile "But tell me...what potion are you planning on making, Chrysandra?"
    p "Persuasion. I wanted to make one to use on my father, but I had no dragon scales."
    b smirk "Ah-hah! Here's one. Once I'm free, you can have as many scales as you like. Perhaps using a potion on your father would be a better way to regain your kingdom than burning it to the ground?"
    p "Ohhhh, I suppose. I had such lovely visions of flames and rubble...but it is expensive to rebuild a castle."
    b neutral "Your pragmatism is delightful. I'm sure we can find something else to destroy together."
    p "Ha. Stop it, Balrung, now you're just teasing me."
    b smile "Not at all. Perhaps we should destroy {b}this{/b} castle? It would look nice as a pile of smoldering debris, wouldn't it? "
    show balrung smile blush at come_closer with dissolve
    b "You and I, soaring above, circling, conflagrating..."
    p "I- I have to start brewing this potion. Find me the rest of these ingredients, and meet me in the kitchen."
    show balrung smirk at reset_zoom with dissolve
    b smirk "Of course, Chrysandra."
    hide balrung with moveoutleft
    scene bg kitchen with fade
    "At least the scale only needs to boil in blood for an hour. But, it took more blood than I thought...I need to sit down."
    scene bg kitchen with vpunch
    "Oh. I'm already sitting down. On the floor."
    show cyril hat neutral at quarterright with moveinleft
    c hat surprised "Princess! You're bleeding!"
    c hat concerned "Which dragon was it?! I'll make sure they can NEVER hurt anyone else again!"
    "I tried to stand up, but couldn't quite manage it."
    p "It was... it wasn't... Balrung...!"
    
    show balrung neutral at center with moveinleft
    b determined "Princess? I have the- oh. {b}You're{/b} here."
    c hat angry "It was YOU! YOU SHALL NOT HURT THE PRINCESS!!"
    b angry "I did nothing of the sort. Stop this ridiculous posturing and help her!"
    c hat concerned "You will regret calling me ridiculous!"
    c hat angry "FULGURENTIA MAXIMA!" #TODO: lots of lightning/
    show cyril hat angry with flash
    show balrung neutral at midleft, squatting with quickmove
    b angry "AHHHHH!"
    p "Stop it, you stupid mage! It wasn't even him, it was me!"
    c hat concerned "You're not making delirious, I mean, you're not making sense, Princess! No, no, I'm going to do what they should have done to this villain in the first place!"
    "He began muttering, trying to remember the words. I grabbed the bloody knife and managed to stand up."
    menu:
        "Attack Cyril":
            $ cyril_dead = True
            show cyril hat surprised with blood
            "I brought the knife down and buried it into Cyril's back. He stopped chanting and fell forward, dead. The magical aura dissipated."
            hide cyril with moveoutbottom
            p "So this...is what it feels like. To have a plot work. To be victorious."
            p "...it's not as much fun as I thought."
            jump balrung_ending
            
        "Threaten to stab yourself":
            p "Stop it, Moronious, or I shall stab myself with this knife!"
            c "What?! Princess, no! What are you doing?!"
            "You bumbling buffoon, I cut my own arm to make a potion! Balrung has been {b}helping{/b} me!"
            c hat surprised "He...didn't hurt you?"
            p "No, idiot! The only one in this castle who has been hurting people is {b}you{/b}!"
            # TODO: ? if (cyril_affection >= MEDIUM_AFFECTION):
            c hat concerned eyes closed "I...I'm not fit for this job. I never should have agreed to it..."
            "He dropped his hands, dejected, and turned to leave."
            c "You're free to leave, Balrung. You m-may not be perfect, but I am no butter. I mean, no better."
            hide cyril with moveoutleft
            jump balrung_ending
        "Shield Balrung" if (balrung_affection >= HIGH_AFFECTION):
            "I ran to stand in front of Balrung. I didn't think that mage would be foolish enough to attack me."
            p "Stop, stop, stop! You bumbling buffoon, I cut my own arm to make a potion! Balrung has been {b}helping{/b} me!"
            c hat surprised "He...didn't hurt you?"
            p "No, idiot! The only one in this castle who has been hurting people is {b}you{/b}!"
            c hat concerned eyes closed "I...I'm not fit for this job. I never should have agreed to it..."
            "He dropped his hands, dejected, and turned to leave."
            c "You're free to leave, Balrung. You m-may not be perfect, but I am no butter. I mean, no better."
            hide cyril with moveoutleft
            jump balrung_ending
        "Wait it out.":
            p "Hmmm, I must admit, I'm curious who would win if you two begin fighting. What better way to prove who is stronger and more fit to aid me?"
            "They looked at each other, surprised. Balrung stood up slowly, shaking, and shook his head."
            show balrung at standing with move
            b determined "..."
            c hat surprised "..."
            p "Well? What are you waiting for? Commence battle!"
            b smirk "Cyril, you've seen the Princess. Who do you really think is a greater threat to the safety of this kingdom? Yes, I know she's a \"princess\", and quite an attractive one at that; but she's selfish, lustful for power, and will stop at nothing."
            b "She had even agreed to poison you in your sleep if it was necessary for our plan. Would you trust the future of this kingdom to someone like that?"
            p "Poisoning the mage was your idea!"
            b angry "You don't care whose life you have to destroy to get what you want. You don't care about the desires and goals of those around you. I know you, Princess, I've seen into your heart and it's dark with malice."
            c "You'd know all about malice, wouldn't you?!"
            b neutral "Yes. I would. I used to be the same. But, Cyril, after all this time, do you know what I really want to do?"
            c hat angry "Yes! You want revenge, and power!"
            b determined "No. I only want to be able to fly over the mountains and be left alone."
            show cyril hat surprised with dissolve
            p "He's lying! He was going to help me destroy [k_name]!"
            b smirk "Cyril, I hope you'll do the right thing and help the Princess see the error of her ways. You mages have helped me to, even though I disagree with the way it was done."
            p "Balrung! I will hunt you down! I will find you and DESTROY YOU!!!"
            # TODO: if her cyril_affection is high enough, send to cyril_attack instead?
            b smile "Farewell, Princess. I hope you find better things to consume your life than revenge."
            hide balrung with moveoutleft
            p "Moronious! Stop him! Why are you just standing there?! KILL HIM!"
            # TODO: Feel free to rewrite Cyril's lines better or end this differently
            c hat concerned "N-no, Princess, I don't th-think I will."
            p "Useless! Betrayed at every turn! When I am Queen, you will regret this!"
            c hat concerned eyes closed blush "You sh-shouldn't be Queen the way you are. I'm terribly sorry, my dear Princess [p_name], but..."
            p "Moronious, you fool, point that wand at the dragon! Not at me!"
            c hat concerned blush "Carceratus!!"
            p "What have you done to me?!"
            c hat neutral "Stay! You will stay here, until you learn to be good! I know, somewhere inside of you, there's goodness and love...please, find it quickly, Princess."
            p "You thought guarding dragons was bad? I {b}will{/b} make your life a hell of mental pain, psychological torture, and physical anguish until you LET. ME. GO!"
            c hat concerned eyes closed "I'm so sorry! It's for your own good...."
            # TODO: jump to a common ending where she ends up imprisoned?                    
     
    
label cyril8:
    
#TODO: she carries him across dragon barrier? 
label niir8: