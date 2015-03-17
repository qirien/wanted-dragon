################################################################################
# WANTED: DRAGON to Aid in Regaining Throne, No Experience Necessary
# 
# This code is CC-BY-SA 4.0. Use it as long as you attribute and share your own code:
# http://creativecommons.org/licenses/by-sa/4.0/
#


# The game starts here.
label intro:
    scene bg gate dusk with fade
    play music princess_theme
    p "Finally! You’d think that if they were going to hold some dragons captive, they would hold them in a place more accessible to princesses who want to harness their power for more important things!"
    p "But first... I’ll have to deal with the mage left to guard this place."
    show cyril hat neutral at center with moveinright
    "{b}This{/b} is the mage in charge?! He's barely more than a child!"
    "...This is exactly the kind of inefficiency I intend to remedy when I am queen!"
    "Still... I’ll have to deal with him somehow."
    c hat concerned "Biggeldy, boggaldy, wap!"
    c hat surprised "I knew I didn't get that spell right!  If only I could remember how that went.  Biggeldy, boggaldy, wu?  Boggaldy, biggaldy... hmmm... I'm not even sure that I'm using the proper words."
#    p "My name is..."
#    $ p_name = renpy.input("What is your name?", "Chrysandra", length=30)
#    p "I am Princess [p_name]."
#    c "How can I help you, Princess [p_name]?"
    
    menu:
        "Play it sweet":
            jump sweet
        "Tell him the truth":
            jump truth
        "Ignore him.":
            jump ignore
        
            
label sweet:
    p "Oh hello! You must be in charge here. How lovely to make your acquaintance, Mr...?"
    c hat smile "Merlonious.  Cyril Merlonious.  At least, the last time somebody called me it.  Which has been a while come to think of it.  "
    c hat surprised "Erm, wait a moment... it's you.  Princess [p_name]!  I almost didn't recognize you!  Your majesty!  Did you find someone to relieve me?  Is that why you're here?"
    c hat smile "I did so know this day would come."
    p "Yes, Moronious. Yes, I am here to relieve you. It’s quite a demotion for me, but well, one must perform one’s royal duties. So if you’ll just show me around, then you can be on your way and leave these… dragons in my care."
    c hat laugh "I can't tell you how happy I am to hear that!  I didn't think this day will come.  I must send word- oh!  I just need the royal seal from you.  Have you spoken with the council of mages?  Is everything in order?"
    p "Oh, how dreadful! They didn’t send me with it! They must have assumed that any person of intelligence would immediately see my royal person and know to do whatever I say."
    c hat concerned "Of course.  But it is the custom, and you know what they say about rules being meant to be followed and all that gobbledy-spook that I think I remembered once.  Ah, well."
    p "Perhaps I could come in out of the rain, and stay until we can get everything sorted out?"
    c hat smile "Well, I guess I haven't had company in quite some time.  And it does get rather dreary with those dragons questioning me.  Come in, yes.  Come in."
    "Ha ha, yes! Everyone falls for the princess-caught-in-the-rain ruse."
    hide cyril
    with moveoutleft
    scene bg hall with fade
    show cyril hat neutral at midright
    with moveinright
    p "It is so cold in here; would you mind showing me to my room?"
    c "Your...room? Yes. Um. Well, you can have mine, that's probably the nicest. I mean, the only room that's not covered in dust, really."
    jump room_intro

