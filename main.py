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
Start of Sprite Creation
"""
answer_key, spriteNames = engine.set_Sprite_Order()
press_space_Sprite = engine.setPressSpace()
press_enter_Sprite = engine.setPressEnter()
instruct_Sprite = engine.setInstructions() 
sprite0 = engine.createSprite(spriteNames[0],0)
sprite1 = engine.createSprite(spriteNames[1],1)
sprite2 = engine.createSprite(spriteNames[2],2)
sprite3 = engine.createSprite(spriteNames[3],3)
sprite4 = engine.createSprite(spriteNames[4],4)
sprite5 = engine.createSprite(spriteNames[5],5)
sprite6 = engine.createSprite(spriteNames[6],6)
sprite7 = engine.createSprite(spriteNames[7],7)
sprite8 = engine.createSprite(spriteNames[8],8)
sprite9 = engine.createSprite(spriteNames[9],9)
sprite10 = engine.createSprite(spriteNames[10],10)
sprite11 = engine.createSprite(spriteNames[11],11)
sprite12 = engine.createSprite(spriteNames[12],12)
sprite13 = engine.createSprite(spriteNames[13],13)
sprite14 = engine.createSprite(spriteNames[14],14)
sprite15 = engine.createSprite(spriteNames[15],15)
sprite16 = engine.createSprite(spriteNames[16],16)
sprite17 = engine.createSprite(spriteNames[17],17)
sprite18 = engine.createSprite(spriteNames[18],18)
sprite19 = engine.createSprite(spriteNames[19],19)



"""
End of Sprite Creation
"""

"""
Start of sound file creation
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
End of sound file creation
"""

"""
Start of status global variables
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

