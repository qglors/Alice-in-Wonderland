#set window dimensions
WIDTH = 1000
HEIGHT = 650

#import module to randomize beetle movements
import random

#initialize global variables

#add actors

title = Actor("title")
#coordinates
title.x = 500
title.y = 220

menu_start = Actor("start")
#coordinates
menu_start.x = 500
menu_start.y = 428

menu_quit = Actor("quit")
#coordinates
menu_quit.x = 500
menu_quit.y = 538

fade = Actor("fade1")

buttons = Actor("button1")
buttons.x = 867
buttons.y = 613

bubble = Actor("bubble")
bubble.x = 500
bubble.y = 567

alice = Actor("alicefront")
alice.x = 485
alice.y = 415

hole = Actor("hole")
hole.x = 164
hole.y = 574

backhole = Actor("backhole")
backhole.x = 160
backhole.y = 485

#visual instructions (at the top right corner)
keyarrowright = Actor("keyarrowright")
keyarrowright.x = 950
keyarrowright.y = 42

keyarrowleft = Actor("keyarrowleft")
keyarrowleft.x = 838
keyarrowleft.y = 42

arrow_to_hole = Actor("arrow_to_hole")
arrow_to_hole.x = 485
arrow_to_hole.y = 241

small_door = Actor("small_door")
small_door.x = 522
small_door.y = 385

speaker = Actor("minidoor")
speaker.x = 62
speaker.y = 484

diagram = Actor("diagram1")
diagram.x = 466
diagram.y = 152

dice = Actor("dice1")
dice.x = 759
dice.y = 153

table = Actor("table")
table.x = 857
table.y = 440

potionred = Actor("potion_red")
potionred.x = 850
potionred.y = 399

potionblue = Actor("potion_blue")
potionblue.x = 834
potionblue.y = 399

bigpotions = Actor("bigpotions")
bigpotions.x = 501
bigpotions.y = 325

left_buttons = Actor("blankleft")
left_buttons.x = 286
left_buttons.y = 56

right_buttons = Actor("blankright")
right_buttons.x = 719
right_buttons.y = 56

drink = Actor("drink")
drink.x = 500
drink.y = 603

key = Actor("key")
key.x = 878
key.y = 408

waterworks = Actor("waterworks")
waterworks.x = 500
waterworks.y = 1351

madhatter = Actor("madhatter")
madhatter.x = 861
madhatter.y = 416

basket = Actor("basket")
basket.x = 504
basket.y = 402

red_card = Actor("red_card")
red_card.x = 463
red_card.y = 399

black_card = Actor("black_card")
black_card.x = 298
black_card.y = 398

qofh = Actor("qofh")
qofh.x = 248
qofh.y = 403

end = Actor("end")
end.x = 500
end.y = 325

#background actor
bg = Actor("sky1")
bg.x = 1200
bg.y = 700

#starters
skyright = "NO"
skyup = "NO"
start_go = "NO"
fade1done = "NO"
draw_text = "NO"
forest_scene = "NO"
darkforest_scene = "YES"
alice_moving = "NO"
fall = "NO"
fallen = "NO"
hall_go = "NO"
explore_hall = "NO"
alice_movable = "YES"
end_hallway = "NO"
wall_move = "NO"
keep_going = "NO"
small_door_work = "NO"
rolling = "NO"
potion_go = "NO"
shrink = "NO"
realshrink = "NO"
waterfill = "NO"
teaparty = "NO"
castle = "NO"

#timers
fade_timer = 1
fade_timer2 = 1
fade_images = 1
bgtimer = 0
text_number = 0
buffer = 0
alice_move_timer = 0
buffer2 = 0
buffer3 = 0
buffer4 = 0
buffer5 = 0
buffer6 = 0
buffer7 = 0
dice_number = 0
dice_list = [0]*30
dicetimer = 0
dicelistnumber = 0
experiment_timer = 0

