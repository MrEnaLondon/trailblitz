# Example file showing a circle moving on screen
import pygame

pygame.init()

#SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0]
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800

# pygame setup
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


background_color = "grey"
#Вова дописал отрисовку полигона

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)

    pygame.draw.polygon(screen, "black", [(screen.get_width() *11 / 12, screen.get_height() / 4),(screen.get_width() / 12, screen.get_height() / 4),(screen.get_width() / 12, screen.get_height() *3 / 4),(screen.get_width() *11/ 12, screen.get_height() *3 / 4)])
    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.polygon(screen, "white", [(screen.get_width() / 12, screen.get_height() * 5 / 12),(screen.get_width() / 6, screen.get_height() / 2),(screen.get_width() / 3, screen.get_height() / 4),(screen.get_width() / 2, screen.get_height() / 2),(screen.get_width() * 2 / 3, screen.get_height() / 4),(screen.get_width() * 5 / 6, screen.get_height() / 2),(screen.get_width() *11 / 12, screen.get_height() * 5 / 12),
                                          (screen.get_width() * 11 / 12, screen.get_height() / 4),(screen.get_width() * 2 / 3, screen.get_height() / 2),(screen.get_width() / 2, screen.get_height() / 3),(screen.get_width() / 3, screen.get_height() / 2),(screen.get_width() / 12, screen.get_height() / 4),])
    pygame.draw.polygon(screen, "white", [(screen.get_width() / 12, screen.get_height() * 7 / 12),(screen.get_width() / 6, screen.get_height() / 2),(screen.get_width() / 3, screen.get_height() * 3 / 4),(screen.get_width() / 2, screen.get_height() / 2),(screen.get_width() * 2 / 3, screen.get_height() * 3 / 4),(screen.get_width() * 5 / 6, screen.get_height() / 2),(screen.get_width() *11 / 12, screen.get_height() * 7 / 12),
                                          (screen.get_width() * 11 / 12, screen.get_height() *3/ 4),(screen.get_width() * 2 / 3, screen.get_height() / 2),(screen.get_width() / 2, screen.get_height() *2/ 3),(screen.get_width() / 3, screen.get_height() / 2),(screen.get_width() / 12, screen.get_height() *3/ 4),])



    player_pos.x, player_pos.y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
         running = False
    if keys[pygame.K_q]:
        background_color = "purple"


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30)/1000

pygame.quit()