label truth:
    p "I’m here to retake my rightful throne. Assist me, and be rewarded. Hinder me, and feel my wrath."
    c "Oh, it's you.  Princess [p_name]!  I almost didn't recognize you!  Your majesty!  I ummm... I most certainly don't want to hinder you.  But I am awfully confused to how I, a humble servant of Dyconis could help you." 
    p "I’m wet, cold, and tired. I need the warmest room in this dreadful castle and a hot bath. If you can’t arrange that, then you are useless to me and had best begone."
    c "Ah, erm, yes of course your highness!  A bath is coming right up!  And a room.  Well, my room is the warmest room, but if you give me some time to relocate I'm sure I could find somewhere else to settle for the moment."
    p "That is acceptable. You may lead me there now."
    hide cyril
    with moveoutleft
    scene bg hall with fade
    show cyril hat neutral at center
    with moveinright
    c "So, this is the castle of the banished.  It hasn't been visited in quite some time.  Or cleaned actually.  Hehehe.  I didn't expect company so I hadn't thought about cleaning.  I suppose I had better get to that.  I do not have any bath salts either, but I am pretty good with heating spells for the water."
    p "Yes, yes. Now, what can you tell me about the other... residents of this place?"
    c "It is just me.  Well, and the dragons.  But they are here from their punishment.  Kidnapping ladies is not a very delightful business I do say.  "
    c "Usually I find I must ignore them or they will try to plead their case.  Well, they don't really do that.  They more mock- anyway.  What brings you here again?"
    menu:
        "Make up something flattering.":
            p "Believe it or not, I was thinking about... you."
            p "Doesn’t it get terribly lonely out here? Don’t you often find yourself wishing for companionship? I try to meet the needs of all the citizens of our realm, as part of my royal duties. Surely there’s something I could help you with..."
            c "Oh erm... you don't say..."
            c "I guess I... I mean as much as anyone... I mean... Oh.  It's a very thoughtful offer from you, surely."
            p "I’m certain we could help each other. But for now..."
            jump room_intro
        "Tell the truth.":
            p "Unfortunately, I find myself in the unenviable position of needing assistance from others to claim the crown that has been wrenched from my rightful hands."
            c "Oh, that is rather disappointing.  But as I believe, you were never in line for the throne?  Is that right?  It was that other girl?  That sister of yours?  "
            c "I do hope I got my facts right.  I'm incredibly mixed up these days.  Don't know my right from my left and my left from my right."
            p "Clearly. You’d best leave the facts to me and concentrate on doing my bidding."
            c "I am sorry to have offended you Princess, I must leave it to you.  Is this to your liking?"
            jump room_intro
    
label room_intro:
    hide cyril
    with moveoutleft
    scene bg bedroom dusk with fade
    show cyril hat neutral at midright
    with moveinright
    p "{b}This{/b} is the best room in the castle?"    
    c "It is.  Well, I’ve tried to make it as comfortable as possible.  I have a few keepsakes from home in it and my frilly rug which does keep it warm in the middle of the cold snap.  "
    c "And it is close to the dragons so I can regularly keep watch over them, as I am supposed to.  Would you like to be somewhere further away?  This is a large castle."
    p "No, no, this will do. You may leave me for now, but I may need your assistance later."
    c "Yes, yes.  I will get right to running that bath for you my majesty. I mean your highness!  Your majesty.  Because you are most certainly not mine... errr... I will see to that bath."
    p "..."
    #TODO: SHOWER?
    scene black with fade
    scene bg bedroom dusk with fade
    
    "That’s better! One of these days I will need to look into obtaining my own weather mage...awful that I should be drenched at the whim of the mere skies)."
    "But now to meet with the dragons..."
    menu:
        "Call for Cyril.":
            scene bg corridor with fade
            p "Mage! Moronious! I'm ready for you now!"
            show cyril hat neutral at center with moveinright
            c "Ready for me to what?"
            p "I wish to speak to the dragons."
            c "If-if you wish me to take you there, I will, though I'm not sure what you'd want with them."
            jump meet_dragons            
        "Explore on your own.":
            jump explore 

label ignore:
    $ cyril_insanity += 1
    p "..."
    c "Oh yes.  Oh of course, there is an apparition in front of me, oh Cyril.  You’ve finally done it.  You’ve gone completely bonkers."
    "He thinks I’m a ghost?! What a strange man... still, I can use that to my advantage and slip past him"
    c "Well, back to that spell again.  Biggeldy- I'll never get it!  Now where did I keep that spell-book.  It was around here somewhere!  "
    c "I just need to find it.  Perhaps one of those surly dragons knows where it got to."    
    "Yes! Lead me right to the dragons!  I’ll just follow from a discreet distance..."  
    
    scene bg dungeon with fade
    
    c "Dragons.  I do need to ask you about my spell book. It seems I've misplaced it."
    c "Again."
    n "Cyril the Cowardly."
    n "And I see you've brought us a tassssty morssssel.  How generous."
    c "Oh don’t mind her.  She’s just my apparition.  Wait.  Why can you see her?"
    jump dragon_chat

label explore:
    "I'll find out more without that silly mage following me around."
    scene bg corridor with fade
    "Now, which way...?"
    show cyril hat neutral at center with moveinright
    c "Princess! You're done with your b-b-bath, then? Please, let me show you around the castle."
    p "I do not require you at the moment. Leave me alone."
    c "Oh, I don't think I should. This castle can be quite confusing, and there's no servants or anyone to help you. Please, I'll show you around."
    p "...Very well. You may start with the dragons."
    
