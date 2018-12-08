import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *
import random
import engine

"""
Start of Window Creation
"""
window = pyglet.window.Window(width=660, height=540, caption="PrediCARO", resizable=False)
window.set_location(400, 100)


r,g,b,a = 1,0.6,0.0,1
pyglet.gl.glClearColor(r,g,b,a)

main_batch = pyglet.graphics.Batch()

"""
End of Window Creation
"""

"""
Sounds
"""
#creates a player and queues the song
background_player = pyglet.media.Player()
background_music = pyglet.media.load('sounds/background-music.mp3')
background_player.queue(background_music) 
#keeps playing for as long as the app is running
background_player.eos_action = pyglet.media.SourceGroup.loop
background_player.play()

correct_sound = pyglet.resource.media('sounds/correct.mp3', streaming = False)

incorrect_sound = pyglet.resource.media('sounds/incorrect.mp3', streaming = False)

"""
End of Sounds
"""

"""
Global Variables and Labels
"""
start = False
enter = False
score = 0
spriteNum = 0
wrong = 0
score_file = open("scores.txt","r")
highscore = score_file.read().splitlines()
if highscore != None:
    highscore = max(highscore)
score_file.close()

score_file_write = open("scores.txt","a")

scores_text = pyglet.text.Label(str(score), font_name="Eight-Bit Madness",font_size = 15, color = (255,255,255,0), x = window.width//2, y = 6*window.height//7, anchor_x = "center", anchor_y = "center")
game_over_text = pyglet.text.Label("GAME OVER", font_name="Eight-Bit Madness",font_size = 45, color = (255,255,255,0), x = window.width//2, y = 5*window.height//7, anchor_x = "center", anchor_y = "center")
copy_scores_text = pyglet.text.Label("Score: " + str(score), font_name="Eight-Bit Madness",font_size = 36, color = (255,255,255,0), x = window.width//2, y = 4*window.height//7, anchor_x = "center", anchor_y = "center")
highscores_text = pyglet.text.Label("Highscore: " + str(highscore), font_name="Eight-Bit Madness",font_size = 36, color = (255,255,255,0), x = window.width//2, y = (4*window.height//7)-60, anchor_x = "center", anchor_y = "center")


"""
End of Global Variables and Labels
"""


"""
Sprite Creation
"""
answer_key = []
spriteNames = []

def setSpriteNames():
    global answer_key
    global spriteNames
    answer_key, spriteNames = engine.set_Sprite_Order()

press_space_Sprite = engine.setPressSpace()
press_enter_Sprite = engine.setPressEnter()
instruct_Sprite = engine.setInstructions() 

spriteList = []

class Sprite:
    global spriteNames

    def __init__(self, spriteNum):
        self.spriteNum = spriteNum
        self.spriteName = spriteNames[self.spriteNum]
        self.sprite = engine.createSprite(spriteNames[self.spriteNum], self.spriteNum)

    def updateSprite(self):
        self.sprite.y -= 2

    def reachZero(self):
        if self.sprite.y == 0:
            return True
        else:
            return False

    def drawSprite(self):
        self.sprite.draw()

    def isCorrect(self, playerAnswer):
        global score
        check = engine.checkCorrect(answer_key, playerAnswer , self.spriteNum)
        if check == True:
            #If the user answered correctly, the score is increased
            #The sprite that was guessed is also removed from visibility
            score += 1
            removeSprite(self.spriteNum)
        else:
            #If the user was wrong, the game ends
            eraseAllSprites()

def setExpressionSprites():
    global answer_key
    global spriteNames
    global spriteList

    for i in range(len(spriteNames)):
        sprite = Sprite(i)
        spriteList.append(sprite)

"""
End of Sprite Creation
"""

#This is a class to make a useless but pretty triangle
class Triangle:
    def __init__(self):
        #self.vertices = pyglet.graphics.vertex_list(3, ('v3f',[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.0,0.5,0.0]), ('c3B',[100,200,220, 200,110,100, 100, 250,100]) )
        self.vertices = pyglet.graphics.vertex_list(3, ('v2f', [0,0, 400,50, 200,0]))

@window.event
def on_draw():
    window.clear()
    press_space_Sprite.draw()
    instruct_Sprite.draw()
    press_enter_Sprite.draw()
    
    for i in range(len(spriteNames)):
        spriteList[i].sprite.draw()

    scores_text.draw()
    game_over_text.draw()
    copy_scores_text.draw()
    highscores_text.draw()
    uselessTriangle = Triangle()
    uselessTriangle.vertices.draw(GL_TRIANGLES)

def removeSprite(spriteNo):
    global spriteNum
    spriteList[spriteNo].sprite.visible = False
    spriteNum += 1

def eraseAllSprites():
    global spriteNum
    global score
    scores_text.color = (0,0,0,0)
    game_over_text.color = (255,255,255,255)
    copy_scores_text.color = (255,255,255,255)
    highscores_text.color = (255,255,255,255)
    copy_scores_text.text = "Score: " + str(score)

    if str(score) >= str(highscore):
        score_file_write.write((str(score) + "\n"))
        highscores_text.text = "New Highscore: " + str(score)
        score_file_write.close()

    spriteNum = -1

    for i in range(len(spriteNames)):
        spriteList[i].sprite.visible = False

def reachZero():
    global spriteNum
    is_zero = spriteList[spriteNum].reachZero()

    if is_zero == True:
        incorrect_sound.play()
        eraseAllSprites()
    elif is_zero == False and spriteNum == len(spriteNames):
        correct_sound.play()
        eraseAllSprites()

@window.event
def on_key_press(symbol,modifiers):
    global start
    global enter
    #If you press SPACE, you get taken to the instructions page
    if symbol == key.SPACE and start == False:
        press_space_Sprite.visible = False
        instruct_Sprite.visible = True
        press_enter_Sprite.visible = True
        start = True
    #If you press ENTER, you start the game
    elif symbol == key.ENTER and enter == False and start == True:
        instruct_Sprite.visible = False
        press_enter_Sprite.visible = False
        enter = True
        startGame(answer_key, spriteNames)
    #If you press T, you answer True and the program
    #checks if you're right
    elif symbol == key.T and enter == True:
        spriteList[spriteNum].isCorrect("T")
    #If you press F, you answer False and the program
    #checks if you're right
    elif symbol == key.F and enter == True:
        spriteList[spriteNum].isCorrect("F")

def startGame(answer_key,spriteNames):
    scores_text.color = (0,0,0,255)

    def update(dt):
        global spriteNum
        for i in range(len(spriteNames)):
            spriteList[i].sprite.y -= 2
        
        if spriteList[spriteNum].reachZero() == True:
            eraseAllSprites()

        scores_text.text = str(score)
    
    pyglet.clock.schedule_interval(update,1/60)

setSpriteNames()
setExpressionSprites()
# print(spriteNames)
# for i in range(len(spriteNames)):
#     print(spriteList[i].spriteNum)
#This line runs the whole application
pyglet.app.run()











