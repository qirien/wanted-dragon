############################################################
# Balrung route endings
#

label balrung_epilogue:
    scene bg kingdom with fade
    show balrung smile at center, basicfade
    show balrung smirk at basicfade
    b "Your kingdom is indeed beautiful, my dear Queen."
    p "Yes... it's a good thing we didn't completely burn it to the ground. Though the fact that their new King could do so at any moment is a wonderful motivator."
    p "I think half the courtiers soiled themselves when you transformed into dragon form at our wedding."
    show balrung smile at basicfade
    b "Yes... that was quite the scene, wasn't it?"
    p "I only wish Magnolia could have seen it, too, and quivered in terror while you threatened to devour her whole... that would have been so nice."
    show balrung neutral at basicfade
    b "I think your sister will enjoy the Academy."
    p "Yes... but that's the dark lining hiding behind this silver cloud. If she gains enough power... she could be a danger to us."
    show balrung smirk at basicfade
    b "She could. But I have plans for that."
    p "Really? Like what?"
    show balrung smile eyes closed at basicfade
    b "If I tell you, it'll spoil all the fun you could have unraveling it for yourself."
    p "Hmph. Well then, I'm not telling you my plans, either."
    show balrung smirk at basicfade
    b "I wouldn't have it any other way."
    show balrung smile blush at come_closer, basicfade
    b "Queen:"
    b "Nigh, how wonderful!"
    b "Lost, tragic course!"
    b "Soft tresses, silken neck, quick kisses,"
    b "Savory yon nuptial love vexes,"
    b "Sibilant treasure rhapsodically enchants,"
    b "Sing, glorious sovereign!"
    p "...I don't sing."
    p "But I do kiss, when the mood strikes me."
    show balrung smile eyes closed at basicfade
    $ renpy.pause(1.6)    
    scene black with fade
    return 

label balrung_revenge_epilogue:
    scene bg bedroom with fade
    play music evil_theme
    p "I must be patient. I will not allow this minor setback derail my plans for [k_name]!"
    "I sat down for some serious plotting. It was too late to stop the coronation, but if the died, then I was still in line for the throne."
    "My plans were interrupted by a pigeon landing on my table. A letter?"
    m_write "Sister,"
    m_write "I'm sorry you missed my coronation. You would have loved the little cinnamon cakes they served."
    "They served cinnamon cakes for {b}her{/b}?!"
    m_write "But it's not too late to come for my wedding!"
    m_write "I've met the most wonderful man. He's a bit older, but I don't mind. He writes the most wonderful poetry..."
    nvl clear
    m_write "Father says it'll be a wonderful step towards the integration of dragonkind into our society."
    m_write "I'm sure you'd like him."
    m_write "Come home, Chrysandra, won't you?"
    m_write "Lots of love,"
    m_write "{b}Queen{/b} Magnolia"
    nvl clear
    
    p "It couldn't be Balrung..."
    p "It has to be him. How many older, poetry-writing dragons are there?!"
    p "The vicious viper! The selfish serpent! The acrimonious adder! The lying lizard!  The, the, the..."
    p "..."
    if (cyril_dead):
        p "Niir!"
        p "Niir!  Where are you when I need you...come to think of it, I haven't seen him since..."
        show cyril at center, basicfade
        hide cyril with red_flash
        p "I suppose when that mage died, it broke the spell. I'm on my own, now."
        p "But... I have this entire castle at my disposal!  I'll find something! I {b}will{/b} be Queen!  You'll see, Mother!"
        "It would just take a bit more time."
    else:
        p "This changes nothing!  Moronious and I have the scepter now, and together we will rid [k_name] of not one illegitimate tyrant, but two!"
        p "Mwah ha ha ha ha!"
    
    ".:. Revenge Never Ends\nEnding 2 of 8"