scores_text = pyglet.text.Label(str(score), font_name="Sans Serif",font_size = 12, color = (0,0,0,0), x = window.width//2, y = 6*window.height//7, anchor_x = "center", anchor_y = "center")
game_over_text = pyglet.text.Label("GAME OVER", font_name="Sans Serif",font_size = 36, color = (0,0,0,0), x = window.width//2, y = 6*window.height//7, anchor_x = "center", anchor_y = "center")
copy_scores_text = pyglet.text.Label("Score: " + str(score), font_name="Sans Serif",font_size = 36, color = (0,0,0,0), x = window.width//2, y = 4*window.height//7, anchor_x = "center", anchor_y = "center")
highscores_text = pyglet.text.Label("Highscore: " + str(highscore), font_name="Sans Serif",font_size = 36, color = (0,0,0,0), x = window.width//2, y = (4*window.height//7)-100, anchor_x = "center", anchor_y = "center")



"""
End of status global variables
"""

#This is a class to make a useless but pretty triangle
class Triangle:
    def __init__(self):
        #self.vertices = pyglet.graphics.vertex_list(3, ('v3f',[-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.0,0.5,0.0]), ('c3B',[100,200,220, 200,110,100, 100, 250,100]) )
        self.vertices = pyglet.graphics.vertex_list(3, ('v2f', [0,0, 400,50, 200,0]))

#This function handles all the window events and draws all the sprites necessary
@window.event
def on_draw():
    window.clear()
    press_space_Sprite.draw()
    instruct_Sprite.draw()
    press_enter_Sprite.draw()
    sprite0.draw()
    sprite1.draw()
    sprite2.draw()
    sprite3.draw()
    sprite4.draw()
    sprite5.draw()
    sprite6.draw()
    sprite7.draw()
    sprite8.draw()
    sprite9.draw()
    sprite10.draw()
    sprite11.draw()
    sprite12.draw()
    sprite13.draw()
    sprite14.draw()
    sprite15.draw()
    sprite16.draw()
    sprite17.draw()
    sprite18.draw()
    sprite19.draw()
    scores_text.draw()
    game_over_text.draw()
    copy_scores_text.draw()
    highscores_text.draw()
    uselessTriangle = Triangle()
    uselessTriangle.vertices.draw(GL_TRIANGLES)

#This function removes a sprite from visibility after it has been correctly evaluate by the user
def removeSprite(spriteNo):
    if spriteNo == 0:
        sprite0.visible = False
    elif spriteNo == 1:
        sprite1.visible = False
    elif spriteNo == 2:
        sprite2.visible = False
    elif spriteNo == 3:
        sprite3.visible = False
    elif spriteNo == 4:
        sprite4.visible = False
    elif spriteNo == 5:
        sprite5.visible = False
    elif spriteNo == 6:
        sprite6.visible = False
    elif spriteNo == 7:
        sprite7.visible = False
    elif spriteNo == 8:
        sprite8.visible = False
    elif spriteNo == 9:
        sprite9.visible = False
    elif spriteNo == 10:
        sprite10.visible = False
    elif spriteNo == 11:
        sprite11.visible = False
    elif spriteNo == 12:
        sprite12.visible = False
    elif spriteNo == 13:
        sprite13.visible = False
    elif spriteNo == 14:
        sprite14.visible = False
    elif spriteNo == 15:
        sprite15.visible = False
    elif spriteNo == 16:
        sprite16.visible = False
    elif spriteNo == 17:
        sprite17.visible = False
    elif spriteNo == 18:
        sprite18.visible = False
    elif spriteNo == 19:
        sprite19.visible = False

#This function erases all the sprites and creates the game over screen
#It also shows and updates the high score
def eraseAllSprites():
    global spriteNum
    global score
    scores_text.color = (0,0,0,0)
    game_over_text.color = (0,0,0,255)
    copy_scores_text.color = (0,0,0,255)
    highscores_text.color = (0,0,0,255)
    copy_scores_text.text = "Score: " + str(score)

    if str(score) >= str(highscore):
        score_file_write.write((str(score) + "\n"))
        highscores_text.text = "New Highscore: " + str(score)
        score_file_write.close()

    spriteNum = -1
    sprite0.visible = False
    sprite1.visible = False
    sprite2.visible = False
    sprite3.visible = False
    sprite4.visible = False
    sprite5.visible = False
    sprite6.visible = False
    sprite7.visible = False
    sprite8.visible = False
    sprite9.visible = False
    sprite10.visible = False
    sprite11.visible = False
    sprite12.visible = False
    sprite13.visible = False
    sprite14.visible = False
    sprite15.visible = False
    sprite16.visible = False
    sprite17.visible = False
    sprite18.visible = False
    sprite19.visible = False

#This function causes the game to be over if a sprite reaches the bottom of the window
#or if all the sprites have been evaluated
def reachZero():
    global spriteNum
    c = spriteNum == 0 and sprite0.y == 0
    c = c or spriteNum == 1 and sprite1.y == 0
    c = c or spriteNum == 2 and sprite2.y == 0
    c = c or spriteNum == 3 and sprite3.y == 0
    c = c or spriteNum == 4 and sprite4.y == 0
    c = c or spriteNum == 5 and sprite5.y == 0
    c = c or spriteNum == 6 and sprite6.y == 0
    c = c or spriteNum == 7 and sprite7.y == 0
    c = c or spriteNum == 8 and sprite8.y == 0
    c = c or spriteNum == 9 and sprite9.y == 0
    c = c or spriteNum == 10 and sprite10.y == 0
    c = c or spriteNum == 11 and sprite11.y == 0
    c = c or spriteNum == 12 and sprite12.y == 0
    c = c or spriteNum == 13 and sprite13.y == 0
    c = c or spriteNum == 14 and sprite14.y == 0
    c = c or spriteNum == 15 and sprite15.y == 0
    c = c or spriteNum == 16 and sprite16.y == 0
    c = c or spriteNum == 17 and sprite17.y == 0
    c = c or spriteNum == 18 and sprite18.y == 0
    c = c or spriteNum == 19 and sprite19.y == 0

    if spriteNum == 20:
        correct_sound.play()
        eraseAllSprites()
    elif c:
        incorrect_sound.play()
        eraseAllSprites()

#This function checks if the current sprite being evaluated 
#was correctly guessed as having the value of True
def checkTrue():
    global spriteNum
    global score
    check = engine.checkCorrect(answer_key, "T",spriteNum)
    if check == True:
        #If the user answered correctly, the score is increased
        #The sprite that was guessed is also removed from visibility
        score += 1
        removeSprite(spriteNum)
        spriteNum += 1
    else:
        #If the user was wrong, the game ends
        eraseAllSprites()

#This function checks if the current sprite being evaluated 
#was correctly guessed as having the value of False
def checkFalse():
    global spriteNum
    global score
    check = engine.checkCorrect(answer_key, "F",spriteNum)
    if check == True:
        score += 1
        removeSprite(spriteNum)
        spriteNum += 1
    else:
        eraseAllSprites()

#This function handles all the input from the keyboard
@window.event
def on_key_press(symbol,modifiers):
    #If you press SPACE, you get taken to the instructions page
    if symbol == key.SPACE:
        press_space_Sprite.visible = False
        instruct_Sprite.visible = True
        press_enter_Sprite.visible = True
    #If you press ENTER, you start the game
    elif symbol == key.ENTER:
        instruct_Sprite.visible = False
        press_enter_Sprite.visible = False
        enter = True
        startGame(answer_key, spriteNames)
    #If you press T, you answer True and the program
    #checks if you're right
    elif symbol == key.T:
        checkTrue()
    #If you press F, you answer False and the program
    #checks if you're right
    elif symbol == key.F:
        checkFalse()

#This function just starts the game
#It also shows the score counter
def startGame(answer_key,spriteNames):
    scores_text.color = (0,0,0,255)

    #This function updates the positions of the sprites
    #This is to show that they are falling
    def update(dt):
        sprite0.y -= 2
        sprite1.y -= 2
        sprite2.y -= 2
        sprite3.y -= 2
        sprite4.y -= 2
        sprite5.y -= 2
        sprite6.y -= 2
        sprite7.y -= 2
        sprite8.y -= 2
        sprite9.y -= 2
        sprite10.y -= 2
        sprite11.y -= 2
        sprite12.y -= 2
        sprite13.y -= 2
        sprite14.y -= 2
        sprite15.y -= 2
        sprite16.y -= 2
        sprite17.y -= 2
        sprite18.y -= 2
        sprite19.y -= 2

        #This function also checks if a sprite has reached zero
        reachZero()
        #It also regularly updates the score
        scores_text.text = str(score)

    #This part runs the update function every 1/60 of a second
    pyglet.clock.schedule_interval(update,1/60)

#This line runs the whole application
pyglet.app.run()