label meet_dragons:
    hide cyril
    with moveoutleft
    scene bg stairs with fade
    show cyril hat neutral at center
    with moveinright
    play music evil_theme    
    c "I must warn you, do not believe a word they say.  They can be quite cutting at times.  I remember this one day where they- well that's not important and I most certainly did not cry for days about it."
    c "The dragons are Niir and Balrung?  Niir, well, don't be surprised if he looks at you like he might eat you for dinner.  He quite looks at every female that way.  It is a good thing that I am not a female sometimes because it is rather disconcerting to be approached like a piece of meat."
    c "He was kidnapping ladies in the marketplace just for fun apparently.  Causing all sorts of trouble until he had to be locked away."
    c "Balrung, he is much more courteous but he is rather stubborn.  He will try to make you see it his way and not by the most honest methods."
    p "Oh my, that sounds dreadful!"
    "And yet also intriguing."
    c "Ah, yes.  Now where did I keep that key.  It is a magic key and it should be... yes.  There it is, right in the stone there.  Accimeidum! Now we shall enter."
    scene bg dungeon with fade
    show cyril hat neutral at quarterleft
    c "Helllo!  Dragons!  It is I, Cyril.  Are you in here?"
    show balrung neutral at center with moveinright
    b "Merlonious. Here to taunt us again? Yes, dangling the key in front of the chained prisoners, very tasteful. But who’s this charming lady?"
    show niir neutral at quarterright with moveinright
    n "I sssssee that you have brought a friend.  Delic-delightful."
    c "Oh no you don't.  This is royalty.  The royal princess [p_name]! And I will not have you looking at her like that Niir.  I mean, I don't- I can't- Regardless, she is here to see you.  Apparently.  Though I still don't get why..."
    menu dragon_chat:
        "Allude to your purpose in veiled terms.":
            $ balrung_affection += 1
            p "I, Princess [p_name], am here in the hopes that one day, old enemies may become allies who work together to remedy the injustices of the realm."
            n smirk "I would rather work on the injustices of that unflattering dress of yours.  How about you come a little closssser, so that I can see it more fully." 
            b angry "There are many injustices I would fight, had I only the freedom to do so."
            c "Now, now.  Behave, you two."
            c "They are here for a reason, Princess - they have behaved badly. They can leave once they find love and find reform.  True reform cannot happen without love, you know.  So they are quite simply prisoners of their own choosing."
            
        "Pretend you are just checking on things.":
            p "I’m Princess [p_name]. I just...wanted to see how things were going here. You aren’t being mistreated, are you?"
            b angry "Well, would you call it mistreatment to keep someone chained not only to a location, but inside an inferior form? This frail human-like appearance is not our normal state, you know."
            c "Oh, he's just being dramatic Princess.  They know the rules of the agreement.  They can leave once they find love and find reform.  True reform cannot happen without love, you know.  So they are quite simply prisoners of their own choosing."
            n smirk "I would call it mistreatment to be kept away from the world daily - to see the sights and smell the wome- flowers.  It has been unfortunate.  Perhapssss you are here to help though?  Eassse the pain?"
    
    # Whom to talk to?
    menu:
        "Address Niir.":

            p "Niir...what an interesting name. Tell me about yourself."
            n concerned "Intrigue you do I?  I ssssuppose I would.  Unlike my decrepit friend here who has no sense for amusement or play.  How about you, are you interesssted in fun?  Perhaps playing a little game?"
            p "Tell me what it is, and then I shall decide."
            n mischief "Oh, it is a game that would have you sssscreaming for more.  That much is for sssure.  Are you afrrrraid of heights?  Perhaps you would like see some of the ssssights of the cassstle?"
            p "What did you have in mind?"
            n smirk "That, is my little sssecret.  You will have to help me leave to find out."
            
            menu:
                "\"I shall consider your... offer, Niir.\"":
                    $ niir_affection += 1
                    p "I shall consider your... offer, Niir."
                    n mischief "I’ll be waiting.  Until then, why not come clossser?  Let usss get...acquainted."
                
                "\"Not interested.\"":
                    p "Not interested."
                    n neutral "Pity.  I could have a lot of ussse for someone like you as my plaything."
                    b determined "This Princess is no one’s ‘plaything’, Niir, least of all yours."
                    n frown "You have no ssssense of fun.  But if you would rather spend time with thisss sourpussss, then you can make your choice."

        "Address Balrung.":
            $ balrung_affection += 1
            p "Balrung...how long have you been here?"
            b neutral "Forty years, by human reckoning. And even though that is but a short time to a long-lived dragon, since we are imprisoned within human form we feel every second of our captivity keenly."
            b smile "Well, I do, at any rate. I’m not sure I can say the same for my heartless young companion here."
            n mischief "Heartlessss? I assssure you, my heart beats quite vigorously."
        
        "Address Cyril.":
            $ cyril_affection += 1
            p "It’s just these two? Aren’t there any other dragons here?"
            c "Well, as I said.  Most of the other dragons have moved on.  Actually, come to think of it, I've forgotten when the last one left.  Who was that heroine who came to- Or maybe it was some wilderbeast.  "
            c "I'm not even sure if I'm remembering it right.  But these two have made this place home for a long time."
            p "You must have considerable magical powers, if you are guarding them here all on your own."
            c "Oh, well I wouldn’t say.  I mean people have said.  Well, my mother.  Once.  But yes, I suppose someone has to do the job and that someone is me.  It’s quite a funny story really, I just fell into it.  "
            c "I was at the council and they were all concerned about the legacy of my master and they were all shouting over one another and didn’t even realize I was in the room.  "
            c "And I was telling them all that something must be done about those pesky dragons..."
            c "And then they all left.  And put out the lamps and I was just there.  So I guess the council had made their decision after all, that I was to do something about the dragons.  And here I am."

    b smile "But, Princess, tell us about yourself. How is the royal family?"
    p "My...family?"
    b smirk "Your father, the king, is he well?"    
    p "Yes, very well, thank you. Do- do you know him?"
    b smile "I met him once, before my sojourn here. He seemed capable, if a bit naïve. And the Queen?"
    p "My mother died several months ago."
    b neutral "I'm terribly sorry; how rude of me to bring it up! Please accept my apologies, Princess."
    p "You didn't know."
    c "B-but, he {b}did{/b} know, I mentioned it several weeks ago? I think? Or maybe I just thought of mentioning it? Or maybe I just thought about thinking about mentioning it?"
    b angry "I don't think so, Merlonious."
    p "Anyway, I am finished here...for now."
    n smirk "Ssseee you later, Prrrrincessss...."
    hide cyril
    with moveoutleft

    scene bg stairs with fade
    show cyril hat neutral at center
    with moveinright
    # After talked to Niir, Balrung, or Cyril
    # TODO: play music cyril_theme
    c "So there we have it.  The dragons.  As you can see my job is not at all easy."
    c "I don't want to dwell on it but there have been some times where I have just felt like giving up!"
    p "You don't say."
    c "But regardless you are here now, your highness, so it isn't all bad!  Not at all."
    c "Food is pretty spare in these parts, thanks to how isolated everything is."
    c "I normally conjure something up, however."
    c "If you'd like, you could join me for a supper.  Otherwise I could bring something to your room?"

    menu:
        "\"I'd rather have something brought to me, and brought to me hot!\"":
            jump broughtfood
        "\"I suppose I could join you if you don't bore with with your stories.\"":
            jump joinmage 

