import pygame, sys, time

#initialize pygame so that we can use all of the built in function in the pygame library

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

#declare font
myriadProFont = pygame.font.SysFont("myriadProFont", 48)

helloWorldText = myriadProFont.render("hello world", 1, (240,230,140),(255,255,255))

x,y = 0,0

#stop pie game from running
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  #blit function actually displays something on screen
  screen.blit(helloWorldText, (x,y))

   #if we are moving things across the screen, it would look more natural
  pygame.display.update()