def draw():
    global fade1done, draw_text, realshrink, teaparty, castle, text_number, buffer, buffer2, fall, buffer7, fallen, buffer3, buffer4, explore_hall, end_hallway, buffer5, small_door_work, buffer6, rolling, alice_movable, waterfill
    bg.draw()
    title.draw()
    menu_start.draw()
    menu_quit.draw()
    fade.draw()
    if fade1done == "YES":
        if text_number <= 1 or text_number == 3 or text_number == 4 or text_number == 5:
            screen.clear()
            bg.image = "forestscene"
            bg.x = 500
            bg.y = 325
            buffer += 1
            if buffer >= 10:
                draw_text = "YES"
            bg.draw()

        if text_number == 2:
            screen.clear()
            bg.image = "dark_forest"
            bg.draw()

        if draw_text == "YES":
            dialogue_exchanges()
            if text_number == 6:
                bg.image = "forestscenereg"
                draw_text = "NO"

        if draw_text == "NO" and text_number == 6 and fallen == "NO":
            screen.clear()
            bg.draw()
            alice.draw()
            draw_keys()
            if alice_moving == "NO" and shrink == "NO" and text_number != 75:
                alice.image = "alicefront"
            buffer2 += 1
            if buffer2 >= 100:
                arrow_to_hole.draw()
            if fall == "YES" and fallen == "NO":
                screen.clear()
                bg.draw()
                draw_keys()
                backhole.draw()
                alice.draw()
                hole.draw()
                fade.draw()

        if fallen == "YES":
            if explore_hall == "NO":
                screen.clear()
                bg.draw()
                draw_keys()
                alice.draw()
                buffer3 += 1
                if buffer3 >= 10:
                    dialogue_exchanges()

            if explore_hall == "YES":
                screen.clear()
                bg.draw()
                draw_keys()
                alice.draw()
                buffer4 += 1
                if buffer4 >= 200:
                    arrow_to_hole.image = "arrow_to_hole2"
                    arrow_to_hole.draw()
                if alice_moving == "NO" and shrink == "NO" and text_number != 75:
                    alice.image = "alicefront"
            if end_hallway == "YES":
                screen.clear()
                bg.draw()
                draw_keys()
                alice.draw()
                buffer5 += 1
                if buffer5 >= 10:
                    dialogue_exchanges()

            if small_door_work == "YES":
                dialogue_exchanges()
                if text_number > 8:
                    screen.clear()
                    speaker.draw()
                    bg.draw()
                    draw_keys()
                    alice.draw()
                    buffer6 += 1
                    if buffer6 >= 10:
                        small_door.draw()
                        speaker.draw()
                        dialogue_exchanges()
                    if text_number == 13 or text_number == 17:
                        diagram.draw()
                    if text_number >= 22 and text_number < 25:
                        diagram.draw()
                    if text_number == 25 or text_number == 26:
                        dice.draw()
                    if text_number >=28:
                        table.draw()
                        key.draw()
                        potionred.draw()
                        potionblue.draw()

                    if alice_movable == "YES":
                        screen.clear()
                        bg.draw()
                        small_door.draw()
                        draw_keys()
                        alice.draw()
                        if alice_moving == "NO" and shrink == "NO" and text_number != 75:
                            alice.image = "alicefront"
                        table.draw()
                        key.draw()
                        potionred.draw()
                        potionblue.draw()
                        if text_number >= 29 and shrink == "NO":
                            if alice.x >= 850 and text_number != 75:
                                alice_movable = "NO"
                                alice.image = "alicefront"
                                dialogue_exchanges()
                    if text_number == 32:
                        diagram.draw()
                    if text_number == 35:
                        screen.clear()
                        bg.draw()
                        small_door.draw()
                        draw_keys()
                        alice.draw()
                        if shrink == "NO" and text_number != 75:
                            alice.image = "alicefront"
                        table.draw()
                        key.draw()
                        fade.image = "fade3"
                        fade.draw()
                        bigpotions.draw()
                        drink.draw()
                        left_buttons.draw()
                        right_buttons.draw()

                    if shrink == "YES" and text_number == 35:
                        buffer7 += 0.1
                        if buffer7 > 12:
                            realshrink = "YES"
                            text_number += 1
                            screen.clear()
                            bg.draw()
                            small_door.draw()
                            draw_keys()
                            alice.draw()
                            if alice_moving == "NO" and text_number != 75:
                                alice.image = "shrunkalicefront"
                            table.draw()
                            key.draw()
                            dialogue_exchanges()
                    if text_number >= 39 and waterfill == "YES":
                        waterworks.draw()
                        if waterworks.y > 650:
                            waterworks.y -= 10
                        if waterworks.y < 650 and text_number >= 41 and castle == "NO":
                            teaparty = "YES"
                if teaparty == "YES":
                    screen.clear()
                    bg.draw()
                    alice.draw()
                    madhatter.draw()
                    speaker.draw()
                    dialogue_exchanges()
                    if text_number >= 53:
                        basket.draw()
                    if text_number == 63 or text_number == 64:
                        diagram.image = "diagram7"
                        diagram.draw()
                if castle == "YES":
                    screen.clear()
                    bg.draw()
                    red_card.draw()
                    black_card.draw()
                    alice.draw()
                    speaker.draw()
                    dialogue_exchanges()
                    if text_number == 82:
                        diagram.image = "diagram9"
                        diagram.x = 805
                        diagram.y = 172
                        diagram.draw()
                    if text_number >= 87:
                        screen.clear()
                        bg.draw()
                        alice.draw()
                        qofh.draw()
                        dialogue_exchanges()
                    if text_number == 88:
                        diagram.image = "diagram8"
                        diagram.x = 55
                        diagram.y = 215
                        diagram.draw()
                    if text_number == 89:
                        diagram.image = "diagram10"
                        diagram.x = 500
                        diagram.y = 276
                        diagram.draw()

                        if alice.x > 1200:
                            fade.image = "fade19"
                            fade.draw()
                            end.draw()




