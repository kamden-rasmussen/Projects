"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
from Ball import ball

class TestBallConstructor( unittest.TestCase ):

    def setUp( self ):
        self.expected_x = 100
        self.expected_y = 200
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

    def test001_XIsSet( self ):
        self.assertEqual( self.constructed_ball.getX( ), self.expected_x )
        return
    
    def test002_YIsSet( self ):
        self.assertEqual( self.constructed_ball.getY( ), self.expected_y )
        return
    
    def test003_SizeIsSet( self ):
        self.assertEqual( self.constructed_ball.getSize( ), self.expected_size )
        return
    
    def test004_DXIsSet( self ):
        self.assertEqual( self.constructed_ball.getDX( ), self.expected_dx )
        return
    
    def test005_DYIsSet( self ):
        self.assertEqual( self.constructed_ball.getDY( ), self.expected_dy )
        return
    
    def test006_MinXIsSet( self ):
        self.assertEqual( self.constructed_ball.getMinX( ), self.expected_min_x )
        return
    
    def test007_MaxXIsSet( self ):
        self.assertEqual( self.constructed_ball.getMaxX( ), self.expected_max_x )
        return
    
    def test008_MinYIsSet( self ):
        self.assertEqual( self.constructed_ball.getMinY( ), self.expected_min_y )
        return
    
    def test009_MaxYIsSet( self ):
        self.assertEqual( self.constructed_ball.getMaxY( ), self.expected_max_y )
        return
    
    def test010_LeftPaddleXIsSet( self ):
        self.assertEqual( self.constructed_ball.getLeftPaddleX( ), self.expected_left_paddle_x )
        return
    
    def test011_LeftPaddleMinYIsSet( self ):
        self.assertEqual( self.constructed_ball.getLeftPaddleMinY( ), self.expected_left_paddle_min_y )
        return
    
    def test012_LeftPaddleMaxYIsSet( self ):
        self.assertEqual( self.constructed_ball.getLeftPaddleMaxY( ), self.expected_left_paddle_max_y )
        return
    
    def test013_RightPaddleXIsSet( self ):
        self.assertEqual( self.constructed_ball.getRightPaddleX( ), self.expected_right_paddle_x )
        return

    def test014_RightPaddleMinYIsSet( self ):
        self.assertEqual( self.constructed_ball.getRightPaddleMinY( ), self.expected_right_paddle_min_y )
        return
    
    def test015_RightPaddleMaxYIsSet( self ):
        self.assertEqual( self.constructed_ball.getRightPaddleMaxY( ), self.expected_right_paddle_max_y )
        return

def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestBallConstructor )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )