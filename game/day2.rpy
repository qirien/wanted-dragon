label day2:
    scene bg bedroom with fade
    show princess at midright with dissolve
    "(Is that knocking?! Who could be brazen enough to wake me up so early?!)"
    p "Niir! I am in no mood for your games! Begone!"
    c "Please, Princess, it is I, Cyril, and I only wanted to-"
    p "Moronious?! This had better be important!"
    show cyril at midleft with moveinleft
    c "Good.  Good.  I'm glad that you opened up."
    c "I don't want you to think that I'm - well, dissapproving."
    c "But some information has come to my attention."
    c "You were {b}banished{/b}, Princess!"
    p "I am well aware of that.  So what are you bothering me for?"
    c "It's just- you were {b}banished{/b}, Princess!"
    p "If you're going to waste my time like a stuttering fool Moronious, I suggest you begone!"
    c "Well, it wouldn't be the first time that you've commanded me to begone."
    c "Anyway, please tell me this is a mistake!  It must be a mistake!"
    c "I'm sure that the kingdom is just overreacting.  Playing a joke perhaps? Like Niir?"
    c "There is no way they would actually b-b-banish you!"
    p "Oh, they did banish me.  And that's why I'm here, to get justice."
    p "And you will be part of those plans Cyril."
    c "Erm-ahem!  Yes.  I don't think that is a good idea- it is already dangerous enough to have a disgraced Princess-"
    p "You don't {b}want{/b} me here?"
    p "(Who does he think he is?  I'm not the one at fault here!  I'd like to {b}see{/b} him try to kick me out!)"
    c "No! I didn't say that."
    c "I'm just {i}concerned{/i} Princess."
    c "If you have serious allegations before you then ah-"
    p "You're ashamed of me being in your presence, then?"
    c "No!  I love you being in my presence."
    c "{i}I do{/i}.  It's just..."
    c "I'm afraid for you and the errr... connotations that are attached to that."
    p "I can handle myself Moronious."
    p "And when I put things right you will see that for yourself."
    c "As long as I'm not seen as {i}aiding and abetting{/i}."
    p "If you are not willing to make sacrifices for your future Queen, then what good are you?"
    c "I am, I am.  Forgive me your majesty."
    p "I forgive you, you foolish mage.  Just don't doubt me again."
    hide cyril with moveoutleft
    #TODO: Have a conversation with Niir and Balrung somehow?!
    
    show niir at right with moveinright
    n "You were banisshhed? Your position musst be desssperate, then."
    show princess at center with move
    p "How long have you been eavesdropping?!"
    n "Long enough to hear you sssnorrrring. Mossst unladylike."
    p "Moronious!"
    show cyril at midleft with moveinleft
    c "Yes, Princess? Oh! What's {b}he{/b} doing here?!"
    p "That was my question. I would have thought that a capable mage would have this room warded against unwanted intrusions."
    n "If you think Cccyril is capable--"
    c "I did! It was! But- oh, the spell's locus...I had it tied to me, not the room! What a dreadful oversight."
    c "I am terribly, terribly sorry, Princess! I shudder to think what these terrible dragons might have tried to do if I had not fixed the ward."
    p "Yes, well, it should have been fixed in the first place!"
    n "Disssapointing. I had ssso many plansss..."
    c "Now I've made two spells - one tied to you, and one to the room. The locus for the room spell is the door, so if you open the door, the spell will allow people through."
    c "I've also added a spell on your person, that creates an anti-dragon barrier. I don't know why I didn't do this in the first place, it must have slipped my mind."
    n "Like ssso many other thingsss."
    p "So dragons cannot touch me now? What would happen if they tried?"
    c "They can only touch you if you reach out to touch them first. As for what would happen... ahem! Let's just say they would regret such an action!"
    p "Hmm. What a powerful spell. Would you like to test it, Niir?"
    n "I have tesssted that ssspell before. I have no desssire to experrrience it again."
    p "I see. Thank you, Cyril; you may go."
    c "P-princess, I don't think it's wise to be alone with this, this..."
    p "Do you not trust your own spell? Or is it I you do not trust?"
    c "No...I trust you, just- please, be careful!"
    hide cyril with moveoutleft
    
    p "Do you have any business with me, dragon?"
    n "Yesss, Balrung wished to ssspeak with you."
    p "Well, where is he? Why doesn't he just come knock on my door?"
    n "I think he jussst likesss to send me on errandsss."
    p "So you weren't really watching me sleep...?"
    n "I'll let you wonderrr about that one."
    hide niir with moveoutright
    
    p "I suppose I'll see what Balrung wants..."
    if (asked_scepter == "Balrung"):
        "(Perhaps he has found the scepter?!)"
        
    scene bg dungeon with fade
    show balrung at midleft with dissolve
    show her at midright with moveinright
    