def update():
    global text_number, fallen, fall, hall_go, rolling


    if fade1done == "NO":
        skymove()
    background_timer()
    start()
    alice_move()
    if text_number == 6 and fallen == "NO":
        fall_in_hole()
    if fall == "YES":
        start_hall()
    button_coordinates()
    dice_roll()
    potion_experiment()
    shrinkcmd()
    teascene()
    castlescene()
    print(text_number)

def skymove():
    global skyright, skyup, fade1done
    if fade1done == "NO":
        if bg.x == 1200:
            skyright = "YES"

        if bg.y == 700:
            skyup = "YES"

        if bg.x == -450:
            skyright = "NO"

        if bg.y == -300:
            skyup = "NO"


        if skyright == "YES":
            bg.x -= 1

        if skyright == "NO":
            bg.x += 1

        if skyup == "YES":
            bg.y -= 1

        if skyup == "NO":
            bg.y += 1



def on_mouse_move(pos, buttons):
    #get global variables

    #add arrows for when player hovers over the menu options
    if menu_start.collidepoint(pos):
        menu_start.image = "start_hovered"
        #coordinates
        menu_start.x = 449
        menu_start.y = 428
    else:
        menu_start.image = "start"
        #coordinates
        menu_start.x = 500
        menu_start.y = 428

    #add arrows for when player hovers over the menu options
    if menu_quit.collidepoint(pos):
        menu_quit.image = "quit_hovered"
        #coordinates
        menu_quit.x = 431
        menu_quit.y = 538
    else:
        menu_quit.image = "quit"
        #coordinates
        menu_quit.x = 500
        menu_quit.y = 538

def on_mouse_down(pos, button):
    #get global variables
    global start_go, text_number, castle, forest_scene, draw_text, waterfill, fallen, explore_hall, hall_go, alice_movable, end_hallway, wall_move, keep_going, small_door_work, rolling, potion_go, teaparty

    #make menu options work
    if bg.image == "sky1" or bg.image == "sky2":
        #if player clicks quit, program quits
        if menu_quit.collidepoint(pos):
            #quit
            quit()

        #if player clicks start, the game begins
        if menu_start.collidepoint(pos):
            #alice sleepy scene
            start_go = "YES"

    if bg.image == "forestscene" or bg.image == "dark_forest":
        if buttons.collidepoint(pos):
            text_number += 1
            if text_number == 2:
                bg.image = "dark_forest"
    if text_number == 6:
        bg.image = "forestscenereg"
    if fallen == "YES":
        alice_movable = "NO"
        if text_number == 6 or text_number == 7:
            if buttons.collidepoint(pos):
                text_number += 1
        if text_number >= 8:
            wall_move = "YES"
            alice_movable = "NO"
            hall_go = "NO"
            explore_hall = "YES"

    if small_door_work == "YES":

        if text_number < 25:
            if buttons.collidepoint(pos):
                text_number += 1
                if text_number >= 9 and text_number!= 13 and text_number != 22:
                    buttons.image = 'button' + (str(text_number))
        if text_number == 25:
            if dice.collidepoint(pos):
                rolling = "YES"
        if text_number > 25 and text_number < 34 and text_number != 29:
            if buttons.collidepoint(pos):
                text_number += 1
                buttons.image = 'button' + (str(text_number))
        if text_number == 29:
            alice_movable = "YES"
            explore_hall = "NO"
        if alice.x >= 850 and text_number == 29:
            if buttons.collidepoint(pos):
                text_number += 1
                buttons.image = 'button' + (str(text_number))

        if text_number >= 30:
            alice_movable = "NO"
        if text_number == 34:
            if buttons.collidepoint(pos):
                text_number += 1
    if text_number == 35:
        if drink.collidepoint(pos):
            potion_go = "YES"
    if text_number >= 36 and text_number != 89:
        if buttons.collidepoint(pos):
            text_number += 1
            button.image = 'button' + (str(text_number))
    if text_number == 39:
        waterfill = "YES"
    if text_number >= 66:
        castle = "YES"
        teaparty = "NO"
    if text_number == 89:
        text_number = 89
    if text_number == 89:
        text_number = 89
        while alice.x < 725:
            alice.x += 5
        while alice.x >= 725 and alice.y < 400:
            alice.y += 5

