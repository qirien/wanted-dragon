################################################################################
# WANTED: DRAGON to Aid in Regaining Throne, No Experience Necessary
#
# This code is CC-BY-SA 4.0. Use it as long as you attribute and share your own code:
# http://creativecommons.org/licenses/by-sa/4.0/
#


# The game starts here.
label intro:
    scene logo with veryslowfade
    $ renpy.pause(1.6)
    play music princess_theme
    scene bg gate dusk
    show rain
    with fade
    play sound "sfx/rain.ogg" loop
    p neutral "Finally! You’d think that if they were going to hold some dragons captive, they would hold them in a place more accessible to princesses who want to harness their power for more important things!"
    p angry "But first... I’ll have to deal with the mage left to guard this place."
    show cyril hat neutral at center with moveinright
    "{b}This{/b} is the mage in charge?! He's barely more than a child!"
    "...This is exactly the kind of inefficiency I intend to remedy when I am queen!"
    show cyril hat concerned at basicfade
    c "{font=fonts/ankecallig-fg.ttf}Luxis Contigo! Luxia Contego? Conmigo?{/font}"
    show cyril hat surprised at basicfade
    c "I knew I didn't get that spell right!  If only I could remember how that went.  {font=fonts/ankecallig-fg.ttf}Luxing Contegus{/font}!  Hmmm... are those the proper words?"

    menu:
        "Play it sweet":
            jump sweet
        "Tell him the truth":
            jump truth
        "Ignore him.":
            jump ignore


label sweet:
    $ cyril_affection += 1
    p smile eyes closed "Oh hello! You must be in charge here. How lovely to make your acquaintance, Mr...?"
    show cyril hat smile at basicfade
    c "Merlonious.  Cyril Merlonious.  At least, the last time somebody called me it.  Which has been a while come to think of it.  "
    show cyril hat surprised at basicfade
    c "Erm, wait a moment... it's you.  Princess [p_name]!  I almost didn't recognize you!  Your Highness!  Did you find someone to relieve me?  Is that why you're here?"
    show cyril hat smile at basicfade
    c "I did so know this day would come."
    p smile "Yes, Moronious. Yes, I am here to relieve you. It’s quite a demotion for me, but well, one must perform one’s royal duties. "
    p smile "So if you’ll just show me around, then you can be on your way and leave these... dragons in my care."
    show cyril hat laugh at basicfade
    c "I can't tell you how happy I am to hear that!  I didn't think this day will come.  I must send word- oh!  "
    c "I just need the royal seal from you.  Have you spoken with the council of mages?  Is everything in order?"
    p surprised "Oh, how dreadful! They didn’t send me with it! They must have assumed that any person of intelligence would immediately see my royal person and know to do whatever I say."
    show cyril hat concerned at basicfade
    c "Of course.  But it is the custom, and you know what they say about rules being meant to be followed and all that gobbledy-spook that I think I remembered once.  Ah, well."
    p friendly "Perhaps I could come in out of the rain, and stay until we can get everything sorted out?"
    show cyril hat smile at basicfade
    c "Well, I guess I haven't had company in quite some time.  And it does get rather dreary with those dragons questioning me.  Come in, yes.  Come in."
    hide cyril at center with moveoutleft
    "Everyone falls for the Princess-caught-in-the-rain ruse."
    stop sound fadeout 2.0
    scene bg hall with fade
    show cyril hat neutral at center
    with moveinright
    p neutral "It is so cold in here; would you mind showing me to my room?"
    c "Your...room? Yes. Um. Well, you can have mine, that's probably the nicest. I mean, the only room that's not covered in dust, really."
    jump room_intro

