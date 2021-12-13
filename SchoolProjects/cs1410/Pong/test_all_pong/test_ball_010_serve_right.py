"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
from Ball import ball

class TestBallServe( unittest.TestCase ):

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

        self.x = 800
        self.min_y = 400.0
        self.max_y = 600.0
        self.minimum_dx = 1.0
        self.maximum_dx = 10.0
        self.minimum_dy = -10.0
        self.maximum_dy =  10.0

        return

    def tearDown( self ):
        return

    def test001_ballServesFromRightDXIsNegative( self ):
        
        for i in range( 100 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            self.assertLess( self.constructed_ball.getDX( ), 0 )
            
        return
    
    def test002_ballServesFromRightDXIsInRange( self ):
        
        for i in range( 100 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            self.assertLessEqual( self.constructed_ball.getDX( ), -self.minimum_dx )
            self.assertGreaterEqual( self.constructed_ball.getDX( ), -self.maximum_dx )
            
        return
    
    def test003_ballServesFromRightDXUsesFullRange( self ):
        minimum_found = self.maximum_dx
        maximum_found = self.minimum_dx
        for i in range( 100 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            minimum_found = min( minimum_found, self.constructed_ball.getDX( ) )
            maximum_found = max( maximum_found, self.constructed_ball.getDX( ) )

        range_found = maximum_found - minimum_found
        range_expected = self.maximum_dx - self.minimum_dx
        # expect range found to be close (at least 80%) to maximum range
        self.assertGreater( range_found, 0.8 * range_expected )
        return
    
    def test004_ballServesFromRightDXHasFractionalPart( self ):
        # at least 1 in 10 should have a fractional part
        found_fractional_part = False
        for i in range( 10 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            value = self.constructed_ball.getDX( )
            if abs( value ) - int( abs( value ) ) > 0:
                found_fractional_part = True
                break

        self.assertTrue( found_fractional_part )
        return
    
    
    def test005_ballServesFromRightDYIsPositiveAndNegative( self ):
        
        # at least 1 in 10 should be positive and at least 1 should be negative
        found_positive = False
        found_negative = False
        for i in range( 10 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            if self.constructed_ball.getDY( ) < 0:
                found_negative = True
            if self.constructed_ball.getDY( ) > 0:
                found_positive = True
            
        self.assertTrue( found_positive )
        self.assertTrue( found_negative )
        return
    
    def test006_ballServesFromRightDYIsInRange( self ):
        
        for i in range( 100 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            self.assertGreaterEqual( self.constructed_ball.getDY( ), self.minimum_dy )
            self.assertLessEqual( self.constructed_ball.getDY( ), self.maximum_dy )
            
        return
    
    def test007_ballServesFromRightDYUsesFullRange( self ):
        minimum_found = self.maximum_dy
        maximum_found = self.minimum_dy
        for i in range( 100 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            minimum_found = min( minimum_found, self.constructed_ball.getDY( ) )
            maximum_found = max( maximum_found, self.constructed_ball.getDY( ) )

        range_found = maximum_found - minimum_found
        range_expected = self.maximum_dy - self.minimum_dy
        # expect range found to be close (at least 80%) to maximum range
        self.assertGreater( range_found, 0.8 * range_expected )
        return
    
    def test008_ballServesFromRightDYHasFractionalPart( self ):
        # at least 1 in 10 should have a fractional part
        found_fractional_part = False
        for i in range( 10 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            value = self.constructed_ball.getDY( )
            if abs( value - int( value ) ) > 0:
                found_fractional_part = True
                break

        self.assertTrue( found_fractional_part )
        return
    
    def test009_ballServesFromRightXIsCorrect( self ):
        
        self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
        self.assertEqual( self.constructed_ball.getX( ), self.x )
            
        return
    
    def test010_ballServesFromRightYIsInRange( self ):
        
        for i in range( 100 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            self.assertGreaterEqual( self.constructed_ball.getY( ), self.min_y )
            self.assertLessEqual( self.constructed_ball.getY( ), self.max_y )
            
        return

    def test011_ballServesFromRightYUsesFullRange( self ):
        minimum_found = self.max_y
        maximum_found = self.min_y
        for i in range( 100 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            minimum_found = min( minimum_found, self.constructed_ball.getY( ) )
            maximum_found = max( maximum_found, self.constructed_ball.getY( ) )

        range_found = maximum_found - minimum_found
        range_expected = self.max_y - self.min_y
        # expect range found to be close (at least 80%) to maximum range
        self.assertGreater( range_found, 0.8 * range_expected )
        return
    
    def test012_ballServesFromRightYHasFractionalPart( self ):
        # at least 1 in 10 should have a fractional part
        found_fractional_part = False
        for i in range( 10 ):
            self.constructed_ball.serveRight( self.x, self.min_y, self.max_y, self.minimum_dx, self.maximum_dx, self.minimum_dy, self.maximum_dy )
            value = self.constructed_ball.getY( )
            if abs( value - int( value ) ) > 0:
                found_fractional_part = True
                break

        self.assertTrue( found_fractional_part )
        return
    
def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestBallServe )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
