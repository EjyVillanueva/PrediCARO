# PrediCARO: A Game of Truth

## Designing the Program
  “PrediCARO” is a simple logic game. The rules are simple, there are falling logical
expressions and the player must decide whether the falling logical expression is true or false. They must click ‘t’ on their keyboard if the expression and ‘f’ otherwise. If the statement reaches the bottom or the player inputted an incorrect answer, it is game over.



## Engine
The game was designed and made using Python 3. The following functions were defined for
the game to be played:

1. set_Truth_Sprites() – generates a list of File names for all the sprite images that evaluate to True
2.set_False_Sprites() – generates a list of File names for all the sprite images that evaluate to False
3. set_Sprite_Order() – shuffles the possible filenames and creates a new list with mixed True and False file names. It then creates an answer key for these soon-to-be sprites.
4. setPressSpace() – #creates the Press Space sprite for main menu
5. setPressEnter() – creates Press Enter sprite
6. setInstructions() – #creates Instructions Sprite
7. createSprite(fileName,num) - This function helps generate truth value expressions as sprites. It also sets the y values such that succeeding sprites are at progressively higher y values.
8. checkCorrect(answer_key,truthVal,spriteNum) - This function checks if the user's evaluation of the expression is correct. It then makes a happy ding sound then returns True if correct. Otherwise, it makes a sad buzzer sound then returns False.

These functions will be used for the game itself. It will be stored in a user-defined module
called engine.

### Sample Code
```markdown
def set_Truth_Sprites():
    fileNames = []
    for i in range(15):
        num = random.randint(1,14)
        fileName = "trueExp/TrueExp" + str(num) + ".png"
        fileNames.append(fileName)

    return fileNames 
```

## Main

Another module that was made is the main engine. This will be the module that the player
will run if he/she wants to play the game. The main engine contains all the necessary functions
in order for the game to run. Pyglet, random and the engine(user-defined module) will be
imported in this module.


Here is where the window is created and modified. Sprites of propositional statements are also
created with the use of the engine module. Sound files such as background music, correct
sound, and incorrect sound are then initialized. Global variables that serve as statuses such as
score, number of sprites, wrong, booleans (start and enter), and the text file that is used to
update scores are declared. With the use of the pyglet module, texts to be displayed are also
initialized (i.e. scores, game over, and high scores).
A class named Triangle is also created to make a useless but pretty triangle.

For the window events, the decorator @window.event manages it.

There are functions that are defined in this module aside from the on_draw() and
on_key_press(symbol,modifiers) that are managed by @window.event:


1.) removeSprite(spriteNo) - removes a sprite from visibility after it has been correctly evaluate
by the user.
2.)eraseAllSprites() - erases all the sprites and creates the game over screen. It also shows and
updates the high score.
3.)reachZero() - causes the game to be over if a sprite reaches the bottom of the window or if all
the sprites have been evaluated.
4.)checkTrue() - checks if the current sprite being evaluated was correctly guessed as having
the value of True
5.)checkFalse() - This function checks if the current sprite being evaluated was correctly
guessed as having the value of False
6.)startGame(answer_key,spriteNames) - This function just starts the game. It also shows the
score counter
6.a) update(dt) - This function updates the positions of the sprites. This is to show that
they are falling
And lastly, pyglet.app.run() is called to run the whole application.

### Sample Code
```markdown
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
```

