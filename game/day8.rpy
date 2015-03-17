label day8:
    p "It's time."
    
label balrung8:
    scene bedroom day with fade
    "That fool mage won't let Balrung go no matter what. I need a new plan..."
    menu:
        "Research potions in the library.":
            "There are some good books on potions in the library. There must be something that can help!"
            scene library with fade
            "Good, it's empty. Now, where was that book...?"
            "Ah yes, {i}Draughts of Death, Destruction, and Devastation{/i}. Death is such an uninteresting solution, but if it's the one that works best..."
            # TODO: page flipping sfx"
            "Hmmm, here's a Concotion of Confusion... but it takes griffon claws, and those aren't easy to find. And three-month dried kelp; I'm not waiting that long."
            "A Potion of Persuasion? That could work... it requires a dragon scale. Well, if we had any dragons in dragon form, that'd be no problem."
            "Transmogrification Tonic? If I could turn into a dragon... but then, I'd be stuck here as well. Unless I drank it after leaving... then I mightn't need help after all..."
            show balrung neutral at center with moveinleft
            b "Chrysandra? There you are! I have another plan, but I'm not satisfied with its chances for success. Tell me you have something better."
            p "Depends. Do you have any dragon scales?"
            b "All you need is one scale?"
            p "Well, and some other ingredients. I thought I saw berry grass on our walk the other day, and I know the kitchen has molasses, and I brought some nightshade."
            b "So many dragons have come and gone, here, we should be able to find at least one dragon scale. Firgol left several months ago from the top tower, so let's try there."
            hide balrung with moveoutleft
            
            scene stairs day with fade
            show balrung neutral at center with moveinright
            p "Tell me about Firgol."
            b "None too bright, but he was honest and sincere. That's what his Princess wanted, I suppose."
            p "She came here seeking a dragon?"
            b "Yes, she was ruling with a regency, and they threatened to take over if she did not produce any heirs. She decided the quickest way to get married was to seek a dragon here."
            p "Why did she choose Firgol?"
            b "Well...Niir wasn't interested, since she was a bit older and not particularly beautiful. I chatted with her several times, but she wanted someone guileless and pliable. Firgol was both."
               
            hide balrung with moveoutleft
            
            scene exterior day with fade
            show balrung neutral at center with moveinleft
            p "What color scales are we looking for?"
            b "I'm afraid I don't know. I couldn't bear to watch {b}him{/b} return to dragon form while I was incapable of doing so."
            b "But tell me...what potion are you planning on making, Chrysandra?"
            p "Persuasion. I wanted to make one to use on my father, but I had no dragon scales."
            b "Ah-hah! Here's one. Once I'm free, you can have as many scales as you like. Perhaps using a potion on your father would be a better way to regain your kingdom than burning it to the ground?"
            p "Ohhhh, I suppose. I had such lovely visions of flames and rubble...but it is expensive to rebuild a castle."
            b "Your pragmatism is delightful. I'm sure we can find something else to destroy together."
            p "Ha. Stop it, Balrung, now you're just teasing me."
            b smile "Not at all. Perhaps we should destroy {b}this{/b} castle? It would look nice as a pile of smoldering debris, wouldn't it? "
            extend smile blush "You and I, soaring above, circling, conflagrating..."
            p "That's quite enough of that; I have to start brewing this potion. Find me the rest of these ingredients, and meet me in the kitchen."
            b smirk "Of course, Chrysandra."
            scene bg kitchen with fade
            "At least the scale only needs to boil in blood for an hour. But, it took more blood than I thought...I need to sit down."
            scene bg kitchen with fade
            "Oh. I'm already sitting down. On the floor."
            show cyril hat neutral at midright with moveinleft
            c hat surprised "Princess! You're bleeding!"
            c hat concerned "Which dragon was it?! I'll make sure they can NEVER hurt anyone else again!"
            "I tried to stand up, but couldn't quite manage it."
            p "It was... it wasn't... Balrung...!"
            
            show balrung neutral at midleft with moveinleft
            b determined "Princess? I have the- oh. {b}You're{/b} here."
            c hat angry "It was YOU! YOU SHALL NOT HURT THE PRINCESS!!"
            b angry "I did nothing of the sort. Stop this ridiculous posturing and help her!"
            c hat concerned "You will regret calling me ridiculous!"
            show cyril hat angry with flash
            c "FULGURENTIA MAXIMA!" #TODO: lots of lightning
            show balrung neutral at left with move
            b "AHHHHH!"
            show balrung at squatting with move
            p "Stop it, you stupid mage! It wasn't even him, it was me!"
            c hat concerned "You're not making delirious, I mean, you're not making sense, Princess! No, no, I'm going to do what they should have done to this villain in the first place!"
            "He began muttering, trying to remember the words. I grabbed the bloody knife and managed to stand up."
            menu:
                "Attack Cyril":
                    show cyril hat surprised with blood
                    "I brought the knife down and buried it into Cyril's back. He stopped chanting and fell forward, dead. The magical aura dissipated."
                    hide cyril with moveoutbottom
                    b "..."
                    p "...he was such a fool."
                    "I looked around. Balrung was still lying down, but breathing. I took a dishtowel and wrapped it around my bleeding arm."
                    p "We're all fools..."
                    
                "Threaten to stab yourself":
                    
                "Shield Balrung" if (balrung_affection >= HIGH_AFFECTION):
                    "I ran to stand in front of Balrung. I didn't think that mage would be foolish enough to attack me."
                    p "Stop, stop, stop! You bumbling buffoon, I cut my own arm to make a potion! Balrung has been {b}helping{/b} me!"
                    c hat surprised "He...didn't hurt you?"
                    p "No, moron! The only one in this castle who has been hurting people is {b}you{/b}!"
                    c hat concerned eyes closed "I...I'm not fit for this job. I never should have agreed to it..."
                    "Now that Moronious was not about to attack us, I wrapped up my arm in a dishtowel and turned to look at Balrung. He lay still, but was breathing."
                    p "You're such a fool..."
                    
            
        "Brainstorm with Balrung.":
            scene dugeon with fade
            show balrung neutral at center with dissolve
            
                                  #TODO: she carries him across dragon barrier? Niir insists on going too, or else he'll tell Cyril
        "Plead with Moronious.":
    
label cyril8:
    
label niir8: