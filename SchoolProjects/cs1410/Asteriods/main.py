import pygame, game, asteroids


TITLE = "Asteriods"
# pixels width
WINDOW_WIDTH  = 1190
# pixels high
WINDOW_HEIGHT = 1190
# frames per second
DESIRED_RATE  = 30

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )

        self.mGame = asteroids.Asteroids(width, height)
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):

        if pygame.K_a in newkeys:
            self.mGame.actOnPressA( )

        elif pygame.K_a in keys:
            self.mGame.actOnHoldA( )

        if pygame.K_UP in newkeys:
            self.mGame.accelerateShip(10)
        elif pygame.K_UP in keys:
            self.mGame.accelerateShip(10)

        if pygame.K_RIGHT in newkeys:
            self.mGame.mShip.rotate(5)
        elif pygame.K_RIGHT in keys:
            self.mGame.mShip.rotate(5)

        if pygame.K_LEFT in newkeys:
            self.mGame.mShip.rotate(-5)
        elif pygame.K_LEFT in keys:
            self.mGame.mShip.rotate(-5)

        if pygame.K_DOWN in newkeys:
            self.mGame.accelerateShip(-10)

        if pygame.K_SPACE in newkeys:
            self.mGame.fire()

        if pygame.K_0 in newkeys:
            self.mGame.mShip.fire()

        self.mGame.evolve(dt)

        return
    
    def paint( self, surface ):
        # Draw the current state of the game instance
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
