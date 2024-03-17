#Characters
define m = Character (_("Miyu"), color = "#FF9633")
define g = Character (_("Ghost"), color="#338FFF")

#Images Miyu
image sadMiyu = im.Scale("SadMiyu.png", 400, 700)
image relaxMiyu = im.Scale("RelaxMiyu.png", 400, 700)
image scaredMiyu = im.Scale("ScaredMiyu.png", 400, 700)
image madMiyu = im.Scale("madMiyu.png", 400, 700)
image unphazedMiyu = im.Scale("unphazedMiyu.png", 400, 700)
image neutralMiyu = im.Scale("neutralMiyu.png", 400, 700)
image worriedMiyu = im.Scale("worriedMiyu.png", 400, 700)

#Images Ghost
image fantome1 = im.Scale ("fantome.png", 400, 500)
image fantome2 = im.Flip("fantome2.png", horizontal=True)
image fantome2 = im.Scale ("fantome2.png", 400, 500)
image fantome3 = im.Scale ("fantome3.png", 400, 500)
image fantome4 = im.Scale ("fantome4.png", 400, 500)

#Images backgroung
image workshop = im.Scale ("workshop.png", 2500, 1200)
image house = im.Scale ("house.png", 2500, 1200)
image babaYaga = im.Scale ("babaYaga.jpg", 1950, 1300)
image tower = im.Scale ("tower.png", 2300, 1100)
image insideTower = im.Scale ("insideTower.png", 2500, 1200)
image experimentations1 = im.Scale ("experimentations1.png", 2500, 1200)
image experimentations2 = im.Scale ("experimentations2.png", 2500, 1200)
image experimentations3 = im.Scale ("experimentations3.png", 2500, 1200)
image dungeon = im.Scale ("dungeon.jpg", 2500, 1200)
image letter = im.Scale ("letter.png", 2200, 1100)
image map = im.Scale ("map.png", 2200, 1090)
image fight = im.Scale ("fight.png", 2500, 1200)

#Choices variables
default good_Choice = 0
default bad_Choice = 0

#Introduction of the scene
label start:

    scene dungeon
    with dissolve
    play music "audio/rain.wav"
    show unphazedMiyu
    with dissolve

    m "{i}{color=A29D9D} *Sigh* {/color}{/i}"
    m "{i}{color=A29D9D}Finally inside! I've never been a big fan of the rain.{/color}{/i}"

    play sound "audio/wetDog.wav"
    stop music fadeout 3
    with vpunch
    with hpunch
    with vpunch
    with hpunch

    m "{i}{color=A29D9D}It was freezing out there.{/color}{/i}"

    play music "audio/fireplace.wav"
    play sound ["<silence 2>", "audio/kid.wav"]

    hide unphazedMiyu
    show relaxMiyu

    m "{i}{color=A29D9D}Luckily it's toasty in here. I'll be able to warm up.{/color}{/i}"

    hide relaxMiyu
    show scaredMiyu

    m "{i}{color=A29D9D}What's that sound???{/color}{/i}"
    m "Who's there?"
    m "..."

    hide scaredMiyu
    show relaxMiyu

    m "{i}{color=A29D9D}Maybe that was just in my head.{/color}{/i}"

    play sound "audio/kid.wav"

    m "..."

    hide relaxMiyu
    play sound "audio/bang.wav"
    show scaredMiyu
    stop music
    play music "audio/suspens.mp3"

    m "{i}{color=A29D9D}Oh no, that's definitely real!{/color}{/i}"
    m "Show yourself!"
    m "I don't like this game...You're scaring me!"

    hide scaredMiyu
    scene black
    with vpunch
    scene white
    with hpunch
    scene dungeon
    show fantome3 at center with moveinleft

    g "BOO!"

    hide fantome3 with moveoutleft
    show fantome2 at right
    with dissolve

    g "{i}{color=A29D9D}I've alwas wanted to do that...I thought it'd be funny but it isn't fun without a reaction since no one can see me...I'll keep trying though, just in in case.{/color}{/i}"
    hide fantome2 at left with moveinleft
    show fantome3 at left
    show scaredMiyu
    with vpunch
    stop music fadeout 2
    play music "audio/theme.mp3" fadein 3

    m "AHHH!"
    g "Wait! How are you able to see me?"
    m "Don't hurt me, I'm just passing by. I don't want any trouble."
    g "Are you working with that witch?!"

    hide fantome3
    show fantome4 at left

    g "Get out of here!"
    m "No no, I'm not working with her. I'm trying to fight her!"

    hide fantome4
    show fantome3 at left

    g "Fight her?"

    hide scaredMiyu
    show sadMiyu
    m "Yes! Just this afternoon, she took my parents while I was out for a walk. When I came back, my house smelled like rotten eggs."
    m "I followed that scent into the forest and found Baba Yaga's weird chicken castle."

    hide sadMiyu
    show madMiyu

    m "I'm sure she's the one that kidnapped them!"
    m "Did you see that witch pass by?"
    g "I might have..."

    hide madMiyu
    show neutralMiyu

    g "How can I trust you?"

    menu:
        "You're wasting my time. It's whatever, I got to go. I got my parents to save.":
            $ bad_Choice +=1
            jump rudeChoice
        "Do you really think I wanted to be outside in this weather?":
            $ good_Choice +=1
            jump niceChoice

