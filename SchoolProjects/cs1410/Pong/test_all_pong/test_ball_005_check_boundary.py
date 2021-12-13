"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
from Ball import ball

class TestBallCheckBoundary( unittest.TestCase ):

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

    def test001_checkTopBouncesY( self ):
        # bounce off of the top
        x = 450
        y = 210
        dx = -10
        dy = -5
        new_y = 197
        expected_y = 203
        expected_dx = -10
        expected_dy = 5
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkTop( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test001a_checkTopBouncesY( self ):
        # bounce off of the top
        x = 450
        y = 250
        dx = -10
        dy = -51
        new_y = 199
        expected_y = 201
        expected_dx = -10
        expected_dy = 51
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkTop( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test001b_checkTopBouncesY( self ):
        # bounce off of the top
        x = 450
        y = 202
        dx = -10
        dy = -3
        new_y = 199
        expected_y = 201
        expected_dx = -10
        expected_dy = 3
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkTop( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test002_checkTopDoesNotBounceY( self ):
        # new y doesn't warrent a bounce
        x = 450
        y = 210
        dx = -10
        dy = -5
        new_y = 204
        expected_y = 204
        expected_dx = -10
        expected_dy = -5
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkTop( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return

    def test002a_checkTopDoesNotBounceY( self ):
        # 
        x = 450
        y = 250
        dx = -10
        dy = -49
        new_y = 201
        expected_y = 201
        expected_dx = -10
        expected_dy = -49
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkTop( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test002b_checkTopDoesNotBounceY( self ):
        # bounce off of the top
        x = 450
        y = 202
        dx = -10
        dy = -1
        new_y = 201
        expected_y = 201
        expected_dx = -10
        expected_dy = -1
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkTop( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    
    def test003_checkBottomBouncesY( self ):
        # bounce off of the bottom
        x = 450
        y = 785
        dx = -10
        dy = 5
        new_y = 803
        expected_y = 771
        expected_dx = -10
        expected_dy = -5
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkBottom( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test004_checkBottomDoesNotBounceY( self ):
        # new y doesn't warrent a bounce
        x = 450
        y = 765
        dx = -10
        dy = 5
        new_y = 786
        expected_y = 786
        expected_dx = -10
        expected_dy = 5
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_y = self.constructed_ball.checkBottom( new_y )
        self.assertEqual( actual_y, expected_y )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return

    def test005_checkLeftStops( self ):
        # stick to the left wall
        x = 108
        y = 460
        dx = -10
        dy = -5
        new_x = 93
        expected_x = 100
        expected_dx = 0
        expected_dy = 0
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_x = self.constructed_ball.checkLeft( new_x )
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test006_checkLeftDoesNotStop( self ):
        # no reach left
        x = 108
        y = 460
        dx = -10
        dy = -5
        new_x = 102
        expected_x = 102
        expected_dx = -10
        expected_dy = -5
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_x = self.constructed_ball.checkLeft( new_x )
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test007_checkRightStops( self ):
        # stick to the right
        x = 878
        y = 460
        dx = 10
        dy = -5
        new_x = 888
        expected_x = 887
        expected_dx = 0
        expected_dy = 0
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_x = self.constructed_ball.checkRight( new_x )
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    def test008_checkRightDoesNotStop( self ):
        # no reach right
        x = 878
        y = 460
        dx = 10
        dy = -5
        new_x = 886
        expected_x = 886
        expected_dx = 10
        expected_dy = -5
        self.constructed_ball.setPosition( x, y )
        self.constructed_ball.setSpeed( dx, dy )
        
        actual_x = self.constructed_ball.checkRight( new_x )
        self.assertEqual( actual_x, expected_x )
        self.assertEqual( self.constructed_ball.getDX( ), expected_dx )
        self.assertEqual( self.constructed_ball.getDY( ), expected_dy )
        return
    
    
def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestBallCheckBoundary )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )