#include "Image.h"
#include <iostream>
#include <vector>

Image::Image()
    :internalHeight(0), internalWidth(0), mainVector(internalHeight * internalWidth * 3){
}

Image::Image(const int& height, const int& width )
    :internalHeight(height), internalWidth(width), mainVector(internalHeight * internalWidth * 3){
}

int Image::getHeight( ) const{
    return internalHeight; 
} 

int Image::getWidth( ) const{
    return internalWidth;
}

bool Image::indexValid( const int& row, const int& column, const int& channel ) const{
//Checks if row, column, and channel are all within the legal limits. Returns true if they all are, and false otherwise.

    bool returnValue = true;

    if (row < 0 || row >= internalHeight || column < 0 || column >= internalWidth || channel < 0 || channel > 2 ){
        returnValue = false;
    }
    
    return returnValue;
}

int Image::index( const int& row, const int& column, const int& channel ) const{ //getWidth?
//Returns the index into the data vector for the location specified by row, column, and channel
    return ( (row * internalWidth * 3) + (column * 3) ) + channel;
}

int Image::getChannel( const int& row, const int& column, const int& channel ) const{
//Returns an int representation of the value in the data vector at the location specified by row, column, and channel. Uses the index method. Returns -1 if the row, column, or channel is not valid. Uses the indexValid method to check.

    if (indexValid(row, column, channel)){
        return  mainVector[index(row, column, channel)];
    } 
    else{
        return -1;
    }
}

void Image::setHeight( const int& height ){ //Need to resize the vector after accepting the new height
    
    if( height >= 0 ){
        internalHeight = height;
        mainVector.resize(internalWidth * internalHeight * 3);
    }
}

void Image::setWidth( const int& width ){  //Need to resize the vector after accepting the new width
    
    if( width >= 0 ){
        internalWidth = width;
        mainVector.resize(internalWidth * internalHeight * 3);
    }
}

void Image::setChannel( const int& row, const int& column, const int& channel, const int& value ) { //Set channel to given value after checking value 
    
    if (indexValid(row, column, channel)){
        int position = index(row, column, channel);
        mainVector[position] = value;
    }
    
    else{
        std::cerr << "Error: Index Invalid";
    } 
}