label rudeChoice:
    g "Good luck with that. This place is a maze."
    g "..."
    hide neutralMiyu with moveoutright
    g "..."
    g "Fine fine, come back. I believe you."
    show unphazedMiyu
    with moveinright
    m "Finally..."
    hide unphazedMiyu
    show neutralMiyu
    with dissolve
    jump continue1

label niceChoice:
    g "That's a good point."
    g "Alright, I believe you."
    g "I don't think anyone would like to be outside right now..."
    hide unphazedMiyu
    show neutralMiyu
    jump continue1


label continue1:
    g "By the way, you never explained how you're able to see me... or even who you are."
    m "First of all, my name is Miyu and like I said before, I am here to save my parents. That's all that matters. "
    m "And I can't see you."
    g "..."
    m "..."
    g "huh?"
    m "Nah, I was just kidding. I can see you."
    m "I've always been able to see ghosts, it's my greatest secret, no one alives knows."
    g "So you've talked to other ghosts before?"
    m "Yeah, but I try not to interact with them. I just like keeping to myself."
    g "You don't have that many friends, do you? Ahahah "

    hide relaxMiyu
    show unphazedMiyu

    m "Whatever smart guy…"

    hide unphazedMiyu
    show neutralMiyu

    g "So what do you want to know exactly?"

    menu:
        "I told you who I was, but how can I know you're not working with that witch...Maybe YOU are trying to kidnap me!":
            $ good_Choice += 1
            jump niceChoice2
        "I just want to know where to find that witch and get out of here.":
            $ bad_Choice += 1
            jump rudeChoice2