def background_timer():
    global bgtimer

    if fade1done == "NO":

        bgtimer += 0.3

        if bgtimer <= 10:
            bg.image = "sky1"

        else:
            bg.image = "sky2"

        if bgtimer >= 20:
            bgtimer = 0

def start():
    #get global variables
    global fade_timer, start_go, fade1done, draw_text, buffer, forest_scene

    list_counter = 1
    fade_list = [1]*19
    number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    numbers = 0


    #rename items in the image lists (to use as the image name file)
    """while list_counter < 19:
        #rename each item in list to the names of my image files
        fadelistimage = 'fade' + str(number_list[numbers])
        #rename each item in list to the names of my image files
        #add one
        numbers += 1
        list_counter += 1"""

           #when player clicks page, page flips
    if start_go == "YES":
        for x in range(19):
            #rename each item in list to the names of my image files
            fadelistimage = 'fade' + str(number_list[numbers])
            #rename each item in list to the names of my image files
            #add one
            numbers += 1
            #timer to slow the flipping down
            fade_timer += 0.018
            #when timer goes up 5 times, index can rise once (slowing the flipping down)
            if fade_timer > numbers:
                fade.image = fadelistimage
                list_counter += 1

        if list_counter > 19:
            fade.image = "fade1"
            fade1done = "YES"

def start_hall():
    #get global variables
    global hall_go, draw_text, buffer, forest_scene, fallen, fade_timer2, alice_movable

    list_counter = 1
    fade_list = [1]*19
    number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    numbers = 0

           #when player clicks page, page flips
    if hall_go == "YES":
        for x in range(19):
            #rename each item in list to the names of my image files
            fadelistimage = 'fade' + str(number_list[numbers])
            #rename each item in list to the names of my image files
            #add one
            numbers += 1
            #timer to slow the flipping down
            fade_timer2 += 0.010
            #when timer goes up 5 times, index can rise once (slowing the flipping down)
            if fade_timer2 > numbers:
                fade.image = fadelistimage
                list_counter += 1
            print ()

        if list_counter > 19:
            bg.image = "hallway"
            bg.x = 1969
            bg.y = 428
            alice.x = 276
            alice.y = 390
            fallen = "YES"
            alice_movable = "NO"

