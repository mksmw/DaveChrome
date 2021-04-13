import pygame
import os
import random

pygame.init()

# I'm using a procedural programming, hence why it's messy

# Constants for GUI
GUI_HEIGHT = 500
GUI_WIDTH = 900
GUI = pygame.display.set_mode((GUI_WIDTH, GUI_HEIGHT))

# Assets Path
# For animation put it in an array
# For static asset, no array
DAVE = pygame.image.load(os.path.join("Assets/Dave", "start.png"))
DAVE_RUN = [pygame.image.load(os.path.join("Assets/Dave", "run1.png")),
            pygame.image.load(os.path.join("Assets/Dave", "run2.png")),
            pygame.image.load(os.path.join("Assets/Dave", "run3.png"))
            ]
DAVE_JUMP = pygame.image.load(os.path.join("Assets/Dave", "jump.png"))
DAVE_SLIDE = pygame.image.load(os.path.join("Assets/Dave", "slide.png"))
PLANET_ONE = pygame.image.load(os.path.join("Assets/Background", "Mars.png"))
PLANET_TWO = pygame.image.load(os.path.join("Assets/Background", "Earth.png"))
PLANET_THREE = pygame.image.load(os.path.join("Assets/Background", "Jupiter.png"))
BACKGROUND = pygame.image.load(os.path.join("Assets/Background", "BackGround.png"))
GLOB = pygame.image.load(os.path.join("Assets/Enemy", "Glob.png"))
IDK = pygame.image.load(os.path.join("Assets/Enemy", "IdkAnymore.png"))