label niceChoice2:
    g "First of all, I don't think that's possible. As I said earlier, I still don't understand why you...why anyone could possibly see me since I'm dead."
    m "Hmm there still could be a chance."
    stop music fadeout 3
    g "Let me explain what happened to me then."
    g "After that, if you don't believe that I hate that witch more than you do, it's up to you."

    hide relaxMiyu
    hide ghost
    scene black
    with dissolve
    scene house

    play music "audio/piano.wav" fadein 1
    g "I died when I was twelve years old."
    g "This was five years ago."
    g "I was playing with some friends next to the forest. We were having fun playing hide and seek."
    g "I hid...but when I got found, it wasn't my friend who was there."

    stop music fadeout 2
    play music "audio/creepy.wav" fadein 2
    scene babaYaga
    with dissolve

    g "It was this creepy old hunchback hag. She had long frizzy white hair and reeked of perfume that tried to hide her decaying odor."
    g "I was scared. She looked like death."
    g "I tried to scream, but I guess I was too far, no one could hear me."

    scene tower
    with dissolve

    g "After that, I only remember seeing specks of a huge tower...and then nothing unit I woke up inside...I guess."

    scene insideTower
    with dissolve

    g "I remember always being dizzy...half asleep and half awake...not really knowing what was happening."

    scene experimentations2
    with dissolve

    g "I think I heard her babble about making some kind of potion that could either giver her eternal life or reverse her aging or both, I'm not sure."
    g "In either case she needs it, she looks horrible Ahahah. "
    g "Sorry, the only thing I can do now is laugh about it."
    g "What happened after, how did you die...?"

    scene experimentations1
    with dissolve

    g "Yes, so I guess I became a test subject."
    g "She started doing experiments on me. It started with only cutting my hair, but then she started to tear out my nails one by one."
    g "At that time, it felt more like torture than anything else."
    g "She took parts of my humanity one by one until I was nothing."
    g "She took my eyes..."
    g "My teeth..."
    g "My liver..."
    g "My pancreas..."
    g "My lungs..."
    g "My kidney..."
    g "And finally my hearth."
    g "She made sure I was conscious  and even recorded my screams, which she said {i}emitted a magical aura.{/i}"
    g "After that, I woke up...but I wasn't alive."
    g "I saw her dehydrate what was left of my body and then crush it into a fine powder."

    scene experimentations3
    with dissolve

    g "I saw her bring one..."
    g "Two..."
    g "Three..."
    g "Four more kids in here."
    g "I saw her do to them the same thing she did to me."
    g "I didn't want to see more. I felt powerless so I came down here."
    stop music fadeout 3
    g "There you go, that's my story."

    play music "audio/sad.mp3" fadein 3
    scene dungeon
    with dissolve
    show sadMiyu at left
    with dissolve
    show fantome2
    with dissolve

    m "I remember when this happened. I was your age at the time and after hearing about the incident, my parents told me not to go roam outside anymore."
    m "Words circulated fast though and she was soon exiled by Bearbadoo."
    m "Not fast enough though..."
    m "I don't know what happened during the five years that followed her exile, but she came back."
    m "I believe she targeted children at first because they embedded more magical power. What doesn't make sense is that she kidnapped my parents ..."
    m "I have to find them, and I need your help to do so."
    m "She must be up to something big, and we got to stop her."
    stop music fadeout 3
    hide sadMiyu
    show neutralMiyu at left

    jump continue2

label rudeChoice2:
    hide fantome3
    show neutralMiyu at left with dissolve
    show fantome2 with dissolve
    g "She's hiding up here."
    g "She's probably doing some experiments on test subjects she decided looked fit for it...She likes to do that."

    stop music fadeout 2
    m "I have to stop that and find my parents!"
    jump continue2

label continue2:
    play music "audio/gloomy.wav" fadein 3
    g "If that's what you really want to do, you'll need to know how to find your way in this maze."
    g "Wait a second, I'll draw you a map of the area"
    g "If you find others like me, they might be able to give more details on the map."
    hide fantome2
    play sound "audio/scribble.wav"
    g "{i}{color=A29D9D} *Scribble* {/color}{/i}"

    hide neutralMiyu
    scene map
    with dissolve
    hide neutralMiyu
    g "There you go, it should help!"
    m "Thank you so much!"

    scene dungeon
    show relaxMiyu
    show fantome3 at left
    with dissolve

    g "Before you go, you need to know that there's a lot more that await you over there than maze like corridors."

    hide relaxMiyu
    show worriedMiyu

    g "You should be careful of creatures."
    g "I told you that the witch made many experimentations."

    hide worriedMiyu
    show scaredMiyu

    g "Some of them are right on the other side of this door. There's wolf like creatures, vampires, bats, and jack o'lanterns."
    g "Even if they may seem friendly at the beginning, you should never trust them."
    g "They're only obeying to the witch. She controls their brain."
    g "They're a lost cause. They're empty shells."
    g "If you see one, you should learn how to defend yourself."

    hide scaredMiyu
    show worriedMiyu

    g "Do you want me to show you?"

    menu:
        "Yes please, I have no clue how to fight them.":
            $ good_Choice += 1
            jump niceChoice3
        "No, it's fine. I should be able to figure it out.":
            $ bad_Choice += 1
            jump rudeChoice3