label broughtfood:
    p "I am tired. You may bring hot food to my room. That will be all, Moronious."
    c "It's Merlonious. You could call me Cyril? No one does, but you could..."
    p "Yes, yes, I said \"that will be all\"!"
    c "Right! Food. I'll bring it later. Bye!"
    return

label joinmage:
    $ cyril_affection += 1
    scene bg kitchen with fade
    show cyril hat neutral at midright
    with moveinleft
    c "Ah, yes Princess.  So glad of you to join me."
    c "I mean glad of me."
    c "I mean I'm the one who's glad."
    c "I'm terribly sorry, I don't seem to be making much sense."
    p "Your name- it's Moronious, isn't it?"
    c "Merlonious. Cyril Merlonious."
    p "Have you ever thought of changing your name to Moronious?"
    c "Why would I do something like that?"
    p "Why not?"
    c "Yes, erm.  Good point."
    c "I'll just whip something up for us.  But nothing too complicated."
    c "Actually, my repertoire isn't that vast with food spells."
    c "So I'd better just do what I can do. Vittus Cottura!"
    p "..."
    c "I hope it is to your liking."
    c "It's not much but I-"
    p "Silence."
    c "Ah, yes.  I will be entirely, completely-"
    c "Silent."
    p "...That's better."
   
    c "Yes, well, I was given the name Merlonious after the great Merlin, you see."
    c "But I guess, to family I've always been Cyril.  Cyril the Competent, they say."
    c "Which actually isn't much of a compliment come to think of it."
    c "But never mind that."
    c "Are you enjoying your meal?"
    p "You do know that I am a princess, correct?"
    p "And in what way did you think that this was worthy of a princess?"
    c "I... I'm not quite sure."
    p "I am sure you will do better next time."
    return