label truth:
    p angry "I’m here to retake my rightful throne. Assist me, and be rewarded. Hinder me, and feel my wrath."
    show cyril hat surprised at basicfade
    c "Oh, it's you.  Princess [p_name]!  I almost didn't recognize you!  Your Highness!"
    c "I ummm... I most certainly don't want to hinder you.  But I am awfully confused to how I, a humble first-star mage, could help you."
    p shout "I’m wet, cold, and tired. I need the warmest room in this dreadful castle and a hot bath. If you can’t arrange that, then you are useless to me and had best begone."
    show cyril hat concerned blush at basicfade
    c "Ah, erm, yes of course your Highness!  A bath is coming right up!  And a room."
    c "Well, my room is the warmest room, but if you give me some time to relocate I'm sure I could find somewhere else to settle for the moment."
    p neutral "That is acceptable. You may lead me there now."
    hide cyril at center with moveoutleft
    stop sound fadeout 2.0
    scene bg hall with fade
    show cyril hat neutral at center
    with moveinright
    show cyril hat smile blush at basicfade
    c "So, this is [castle_name!t].  It hasn't been visited in quite some time.  Or cleaned actually.  Hehehe.  "
    c "I didn't expect company so I hadn't thought about cleaning.  I suppose I had better get to that.  I do not have any bath salts either, but I am pretty good with heating spells for the water."
    p angry "Yes, yes. Now, what can you tell me about the other... residents of this place?"
    show cyril hat concerned at basicfade
    c "It is just me.  Well, and the dragons.  But they are here for their punishment.  Kidnapping ladies is not a very delightful business I do say.  "
    show cyril hat neutral at basicfade
    c "Usually I find I must ignore them or they will try to plead their case.  Well, they don't really do that.  They more mock- anyway.  What brings you here again?"
    menu:
        "Make up something flattering.":
            $ cyril_affection += 1
            p laugh eyes closed "Believe it or not, I was thinking about... you."
            p smile "Doesn’t it get terribly lonely out here? Don’t you often find yourself wishing for companionship? "
            p smile "I try to meet the needs of all the citizens of our realm, as part of my royal duties. Surely there’s something I could help you with..."
            show cyril hat smile blush at basicfade
            c "Oh erm... you don't say..."
            show cyril hat smile blush eyes closed at basicfade
            c "I guess I... I mean as much as anyone... I mean... Oh.  It's a very thoughtful offer from you, surely."
            p laugh "I’m certain we could help each other. But for now...is this my new room?"
            show cyril hat concerned blush at center
            c "Yes, it's my- your room, now."
            jump room_intro
        "Tell the truth.":
            p tsk "Unfortunately, I find myself in the unenviable position of needing assistance from others to claim the crown that has been wrenched from my rightful hands."
            show cyril hat concerned at basicfade
            c "Oh, that is rather disappointing.  But as I believe, you were never in line for the throne?  Is that right?  It was that other girl?  That sister of yours?  "
            show cyril hat concerned blush at basicfade
            c "I do hope I got my facts right.  I'm incredibly mixed up these days.  Don't know my right from my left and my left from my right."
            p angry "Clearly. You’d best leave the facts to me and concentrate on doing my bidding."
            show cyril hat concerned blush eyes closed at basicfade
            c "I am sorry to have offended you Princess; I will leave it to you.  But, we've arrived at my room- er, your room. Is this to your liking?"
            jump room_intro

label room_intro:
    hide cyril at center with moveoutleft
    scene bg bedroom candle with fade
    show cyril hat neutral at center
    with moveinright
    p shocked "{b}This{/b} is the best room in the castle?"
    show cyril hat concerned at basicfade
    c "It is.  Well, I’ve tried to make it as comfortable as possible.  I have a few keepsakes from home in it and my frilly rug which does keep it warm in the middle of the cold snap.  "
    show cyril hat neutral at basicfade
    c "And it is close to the dragons so I can regularly keep watch over them, as I am supposed to.  Would you like to be somewhere further away?  This is a large castle."
    p neutral "No, no, this will do. Prepare my bath, and then you may leave."
    show cyril hat concerned blush at basicfade
    c "Yes, yes.  I will get right to running that bath for you my majesty. I mean my Highness!  Your Highness.  Because you are most certainly not mine... errr... I will see to that bath."
    p surprised "..."
    #TODO: SHOWER? splash sfx?
    scene black with fade
    scene bg bedroom candle with fade

    "That’s better! One of these days I will need to look into obtaining my own weather mage...awful that I should be drenched at the whim of the mere skies."
    "But now to meet with the dragons..."
    menu:
        "Call for the mage.":
            scene bg corridor with fade
            p shout "Mage! Moronious! I'm ready for you now!"
            show cyril hat neutral at center with moveinright
            show cyril hat surprised at basicfade
            c "Ready for me to what?"
            p neutral "I wish to speak to the dragons."
            show cyril hat concerned blush at basicfade
            c "If-if you wish me to take you there, I will, though I'm not sure what you'd want with them."
            jump meet_dragons
        "Explore on your own.":
            jump explore