class Dave:
    # Position of dave in the GUI
    POS_X = 100
    POS_Y = 295
    POS_Y_SLIDE = 320
    JUMP_VELOCITY = 8.5

    # Initializing the asset
    def __init__(self):
        self.run_img = DAVE_RUN
        self.slide_img = DAVE_SLIDE
        self.jump_img = DAVE_JUMP

        # Using run as the default
        self.dave_run = True
        self.dave_slide = False
        self.dave_jump = False

        self.step_index = 2
        self.jump_vel = self.JUMP_VELOCITY
        self.image = self.run_img[2]
        # hit box for dave
        self.dave_hit = self.image.get_rect()
        self.dave_hit.x = self.POS_X
        self.dave_hit.y = self.POS_Y

    def update(self, userInput):
        if self.dave_run:
            self.run()
        if self.dave_slide:
            self.slide()
        if self.dave_jump:
            self.jump()

        # step index to reset every 10 steps
        if self.step_index >= 30:
            self.step_index = 0

        if userInput[pygame.K_SPACE] and not self.dave_jump:
            self.dave_run = False
            self.dave_slide = False
            self.dave_jump = True
        elif userInput[pygame.K_s] and not self.dave_jump:
            self.dave_run = False
            self.dave_slide = True
            self.dave_jump = False
        elif not (self.dave_jump or userInput[pygame.K_DOWN]):
            self.dave_run = True
            self.dave_slide = False
            self.dave_jump = False

    # Run method
    def run(self):
        self.image = self.run_img[self.step_index // 10]
        self.dave_hit = self.image.get_rect()
        self.dave_hit.x = self.POS_X
        self.dave_hit.y = self.POS_Y
        # running speed
        self.step_index += 5

    # Slide method
    def slide(self):
        self.image = self.slide_img
        self.dave_hit = self.image.get_rect()
        self.dave_hit.x = self.POS_X
        self.dave_hit.y = self.POS_Y_SLIDE

    # Jump method
    def jump(self):
        self.image = self.jump_img
        if self.dave_jump:
            self.dave_hit.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            if self.jump_vel < - self.JUMP_VELOCITY:
                self.dave_jump = False
                self.jump_vel = self.JUMP_VELOCITY

    # Draw method
    def draw(self, GUI):
        GUI.blit(self.image, (self.dave_hit.x, self.dave_hit.y))


class Planet:
    def __init__(self):
        self.x = GUI_WIDTH + random.randint(700, 800)
        # Random y-parameter for planets
        self.y = random.randint(50, 150)
        self.image = PLANET_ONE
        self.width = self.image.get_width()

    def update(self):
        # Moving planet from right to left
        self.x -= game_speed
        if self.x < -self.width:
            self.x = GUI_WIDTH + random.randint(200, 300)
            self.y = random.randint(50, 150)

    def draw(self, GUI):
        GUI.blit(self.image, (self.x, self.y))


class PlanetTwo:
    def __init__(self):
        self.x = GUI_WIDTH + random.randint(400, 650)
        # Random y-parameter for planets
        self.y = random.randint(90, 150)
        self.image = PLANET_TWO
        self.width = self.image.get_width()

    def update(self):
        # Moving planet from right to left
        self.x -= game_speed
        if self.x < -self.width:
            self.x = GUI_WIDTH + random.randint(400, 700)
            self.y = random.randint(80, 150)

    def draw(self, GUI):
        GUI.blit(self.image, (self.x, self.y))


class PlanetThree:
    def __init__(self):
        self.x = GUI_WIDTH + random.randint(200, 300)
        # Random y-parameter for planets
        self.y = random.randint(120, 150)
        self.image = PLANET_THREE
        self.width = self.image.get_width()

    def update(self):
        # Moving planet from right to left
        self.x -= game_speed
        if self.x < -self.width:
            self.x = GUI_WIDTH + random.randint(100, 120)
            self.y = random.randint(80, 150)

    def draw(self, GUI):
        GUI.blit(self.image, (self.x, self.y))


class Obstacles:
    def __init__(self, image, type):  # type
        self.image = image
        # If you got hella nemesis we put type on here
        # Since I'm using just one then one is enough
        self.type = type
        self.hit = self.image.get_rect()
        self.hit.x = GUI_WIDTH

    def update(self):
        self.hit.x -= game_speed_two
        # To remove the obstacle from the left hand side
        if self.hit.x < -self.hit.width:
            obstacles.pop()

    def draw(self, GUI):
        GUI.blit(self.image, self.hit)


class Glob(Obstacles):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.hit.y = 325


class Idk(Obstacles):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.hit.y = 270


def main():
    global game_speed, game_speed_two, bg_pos_x, bg_pos_y, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dave()
    planet = Planet()
    planetTwo = PlanetTwo()
    planetThree = PlanetThree()
    points = 0
    game_speed = 5
    game_speed_two = 20
    bg_pos_x = 0
    bg_pos_y = 380
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    # Score method to increment the speed by one unit
    # For everyone 100 points scored
    def score():
        global points, game_speed_two
        points += 1
        if points % 100 == 0:
            game_speed_two += 1
        text = font.render("Yo Score: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (810, 40)
        GUI.blit(text, textRect)

    def background():
        global bg_pos_x, bg_pos_y
        image_width = BACKGROUND.get_width()
        GUI.blit(BACKGROUND, (bg_pos_x, bg_pos_y))
        GUI.blit(BACKGROUND, (image_width + bg_pos_x, bg_pos_y))
        # Whenever a background image is move off the gui another background is created
        # infinite loop of background basically
        if bg_pos_x <= -image_width:
            GUI.blit(BACKGROUND, (image_width + bg_pos_x, bg_pos_y))
            bg_pos_x = 0
        bg_pos_x -= game_speed_two

    # To exit to game when tapping the exit button
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Filling the screen with the color white
        GUI.fill('pink')

        # Getting user input from keyboard
        user_input = pygame.key.get_pressed()

        # Draw and update the dave on the screen
        player.draw(GUI)
        player.update(user_input)

        # Draw obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Glob(GLOB))
            else:
                obstacles.append((Idk(IDK)))

        for obstacle in obstacles:
            obstacle.draw(GUI)
            obstacle.update()
            if player.dave_hit.colliderect(obstacle.hit):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        # Draw planet and background
        planet.draw(GUI)
        planet.update()

        planetTwo.draw(GUI)
        planetTwo.update()

        planetThree.draw(GUI)
        planetThree.update()

        background()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        GUI.fill('pink')
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press Any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press Any Key to Start", True, (0, 0, 0))
            score = font.render("Yo Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (GUI_WIDTH // 2, GUI_HEIGHT // 2 + 90)
            GUI.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (GUI_WIDTH // 2, GUI_HEIGHT // 2 + 40)
        GUI.blit(text, textRect)
        GUI.blit(DAVE, (GUI_WIDTH // 2 - 50, GUI_HEIGHT // 2 - 120))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)
