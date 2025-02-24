import pygame
import time
import random

# Constants
size = 40 
initial_length = 3

# Game Class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800)) #resolution(height, width)
        pygame.display.set_caption("Snake Game")  

        # Game states and features -> flag is good practice
        self.score = 0
        self.game_started = False
        self.paused = False
        self.running = True # ** to play game infinite times, timer, delay
        self.direction = 'Down' # ball up

        # Snake
        self.block = pygame.image.load("img/block.jpg") # to load img, 
        self.block_x = [size] * initial_length # essential for collision detection
        self.block_y = [size] * initial_length # array cz snake has multiple blocks


        # Apple
        self.apple = pygame.image.load("img/apple.jpg")
        self.apple_x, self.apple_y = self.randomApple() #x, y tells position of block


    #Movements -> functions for neatness
    def move_up(self): # row change, column same
        self.block_y[0] -= size

    def move_down(self):
        self.block_y[0] += size

    def move_left(self): # column change, row same
        self.block_x[0] -= size

    def move_right(self):
        self.block_x[0] += size

    def handle_movement(self, event): # automatic key detection in pygame
        if event.key == pygame.K_UP and self.direction != 'Down': # extra but better cz already defined  
            self.direction = 'Up'
        elif event.key == pygame.K_DOWN and self.direction != 'Up':
            self.direction = 'Down'
        elif event.key == pygame.K_LEFT and self.direction != 'Right':
            self.direction = 'Left'
        elif event.key == pygame.K_RIGHT and self.direction != 'Left':
            self.direction = 'Right'

    def checkDirection(self): # main thing  
        for i in range(len(self.block_x) - 1, 0, -1): # reverse loop, in case of long body
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]

        if self.direction == 'Up':
            self.move_up()
        elif self.direction == 'Down':
            self.move_down()
        elif self.direction == 'Left':
            self.move_left()
        elif self.direction == 'Right':
            self.move_right()

    #
    def checkCollision(self): #   remember resolution
        if self.block_x[0] < 0 or self.block_y[0] < 0 or self.block_x[0] >= 1000 or self.block_y[0] >= 800: # last row, last column
            self.game_over() # edges
        for i in range(1, len(self.block_x)):
            if self.block_x[0] == self.block_x[i] and self.block_y[0] == self.block_y[i]:
                self.game_over() 

    def randomApple(self):
        apple_x = random.randint(0, (1000 // size) - 1) * size # apple x or y inside screen 
        apple_y = random.randint(0, (800 // size) - 1) * size
        return apple_x, apple_y

    def collectApple(self):
        if self.block_x[0] == self.apple_x and self.block_y[0] == self.apple_y:
            self.block_x.append(self.block_x[-1])  
            self.block_y.append(self.block_y[-1])
            self.score += 1
            self.apple_x, self.apple_y = self.randomApple() # new apple

    def displayScore(self): # graphic part
        font = pygame.font.SysFont("comicsans", 20)
        playerScore = font.render("Score: %d" % self.score, True, (255, 255, 255)) 
        self.screen.blit(playerScore, (10, 10))

    # Main Game Features  

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                self.running = False # game over
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif not self.game_started:
                    if event.key == pygame.K_RETURN: # enter
                        self.game_started = True
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
                elif self.game_started and not self.paused:
                    self.handle_movement(event)


    def update_screen(self):
        self.screen.fill((137, 119, 181)) # fill colour, screen is variable
        for i in range(len(self.block_x)):
            self.screen.blit(self.block, (self.block_x[i], self.block_y[i]))
        self.screen.blit(self.apple, (self.apple_x, self.apple_y)) # blit is print
        self.displayScore()
        pygame.display.update() # imp

    # Game run
    def run(self):
        while self.running:
            if not self.game_started:
                self.startScreen()
            else:
                self.handle_events()
                if not self.paused:
                    self.checkDirection()
                    self.collectApple()
                    self.checkCollision()
                    self.update_screen()

                    time.sleep(0.17) # delay, slow snake, seconds
        pygame.quit()  

    # Game Start
    def startScreen(self):
        self.screen.fill((137, 119, 181))
        font = pygame.font.SysFont("comicsans", 60)
        title = font.render("Snake Game", True, (255, 255, 255))
        startFont = pygame.font.SysFont("comicsans", 40)
        play_button = startFont.render("Press Enter to Play", True, (255, 255, 255))

        self.screen.blit(title, (300, 300)) # what and where(dest) to display
        self.screen.blit(play_button, (300, 400))
        pygame.display.update()

        while not self.game_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.game_started = True

    # Game Over
    def game_over(self):
        self.screen.fill((137, 119, 181))  # Background color
        font = pygame.font.SysFont("comicsans", 30)
        over_text = font.render("Game Over!", True, (255, 255, 255))
        restart_text = font.render("Press Enter to Restart", True, (255, 255, 255))
        exit_text = font.render("Press Esc to Quit", True, (255, 255, 255))
        score_text = font.render("Your Score is : %d" % self.score, True, (255, 255, 255))

        self.screen.blit(over_text, (300, 300))
        self.screen.blit(score_text, (300, 350))
        self.screen.blit(restart_text, (300, 400))
        self.screen.blit(exit_text, (300, 450))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.__init__()
                        self.run()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        quit()
# Entry point
if __name__ == "__main__": 
    game = Game() #game is object
    game.run()