label balrung_ending:
    play music balrung_theme
    "Now that Moronious was not about to attack us, I wrapped up my arm in a dishtowel and turned to look at Balrung. He lay still, but was breathing."
    "Slowly, he opened his eyes, and I helped him sit up."
    show balrung neutral at center, come_closer, basicfade
    show balrung determined at basicfade
    b "Such a fool..."
    p "Yes, I shall be glad to be rid of him."
    show balrung angry at basicfade
    b "I meant you."
    p "How dare you speak to your future Queen so disrespectfully?!"
    show balrung smirk at basicfade
    b "Is it still disrespectful if I am your King?"
    p "King?!"
    show balrung smile at basicfade
    b "You freed me, Princess, and I want to aid you. What better way to help you maintain your kingdom than to serve by your side?"
    "He would be useful...but could he really help me?"
    p "You claim to have great power as a dragon. Moronious' spell is now broken, so show me!"
    show balrung smirk at basicfade
    b "I will."
    hide balrung with red_flash
    scene bg kitchen with punch_long
    "He shook his head and stretched, and stretched, and stretched, skin shimmering into deep red scales. Wings emerged from his back and beat the air like waves crashing against a ship."
    play sound "sfx/fireball.ogg"    
    scene bg kitchen with red_flash    
    "Balrung breathed a ball of fire at one of the chairs, turning it instantly to ash. His reptilian eyes looked at me for my response."
    # TODO: fireball vfx?
    menu:
        "Make him your King." if (balrung_affection >= HIGH_AFFECTION):
            p "Balrung, your patient ruthlessness, and powers over flight and fire, will help you serve me well as my King. Now, let me climb on your back and take us to [k_name]."
            b "What an excellent future we shall have together. None will dare to defy our reign!"
            p "Mwah ha ha ha ha!"
            b "Bwah ha ha ha ha!"
            scene bg sunset with fade            
            play music happy_ending
            "With a rush of wings and dust, we flew out of the dungeon and into the wide evening sky. Balrung let fly a fireball at the gates of his old prison, just for fun."
            play sound "sfx/fireball.ogg"
            "With a dragon on my side, my father would {b}have{/b} to make me Queen... and if not, well, I'd make sure there was no other choice."
            "And Balrung would be an valuable ally to have as we ruled together."
            "I reached down to pat his scaly cheek and could tell from the gleam in his eye that he was thinking the exact same thing. I'd never lack a worthy opponent again."
            p "You're such an ambitious schemer."
            b "And you're dreadfully ruthless."
            p "Mwah ha ha ha ha!"            
            b "Bwah ha ha ha!"
            call credits
            jump balrung_epilogue
        "Make him an advisor.":
            p "While I admire your patient ruthlessness, you are not fit to be my King. You may be an advisor."
            b "Oh ho ho. I let you win a few games of Queens and Pawns and you imagine yourself some sort of master strategist. No, Princess, I will not serve you as anything less than an equal."
            b "A pity. If you change your mind, I am going to go raze the kingdom of [k_name]. You'll be able to find me on the throne by tomorrow afternoon."

        "Leave him here.":
            p "I don't need any King telling me what to do!"
            b "A pity. I rather enjoyed our time together. But I won't try to force you to change your mind. I've learned that lesson, at any rate."
            
    play music princess_theme            
    "In a whoosh of wings, he was gone." 
    scene bg kitchen with hpunch    
    if (cyril_dead):
        "Leaving several shiny red scales behind."
        p "With these, I can make as many Potions of Persuasion as I want! I'll become Queen all on my own! Mwah ha ha ha ha!"
        call credits
        jump balrung_revenge_epilogue
    else:
        p "..."
        show cyril neutral hat at center with moveinleft
        c "...Princess! I found it! The Scepter! It was under Balrung's bed the whole time!"
        p "Mwah ha ha ha... he left behind the Scepter of Lavendorm?! The fool! Moronious!"
        c "Y-yes your highness?"
        p "Shall we attack that evil dragon?"
        c "We shall!"
        play sound "sfx/electricity.ogg"
        call credits
        jump balrung_revenge_epilogue
                   
label imprisoned_epilogue:
    scene bg dungeon with fade
    show cyril hat concerned at midleft with moveinleft
    play music cyril_theme
    c "I've brought you your breakfast, your Highness."
    "I threw the bowl at his ridiculous face and it knocked off his ridiculous hat. Niir snatched it up and grinned."
    show cyril surprised at basicfade
    show niir at midright with moveinright
    show niir mischief at basicfade
    n "Oooh, you're a much more interesssting companion."
    show cyril concerned blush at basicfade
    c "That was quite uncalled for.  I don’t think you’ve made any progress with your reform, you know."
    show cyril concerned eyes closed at basicfade
    c "Your father expects me to keep him updated and at this rate I will have nothing to update him with!"
    p "My sister put you up to this, didn't she?! DIDN'T SHE?! She thinks she's won, but she's wrong! Eventually I will escape and PUNISH YOU ALL!!!!"
    show cyril neutral at basicfade
    c "Now, now Princess.  It might have taken me a week, but you were always going to show your true colors at the end.  Just start reflecting on your own behavior and soon you will understand what it is you have to do."
    show cyril smile at basicfade
    c "I do believe you can change.  I have seen it happen to dragons, why not you?"
    p "...I will kill you. I will rip off your fingers and toes one by one and feed them to your stupid dragons!"
    show niir frown at basicfade
    n "...that's disgusssting!"
    show cyril concerned blush at basicfade
    c "I will let that slide because I know you don’t mean that, Princess.  I’ll tell your father that you’re starting to see the error of your ways."
    show cyril neutral at basicfade
    c "See you at dinner, when I do hope you will be more agreeable."
    "It was impossible. How had it come to this?! I thought I had him wrapped around my finger, and then..."
    "...but I refused to be beaten. It wasn't too late to escape this hell and return to [k_name]. I'd just have to be more careful, lay better plans, put on my good-princess face, and THEN take my revenge. On all of them!"
    "Mwah ha ha ha ha!"
    