def roleplay(text_number):
    #all of the dialogue blurbs in the entire game
    responses = ["Ahh...","What a beautiful day!", "x rustle rustle x", "???", "What was that?",
    "I'll go check it out!", "Where am I?", "Doors?", "Six doors?", "Yup!", "I live here! You're in Wonderland!",
    "One of these doors will lead you back home!", "Oh, I don't know. Probably nothing good.","But I only have a 1 in 6 chance of getting it right!",
    "Oh, no, no, no! You can pick two doors! You get a safety net!",
    "Whaaat? Being able to pick two doors increases the probability of \nchoosing the right one!",
    "Your second pick is a dependant event! You've got a \n1 in 6 chance of getting it right on your first try, and if it's \nwrong, you have a 1 in 5 chance of...", "getting it right the second time! Using the additive principal and conditional \nprobability, we know that brings the probability of picking \nthe right door to 1 in 3! ",
    "Or...", "I can roll a die!", "If it lands on a prime or odd number, I'll let you go through me!", "Yeah, why not?", "The chances of winning are so much higher. The primes on a dice are 2, 3, and 5. \nHalf of the numbers. The odds on a dice are 1, 3,and 5. Also half.",
    "But the probabilities of rolling an odd or a prime are non-mutually exclusive events \nbecause there are overlapping numbers. There are two overlapping numbers.",
    "So according to the additive principal for non-mutually exclusive events, the \nprobability of being able to leave is 2 in 3, which is a lot higher than choosing \ntwo doors, which was 1 in 3.",
    "Gee, then I guess it's your lucky day!", "Golly! You won! Congrats!", "Yay! Wait, how do I get through? You're way too small. \nAnd... wait, you're locked.", "Lucky for you, right there on that table, there's a key and shrinking potions!",
    "There are two. How do I know which one's which?", "Actually, believe it or not, it's both.", "...No. There's a 50 percent chance each one will work. In order to shrink, \nthey both have to work.",
    "Well, the chance of one of them working is 1 in 2. And since they're mutually \nexclusive and independant, according to the muliplicative rule, that's 1 in 2 \nmultiplied by 1 in 2, which is a 1 in 4 chance they both work.",
    "The theoretical probability says that if you try the experiment four times, \nyou'll succeed once. You can go ahead and find the experimental probability: the \nnumber of occurences over the number of tries!",
    "But you can go ahead and find the experimental probability!", "Woah! Nice!", "Wait, I forgot the key...", "Aw, well that's too bad.", "Woah there, don't start crying now...",
    "AHHH!!!! I WANT TO GO HOME!", "boohoohoohoohooohooohoo", "Phew! Luckily the pressure of the tears broke through the doors! \nThat talking door was strange...", "Now... how do I get home?", "Hey, you there!",
    "Would you like to join my friends and I for a tea party?", "No thanks...", "Why not?!", "I gotta go home...", "It's just for a little while!","Maybe if it's just for a little bit... What are you having?",
    "What would you like? We have everything anyone could possibly want on \na sandwich! You can pair it with all our different kinds of tea!", "Oh? What do you have?",
    "What do we have? EVERYTHING! Here, take a look.", "Wow, you really do have everything in here! I don't even know what to try!",
    "Go ahead, try it all! Try every combination if you must!", "How many combinations are there?", "Well let's just see.", "For buns, we have seseame, white, and whole wheat. For veggies, we have tomatos, \nlettuce, and cucumbers.",
    "For meat, we have bacon, steak, and chicken. We have four sauces: ketchup, \nranch, mustard, and barbecue.",
    "And of course, for tea, we have green tea, ginseng, chamomile, and jasmine.", "Now, how many combinations is that?",
    "Well, the fundamental counting principal says that when we have multiple \nevents, we can find the number of ways they can occur togetherby multiplying \nthe number of ways each event can occur on its own.",
    "So, one event here would be the veggies. There are three ways you can have \na veggie in your sandwich. Now we can multiply all of them!",
    "Three bun options multiplied by three veggie options multiplied by three meat \noptions multiplied by four sauce options multiplied by 4 tea options?", "That's 432 combinations.", "Woah. I don't think I can stomach that much food and tea. I think I'll just put \neverything into one sandwich.", "Wow, that was delicious.",
    "Woah, a castle! I bet someone here could help me get home.", "Hi, my name is Alice, and I was wondering-", "WHO IS THIS? THIS TRESSPASSER?", "Who's that?", "The Queen of Hearts.", "Ah...", "Um... Your Majesty, I swear I wasn't tresspassing. I was just hoping you \ncould help me out-", "TRESSPASSER! CAPTURE HER!", "Oh, no.",
    "GUARDS! FIVE OF YOU! AFTER HER!", "Which five, Your Majesty?", "Cards from ace to ten. There are 40 of you. There are 40C5 combinations I can use. \nThat's 658008 ways you useless cards can group yourselves and nobody's \nmoving? LEAVE NOW AND THERE'S A 20 PERCENT CHANCE I WON'T FIRE YOU!!!",
    "Yes, Your Majesty.", "Agh! Where did she run off to? We're going to get fired!", "We might not. She said there's a 20 percent chance we won't.", "That means there's an 80 percent chance we will. Complementary events add \nup to one.", "We'd better catch her then.", "HOW HAVE YOU NOT FOUND HER YET?!", "We're deeply sorry, Your Majesty.",
    "SHE'S RIGHT THERE! I'll get her myself. COME HERE, YOU TRESSPASSER!", "Oh no, oh no... She's in the Labyrinth... How do I get out of here?", "If I use pascal's triangle, I can figure out a few ways to get out of here \nwithout bumping into her.", "There are 9 ways to get out of here!"]


    #return the dialogue to the draw function
    return responses[text_number]

