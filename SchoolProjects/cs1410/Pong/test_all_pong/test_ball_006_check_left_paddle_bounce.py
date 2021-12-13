"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
from Ball import ball

class TestBallCheckPaddleBounce( unittest.TestCase ):

    def setUp( self ):
        self.expected_x = 0
        self.expected_y = 0
        self.expected_size = 13
        self.expected_dx = 0
        self.expected_dy = 0
        self.expected_min_x = 100
        self.expected_max_x = 900
        self.expected_min_y = 200
        self.expected_max_y = 800
        self.expected_left_paddle_x = 150
        self.expected_left_paddle_min_y = self.expected_min_y
        self.expected_left_paddle_max_y = self.expected_max_y
        self.expected_right_paddle_x = 850
        self.expected_right_paddle_min_y = self.expected_min_y
        self.expected_right_paddle_max_y = self.expected_max_y

        self.constructed_ball = ball.Ball( self.expected_size, self.expected_min_x, self.expected_max_x, self.expected_min_y, self.expected_max_y, self.expected_left_paddle_x, self.expected_right_paddle_x )
        
        return

    def tearDown( self ):
        return

    def test001_bouncesFromLeftPaddle( self ):
        paddle_min_y = 400
        paddle_max_y = 450

        ball_x = 155
        ball_y = 420
        ball_new_x = 142
        ball_new_y = 435
        ball_dx = -13
        ball_dy = 15
        expected_x = 158
        expected_dx = 13

        self.constructed_ball.setLeftPaddleY( paddle_min_y, paddle_max_y )
        self.constructed_ball.setPosition( ball_x, ball_y )
        self.constructed_ball.setSpeed( ball_dx, ball_dy )
        
        actual_x = self.constructed_ball.checkLeftPaddle( ball_new_x, ball_new_y )
        
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getX( ), ball_x )
        self.assertEqual( self.constructed_ball.getY( ), ball_y )
        self.assertEqual( self.constructed_ball.getDY( ), ball_dy )
        return
    
    def test002_doesNotBounceFromLeftPaddleDueToHighX( self ):
        paddle_min_y = 400
        paddle_max_y = 450

        ball_x = 175
        ball_y = 420
        ball_new_x = 162
        ball_new_y = 435
        ball_dx = -13
        ball_dy = 15
        expected_x = 162
        expected_dx = -13

        self.constructed_ball.setLeftPaddleY( paddle_min_y, paddle_max_y )
        self.constructed_ball.setPosition( ball_x, ball_y )
        self.constructed_ball.setSpeed( ball_dx, ball_dy )
        
        actual_x = self.constructed_ball.checkLeftPaddle( ball_new_x, ball_new_y )
        
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getX( ), ball_x )
        self.assertEqual( self.constructed_ball.getY( ), ball_y )
        self.assertEqual( self.constructed_ball.getDY( ), ball_dy )
        return
    
    def test003_doesNotBounceFromLeftPaddleDueToLowX( self ):
        paddle_min_y = 400
        paddle_max_y = 450

        ball_x = 145
        ball_y = 420
        ball_new_x = 132
        ball_new_y = 435
        ball_dx = -13
        ball_dy = 15
        expected_x = 132
        expected_dx = -13

        self.constructed_ball.setLeftPaddleY( paddle_min_y, paddle_max_y )
        self.constructed_ball.setPosition( ball_x, ball_y )
        self.constructed_ball.setSpeed( ball_dx, ball_dy )
        
        actual_x = self.constructed_ball.checkLeftPaddle( ball_new_x, ball_new_y )
        
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getX( ), ball_x )
        self.assertEqual( self.constructed_ball.getY( ), ball_y )
        self.assertEqual( self.constructed_ball.getDY( ), ball_dy )
        return
    
    def test004_doesNotBounceFromLeftPaddleDueToHighY( self ):
        paddle_min_y = 400
        paddle_max_y = 450

        ball_x = 155
        ball_y = 441
        ball_new_x = 145
        ball_new_y = 461
        ball_dx = -13
        ball_dy = 20
        expected_x = 145
        expected_dx = -13

        self.constructed_ball.setLeftPaddleY( paddle_min_y, paddle_max_y )
        self.constructed_ball.setPosition( ball_x, ball_y )
        self.constructed_ball.setSpeed( ball_dx, ball_dy )
        
        actual_x = self.constructed_ball.checkLeftPaddle( ball_new_x, ball_new_y )
        
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getX( ), ball_x )
        self.assertEqual( self.constructed_ball.getY( ), ball_y )
        self.assertEqual( self.constructed_ball.getDY( ), ball_dy )
        return
    
    def test005_doesNotBounceFromLeftPaddleDueToLowY( self ):
        paddle_min_y = 400
        paddle_max_y = 450

        ball_x = 155
        ball_y = 409
        ball_new_x = 145
        ball_new_y = 389
        ball_dx = -13
        ball_dy = -20
        expected_x = 145
        expected_dx = -13

        self.constructed_ball.setLeftPaddleY( paddle_min_y, paddle_max_y )
        self.constructed_ball.setPosition( ball_x, ball_y )
        self.constructed_ball.setSpeed( ball_dx, ball_dy )
        
        actual_x = self.constructed_ball.checkLeftPaddle( ball_new_x, ball_new_y )
        
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getX( ), ball_x )
        self.assertEqual( self.constructed_ball.getY( ), ball_y )
        self.assertEqual( self.constructed_ball.getDY( ), ball_dy )
        return
    
def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestBallCheckPaddleBounce )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )

