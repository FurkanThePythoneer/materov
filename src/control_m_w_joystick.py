import time
import os
import sys
import pygame

pygame.display.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()


        
if __name__ == '__main__':
    print('Starting...')

    while True:

        # Get next pygame event
        pygame.event.pump()

        name = controller.get_name()
        
        axes = []
        for k in range(controller.get_numaxes()):
            axes.append(controller.get_axis(k))

        buttons = []
        for k in range(controller.get_numbuttons()):
            buttons.append(controller.get_button(k))
        
        print('Axes: {} Buttons: {} '.format(axes, buttons), end='')
        print('\n')


