import pygame
import random




def start_game():
    pygame.init()


    screen_width = 800
    screen_height = 600
    player_size = 50
    player_speed = 4
    bullet_speed = 2
    enemy_size = 50
    enemy_speed = 0.2
    danger_size = 49
    danger_speed = 3

    white = (255, 255, 255)


    background_image = pygame.image.load("galaxy.jpg")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


    player_image = pygame.image.load("rocket.png")
    player_image = pygame.transform.scale(player_image, (player_size, player_size))

    bullet_image = pygame.image.load("bullet.png")
    bullet_image = pygame.transform.scale(bullet_image, (5, 10))

    enemy_image = pygame.image.load("asteroid.png")
    enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))




    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Шутер ")


    player = pygame.Rect(screen_width // 2 - player_size // 2, screen_height - player_size - 10, player_size, player_size)


    bullets = []


    enemies = []


    score = 0
    font = pygame.font.Font(None, 36)


    def draw_score():
        score_text = font.render("Score: " + str(score), True, white)
        screen.blit(score_text, (10, 10))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < screen_width:
            player.x += player_speed


        if keys[pygame.K_SPACE]:
            bullet = pygame.Rect(player.centerx - 2, player.top - 10, 5, 10)
            bullets.append(bullet)


        bullets = [bullet for bullet in bullets if bullet.y > 0]
        for bullet in bullets:
            bullet.y -= bullet_speed


        if random.randint(0, 200) < 2:
            enemy = pygame.Rect(random.randint(0, screen_width - enemy_size), 0, enemy_size, enemy_size)
            enemies.append(enemy)




        if random.randint(0, 200) < 2:
            danger = pygame.Rect(random.randint(0, screen_width - danger_size), 50, danger_size, danger_size)
            enemies.append(danger)


        for enemy in enemies:
            enemy.y += enemy_speed


        for enemy1 in enemies:
            enemy1.y += danger_speed
        enemies = [danger for danger in enemies if danger.y < screen_height]


        for bullet in bullets:
            for enemy in enemies:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1


        for enemy in enemies:
            if player.colliderect(enemy):
                running = False



        for enemy1 in enemies:
            if player.colliderect(enemy1):
                running = False

        screen.blit(background_image, (0, 0))


        screen.blit(player_image, player.topleft)


        for bullet in bullets:
            screen.blit(bullet_image, bullet.topleft)



        for enemy in enemies:
            screen.blit(enemy_image, enemy.topleft)





        draw_score()


        pygame.display.flip()


    pygame.time.Clock().tick(60)

    pygame.quit()
