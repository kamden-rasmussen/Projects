#include "NumberGrid.h"
#include "PPM.h"
#include <iostream>
#include <vector>

NumberGrid::NumberGrid()
    : mHeight(300), mWidth(400), mMaxValue(255), mNGVector((mHeight * mWidth), 0){}

NumberGrid::NumberGrid( const int& height, const int& width )
    : mHeight(height), mWidth(width), mMaxValue(255), mNGVector((mHeight * mWidth), 0){}

NumberGrid::~NumberGrid(){
}
int NumberGrid::getHeight( ) const{
    return mHeight;
}
int NumberGrid::getWidth( ) const{
    return mWidth;
}
int NumberGrid::getMaxNumber( ) const{
    return mMaxValue;
}
void NumberGrid::setGridSize( const int& height, const int& width ){
    if(height >= 2 && width >= 2){
        mHeight = height;
        mWidth = width;
        mNGVector.resize(mHeight * mWidth, 0);
    }
    else{
        std::cerr << "one of the values is < 2";
    }
}

void NumberGrid::setMaxNumber( const int& number ){
    if(number >= 0){
        mMaxValue = number;
    }

}
const std::vector< int >& NumberGrid::getNumbers( ) const{
    return mNGVector;
}
int NumberGrid::index( const int& row, const int& column ) const{
    return ((mWidth * row) + column);
}
bool NumberGrid::indexValid( const int& row, const int& column ) const{
    return 0 <= row && row < mHeight && 0 <= column && column < mWidth;
}
bool NumberGrid::numberValid( const int& number ) const{
    return number >= 0 && number <= mMaxValue;
}
int NumberGrid::getNumber( const int& row, const int& column ) const{
    if(indexValid(row, column)){
        return (mNGVector[index(row , column)]);
    }
    else{
        return - 1;
    }
}
void NumberGrid::setNumber( const int& row, const int& column, const int& number ){
    if( numberValid(number) && indexValid(row, column)){
        mNGVector[index(row, column)] = number;
    }
}
void NumberGrid::setPPM( PPM& ppm ) const{
    ppm.setHeight(mHeight);
    ppm.setWidth(mWidth);
    ppm.setMaxColorValue(63);
    
    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            
            int value = getNumber(row, column);

            if(value == 0){
                ppm.setPixel(row, column, 0, 0, 0);
            }
            else if(value == mMaxValue){
                ppm.setPixel(row, column, 63, 31, 31);
            }
            else if((value % 8) == 0){
                ppm.setPixel(row, column, 63, 63, 63);
            }
            else if((value % 8) == 1){
                ppm.setPixel(row, column, 63, 31, 31);
            }
            else if((value % 8) == 2){
                ppm.setPixel(row, column, 63, 63, 31);
            }            
            else if((value % 8) == 3){
                ppm.setPixel(row, column, 31, 63, 31);
            }
            else if((value % 8) == 4){
                ppm.setPixel(row, column, 0, 0, 0);
            }
            else if((value % 8) == 5){
                ppm.setPixel(row, column, 31, 63, 63);
            }
            else if((value % 8) == 6){
                ppm.setPixel(row, column, 31, 31, 63);
            }
            else if((value % 8) == 7){
                ppm.setPixel(row, column, 63, 31, 63);
            }
            else{
                std::cerr << " Failed to set NumberGrid Value ";
            }


        }   
    }

}
void NumberGrid::setPPM( PPM& ppm, const ColorTable& colors ) const{
    if( colors.getNumberOfColors() >= 2){
        ppm.setHeight(mHeight);
        ppm.setWidth(mWidth);
        ppm.setMaxColorValue(colors.getMaxChannelValue());

        for(int row = 0; row < getHeight();row++){
            for(int column = 0; column < getWidth(); column++){
            
                int KolbysIsNamedValue = getNumber(row, column);
                int indexValue;

                if( KolbysIsNamedValue == getMaxNumber() ){
                    indexValue = colors.getNumberOfColors() - 1;
                }
                else{
                    indexValue = KolbysIsNamedValue % colors.getNumberOfColors();
                }
                int tempRed = colors[indexValue].getRed();
                int tempGreen = colors[indexValue].getGreen();
                int tempBlue = colors[indexValue].getBlue();

                ppm.setPixel(row, column, tempRed, tempGreen, tempBlue);   
                
            }
        }
    }
}
 // Uses the currently stored grid numbers to configure an image in the PPM object. Sets the width and height of the image to match the width and
 // height of the grid. Sets the maximum color value to the maximum color value of any color in the color table (getMaxChannelValue()). For
 // each pixel in the PPM object, sets the color based on the grid number for the pixel. If the color table does not have at least 2 colors,
 // make no changes to the PPM object. The grid number will be used as the index into the color table, with a special case: if the grid number is the
 // maximum grid number, use the color table item with the highest index number; otherwise use grid number modulus color table size as the index into the table.

 void NumberGrid::calculateAllNumbers(){
     for(int row = 0; row < getHeight(); row++){
         for(int column = 0; column < getWidth(); column++){
             int tempNumber = calculateNumber(row, column);
             setNumber(row, column, tempNumber);
         }
     }
 }