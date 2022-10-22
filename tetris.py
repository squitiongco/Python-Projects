import pygame 

from game import Game 

screen_size = width, height = 400, 650

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    fps = 3
    
    window_closed = False
    
    game = Game(screen)
    
    while not window_closed: 
        screen.fill((0, 0, 0))
        
        if game.is_over:
            font = pygame.font.SysFont('Calibri', 18, True, False)
            text = font.render("Press enter to start the game", True, (255, 255, 255))
            screen.blit(text, [80, height // 2 + 40])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      window_closed = True
                      
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game.reset()
        
        else:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    window_closed = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game.rotate()
                        
                    elif event.key == pygame.K_LEFT:
                        game.move_left()
                        
                    elif event.key == pygame.K_RIGHT:
                        game.move_right()
                        
            game.update()
            game.render()
        
        pygame.display.flip()
        clock.tick(fps)
        
    pygame.quit()
       
        
    # Display score to the user. 
    
    # Close window when user quits. 