label ignore:
    $ cyril_insanity += 1
    p neutral "..."
    show cyril hat concerned at basicfade
    c "Oh yes.  Oh, of course, there is an apparition in front of me. Oh Cyril.  You’ve finally done it.  You’ve gone completely bonkers."
    "He thinks I’m a ghost?! What a strange man... still, I can use that to my advantage and slip past him."
    show cyril hat neutral at basicfade
    c "Well, back to that spell again.  {font=fonts/ankecallig-fg.ttf}Luxius Conremo!{/font} - I'll never get it!  Now where did I keep that spellbook.  It was around here somewhere!  "
    show cyril hat surprised at basicfade
    c "I just need to find it.  Perhaps one of those surly dragons knows where it got to."
    "Yes! Lead me right to the dragons!  I’ll just follow from a discreet distance..."

    stop sound fadeout 2.0
    play music evil_theme
    scene bg dungeon night with fade
    show balrung neutral at center, basicfade
    show niir neutral at quarterright, basicfade
    show cyril hat neutral at quarterleft with moveinleft

    show cyril hat concerned at basicfade
    c "Dragons.  I do need to ask you about my spell book. It seems I've misplaced it."
    show cyril hat angry at basicfade
    c "Again."
    n "Cyril the Cowardly."
    n "And I see you've brought us a tassssty morssssel.  How generous."
    show cyril hat neutral at basicfade
    c "Oh don’t mind her.  She’s just an apparition.  Wait.  Why can you see her?"

    jump dragon_chat

label explore:
    "I'll find out more without that silly mage following me around."
    scene bg corridor with fade
    "Now, which way...?"
    show cyril hat neutral at center with moveinright
    show cyril hat smile blush at basicfade
    c "Princess! You're done with your b-b-bath, then? Please, let me show you around the castle."
    p "I do not require you at the moment. Leave me alone."
    show cyril hat concerned blush at basicfade
    c "Oh, I don't think I should. This castle can be quite confusing, and there's no servants or anyone to help you. Please, I'll show you around."
    p angry "...Very well. You may start with the dragons."

