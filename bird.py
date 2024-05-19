import random
import pygame
import pygame.freetype

# Ініціалізація Pygame та налаштування годинника
pygame.init()
clock = pygame.time.Clock()

# Створення вікна гри
screen = pygame.display.set_mode((1000, 600))
background = pygame.transform.scale(pygame.image.load('background.png'), (1000, 600))
pygame.display.set_caption('Flappy Bird')

# Завантаження графіки для пташки та перешкод
bird_image = pygame.image.load('bird2.png')
wall_image = pygame.image.load('pipe.png')

# Зміна розмірів графіки для пташки та перешкод
bird_image = pygame.transform.scale(bird_image, (80, 60))
wall_image = pygame.transform.scale(wall_image, (100, 500))

# Визначення початкової позиції пташки
bird_rect = bird_image.get_rect()
bird_rect.center = (300, 300)
font = pygame.freetype.Font(None, 30)

# Початкова швидкість пташки та значення гравітації та стрибка
bird_speed = 0
gravity = 0.5
jump = 5

wall_group = pygame.sprite.Group()
spawn_wall_event = pygame.USEREVENT
pygame.time.set_timer(spawn_wall_event, 1000)

score = 0
game_status = 'game'

# Клас для представлення перешкод
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        global game_status, score
        self.rect.x -= 10
        # Перевірка колізії з пташкою
        if self.rect.colliderect(bird_rect):
            game_status = 'menu'
        # Перевірка, чи пташка успішно пролетіла перешкоду
        elif self.rect.right < bird_rect.left and not hasattr(self, 'scored'):
            score += 1
            self.scored = True


running = True

while running:
    for event in pygame.event.get():
        # Обробка подій користувача
        if event.type == pygame.QUIT:
            running = False
        # Створення нових перешкод та додавання їх до групи
        if event.type == spawn_wall_event:
            wall = Wall((1050, random.choice([-50, -100, -150])), wall_image)
            wall_group.add(wall)
            wall = Wall((1050, random.choice([650, 700, 750])), wall_image)
            wall_group.add(wall)

    screen.fill((100, 100, 100))
    
    if game_status == 'game':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bird_speed = -jump
        else:
            bird_speed += gravity
        bird_rect.centery += int(bird_speed)

        # Додайте умову для перевірки виходу за межі екрану
        if bird_rect.bottom > 600:  # 600 - висота екрану
            game_status = 'menu'
        
        # Відображення фону, пташки та перешкод
        screen.blit(background, (0, 0))
        screen.blit(bird_image, bird_rect)
        wall_group.update()
        wall_group.draw(screen)

        # Відображення рахунку
        font.render_to(screen, (10, 10), f'Score: {score//2}', (255, 255, 255))
    else:
        font.render_to(screen, (300, 300), 'Game over', (200, 0, 0))

    pygame.display.flip()
    clock.tick(60)



# import random
# import pygame
# import pygame.freetype

# 
# pygame.init()
# clock = pygame.time.Clock()

# 
# screen = pygame.display.set_mode((1000, 600))
# background = pygame.transform.scale(pygame.image.load('background.png'), (1000, 600))
# pygame.display.set_caption('Flappy Bird')

# 
# bird_image = pygame.image.load('bird.png')
# wall_image = pygame.image.load('pipe.png')

# 
# bird_image = pygame.transform.scale(bird_image, (80, 60))
# wall_image = pygame.transform.scale(wall_image, (100, 500))

# 
# bird_rect = bird_image.get_rect()
# bird_rect.center = (300, 300)

# # Налаштування шрифту для відображення рахунку
# font = pygame.freetype.Font(None, 30)

# 
# bird_speed = 0
# gravity = 0.5
# jump = 5

# # Створення групи для перешкод
# wall_group = pygame.sprite.Group()

# # Встановлення таймера для спавну перешкод
# spawn_wall_event = pygame.USEREVENT
# pygame.time.set_timer(spawn_wall_event, 1000)

# # Ініціалізація змінних для рахунку та статусу гри
# score = 0
# game_status = 'game'


# 
# class Wall(pygame.sprite.Sprite):
#     def init(self, pos, image):
#         super().init()
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.rect.center = pos

#     def update(self):
#         global game_status, score
#         # Рух перешкоди вліво
#         self.rect.x -= 10
#         
#         if self.rect.colliderect(bird_rect):
#             game_status = 'menu'
#         
#         elif self.rect.right < bird_rect.left and not hasattr(self, 'scored'):
#             score += 1
#             self.scored = True


# running = True

# while running:
#     for event in pygame.event.get():
#         # Обробка подій користувача
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == spawn_wall_event:
#             # Створення нових перешкод та додавання їх до групи
#             wall = Wall((1050, random.choice([-50, -100, -150])), wall_image)
#             wall_group.add(wall)
#             wall = Wall((1050, random.choice([650, 700, 750])), wall_image)
#             wall_group.add(wall)

#     # Заповнення екрану фоновим кольором
#     screen.fill((100, 100, 100))

#     # Логіка гри
#     if game_status == 'game':
#         keys = pygame.key.get_pressed()
#         # Обробка стрибка пташки
#         if keys[pygame.K_SPACE]:
#             bird_speed = -jump
#         else:
#             bird_speed += gravity
#         bird_rect.centery += int(bird_speed)

#         # Відображення фону, пташки та перешкод
#         screen.blit(background, (0, 0))
#         screen.blit(bird_image, bird_rect)
#         wall_group.update()
#         wall_group.draw(screen)

#         # Відображення рахунку
#         font.render_to(screen, (10, 10), f'Score: {score // 2}', (255, 255, 255))
#     else:
#         # Відображення напису "Гра закінчена" при завершенні гри
#         font.render_to(screen, (300, 300), 'Гра закінчена', (200, 0, 0))

#     # Оновлення екрану
#     pygame.display.flip()
#     clock.tick(60)