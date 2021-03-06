"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
from Ball import ball

class TestBallSetPaddleY( unittest.TestCase ):

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

    def test001_LeftPaddleValidYIsSet( self ):
        min_y = 313
        max_y = 363
        self.constructed_ball.setLeftPaddleY( min_y, max_y )
        self.assertEqual( self.constructed_ball.getLeftPaddleMinY( ), min_y )
        self.assertEqual( self.constructed_ball.getLeftPaddleMaxY( ), max_y )
        return
    
    def test002_RightPaddleValidYIsSet( self ):
        min_y = 413
        max_y = 463
        self.constructed_ball.setRightPaddleY( min_y, max_y )
        self.assertEqual( self.constructed_ball.getRightPaddleMinY( ), min_y )
        self.assertEqual( self.constructed_ball.getRightPaddleMaxY( ), max_y )
        return

    def test003_LeftPaddleInvalidLowYIsNotSet( self ):
        min_y = 199
        max_y = 363
        self.constructed_ball.setLeftPaddleY( min_y, max_y )
        self.assertNotEqual( self.constructed_ball.getLeftPaddleMinY( ), min_y )
        self.assertNotEqual( self.constructed_ball.getLeftPaddleMaxY( ), max_y )
        return
    
    def test004_LeftPaddleInvalidHighYIsNotSet( self ):
        min_y = 363
        max_y = 801
        self.constructed_ball.setLeftPaddleY( min_y, max_y )
        self.assertNotEqual( self.constructed_ball.getLeftPaddleMinY( ), min_y )
        self.assertNotEqual( self.constructed_ball.getLeftPaddleMaxY( ), max_y )
        return
    
    def test005_RightPaddleInvalidLowYIsNotSet( self ):
        min_y = 199
        max_y = 363
        self.constructed_ball.setRightPaddleY( min_y, max_y )
        self.assertNotEqual( self.constructed_ball.getRightPaddleMinY( ), min_y )
        self.assertNotEqual( self.constructed_ball.getRightPaddleMaxY( ), max_y )
        return
    
    def test006_RightPaddleInvalidHighYIsNotSet( self ):
        min_y = 363
        max_y = 801
        self.constructed_ball.setRightPaddleY( min_y, max_y )
        self.assertNotEqual( self.constructed_ball.getRightPaddleMinY( ), min_y )
        self.assertNotEqual( self.constructed_ball.getRightPaddleMaxY( ), max_y )
        return
    
    def test007_LeftPaddleInvertedYIsNotSet( self ):
        min_y = 363
        max_y = 263
        self.constructed_ball.setLeftPaddleY( min_y, max_y )
        self.assertNotEqual( self.constructed_ball.getLeftPaddleMinY( ), min_y )
        self.assertNotEqual( self.constructed_ball.getLeftPaddleMaxY( ), max_y )
        return
    
    def test008_RightPaddleInvertedYIsNotSet( self ):
        min_y = 363
        max_y = 263
        self.constructed_ball.setRightPaddleY( min_y, max_y )
        self.assertNotEqual( self.constructed_ball.getRightPaddleMinY( ), min_y )
        self.assertNotEqual( self.constructed_ball.getRightPaddleMaxY( ), max_y )
        return

    def test009_LeftPaddleValidLowYIsSet( self ):
        min_y = 200
        max_y = 363
        self.constructed_ball.setLeftPaddleY( min_y, max_y )
        self.assertEqual( self.constructed_ball.getLeftPaddleMinY( ), min_y )
        self.assertEqual( self.constructed_ball.getLeftPaddleMaxY( ), max_y )
        return
    
    def test010_LeftPaddleValidHighYIsSet( self ):
        min_y = 363
        max_y = 800
        self.constructed_ball.setLeftPaddleY( min_y, max_y )
        self.assertEqual( self.constructed_ball.getLeftPaddleMinY( ), min_y )
        self.assertEqual( self.constructed_ball.getLeftPaddleMaxY( ), max_y )
        return
    
    def test011_RightPaddleValidLowYIsSet( self ):
        min_y = 200
        max_y = 363
        self.constructed_ball.setRightPaddleY( min_y, max_y )
        self.assertEqual( self.constructed_ball.getRightPaddleMinY( ), min_y )
        self.assertEqual( self.constructed_ball.getRightPaddleMaxY( ), max_y )
        return
    
    def test012_RightPaddleValidHighYIsSet( self ):
        min_y = 363
        max_y = 800
        self.constructed_ball.setRightPaddleY( min_y, max_y )
        self.assertEqual( self.constructed_ball.getRightPaddleMinY( ), min_y )
        self.assertEqual( self.constructed_ball.getRightPaddleMaxY( ), max_y )
        return
    
    
def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestBallSetPaddleY )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
