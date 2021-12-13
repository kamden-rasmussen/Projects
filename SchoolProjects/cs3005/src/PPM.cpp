#include "PPM.h"
#include <iostream>


PPM::PPM()
    : Image(), internalMaxColor(1){
}

PPM::PPM( const int& height, const int& width )
    : Image(height, width), internalMaxColor(1){
}

int PPM::getMaxColorValue( ) const{
    return internalMaxColor;
}

bool PPM::valueValid( const int& value ) const{
    if( 0 <= value && value <= internalMaxColor ){
        return true;
    }

    else{
        return false;
    }
} 

void PPM::setMaxColorValue( const int& max_color_value ){
    if( 1 <= max_color_value && max_color_value<= 255){
        internalMaxColor = max_color_value;
    }
} 

void PPM::setChannel( const int& row, const int& column, const int& channel, const int& value ){
    if(valueValid(value)){
        Image::setChannel(row, column, channel, value);
    }
    else{
        //std::cerr << "Error: Value Invalid ";
    }
}
void PPM::setPixel( const int& row, const int& column, const int& red, const int& green, const int& blue ){
    for(int channel = 0; channel < 3; channel++){
        if(channel == 0){
            setChannel(row, column, channel, red);
        }
        else if(channel == 1){
            setChannel(row, column, channel, green);
        }
        else if(channel == 2){
            setChannel(row, column, channel, blue);
        }
    }
}

void PPM::writeStream(std::ostream& os) const{
    os << "P6 " << getWidth() << " " << getHeight() << " " << getMaxColorValue() << "\n";

    for (int row = 0; row < getHeight(); row++) {
        for (int column = 0; column < getWidth(); column++) {

            for (int channel = 0; channel < 3; channel++) {
                int value = getChannel(row, column, channel);
                unsigned char byte = value;
                os.write((char *) &byte, 1);
            }
        }
    }
}

void PPM::readStream(std::istream& is){
    std::string inputValue;
    int isWidth;
    int isHeight;
    int isMaxColor;
    unsigned char isByte;
    is >> inputValue >> isWidth >> isHeight >> isMaxColor;
    is.read((char *) &isByte, 1);
    setWidth(isWidth);
    setHeight(isHeight);
    setMaxColorValue(isMaxColor);

    for (int row = 0; row < isHeight; row++) {
        for (int column = 0; column < isWidth; column++) {
            for (int channel = 0; channel < 3; channel++) {
                is.read((char *) &isByte, 1);
                setChannel(row, column, channel, isByte);
            }
        }
    }
}
bool PPM::operator== ( const PPM& rhs ) const{
    return((getHeight() * getWidth()) == (rhs.getHeight() *  rhs.getWidth()));
}

bool PPM::operator!=( const PPM& rhs ) const{
    return((getHeight() * getWidth()) != (rhs.getHeight() *  rhs.getWidth()));
}
bool PPM::operator<( const PPM& rhs ) const{
    return((getHeight() * getWidth()) < (rhs.getHeight() *  rhs.getWidth()));
}
bool PPM::operator<=( const PPM& rhs ) const{
    return((getHeight() * getWidth()) <= (rhs.getHeight() *  rhs.getWidth()));
}
bool PPM::operator>( const PPM& rhs ) const{
    return((getHeight() * getWidth()) > (rhs.getHeight() *  rhs.getWidth()));
}
bool PPM::operator>=( const PPM& rhs ) const{
    return((getHeight() * getWidth()) >= (rhs.getHeight() *  rhs.getWidth()));
}
PPM& PPM::operator+=( const PPM& rhs ){
    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) + rhs.getChannel(row, column, channel);
                
                if(newValue < getMaxColorValue()){
                    setChannel(row, column, channel, newValue);
                }
                else{
                    setChannel(row, column, channel, getMaxColorValue());
                }
            }
        }
    }
    return *this;
}
PPM& PPM::operator-=( const PPM& rhs ){
    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) - rhs.getChannel(row, column, channel);
                
                if(newValue > 0){
                    setChannel(row, column, channel, newValue);
                }
                else{
                    setChannel(row, column, channel, 0);
                }
            }
        }
    }
    return *this;
}
PPM& PPM::operator*=( const double& rhs ){
    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) * rhs;
                
                if(newValue <= getMaxColorValue() && newValue >= 0){
                    setChannel(row, column, channel, newValue);
                }
                else if(newValue < 0){
                    setChannel(row, column, channel, 0);
                }
                else{
                    setChannel(row, column, channel, getMaxColorValue());
                }
            }
        }
    }
    return *this;
}
PPM& PPM::operator/=( const double& rhs ){
    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) / rhs;
                
                if(newValue <= getMaxColorValue() && newValue >= 0){
                    setChannel(row, column, channel, newValue);
                }
                else if(newValue < 0){
                    setChannel(row, column, channel, 0);
                }
                else{
                    setChannel(row, column, channel, getMaxColorValue());
                }
            }
        }
    }
    return *this;
}
PPM PPM::operator+( const PPM& rhs ) const{
    PPM newObject;
    newObject.setHeight(getHeight());
    newObject.setWidth(getWidth());
    newObject.setMaxColorValue(getMaxColorValue());

    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) + rhs.getChannel(row, column, channel);
                
                if(newValue < getMaxColorValue()){
                    newObject.setChannel(row, column, channel, newValue);
                }
                else{
                    newObject.setChannel(row, column, channel, getMaxColorValue());
                }
            }
        }
    }
    return newObject;
}
PPM PPM::operator-( const PPM& rhs ) const{
    PPM newObject;
    newObject.setHeight(getHeight());
    newObject.setWidth(getWidth());
    newObject.setMaxColorValue(getMaxColorValue());
    
    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) - rhs.getChannel(row, column, channel);
                
                if(newValue > 0){
                    newObject.setChannel(row, column, channel, newValue);
                }
                else{
                    newObject.setChannel(row, column, channel, 0);
                }
            }
        }
    }
    return newObject;
}
PPM PPM::operator*( const double& rhs ) const{       
    PPM newObject;
    newObject.setHeight(getHeight());
    newObject.setWidth(getWidth());
    newObject.setMaxColorValue(getMaxColorValue());

    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) * rhs;
                
                if(newValue <= getMaxColorValue() && newValue >= 0){
                    newObject.setChannel(row, column, channel, newValue);
                }
                else if(newValue < 0){
                    newObject.setChannel(row, column, channel, 0);
                }
                else{
                    newObject.setChannel(row, column, channel, getMaxColorValue());
                }
            }
        }
    }
    return newObject;

}
PPM PPM::operator/( const double& rhs ) const{
    PPM newObject;
    newObject.setHeight(getHeight());
    newObject.setWidth(getWidth());
    newObject.setMaxColorValue(getMaxColorValue());

    for(int row = 0; row < getHeight();row++){
        for(int column = 0; column < getWidth(); column++){
            for(int channel = 0; channel < 3; channel++){     
                int newValue = getChannel(row, column, channel) / rhs;
                
                if(newValue <= getMaxColorValue() && newValue >= 0){
                    newObject.setChannel(row, column, channel, newValue);
                }
                else if(newValue < 0){
                    newObject.setChannel(row, column, channel, 0);
                }
                else{
                    newObject.setChannel(row, column, channel, getMaxColorValue());
                }
            }
        }
    }
    return newObject;
}