#function to keep the story going when it's time for a dialogue exchange
#for convenience
def dialogue_exchanges():
    global text_number
    #draw text box
    bubble.draw()
    button_coordinates()
    if text_number != 25:
        buttons.draw()
    #add text (from a list of texts)
    screen.draw.text(roleplay(text_number), (46, 525), color="black", fontname="dk butterfly ball", fontsize=25)
    #add interactive(clickable) buttons

def alice_move():
    #get global variables
    global text_number, alice_move_timer, alice_moving, explore_hall, alice_movable, text_number, shrink, end_hallway, wall_move, keep_going, small_door_work
    if shrink == "NO":
        if explore_hall == "NO":
            if alice_movable == "YES":
                #when first dialogue exchange has finished
                if text_number >= 6:
                    #mouse moves left when the player clicks the left arrow on the keyboard
                    if keyboard.left:
                        alice_moving = "YES"
                        #same key on the visual instructions presses down
                        keyarrowleft.image = "keyarrowleft_down"
                        #coordinates of visual instructions
                        keyarrowleft.x = 838
                        keyarrowleft.y = 49
                        #mouse moves left
                        alice.x -= 5
                        #timer for movement animation
                        alice_move_timer += 0.5
                        #reset when timer gets too high
                        if alice_move_timer > 4:
                            alice_move_timer = 1
                        #flip between two mouse images
                        if alice_move_timer >= 1 and alice_move_timer <= 2:
                            alice.image = "aliceleftrun2"
                        if alice_move_timer >= 3 and alice_move_timer <= 4:
                            alice.image = "aliceleftrun1"

                    #mouse moves right when the player clicks the right arrow on the keyboard
                    elif keyboard.right:
                        alice_moving = "YES"
                        alice_moving = "YES"
                        #same key on the visual instructions presses down
                        keyarrowright.image = "keyarrowright_down"
                        #coordinates of visual instructions
                        keyarrowright.x = 950
                        keyarrowright.y = 49
                        #mouse moves right
                        alice.x += 5
                        #timer for movement animation
                        alice_move_timer += 0.5
                        #reset when timer gets too high
                        if alice_move_timer > 4:
                            alice_move_timer = 1
                        #flip between two mouse images
                        if alice_move_timer >= 1 and alice_move_timer <= 2:
                            alice.image = "alicerightrun1"
                        if alice_move_timer >= 3 and alice_move_timer <= 4:
                            alice.image = "alicerightrun2"

        if explore_hall == "YES":
            if keyboard.left:
                if wall_move == "YES":
                    bg.x += 5
                    if bg.x >= 1980:
                        bg.x = 1975
                    #same key on the visual instructions presses down
                    keyarrowleft.image = "keyarrowleft_down"
                    #coordinates of visual instructions
                    keyarrowleft.x = 838
                    keyarrowleft.y = 49
                    alice_move_timer += 0.5
                    #reset when timer gets too high
                    if alice_move_timer > 4:
                        alice_move_timer = 1
                    #flip between two mouse images
                    if alice_move_timer >= 1 and alice_move_timer <= 2:
                        alice.image = "aliceleftrun2"
                    if alice_move_timer >= 3 and alice_move_timer <= 4:
                        alice.image = "aliceleftrun1"
        if keyboard.right:
            if wall_move == "YES":
                bg.x -= 5
                alice_move_timer += 0.5
                #reset when timer gets too high
                if alice_move_timer > 4:
                    alice_move_timer = 1
                #same key on the visual instructions presses down
                keyarrowright.image = "keyarrowright_down"
                #coordinates of visual instructions
                keyarrowright.x = 950
                keyarrowright.y = 49
                #flip between two mouse images
                if alice_move_timer >= 1 and alice_move_timer <= 2:
                    alice.image = "alicerightrun1"
                if alice_move_timer >= 3 and alice_move_timer <= 4:
                    alice.image = "alicerightrun2"
        if bg.x <= -560:
            small_door_work = "YES"
            end_hallway = "YES"
            wall_move = "NO"
            small_door_work = "YES"

    if shrink == "YES":
        if keyboard.left:
            alice_moving = "YES"
            #same key on the visual instructions presses down
            keyarrowleft.image = "keyarrowleft_down"
            #coordinates of visual instructions
            keyarrowleft.x = 838
            keyarrowleft.y = 49
            #mouse moves left
            alice.x -= 5
            #timer for movement animation
            alice_move_timer += 0.5
            #reset when timer gets too high
            if alice_move_timer > 4:
                alice_move_timer = 1
            #flip between two mouse images
            if alice_move_timer >= 1 and alice_move_timer <= 2:
                alice.image = "shrunkaliceleftrun2"
            if alice_move_timer >= 3 and alice_move_timer <= 4:
                alice.image = "shrunkaliceleftrun1"

            #mouse moves right when the player clicks the right arrow on the keyboard
        elif keyboard.right:
            alice_moving = "YES"
            alice_moving = "YES"
            #same key on the visual instructions presses down
            keyarrowright.image = "keyarrowright_down"
            #coordinates of visual instructions
            keyarrowright.x = 950
            keyarrowright.y = 49
            #mouse moves right
            alice.x += 5
            #timer for movement animation
            alice_move_timer += 0.5
            #reset when timer gets too high
            if alice_move_timer > 4:
                alice_move_timer = 1
            #flip between two mouse images
            if alice_move_timer >= 1 and alice_move_timer <= 2:
                alice.image = "shrunkalicerightrun1"
            if alice_move_timer >= 3 and alice_move_timer <= 4:
                alice.image = "shrunkalicerightrun2"

