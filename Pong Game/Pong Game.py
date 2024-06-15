import pygame  # is a set of Python modules designed for writing video games
import random  # provides functions to generate random numbers.

SCREEN_WIDTH = 960  # Defines the width of the game window in pixels.
SCREEN_HEIGHT = 720
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():
    # ---------Setting up the environment--------------

    pygame.init()  # Initializes all the Pygame modules. This is necessary before using any other Pygame functions

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Sets up the game window with the specified width and height
    pygame.display.set_caption('PONG')  # Sets the title of the game window to "Pong".

    clock = pygame.time.Clock()  # Creates a clock object to help control the frame rate of the game
    started = False

    # creates rectangular paddles to play (x-coordinate, y-coordinate, width, height)
    paddle_left_rect = pygame.Rect(30, SCREEN_HEIGHT / 2 - 50, 7, 100)
    paddle_right_rect = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT / 2 - 50, 7, 100)
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)  # the pong ball

    # creates the movement speed of the paddle to zero
    paddle_left_move = 0
    paddle_right_move = 0

    # create a random speed for the ball
    ball_accel_x = random.choice([-1, 1]) * random.randint(2, 4) * 0.1  # Sets the horizontal speed of the ball to a random value between 0.2 and 0.4, with a random direction (left or right).
    ball_accel_y = random.choice([-1, 1]) * random.randint(2, 4) * 0.1

    # ------Setting up the game-------

    while True:
        screen.fill(COLOR_BLACK)

        for event in pygame.event.get():  # Iterates over all events in the event queue.
            if event.type == pygame.QUIT:  # Checks if the event is a quit event (like closing the window).
                pygame.quit()  # Quits all Pygame modules.
                return
            if event.type == pygame.KEYDOWN:  # Checks if a key has been pressed down.
                if event.key == pygame.K_SPACE:  # Checks if the space key is pressed to start the game.
                    started = True  # sets the game state to started
                if event.key == pygame.K_w:  # Checks if the 'W' key is pressed to move the first paddle up.
                    paddle_left_move = -0.5  # Sets the first paddle's movement speed to negative (up).
                if event.key == pygame.K_s:  # Checks if the 'S' key is pressed to move the first paddle down.
                    paddle_left_move = 0.5
                if event.key == pygame.K_UP:  # Checks if the up arrow key is pressed to move the second paddle up.
                    paddle_right_move = -0.5
                if event.key == pygame.K_DOWN:  # Checks if the down arrow key is pressed to move the second paddle down.
                    paddle_right_move = 0.5
            if event.type == pygame.KEYUP:  # Checks if a key has been released.
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_left_move = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_right_move = 0.0

        delta_time = clock.tick(60)  # Limits the game loop to run at 60 frames per second and returns the time (in milliseconds) since the last tick

        if not started:
            font = pygame.font.SysFont('Consolas', 30)  # Creates a font object with the 'Consolas' font and size 30.
            text = font.render('Press Space to Start', True, COLOR_WHITE)
            text_rect = text.get_rect()  # Gets the rectangle of the rendered text.
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Centers the text on the screen.
            screen.blit(text, text_rect)  # Draws the text on the screen at the specified position.
        else:  # Executes if the game has started.
            paddle_left_rect.top += paddle_left_move * delta_time  # Moves the first paddle vertically based on its speed and delta time.
            paddle_right_rect.top += paddle_right_move * delta_time #Moves the second paddle vertically based on its speed and delta time.

            if paddle_left_rect.top < 0:    # Checks if the first paddle is going above the top edge of the screen.
                paddle_left_rect.top = 0
            if paddle_right_rect.top < 0:   # Checks if the second paddle is going above the top edge of the screen.
                paddle_right_rect.top = 0
            if paddle_left_rect.bottom > SCREEN_HEIGHT: # Checks if the first paddle is going below the bottom edge of the screen.
                paddle_left_rect.bottom = SCREEN_HEIGHT
            if paddle_right_rect.bottom > SCREEN_HEIGHT:
                paddle_right_rect.bottom = SCREEN_HEIGHT
            if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT: # Checks if the ball hits the top or bottom edge of the screen.
                ball_accel_y *= -1  # Reverses the vertical direction of the ball.
            if ball_rect.left <= 0 or ball_rect.right >= SCREEN_WIDTH: # Checks if the ball goes past the left or right edge of the screen (a player scores).
                started = False
                ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                ball_accel_x = random.choice([-1, 1]) * random.randint(2, 4) * 0.1
                ball_accel_y = random.choice([-1, 1]) * random.randint(2, 4) * 0.1
            if paddle_left_rect.colliderect(ball_rect) and ball_accel_x < 0:    # Checks if the ball collides with the first paddle and is moving left.
                ball_accel_x *= -1  # Reverses the horizontal direction of the ball.
                ball_rect.left = paddle_left_rect.right # Adjusts the ball position to avoid sticking into the paddle.
            if paddle_right_rect.colliderect(ball_rect) and ball_accel_x > 0:   # Checks if the ball collides with the second paddle and is moving right.
                ball_accel_x *= -1
                ball_rect.right = paddle_right_rect.left    #  Adjusts the ball position to avoid sticking into the paddle.

            ball_rect.left += ball_accel_x * delta_time # Moves the ball horizontally based on its speed and delta time.
            ball_rect.top += ball_accel_y * delta_time

            pygame.draw.rect(screen, COLOR_WHITE, paddle_left_rect) # Draws the first paddle on the screen.
            pygame.draw.rect(screen, COLOR_WHITE, paddle_right_rect)    # Draws the second paddle on the screen.
            pygame.draw.rect(screen, COLOR_WHITE, ball_rect)    # Draws the ball on the screen.

        pygame.display.flip()   #  Updates the full display surface to the screen, making everything drawn visible.

if __name__ == '__main__':
    main()