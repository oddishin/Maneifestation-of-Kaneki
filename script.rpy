
# -----------
# GAME START
# -----------

label start:

    pause 1.0

    news "Early this morning, authorities discovered several unidentified male bodies inside the Aqua Building, a commercial center located in Tokyo's 20th Ward."

    scene rize_walk
    with Dissolve(1.0)

    news "Investigators found what is believed to be ghoul saliva on the bodies of the deceased." 

    news "As a result, the incident has been labeled a ghoul crime." 

    scene kan_hide
    with dissolve

    kan "Aw c'mon, it's not that funny!" 

    hid "Man, you're hopeless! Ya can't take her to a bookstore on the first date!"

    kan "Why not? She might think it's an awesome idea!"

    hid "Look, don't do it. Trust me." 
    
    hid "She'll think you're lame."

    kan "Then I'll take her to Big Girl, for hamburgers."

    hid "Hahaha!"

    kan "I'm being serious, Hide! Quit laughing!"

    hid "I know! That makes it even funnier!" 
    
    hid "You can't take her to a place called 'Big Girl.'"

    kan "Since when are you the expert?" 

    scene kan_hide3
    with dissolve
    
    kan "Fine, then were would you take a date?"

    hid "That's easy! I'd pay attention to what the girl's into and then pick a place I think she'd enjoy."

    kan "Such as?"

    hid "Uh, y'know. Girly places."

    kan "You don't even have a clue, do you?"

    hid "If I did, I'd be out with a hot chick right now instead of sittin' here lookin' at your ugly mug!"

    kan "Yeah, you've got a good point."

    scene kan_hide2
    with dissolve

    # sfx: sip coffee

    hid "So? Who is she? Which one of these chicks is your special lady friend?"

    kan "H-huh?"

    hid "Is that her?!"

    scene touka
    with dissolve

    kan "No!" 
    
    kan "But she's pretty cute, too."

    hid "Excuse me, Miss?" 

    hid "Can I get a cappuccino?"
    
    scene kan_hide_tou
    with dissolve

    hid "You want one, Kaneki?"

    kan "No, I'm still working on mine."

    tou "So one cappuccino?"

    hid "Oh, and what is your name?"

    kan "H-Hide!"

    tou "I'm. . . . Touka Kirishima."

    tou "Lemme just cut to the chase. Are you seeing anyone?"

    kan "Cut it out, idiot!"

    scene kan_hide3
    with dissolve

    hid "Man, what a hottie."

    kan "If you get me kicked out of here I will never forgive you!"

    kan "This coffee shop is the only place I ever run into her."

    # sfx: door opens

    ". . . ."

    hid "Hm?"

    scene rize 
    with dissolve

    kan "That's her. That's the girl."

    hid "Pfftt."

    hid "You don't have a chance. You and her would be like 'Beauty and the Bonehead.'"

    kan "You mean 'the Beast?'"

    hid "Whatever. Now that I've seen you lovesick, I've got blackmail for days." 
    
    scene hide_leave
    with dissolve

    hid "I'm gonna jet." 

    kan "What? You're leaving?"

    hid "I'll see you later, Touka." 
    
    hid "Good luck, Kaneki! You're gonna need all you can get, buddy!"

    kan "Hmm. . . ."

    menu:

        "Pull out book":

            jump act2

label act2:

    scene kan_read1
    with dissolve

    # sfx: pages flipping

    kan ". . . ."

    kan ". . . ."

    scene kan_read2

    kan "Hm?"

    scene rize_read
    with dissolve

    kan "{i}Huh? She reading the same book?{/i}"

    rize "*smiles*"

    scene city_night
    with Dissolve(1.0)

    show hide_ at partialleft
    with dissolve

    hid "Man, you are one lucky bastard, you know that?"

    show kaneki_ at partialright
    with dissolve

    kan "No joke! Who would've thought she'd like the same author that I do?"

    hid "For real. What's the girl's name again? Sen Takasaki?"
    
    kan "Sen Takatsuki! And get this, we made plans to go to the bookstore together on Sunday."

    hid "Seriously? That sounds about as exciting as watching paint dry to me." 
    
    hid "But you kids have fun."

    kan "Thanks, man."

    hide hide_
    with moveoutleft

    pause(0.2)

    show restaurant
    hide kaneki_
    with slow_fade

    show kaneki_ at centerleft
    show rize_ at centerright

    rize "So tell me, Kaneki, out of all of Takatsuki's novels, which one is your favorite?"

    kan "Guess I'd have to go with her first book."

    rize "Well, that's understandable, it was her breakout hit." 
    
    rize "It's my favorite. Her writing just speaks to me."

    kan "Yeah, I feel the same way!" 
    
    kan "It's so good and to think she wrote it when she was just a teen!"

    kan "*cough* *cough*"

    show cough
    hide kaneki_
    with dissolve
    hide rize_
    with dissolve

    rize "Are you all right, Kaneki?"

    kan "U-uh, yeah... I am now!" 
    
    kan "I'm fine, so anyway..."

    scene date1
    with dissolve

    kan "How's your food? You didn't eat very much, did you?"

    rize ". . . ."

    kan "U-um. . . ."

    rize "Actually, I'm, uh. . . . I'm on a diet."

    rize ". . . ."

    scene restaurant
    with dissolve

    rize "I need to go powder my nose."

    # sfx: footsteps

    rize ". . . ."

    kan "{i}Wow, she's such a lady.{/i}"

    menu:

        "Conclude date":

            jump act3

label act3:

    scene end_date_bg
    with slow_fade

    show kaneki_ at centerleft
    with dissolve
    show rize_ at centerright
    with dissolve

    rize "Thank you, I had a great time today."

    kan "No, thank you! It's been fun." 

    rize ". . . ."

    kan "Uh. . . ."

    show end_date_cg
    hide kaneki_
    with dissolve
    hide rize_
    with dissolve

    rize "I hate to ask this of you, but I live in the area where all of the attacks have been happening."

    kan "You mean, with the ghouls?"

    rize ". . . ."

    rize "I don't want you to think I'm weak or anything, but I'm scared to walk home alone."

    rize "The very thought of it terrifies me."

    rize ". . . ."

    kan "I'll walk you home."

    rize "H-huh?"

    kan "I mean, what kind of date would I be if I didn't at least do that much?"

    rize ". . . ."

    scene street
    with dissolve

    rize "Have you always been into reading or is it more of a newfound passion?"

    kan "I grew up around books. My dad had a ton in the house."

    kan "He passed away when I was little. I barely even remember him." 
    
    kan "It may sound weird, but when I read his books I felt closer to him."

    kan "My mom had to work a lot to make ends meet, so I spent most of my time home alone reading."

    kan "Then, ever since my mom died. . . ."

    kan ". . . ."

    kan "Hide's the only other person I've talked to abou this."

    rize "Thanks for sharing it with me."

    scene alley1
    with dissolve

    rize ". . . ."

    kan "Hm?"

    rize "It's this way."

    kan "Oh, okay."

    menu:

        "Proceed down the alley":

            jump act4

label act4:

    scene alley2
    with slow_fade

    rize "Well, I'm right over here, so, goodnight."

    kan ". . . ."

    kan "Rize! Um. . . ."

    rize "Hm?"

    kan "I'd like to see you again."
    
    kan "I mean, only if you want to."

    rize ". . . ."

    rize "Kaneki."

    kan "Uh, yeah?"

    rize "The truth is, I've had my eye on you, too."

    rize "I'll admit, I love the way you look at me."

    kan "Does that mean you feel the same way?"

    scene realize1
    with dissolve

    rize "Yeah. I want you, just as much as you. . . ."

    scene realize2
    with dissolve

    rize ". . . ."

    scene realize3
    with dissolve

    rize ". . . . want me."

    # sfx: bite
    # sfx: train rattling

    scene bite
    with vpunch

    ". . . ."

    ". . . ."

    ". . . ."

    scene scared
    with vpunch

    rize "Ah! Tasty!"

    kan "*grunting, crying*"

    rize "You see, here's the thing." 
    
    rize "There's something I like even more than reading. Know  what that is?"

    rize "Ripping the organs out of someone who's too terrified to run away from me."

    rize "Oh, how I love the look on your face!"

    rize "So what do you say, Kaneki? Will you let me have my fun?"

    rize "Hahahahaha!"

    scene kan_run
    with vpunch

    kan "No way! No way!" 
    
    kan "No way! Hng-"

    kan "AHH!"

    rize "You can't run from me, silly!"

    # sfx: wall smashing

    scene evil_smile
    with dissolve

    rize "I'm coming for you, Kaneki!"

    scene evil_smile
    with vpunch

    # sfx: stabbing noise

    rize ". . . ."

    rize "Wow, I've really made a mess of you, haven't I?"
    
    scene evil_con

    rize "Huh?"

    rize "Uh-oh, it looks like you died on me." 

    rize "Aw, that's too bad."

    rize "I was hoping you'd last a little longer. You've got just the right amount of fat on you."

    # sfx: wire snap 

    scene evil_con
    with hpunch

    rize "And your flesh is so tender and tasty."

    # sfx: wire snap 

    scene evil_con
    with hpunch

    # sfx: building crash

    scene black
    
    pause(2.0)

    ". . . ."

    # sfx: siren blaring

    rize "How. . . . could. . . ."

    rize ". . . . this happen?"

    menu:

        "Fade out of consciousness":

            jump act5

label act5:

    scene black

    kan ". . . ."

    kan ". . . ."

    dr "His abdominal organs ruptured!"
    
    scene water 
    with slow_fade

    kan ". . . . where am I?"

    dr "We need to operate immediately!"

    kan "What is this place?"

    kan "I thought. . . ."

    scene kan_water
    with slow_dissolve    

    kan "I thought I was on a date with Rize. . . ."

    dr "Prepare for organ transplantation."

    nur "We need consent from the next of kin!"

    scene kan_rize_float
    with slow_dissolve

    kan ". . . . Transplantation. . . ." 
    
    kan ". . . . Next of kin. . . .?"

    kan "What the hell are they talking about?"

    nur "You can't, Dr. Kanou!"

    dr "I'll take full responsibility!" 
    
    dr "He needs her organs to survive!"

    scene kan_float
    with slow_dissolve 

    kan ". . . ."

    kan "It's so warm. . . ."

    kan "But why. . . .?"

    scene black
    with sslow_fade

    # sfx: heart monitor beeping

    ". . . ."

    ". . . ."

    scene eye_closed
    with sslow_dissolve

    kan ". . . ."

    kan ". . . ."

    scene eye_open
    with vpunch

    kan ". . . .!"

    scene kan_hosp
    with sslow_dissolve

    kan ". . . ."
    
    kan ". . . ."
    
    scene black
    with sslow_fade

    return