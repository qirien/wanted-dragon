# Balrung's Route

label balrung_time1:
    scene bg dungeon with fade
    show balrung at midright with dissolve
    show princess at midleft with moveinleft
    b "Princess. What a pleasure it is to see your face. But, of course, you didn't come here to talk with me. Are you looking for Niir?"
    p "No, I wanted to talk to you."
    b "Surely Niir's power or Cyril's magic would be more to your liking?"
    p "My...liking?"
    b "Yes, I imagine you're looking for some gullible fool that you can trick in to using their powers for your benefit? A thrall, a lackey, a minion?"
    p "No, no of course not!"
    "(Is it that obvious?!)"
    b "Oh really? My apologies, then. What {b}does{/b} bring you here?"
    p "I..."
    menu:
        "I'm bored.":
            p "I'm bored. You're the least likely to offend or annoy me."
            b "Oh, shall I entertain you, then? Like a jester?"
            p "I have a hard time imagining that!"
            b "But not the humility, alas."
            
        "I need an ally.":
            p "I need an ally. I will rule this kingdom one day, and will need a loyal...partner."
            b "Oh? And you thought I would suit you?"
            


label balrung_time2:
     
     menu:
          "Pay attention":
                 b "We met forty years ago. I was young, then, full of ideals of cooperation and mutual understanding. She was a mage who came to live among our kind to learn more about us and (though she never said it) to prove to us that humans were worth talking to."
                 b "She was... like you, in many ways. Powerful. Ambitious. Intelligent.  Her Queens and Pawns strategies were always elegant and ruthless; her victories surprising yet inevitable."
                 b "We played many games together. After her studies were complete and she returned to her Academy, I'd take on this feeble human form just to meet her there and match wits with her."
                  b "I'm not sure she understood how much of a sacrifice that was for me; how I was ridiculed, how many friends I alienated."
     "Focus on strategy.":
                  b "Forty years ago... blah, blah, cooperation... blah, blah ambitious, blah blah, strategies... blah, blah, sacrifice."
                  "(Ah-hah! He's trying to draw my attention with his Queens while the Pawns setup a chain reaction! My Queens shall whittle down his defenses while he's not paying attention.)"

                  b "So when I invited her to join me, permanently, as a part of a human-dragon marriage alliance, I thought she'd be honored. It was her life's work, after all."
                  b "But she refused. She wanted {b}me{/b} to join {b}her{/b}. You humans always want to be the ones in charge."
                  p "Of course we do. But wouldn't that accomplish the same thing?"
                  b "It's completely different! You humans want to use us, subordinate us, rule us! I wanted an alliance of equal partners!"
                  b "I should have waited. I should have elucidated my proposal more elegantly."
                  p "What did you do?"
                  b "When she wouldn't come with me, I brought her with me anyway."
                  p "You kidnapped her?!"
                  b "No! I would have let her leave, once she had listened to me! She refused to even talk to me! And her professors were influencing her with their human-supremacy attitudes. I had to bring her away from all of that."
                  p "That's quite evil of you. Did it work?"
                  b "No. No, it...didn't work at all. She used her magic, and her very life force, to transform my lair into this... prison. To trap me in human form, and make it possible for her colleagues to trap other dragons who failed to conform to their human ideals of dragon behavior."
                  menu:
                            "Serves you right.":
                                        p "Serves you right. That's what you wanted to do to her, after all - trap her here with you."
                                        b "I didn't want that. I wanted her to choose to be with me. But she chose to die instead... am I really that despicable?"
                            "You loved her.":
                                        p "You loved her, then?"
                                        b "Of course I loved her! That was the point of the whole thing! But she chose to die rather than be with me... am I really that despicable?"

                   p "You were a fool for discarding your strategy in favor of emotion. Much like this game. Do you wish to resign?"
                   b "Resign? But...oh, I see. I've lost, haven't I? Well done, Princess."
                   b "Yes, I resign. I've learned that much from my mistakes, at least."
                   b "But, Princess?"
                   p "Yes?"
                   b "Perhaps one day strategy and emotion can be aligned towards the same goal."