#include "JuliaSet.h"

JuliaSet::JuliaSet()
: ComplexFractal(), jA(-0.650492), jB(-0.478235){
    setMaxNumber(255);
}

JuliaSet::JuliaSet( const int& height, const int& width, const double& min_x, const double& max_x, const double& min_y, const double& max_y, const double& a, const double& b )
: ComplexFractal(height, width, min_x, max_x, min_y, max_y), jA(a), jB(b){
}

JuliaSet::~JuliaSet(){
}

double JuliaSet::getA( ) const{
    return jA;
}

double JuliaSet::getB( ) const{
    return jB;
}

void JuliaSet::setParameters( const double& a, const double& b ){
    if(
        -2 <= a && a <= 2 &&
        -2 <= b && b <= 2
    ){
        jA = a;
        jB = b;
    }
}

void JuliaSet::calculateNextPoint( const double x0, const double y0, double& x1, double &y1 ) const{
    x1 = x0*x0 - y0*y0 + jA;
    y1 = 2*x0*y0 + jB;
}

int JuliaSet::calculatePlaneEscapeCount( const double& x0, const double& y0 ) const{
    int count = 0;
    double x = x0;
    double y = y0;
    for(; count <= getMaxNumber() - 1; count++ ){
        if( (x*x) + (y*y) > 4 ){
            break;
        }  
        double x1;
        double y1;
        calculateNextPoint(x, y, x1, y1);
        x = x1;
        y = y1;
    }
    return count;
}

//Calculate the number of iterations required for x0, y0 to escape. The return value should be in the range 0 to maximum escape
// count, inclusive. 0 means immediately escaped, before any applications of the function. Maximum escape count means never escaped,
// or escaped on the last step. Escape means the distance from the origin is more than 2.


int JuliaSet::calculateNumber( const int& row, const int& column ) const{
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

JuliaSetFour::JuliaSetFour()
    :JuliaSet(){
}

JuliaSetFour::~JuliaSetFour( ){
}

void JuliaSetFour::calculateNextPoint(const double x0, const double y0, double& x1, double &y1) const{
    x1 = (x0*x0*x0*x0) - 6 * (x0*x0) * (y0*y0) + (y0*y0*y0*y0) + getA();
    //x' = x^4 - 6 x^2 y^2 + y^4 + a
    
    y1 = 4 * (x0*x0*x0) * y0 - 4 * x0 * (y0*y0*y0) + getB();
    //y' = 4 x^3 y - 4 x y^3 + b
}