# PrediCARO: A Game of Truth

## Designing the Program
  “PrediCARO” is a simple logic game. The rules are simple, there are falling logical
expressions and the player must decide whether the falling logical expression is true or false. They must click ‘t’ on their keyboard if the expression and ‘f’ otherwise. If the statement reaches the bottom or the player inputted an incorrect answer, it is game over.



## Engine
The game was designed and made using Python 3. The following functions were defined for
the game to be played:

```markdown
import pyglet
from pyglet.window import key
from pyglet.window import mouse
import random

correct_sound = pyglet.resource.media('sounds/correct.mp3', streaming = False)

incorrect_sound = pyglet.resource.media('sounds/incorrect.mp3', streaming = False)

#generates a list of File names for all the sprite images that evaluate to True
def set_Truth_Sprites():
    fileNames = []
    for i in range(15):
        num = random.randint(1,14)
        fileName = "trueExp/TrueExp" + str(num) + ".png"
        fileNames.append(fileName)

    return fileNames 

#generates a list of File names for all the sprite images that evaluate to False
def set_False_Sprites():
    fileNames = []
    for i in range(15):
        num = random.randint(1,11)
        fileName = "falseExp/FalseExp" + str(num) + ".png"
        fileNames.append(fileName)

    return fileNames 

#shuffles the possible filenames and creates a new list with mixed True and False file names
#creates an answer key for these soon-to-be sprites
def set_Sprite_Order():
    answer_key = []
    spriteNames = []
    truths = set_Truth_Sprites()
    falses = set_False_Sprites()
    for i in range(20):
        val = random.randint(0,1)
        num = random.randint(0,14)
        if val == 0:
            answer_key.append("F")
            spriteNames.append(falses[num])
        elif val == 1:
            answer_key.append("T")
            spriteNames.append(truths[num])
    return answer_key, spriteNames

def setPressSpace():
    #creates the Press Space sprite for main menu
    press_space= pyglet.image.load_animation('menu-images/Press-Space.gif')
    press_space_Sprite = pyglet.sprite.Sprite(press_space, x = 27, y = 270)
    press_space_Sprite.scale = 0.45
    press_space_Sprite.visible = True 
    return press_space_Sprite

def setPressEnter():
    #creates Press Enter sprite
    press_enter = pyglet.image.load_animation('menu-images/Press-Enter.gif')
    press_enter_Sprite = pyglet.sprite.Sprite(press_enter, x = 135, y = 60)
    press_enter_Sprite.scale = 0.25
    press_enter_Sprite.visible = False
    return press_enter_Sprite

def setInstructions():
    #creates Instructions Sprite
    instructions = pyglet.image.load_animation('menu-images/Instructions-Sprite.png')
    instruct_Sprite = pyglet.sprite.Sprite(instructions, x = 85, y = 122)
    instruct_Sprite.scale = 0.38
    instruct_Sprite.visible = False
    return instruct_Sprite

def createSprite(fileName,num):
    #this function helps generate truth value expressions as sprites
    #it also sets the y values such that succeeding sprites are at progressively higher y values
    true = pyglet.image.load_animation(fileName)
    trueSprite = pyglet.sprite.Sprite(true, x = 50, y = 600+(num*250))
    trueSprite.scale = 0.4
    trueSprite.visible = True
    return trueSprite

def checkCorrect(answer_key,truthVal,spriteNum):
    #this function checks if the user's evaluation of the expression is correct
    #makes a happy ding sound then returns True if correct
    #makes a sad buzzer sound then returns False if incorrect
    if answer_key[spriteNum] == truthVal:
        correct_sound.play()
        return True
    elif answer_key[spriteNum] != truthVal:
        incorrect_sound.play()
        return False

```

## Main