#when player releases a key
def on_key_up(key):

    global alice_move_timer, alice_moving, fallen
    #when the key is no longer being pressed, visual instructions go back to normal

    #when the key is no longer being pressed, visual instructions go back to normal
    if key == keys.RIGHT:
        alice_moving = "NO"
        alice_move_timer = 0
        keyarrowright.image = "keyarrowright"
        #reset coordinates
        keyarrowright.x = 950
        keyarrowright.y = 42

    #when the key is no longer being pressed, visual instructions go back to normal
    if key == keys.LEFT:
        alice_moving = "NO"
        alice_move_timer = 0
        keyarrowleft.image = "keyarrowleft"
        #reset coordinates
        keyarrowleft.x = 838
        keyarrowleft.y = 42

def draw_keys():
    keyarrowleft.draw()
    keyarrowright.draw()

def fall_in_hole():
    global fall, text_number, fallen, hall_go

    buffer = 0

    if fallen == "NO":
        if alice.x <= 161:
            fall = "YES"
            hall_go = "YES"
            hole.draw()
            alice.y += 10
            alice.x = 161

        if alice.y >= 800:
            hall_go = "YES"

def button_coordinates():
    global text_number

    if text_number == 9:
        buttons.x = 817

    if text_number == 10 or text_number == 13 or text_number == 28 or text_number == 21 or text_number == 25 or text_number == 23 or text_number == 16 or text_number == 37 or text_number == 38 or text_number == 18 or text_number == 27 or text_number == 19 or text_number == 26 or text_number == 29 or text_number == 31 or text_number == 12 or text_number == 24 or text_number == 24:
        buttons.x = 867

    if text_number == 13 or text_number == 22 or text_number == 29 or text_number == 23 or text_number == 24 or text_number == 27 or text_number == 36 :
        speaker.image = "minialice"
    else:
        if text_number < 41:
            speaker.image = "minidoor"

    if text_number == 39 or text_number == 40:
        speaker.image = "minialicecry"
        buttons.image = "button18"

    if text_number == 17:
        diagram.image = "diagram2"
    elif text_number == 22:
        diagram.image = "diagram3"
    elif text_number == 23:
        diagram.image = "diagram4"
    elif text_number == 24:
        diagram.image = "diagram5"
    elif text_number == 32:
        diagram.image = "diagram6"

    if text_number == 11:
        buttons.x = 751

    if text_number == 14:
        buttons.x = 771

    if text_number == 15 or text_number == 30 or text_number == 17 or text_number == 32:
        buttons.x = 835

    if text_number == 20:
        buttons.x = 764

    if text_number == 30:
        buttons.x = 755

    if text_number == 89:
        text_number = 89