label meet_dragons:
    hide cyril at center with moveoutleft
    scene bg stairs night with fade
    show cyril hat neutral at center
    with moveinright
    show cyril hat concerned at basicfade
    c "I must warn you, do not believe a word they say.  They can be quite cutting at times.  I remember this one day where they- well, that's not important, and I most certainly did not cry for days about it."
    show cyril hat neutral at basicfade
    c "The dragons are Niir and Balrung?  Niir, well, don't be surprised if he looks at you like he might eat you for dinner.  He looks at every female that way.  "
    c "It is a good thing that I am not a female sometimes because I don't know what I'd do if he talked to me like that!"
    show cyril hat angry at basicfade
    c "He was kidnapping ladies in the marketplace, just for fun, apparently.  Causing all sorts of trouble until he had to be locked away."
    show cyril hat concerned at basicfade
    c "Balrung, he is much more courteous but also rather stubborn.  He will try to make you see things his way, and not by the most honest methods."
    p surprised "Oh my, that sounds dreadful!"
    "And yet also intriguing."
    hide cyril at center with moveoutright
    play music evil_theme
    scene bg dungeon night with fade
    show cyril hat neutral at quarterleft with moveinleft
    c "Helllo!  Dragons!  It is I, Cyril.  Are you in here?"
    show balrung neutral at center with moveinright
    show cyril hat neutral at basicfade
    show balrung smirk at basicfade
    b "Merlonious. Here to taunt us again? Yes, dangling the key in front of the chained prisoners, very tasteful. But who’s this charming lady?"
    show niir neutral at quarterright with moveinright
    n "Cccyril the Chassssste.  I sssssee that you have brought a lady friend.  Delic-delightful."
    show cyril hat concerned at basicfade
    c "Oh, no you don't!  This is royalty.  The royal Princess [p_name]! And I will not have you looking at her like that Niir."
    show cyril hat concerned blush at basicfade
    c "I mean, I don't- I can't- Regardless, she is here to see you.  Apparently.  Though I still don't get why..."
    menu dragon_chat:
        "Allude to your purpose in veiled terms.":
            $ balrung_affection += 1
            p neutral "I, Princess [p_name], am here in the hopes that one day, old enemies may become allies who work together to remedy the injustices of the realm."
            show niir smirk at basicfade
            n "I would rather work on the injustices of that unflattering dress of yours.  How about you come a little closssser, so that I can see it more fully."
            show balrung angry at basicfade
            b "There are many injustices I would fight, had I only the freedom to do so."
            show cyril hat angry at basicfade
            c "Now, now.  Behave, you two."
            show cyril hat concerned at basicfade
            c "They are here for a reason, Princess - they have behaved badly. They can leave once they find love and find reform."
            c "True reform cannot happen without love, you know.  So they are quite simply prisoners of their own choosing."

        "Pretend you are just checking on things.":
            $ cyril_affection += 1
            p smile "I’m Princess [p_name]. I just...wanted to see how things were going here. You aren’t being mistreated, are you?"
            show balrung angry at basicfade
            b "Would you call it mistreatment to keep someone chained not only to a location, but inside an inferior form? This frail human appearance is not our normal state, you know."
            show cyril hat concerned at basicfade
            c "Oh, he's just being dramatic Princess.  They know the rules of the agreement.  They can leave once they find love and find reform."
            c "True reform cannot happen without love, you know.  So they are quite simply prisoners of their own choosing."
            show niir sad at basicfade
            n "I would call it mistreatment to be kept away from the world daily - to see the sights and sssmell the... flowers."
            show niir mischief at basicfade
            n "Perhapssss you are here to help though?  Eassse the pain?"

    if (cyril_insanity > 0):
        show cyril hat surprised at basicfade
        c "Sooo...wait, you're not an apparition? You're real? Why didn't you say something to me earlier?"
        p angry "I am not interested in unnecessary conversation."
        show balrung smirk at basicfade
        b "What {b}are{/b} you interested in, then?"
    # Whom to talk to?
    menu:
        "Address Niir.":
            p friendly "Niir...what an interesting name. Tell me about yourself."
            show niir concerned at basicfade
            n "Intrigue you do I?  I ssssuppose I would.  Unlike my decrepit friend here who has no ssssense of amusement or... play."
            n "How about you, are you interesssted in fun?  Perhapsss playing a little game?"
            p neutral "Tell me what it is, and then I shall decide."
            show niir mischief at basicfade
            n "Oh, it is a game that would have you sssscreaming for more.  That much is for sssure."
            n "Are you afrrrraid of heights?  Perhaps you would like see some of the ssssights of the cassstle?"
            p surprised "What did you have in mind?"
            show niir smirk at basicfade
            n "That, is my little sssecret.  You will have to help me leave to find out."

            menu:
                "\"I shall consider your... offer, Niir.\"":
                    $ niir_affection += 1
                    p smile "I shall consider your... offer, Niir."
                    show niir mischief zoomin at center, come_closer, basicfade
                    n "I’ll be waiting.  Until then, why not come clossser?  Let usss get... {i}acquainted{/i}."
                    p angry "I can acquaint myself with you well enough from here."
                    show niir frown at quarterright, reset_zoom

                "\"Not interested.\"":
                    p tsk "Not interested."
                    show niir smirk at basicfade
                    n "Pity.  I could have a lot of ussse for someone like you as my plaything."
                    show balrung determined at basicfade
                    b "This Princess is no one’s ‘plaything’, Niir, least of all yours."
                    show niir frown at basicfade
                    n "You have no ssssense of fun.  But if you would rather spend time with thisss sourpussss, then you can make your choice."

        "Address Balrung.":
            $ balrung_affection += 1
            p laugh "Balrung...how long have you been here?"
            show balrung neutral at basicfade
            b "Forty years, by human reckoning. And even though that is but a short time to a long-lived dragon, since we are imprisoned within human form we feel every second of our captivity keenly."
            show balrung smile at basicfade
            b "Well, I do, at any rate. I’m not sure I can say the same for my heartless young associate here."
            show niir mischief at basicfade
            n "Heartlessss? I assssure you, my heart beats quite vigorously."

        "Address Moronious.":
            $ cyril_affection += 1
            p angry "It’s just these two? Aren’t there any other dragons here?"
            show cyril hat neutral at basicfade
            c "Most of the other dragons have moved on.  Actually, come to think of it, I've forgotten when the last one left.  Findol? Firgol? And he left with a young lady?  "
            show cyril hat concerned at basicfade
            c "I'm not even sure if I'm remembering it right.  But these two have made this place home for a long time."
            p laugh "You must have considerable magical powers, if you are guarding them here all on your own."
            show cyril hat smile blush at basicfade
            c "Oh, well I wouldn’t say.  I mean people have said.  Well, my mother.  Once.  But yes, I suppose someone has to do the job and that someone is me. "
            c "It’s quite a funny story really, I just fell into it.  "
            show cyril hat neutral at basicfade
            c "I was at the council and they were all concerned about the legacy of my master and they were all shouting over one another and didn’t even realize I was in the room.  "
            c "And I was telling them all that they needed someone new to guard these pesky dragons..."
            show cyril hat concerned at basicfade
            c "And then they all left.  And put out the lamps and I was just there.  So I guess the council had made their decision after all, that I was to do something about the dragons.  And here I am."

    show balrung smile at basicfade
    b "Yes, yes...But, Princess, tell us about yourself. How is the royal family?"
    p surprised "My...family?"
    show balrung smirk at basicfade
    b "Your father, the king, is he well?"
    p neutral "Yes, very well, thank you. Do- do you know him?"
    show balrung smile at basicfade
    b "I met him once, before my sojourn here. He seemed capable, if a bit naïve. And the Queen?"
    p angry "My mother died several months ago."
    show balrung neutral at basicfade
    b "I'm terribly sorry; how rude of me to bring it up! Please accept my apologies, Princess."
    p neutral "You didn't know."
    show cyril hat concerned blush at basicfade
    c "B-but, he {b}did{/b} know, I mentioned it several weeks ago? I think? Or maybe I just thought of mentioning it? Or maybe I just thought about thinking about mentioning it?"
    show balrung angry at basicfade
    b "I don't think so, Merlonious."
    p neutral "Anyway, I am finished here...for now."
    show niir mischief at basicfade
    n "Ssseee you later, Prrrrincessss...."
    hide cyril at quarterleft with moveoutleft

    play music cyril_theme
    scene bg stairs night with fade
    show cyril hat neutral at center
    with moveinright
    # After talked to Niir, Balrung, or Cyril
    show cyril hat concerned at basicfade
    c "So there we have it.  The dragons.  As you can see my job is not at all easy."
    show cyril hat concerned eyes closed at basicfade
    c "I don't want to dwell on it but there have been some times where I have just felt like giving up!"
    p laugh eyes closed "You really are quite pathetic, aren't you?"
    show cyril hat surprised at basicfade
    c "Ex-excuse me?"
    p laugh "I mean, no one knows who you are.  You're guarding this tower with no reward."
    p smile "You're completely pathetic."
    show cyril hat concerned blush at basicfade
    c "I-I... I assure you that I'm not."
    show cyril hat concerned eyes closed at basicfade
    c "Surely, some people have said some things akin to that, but they d-do not know."
    p angry "You assure me?  How inspiring.  So I should believe you then?"
    p neutral "Is it not true that you cannot do a thing here?"
    show cyril hat concerned  at basicfade
    c "I am loyal.  I did not have to take up post here."
    p angry "And where has your loyalty got you?  Hmmm?"
    show cyril hat angry at basicfade
    "His eyes flashed with uncharacteristic anger."
    "What do you know?  There is something boiling under that bumbling facade."
    c "You are testing me, Princess."
    "And I've never had so much fun."
    show cyril hat surprised at basicfade
    c "What are you doing, your Highness?"
    p laugh "Taking your wand, of course."
    p laugh eyes closed "You don't really need it, do you?"
    show cyril hat concerned blush eyes closed at basicfade
    c "I do... need it.  Most certainly."
    p laugh "Beg me."
    show cyril hat concerned blush at basicfade
    c "Um- pardon?"
    p laugh "Beg me for it."
    "He is not proving himself in the slightest."
    "But still it is amusing... perhaps he could make a good {i}slave{/i} one day..."
    show cyril hat surprised at basicfade
    c "I will not."
    p smile "Of course you will, you're pathetic and I can do whatever I lik-"
    play sound "sfx/electricity.ogg"
    show cyril hat angry with magic_flash
    c "You {b}will not{/b}."
    "Is that lightning?"
    "The mage Moronious has {i}actually{/i} become scary."
    p neutral "Fine.  Have your wand."
    "Perhaps he is worth more than a slave after all."
    stop sound fadeout 2.0
    show cyril hat smile blush eyes closed at basicfade
    c "Thank you, your Highness. Now, where was I? Oh yes, I was going to invite you to supper!"
    show cyril hat concerned blush at basicfade
    c "Food is pretty spare in these parts, thanks to how isolated everything is."
    show cyril hat smile blush at basicfade
    c "I normally conjure something up, so, if you'd like, you could join me for a supper.  Otherwise, I could bring something to your room?"

    menu:
        "\"Bring food to my room!\"":
            jump broughtfood
        "\"I suppose I could join you...\"":
            p smile "I suppose I could join you if you don't bore me with with your stories."
            jump joinmage

label broughtfood:
    p neutral "I am tired. You may bring hot food to my room. That will be all, Moronious."
    show cyril hat concerned blush eyes closed at basicfade
    c "I-It's Merlonious. You could call me Cyril? No one does, but you could..."
    p angry "Yes, yes, I said \"that will be all\"!"
    show cyril hat smile blush at basicfade
    c "Right! Food. I'll bring it later. Bye!"
    hide cyril at center with moveoutleft
    return

label joinmage:
    $ cyril_affection += 1
    scene bg kitchen with fade
    show cyril hat neutral at center
    with moveinleft
    show cyril hat smile at basicfade
    c "Ah, yes, Princess.  So glad of you to join me."
    show cyril hat concerned blush eyes closed at basicfade
    c "I mean glad of me."
    show cyril hat smile blush at basicfade
    c "I mean I'm the one who's glad."
    show cyril hat concerned blush at basicfade
    c "I'm terribly sorry, I don't seem to be making much sense."
    p laugh "Your name- it's Moronious, isn't it?"
    show cyril hat neutral at basicfade
    c "Merlonious. Cyril Merlonious."
    p surprised "Have you ever thought of changing your name to Moronious?"
    show cyril hat surprised at basicfade
    c "Why would I do something like that?"
    p laugh eyes closed "Why not?"
    show cyril hat neutral at basicfade
    c "Yes, erm.  Good point."
    show cyril hat smile at basicfade
    c "I'll just whip something up for us.  But nothing too complicated."
    show cyril hat concerned at basicfade
    c "Actually, my repertoire isn't that vast with food spells."
    show cyril hat neutral at basicfade
    c "So I'd better just do what I can do. {font=fonts/ankecallig-fg.ttf}Vittus Cottura{/font}!"
    show cyril hat neutral with magic_flash
    p tsk "..."
    show cyril hat smile at basicfade
    c "I hope it is to your liking."
    show cyril hat smile blush at basicfade
    c "It's not much but I-"
    p shout "Silence."
    show cyril hat concerned blush at basicfade
    c "Ah, yes.  I will be entirely, completely-"
    show cyril hat concerned blush eyes closed at basicfade
    c "Silent."
    p neutral "...That's better."
    show cyril hat concerned at basicfade
    c "..."
    show cyril hat smile at basicfade
    c "Yes, well, I was given the name Merlonious after the great Merlin, you see."
    show cyril hat neutral at basicfade
    c "But I guess, to family I've always been Cyril. Cyril the Competent, they say."
    show cyril hat concerned at basicfade
    c "Which actually isn't much of a compliment, come to think of it."
    show cyril hat laugh at basicfade
    c "But never mind that."
    show cyril hat smile blush at basicfade
    c "Are you enjoying your meal?"
    p angry "You do know that I am the Princess, correct?"
    p tsk "And in what way did you think that this was worthy of a princess?"
    show cyril hat concerned blush at basicfade
    c "I... I'm not quite sure."
    p neutral "I am sure you will do better next time."
    return
