#include "ColorTable.h"

#include <vector>
#include <iostream>


Color::Color() 
: cRed(0), cGreen(0), cBlue(0){
}

Color::Color( const int& red, const int& green, const int& blue )
: cRed(red), cGreen(green), cBlue(blue){
}

int Color::getRed( ) const{
    return cRed;
}

int Color::getGreen( ) const{
    return cGreen;
}

int Color::getBlue( ) const{
    return cBlue;
}

int Color::getChannel( const int& channel ) const{
    if( channel == 0){
        return cRed;
    }
    else if( channel == 1){
        return cGreen;
    }
    else if(channel == 2){
        return cBlue;
    }
    else{
        std::cerr << "color getChannel out of range ";
        return -1;
    }
}

void Color::setRed( const int& value ){
    if(value >= 0){
        cRed = value;
    }
}

void Color::setGreen( const int& value ){
    if(value >= 0){
        cGreen = value;
    }
}

void Color::setBlue( const int& value ){
    if(value >= 0){
        cBlue = value;
    }    
}

void Color::setChannel( const int& channel, const int& value ){
    if(value >=0 ){
        if(0 == channel){
            cRed = value;
        }
        else if(1 == channel){
            cGreen = value;
        }
        else if(2 == channel){
            cBlue = value;
        }
    }
}

void Color::invert( const int& max_color_value ){
    if(cRed <= max_color_value && cGreen <= max_color_value && cBlue <= max_color_value){
        setRed(max_color_value - cRed);
        setGreen(max_color_value - cGreen);
        setBlue( max_color_value - cBlue);
    }
}

bool Color::operator==( const Color& rhs ) const{
    return rhs.getRed() == cRed && rhs.getGreen() == cGreen && rhs.getBlue() == cBlue;
}

std::ostream& operator<<( std::ostream& os, const Color& color ){
    return os << color.getRed() << ":" << color.getGreen() << ":" << color.getBlue();
}

// Color Table -----------------------------------------------------------------------------------
ColorTable::ColorTable(const int& num_color)
    : vectorOfColors(num_color){
}

int ColorTable::getNumberOfColors( ) const{
    return vectorOfColors.size();
}

void ColorTable::setNumberOfColors( const int& num_color ){
    vectorOfColors.resize(num_color);
}

const Color& ColorTable::operator[]( const int& i ) const{
    if(0 <= i && i < getNumberOfColors()){
        return vectorOfColors[i];
    }
    else{
        static Color ec( -1, -1, -1 );
        static Color c( -1, -1, -1 );
        c = ec;
        return c;
    }
}

Color& ColorTable::operator[]( const int& i ){
    if(0 <= i && i < getNumberOfColors()){
        return vectorOfColors[i];
    }
    else{
        static Color ec( -1, -1, -1 );
        static Color c( -1, -1, -1 );
        c = ec;
        return c;
    }
}

void ColorTable::setRandomColor( const int& max_color_value, const int& position ){
    if(position < getNumberOfColors() && max_color_value >= 0 && position >= 0){
        int ranVal = ((std::rand()) % (max_color_value + 1));
        vectorOfColors[position].setRed(ranVal);
        int ranVal2 = ((std::rand()) % (max_color_value + 1));
        vectorOfColors[position].setGreen(ranVal2);
        int ranVal3 = ((std::rand()) % (max_color_value + 1));
        vectorOfColors[position].setBlue(ranVal3);

    }
}

double ColorTable::gradientSlope(const double y1, const double y2, const double x1, const double x2) const{
    double val = (y2 - y1) / (x2 - x1);
    return val;
//color 10 @ pos 20
//goal is to get to downarrow
//color 30 @ pos 40
}

double ColorTable::gradientValue(const double y1, const double x1, const double slope, const double x) const{
    double returnValue = (slope * (x - x1) + y1);
    return returnValue;
// uses gradient slope to calculate the COLOR VALUE you need to insert into a specific position in the vector
}


void ColorTable::insertGradient( const Color& color1, const Color& color2, const int& position1, const int& position2 ){
    if( position1 < position2 && 0 <= position1 && position1 < getNumberOfColors() && 0 <= position2 && position2 < getNumberOfColors() ){
        for(int i = position1; i <= position2; i++){
            for(int j = 0; j < 3; j++){
                double valueOfSlope = gradientSlope( color1.getChannel(j), color2.getChannel(j), position1, position2 );
                double newVal = gradientValue(color1.getChannel(j), position1, valueOfSlope, i);
                vectorOfColors[i].setChannel(j, newVal);

            }
        }
    }
}

int ColorTable::getMaxChannelValue( ) const{
    int maxValue = 0;
    for(int i = 0; i < getNumberOfColors(); i++){
        for(int channel = 0; channel < 3; channel++){
            if(vectorOfColors[i].getChannel(channel) > maxValue){
                maxValue = vectorOfColors[i].getChannel(channel);
            }
        }
    }
    return maxValue;
}