label niceChoice3:
    g "Alright!"
    g "First of all, I am just a kid so don't take everything I say too seriously, you can still experiment on your own."
    g "I heard that combo attacks work great on those creatures."
    g "Since you're a dog, I'm pretty sure you could use those claws to do some serious damage to them."
    m "I've never fought anyone though...I don't know where to start."
    g "Alright just try doing what I say."
    stop music fadeout 2
    jump fightPractice

label rudeChoice3:
    g "Alright!"

label continue3:
    scene dungeon with dissolve
    show fantome2 at right with moveinright
    show worriedMiyu
    with dissolve
    play music "audio/nostalgic.wav"
    g "Are you ready to go now?"
    m "I can only hope I am."
    m "Thank you...?"
    m "I don't even know your name."
    m "I'm so sorry, I was so focused on saving my parents that I didn't even ask."
    m "So what's your name?"
    g "It's all right, I can understand."
    g "I'm Maximus... well I prefer Max."
    m "Thank you Max."

    #Good ending
    if good_Choice >= 2:
        m "I'm really happy to have met you. I hope we'll be able to see each other after this."
        g "Yes, I do too..."
        hide worriedMiyu with moveoutright
        g "..."
        g "..."
        g "Wait!"
        show relaxMiyu with dissolve
        hide fantome2 with dissolve
        m "Yes?"
        hide relaxMiyu with dissolve
        show fantome2 at center

        g "I know you're only here to save your parents, but I was wondering if you could do me favor?"
        g "I know we just met, but you seem like someone I can trust."
        g "I mean you took the time to listen to me even though you were in a rush. That matters to me. You're the first person I talk to in five years."
        g "I needed that, thank you."
        g "Anyway, what I wanted to say is that I was wondering if you would mind relaying a message to my parents."
        g "I know it's a lot to ask and it would of course be after you found your parents."

        menu:
            m "Hmm..."
            "Of course, I can do that!":
                jump choix1
            "I'm sorry, I already have a lot on my plate...":
                jump choix2

    #Bad ending
    else:
        g "Be careful over there! And good luck... I think you'll need that too."
        m "For sure I will."
        g "Goodbye, it was nice meeting you."
        jump end

label choix1:
    g "Thank you so much"
    g "I'll write them a letter; it'll be easier for you to deliver."
    play sound "audio/scribble.wav"
    g "{i}{color=A29D9D} *Scribble* {/color}{/i}"

    scene letter
    hide relaxMiyu
    hide fantome2

    g "There you go."

    scene dungeon
    show sadMiyu
    show fantome2 at right


    m "Are you sure that's what you want to tell them..."
    g "Yes, I don't want them to worry. I would prefer letting them think I am well and happy. "
    g "I don't want them to be sad..."
    m "I can understand that. That's noble of you."

    hide sadMiyu
    show worriedMiyu

    m "Where should I deliver this letter?"
    g "We lived in the city. If my parents are still there, they should be at 3672 Waffle Street."
    g "If they moved, can you try asking around?"
    g "Their name are Finny and Georgie Huffpatoof."

    hide worriedMiyu
    show sadMiyu

    m "Alright Max Huffpatoof! I'll do that for you."
    g "Thank you so much!"
    g "Good luck and be careful!"
    m "I will!"
    jump end


label choix2:
    g "It's alright, I can understand."
    g "Focus on finding your parents, they need your help."
    m "I will."
    jump end


label end:
    stop music fadeout 2
    scene black
    with dissolve
    "Credits:
\nScenario by Anabel Prévost
\nSound editing by Angelito III Posadas"
with dissolve
"Music/ sounds:

