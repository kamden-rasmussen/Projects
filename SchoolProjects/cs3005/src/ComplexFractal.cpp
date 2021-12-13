#include "ComplexFractal.h"
#include <iostream>
#include <cmath>

ComplexFractal::ComplexFractal()
: ThreadedGrid(200, 300), minX(-1.5), minY(-1), maxX(1.5), maxY(1), deltaX(.01), deltaY(.01){
}

ComplexFractal::ComplexFractal( const int& height, const int& width, const double& min_x, const double& max_x, const double& min_y, const double& max_y )
: ThreadedGrid(height, width), minX(min_x), minY(min_y), maxX(max_x), maxY(max_y){
}

ComplexFractal::~ComplexFractal(){
}

double ComplexFractal::getMinX( ) const{
    return minX;
}

double ComplexFractal::getMaxX( ) const{
    return maxX;
} 

double ComplexFractal::getMinY( ) const{
    return minY;
}

double ComplexFractal::getMaxY( ) const{
    return maxY;
}

void ComplexFractal::setGridSize( const int& height, const int& width ){
    if(height >= 2 && width >= 2){
        NumberGrid::setGridSize(height, width);
        setDeltas(calculateDeltaX(), calculateDeltaY());
    }
}

void ComplexFractal::setPlaneSize( const double& min_x, const double& max_x, const double& min_y, const double& max_y ){
    if(
        -2.0 <= min_x && min_x <= 2.0 && min_x != max_x &&
        -2.0 <= max_x && max_x <= 2.0 && 
        -2.0 <= min_y && min_y <= 2.0 && min_y != max_y &&
        -2.0 <= max_y && max_y <= 2.0 
        ){
            minX = min_x;
            maxX = max_x;
            minY = min_y;
            maxY = max_y;

            if( min_x > max_x ){
                minX = max_x;
                maxX = min_x;
            }
            if(min_y > max_y){
                minY = max_y;
                maxY = min_y;   
            }

            setGridSize(abs(maxY) - abs(minY), abs(maxX) - abs(minX));
            setDeltas(calculateDeltaX(), calculateDeltaY());
        }
}

double ComplexFractal::getDeltaX( ) const{
    return deltaX;
}

double ComplexFractal::getDeltaY( ) const{
    return deltaY;
}

void ComplexFractal::setDeltas( const double& delta_x, const double& delta_y ){
    if( delta_x >= 0 && delta_y >= 0){
        deltaX = delta_x;
        deltaY = delta_y;
    }
}

double ComplexFractal::calculateDeltaX( ) const{
    return (maxX - minX) / (getWidth() - 1);
}

double ComplexFractal::calculateDeltaY( ) const{
    return (maxY - minY) / (getHeight() - 1);
}

double ComplexFractal::calculatePlaneXFromPixelColumn( const int& column ) const{
    if(0 <= column && column < getWidth()){
        return (minX + column * deltaX);
    }
    return 0;
}
//double calculatePlaneXFromPixelColumn( const int& column ) const; Calculate the plane x value for a given column. If the column index is out of range (if column is less than zero or column is greater than or equal to the grid width),
// return 0. Do not call calculateDeltaX() here. Use getDeltaX() or directly access the data member. The value should have already been calculated previously.

double ComplexFractal::calculatePlaneYFromPixelRow( const int& row ) const{

    if(0 <= row && row < getHeight()){
        return (maxY - row * deltaY);
    }
    else{
        return 0;
    }
}

void ComplexFractal::calculatePlaneCoordinatesFromPixelCoordinates( const int& row, const int& column, double& x, double& y ) const{  
    if( 
        0 <= column && column < getWidth() &&
        0 <= row && row < getHeight()
    ){
        x = calculatePlaneXFromPixelColumn(column);
        y = calculatePlaneYFromPixelRow(row);
    }
    else{
        x = 0;
        y = 0;
    }
}

int ComplexFractal::calculateNumber( const int& row, const int& column ) const{
    if( 0 <= row && row < getHeight() && 0 <= column && column < getWidth()){
        return std::abs(getMaxNumber() * std::sin(10*calculatePlaneXFromPixelColumn(column)) * std::cos(10*calculatePlaneYFromPixelRow(row)));
    }   
    else{
        return -1;
    }
}

void ComplexFractal::zoomPlane( const double& zoom_factor ){
    double currentXSize = maxX - minX;
    double currentYSize = maxY - minY;

    double deseiredXSize = currentXSize * zoom_factor;
    double deseiredYSize = currentYSize * zoom_factor;

    double changeInX = (currentXSize - deseiredXSize) / 2;
    double changeInY = (currentYSize - deseiredYSize) / 2;

    double newMinX = minX + changeInX;
    double newMinY = minY + changeInY;

    double newMaxX = maxX - changeInX;
    double newMaxY = maxY - changeInY;

    if(newMinX <= -2.0){
        newMinX = -2.0;
    }
    if(newMaxX >= 2.0){
        newMaxX = 2.0;
    }
    if(newMinY <= -2.0){
        newMinY = -2.0;
    }
    if(newMaxY >= 2.0){
        newMaxY = 2.0;
    }

    setPlaneSize(newMinX, newMaxX, newMinY, newMaxY);

}