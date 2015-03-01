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
            