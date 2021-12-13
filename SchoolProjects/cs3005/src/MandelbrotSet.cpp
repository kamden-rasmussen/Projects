#include "MandelbrotSet.h"

MandelbrotSet::MandelbrotSet( )
: ComplexFractal() {
}

MandelbrotSet::MandelbrotSet( const int& height, const int& width, const double& min_x, const double& max_x, const double& min_y, const double& max_y )
: ComplexFractal(height, width, min_x, max_x, min_y, max_y) {
}

MandelbrotSet::~MandelbrotSet( ){ 
}

void MandelbrotSet::calculateNextPoint( const double x0, const double y0, const double& a, const double& b, double& x1, double &y1 ) const{
    x1 = x0*x0 - y0*y0 + a;
    y1 = 2*x0*y0 + b;
}

int MandelbrotSet::calculatePlaneEscapeCount( const double& a, const double& b ) const{
    int count = 0;
    double newX = 0.0;
    double newY = 0.0;
    double x = 0.0;
    double y = 0.0;
    calculateNextPoint(x, y, a, b, newX, newY);
    x = newX;
    y = newY;

    for(; count <= getMaxNumber() - 1; count++ ){
        if( (newX*newX) + (newY*newY) > 4 ){
            break;
        }  
        calculateNextPoint(x, y, a, b, newX, newY);
        x = newX;
        y = newY;
    }
    return count;
}

int MandelbrotSet::calculateNumber( const int& row, const int& column ) const{
    double x = 0;
    double y = 0;
    if(
        0 <= row && row < getHeight() &&
        0 <= column && column < getWidth()
    ){
        calculatePlaneCoordinatesFromPixelCoordinates(row, column, x, y);
        return calculatePlaneEscapeCount(x, y);
    }
    else{
        return -1;
    }
}