\nBlue Sizzle music by Kevin MacLeod
\nCreepy Lullaby music by InspectorJ
\nDistorted Beep Incorrect by edwardszakal"
with dissolve
"Dramatic sound by AUDACITIER
\nDreamy cinematic moments music by Setuniman
\nElectro win sound by Unlistenable
\nFairy Tale Intro music by GregorQuendel"
with dissolve
"Fireplace sound by Shurooq Siddiqui
\nGloomy music by Setuniman
\nGood! sound by syseQ
\nHorror Violin sound effect by Matteo Garofalo"
with dissolve
"Rain and thunder Sound by Relaxing Music Channel
\nSad heaven piano music by PSOVOD
\nScheming Weasel (faster version) music by Kevin MacLeod
\nWet shaking dog sound by crooner"
with dissolve
"Images:
\nBaba Yaga illustration by KateMaxpaint @ deviantArt
\nDungeon illustration by Rukkits @ deviantArt
\nGhosts illustrations by pikisuperstar"
with dissolve
"Miyu illustration by Anabel Prévost
\nMiyu's faces illustrations by mamewmy
\nPaper effect by boggus
\nWitches and Wizards Backgrounds by Lornn"

return
##########QTE##########
label qte_setup(time_start, time_max, interval, typebutton, x_align, y_align):

    # récupération des variables envoyés à la fondction
    $ time_start = time_start
    $ typebutton = typebutton
    $ time_max = time_max       # temps max pour faire l'action
    $ interval = interval

    $ trigger_key = []
    $ trigger_key_display = ""

    $ x_align = renpy.random.randint(1, 9) * 0.1 # emplacement aléatoire sur l'axe Y
    $ y_align = renpy.random.randint(1, 9) * 0.1 # emplacement aléatoire sur l'axe Y

    $ arr_keys         = ["K_LEFT", "K_RIGHT", "K_UP", "K_DOWN"]     #touche à presser.
    $ arr_keys_display = ["Left", "Right", "Up", "Down"]    #commande affichée à l'écran.
    $ trigger_key = renpy.random.choice(arr_keys) # choix aléatoire de valeur parmi le tableau.

    $ trigger_key_display = arr_keys_display[arr_keys.index(trigger_key)] # correspondance avec l'affichage.

    if typebutton == "alttab":
        call screen qte_button_alttab() # soit il faut cliquer sur une icone.
    elif typebutton == "keypress":
        call screen qte_button_keypress(trigger_key_display) # soit on attend une touche.

    # suivant le retour qu'on à eut :
    if _return == 1:
        if typebutton == "keypress":
            $ cont += 1
            play sound "audio/good.wav"
    else:
        play sound "/audio/buzz.mp3" # mauvaise réponse mp3

    return

############################################################## choix de menu en temps limité

############################################################## utilisation d'un QTE

label fightPractice:

    hide screen countdown2

    $ cont = 0 #continue variable
    $ totalContMoves = 0
    $ temp = 0

    # Préparation du QTE :

    scene fight with dissolve
    g "Do exactly what I tell you to do."
    g "This is how you'll be able to defeat the creatures!"
    play music "audio/fight.mp3"

    scene fight with vpunch

    # qte_setup(time_start, time_max, interval, typebutton, x_align, y_align)
    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move1a # le from doit être différent pour chaque appel.
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1 # total des réussites.

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move1b
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move1c
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    if temp < 3:
        g "Let's keep going! You'll get it the next time!"

    $ temp = 0

    scene fight with dissolve
    "Again!"

    scene fight with dissolve

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move2a
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move2b
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move2c
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    if temp < 3:
        g "It's alright. Practice makes perfect!"

    $ temp = 0

    scene fight with dissolve
    g "One last time!"

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move3a
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move3b
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    call qte_setup(1, 1, 0.5, "keypress", renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_move3c
    if cont == 1:
        $ cont = 0
        $ temp += 1
        $ totalContMoves += 1

    scene fight with dissolve
    stop music fadeout 2

    if totalContMoves < 7:
        scene fight with fade
        play sound "/audio/dramatic.mp3"
        g "It's alright, you got # [totalContMoves] on 9 good hits! You'll soon get used to it!"


    else:
        play sound "audio/win.wav"
        scene dungeon with fade
        g "That's really good!"
        g "I don't think I showed you anything you didn't already know."
    jump continue3
