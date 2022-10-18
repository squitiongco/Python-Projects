import pygame 

screen_size = width, height = 400, 800

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    fps = 3
    
    window_closed = False
    
    while not window_closed: 
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_closed = True
                
        pygame.display.flip()
        clock.tick(fps)
        
    pygame.quit()
    
    # React to the user's actions. 
    
    # Display score to the user. 
    
    # Close window when user quits. 