def dice_roll():
    global dice_number, dice_list, rolling, dicetimer, dicelistnumber, text_number
    random_dice = 0
    answer_list = ["dice1","dice2","dice3","dice5"]

    while dice_number <= 19:
        for x in range(len(dice_list)):
            random_dice = random.randint(1,6)
            dice_list[dice_number] = random_dice
            dice_number += 1

    if rolling == "YES":
        if dicelistnumber <= 29:
            dicetimer += 1
            if dicetimer >= 10:
                dice.image = 'dice' + str(dice_list[dicelistnumber])
                dicelistnumber += 1
                dicetimer = 0
        if dicelistnumber == 30:
            dice.image = random.choice(answer_list)
            text_number += 1
            rolling = "NO"

def potion_experiment():
    global text_number, potion_go, shrink, experiment_timer

    if text_number == 35:
        if potion_go == "YES":
            left = random.randint(1,2)
            right = random.randint(1,2)

            if left == 1:
                left_buttons.image = "failleft"
            else:
                left_buttons.image = "successleft"

            if right == 2:
                right_buttons.image = "failright"
            else:
                right_buttons.image = "successright"

            if right_buttons.image == "successright" and left_buttons.image == "successleft":
                shrink = "YES"
            potion_go = "NO"

def shrinkcmd():
    global realshrink
    if realshrink == "YES" and text_number != 75:
        alice.image = "shrunkalicefront"
        alice.y = 450

def teascene():
    global teaparty, text_number, castle

    if teaparty == "YES" and text_number != 75:
        bg.image = "teaforest"
        bg.x = 774
        bg.y = 136
        alice.x = 340
        alice.y = 415
        alice.image = "alicefront"
        shrink = "NO"
        buttons.image = "button18"

        if text_number == 41 or text_number == 42 or text_number == 45 or text_number == 47 or text_number == 49 or text_number == 51 or text_number == 53 or text_number == 55 or text_number == 61 or text_number == 62 or text_number == 65:
            speaker.image = "minialice"
        else:
            if text_number < 66:
                speaker.image = "minihatter"

        if text_number >= 66:
            castle = "YES"
            teaparty = "NO"

def castlescene():
    global text_number, castle, alice_move_timer

    if castle == "YES":
        bg.image = "castle"
        bg.x = 613
        bg.y = 341
        if text_number < 75 and text_number != 75:
            alice.x = 387
            alice.y = 443
            alice.image = "alicefront"
        shrink = "NO"
        buttons.image = "button18"

        if text_number >= 75 and text_number < 87:
            alice.x -= 5
            alice_move_timer += 0.5
            #reset when timer gets too high
            if alice_move_timer > 4:
                alice_move_timer = 1
            #flip between two mouse images
            if alice_move_timer >= 1 and alice_move_timer <= 2:
                alice.image = "aliceleftrun2"
            if alice_move_timer >= 3 and alice_move_timer <= 4:
                alice.image = "aliceleftrun1"
        if text_number >= 87:
            bg.image = "labyrinth"
            alice.image = "alicefront"
            bg.x = 500
            bg.y = 325
            if text_number != 89:
                alice.x = 95
                alice.y = 79


        if text_number == 66 or text_number == 70 or text_number == 72 or text_number == 73 or text_number == 75 or text_number == 87 or text_number == 88:
            speaker.image = "minialice"
        if  text_number == 69 or text_number == 74 or text_number == 76 or text_number == 78 or text_number == 84 or text_number == 86:
            speaker.image = "qofh"
        if text_number == 71 or text_number == 80 or text_number == 82 or text_number == 85:
            speaker.image = "black_card"
        if text_number == 77 or text_number == 79 or text_number == 81 or text_number == 83:
            speaker.image = "red_card"
        if text_number == 89:
            text_number = 89
            gogoalice = "YES"
            while alice.x < 725:
                alice.x += 5
            while alice.x >= 725 and alice.y < 400:
                alice.y += 5

        if text_number == 89:
            alice.x += 5
            alice_move_timer += 0.5
            #reset when timer gets too high
            if alice_move_timer > 4:
                alice_move_timer = 1
            #flip between two mouse images
            if alice_move_timer >= 1 and alice_move_timer <= 2:
                alice.image = "alicerightrun2"
            if alice_move_timer >= 3 and alice_move_timer <= 4:
                alice.image = "alicerightrun1"