void PPM::grayFromChannel( PPM& dst, const int& src_channel ) const{
    dst = *this;
    for(int row = 0; row < dst.getHeight();row++){
        for(int column = 0; column < dst.getWidth(); column++){
            int valueToCopy = dst.getChannel(row, column, src_channel);
            dst.setPixel(row, column, valueToCopy, valueToCopy, valueToCopy);
        }
    }
}

void PPM::grayFromRed( PPM& dst ) const{
    grayFromChannel(dst, 0);
}
void PPM::grayFromGreen( PPM& dst ) const{
     grayFromChannel(dst, 1);
}
void PPM::grayFromBlue( PPM& dst ) const{
     grayFromChannel(dst, 2);
}
double PPM::linearColorimetricPixelValue( const int& row, const int& column ) const{
    // 0.2126*red + 0.7152*green + 0.0722*blue
    return (getChannel(row, column, 0) * 0.2126) + (getChannel(row, column, 1) * 0.7152) + (getChannel(row, column, 2) * 0.0722);
}
void PPM::grayFromLinearColorimetric( PPM& dst ) const{
    dst = *this;
    for(int row = 0; row < dst.getHeight();row++){
        for(int column = 0; column < dst.getWidth(); column++){
            int val = linearColorimetricPixelValue(row, column);
            dst.setPixel(row, column, val, val, val);
        }
    }
}

void PPM::orangeFilter(PPM& dst) const{
    dst = *this;

    for(int row = 0; row < dst.getHeight();row++){
        for(int column = 0; column < dst.getWidth(); column++){
            int old_red = dst.getChannel(row, column, 0);
            int old_green = dst.getChannel(row, column, 1);
            int old_blue = dst.getChannel(row, column, 2);

            int new_red = 2*(2*old_red+old_green)/3;
            if(new_red > dst.getMaxColorValue()){
                new_red = dst.getMaxColorValue();

            }

            int new_green = 2*(2*old_red+old_green)/6;
            if(new_green > dst.getMaxColorValue()){
                new_red = dst.getMaxColorValue();
            }

            int new_blue = old_blue/2;
            if(new_blue > dst.getMaxColorValue()){
                new_red = dst.getMaxColorValue();
            }

            dst.setPixel(row, column, new_red, new_green, new_blue);
        }
    }
}


int PPM::antiAliasPixelValue(int n, int row, int column, int channel) const{

    int totalChannelVal = 0;

    for(int indexOverRow = row * n; indexOverRow < (row + 1) * n; indexOverRow++ ){
        for(int indexOverColumn = column * n; indexOverColumn < (column + 1) * n; indexOverColumn++){
            totalChannelVal += getChannel(indexOverRow, indexOverColumn, channel);
        }
    }

//Loops over an n-by-n area of the PPM. Adds the total value of channel’s values in the area. 
//Returns the total value divided by the number of values added together. 
//n is the size of the area to average over. row is the row number in the output image, and column is the column number in the output image. 
//Use the formulas above to build the loops that loop over the row and column in the big image. channel will be the channel index (0, 1, 2), 
//appropriate for use with getChannel()
    int returnVal = (totalChannelVal / (n * n));
    return returnVal;
}

void PPM::antiAlias(const int& n, PPM& dst) const{

    dst.setHeight(getHeight() / n);
    dst.setWidth(getWidth() / n);
    dst.setMaxColorValue(getMaxColorValue());

    int row;
    int column;
    int newRed;
    int newGreen;
    int newBlue;

    for(row = 0; row < dst.getHeight(); row++){
        for(column = 0; column < dst.getWidth(); column++){
            newRed = antiAliasPixelValue(n, row, column, 0);
            newGreen = antiAliasPixelValue(n, row, column, 1);
            newBlue = antiAliasPixelValue(n, row, column, 2);
            dst.setPixel(row, column, newRed, newGreen, newBlue);
        }
    }
}
