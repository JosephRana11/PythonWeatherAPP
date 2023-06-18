import pygame
from sys import exit
import Weather

print(Weather.main_weather)

pygame.init()
screen_width = 300
screen_height = 550
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption('WeatherX')

pygame.mixer.music.load('music\kiki.wav')
pygame.mixer.music.play(-1,0,2000)


test_font1 = pygame.font.Font('venv\pixeled\Pixeled.ttf' , 10)
text_1 = test_font1.render('WeatherX' , True , 'Green')
text1_rect = text_1.get_rect(center = (150,50))

test_font2 = pygame.font.Font('venv\pixeled\Pixeled.ttf' , 15)
text_2 = test_font2.render(f'Today:{Weather.main_weather}', False , 'Black')
text_2_rect = text_2.get_rect(center = (150,107))

test_font3 = pygame.font.Font('venv\pixeled\Pixeled.ttf' , 10)
text_3 = test_font3.render(f'Max Temp:{Weather.rounded_max_cel}C', False , 'Red')
text_3_rect = text_3.get_rect(center = (150,150))

test_font4 = pygame.font.Font('venv\pixeled\Pixeled.ttf' , 10)
text_4 = test_font4.render(f'Max Temp:{Weather.rounded_min_cel}C', False , 'Blue')
text_4_rect = text_4.get_rect(center = (150,180))

test_font5 = pygame.font.Font('venv\pixeled\Pixeled.ttf' , 10)
text_5 = test_font4.render('Location : Lalitpur,NP', False , 'Black')
text_5_rect = text_5.get_rect(center = (150,75))

test_font6 = pygame.font.Font('venv\pixeled\Pixeled.ttf' , 10)
text_6 = test_font4.render('By Joseph Rana', False , 'Yellow')
text_6_rect = text_5.get_rect(center = (250,520))

background1 = pygame.image.load('venv/city_assets/city 1/10.png')
background1_rework = pygame.transform.scale(background1, (screen_width+400, screen_height)).convert_alpha()
background2 = pygame.image.load('venv/city_assets/city 2/10.png')
background2_rework = pygame.transform.scale(background2, (screen_width+400, screen_height)).convert_alpha()

second_screen = False
first_screen = True
alpha1 = 0
alpha2 =  0
alpha_weatherx = 0


switch = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if second_screen == True:
                second_screen = False
                alpha2 = 0

            else:
                second_screen = True

    background2_rework.set_alpha(alpha2)
    background1_rework.set_alpha(alpha1)
    if first_screen :
        alpha1 += 1
        screen.blit(background1_rework, (-70, 0))
    if second_screen:
        alpha2 += 1
        screen.blit(background2_rework, (0,0))
    text_1.set_alpha(alpha_weatherx)
    if alpha_weatherx < 255:
      alpha_weatherx = alpha_weatherx+1
    screen.blit(text_1, text1_rect)
    screen.blit(text_2, text_2_rect)
    screen.blit(text_3 , text_3_rect)
    screen.blit(text_4 , text_4_rect)
    screen.blit(text_5 , text_5_rect)
    screen.blit(text_6 ,  text_6_rect)

    pygame.display.update()
