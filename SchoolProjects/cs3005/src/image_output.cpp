#include <iostream>
#include "Image.h"
#include "PPM.h"
#include "image_menu.h"
#include <fstream> 
#include <ios>
#include <string>


void drawAsciiImage(ActionData& action_data){

    for (int row = 0; row < action_data.getOutputImage().getHeight();row++){
        for (int column = 0; column < action_data.getOutputImage().getWidth();column++){

            int sumOfRGB = 0;
/*            for (int channel = 0;channel < 3;channel++){
                int positioinInVector = image.getChannel(row, column, channel);

                //os << "valOfPosInVector " << image.mainVector[positioinInVector] << std::endl ;
                sumOfRGB += image.mainVector[positioinInVector];            
                } */
            sumOfRGB = action_data.getOutputImage().getChannel(row, column, 0) + action_data.getOutputImage().getChannel(row, column, 1) + action_data.getOutputImage().getChannel(row, column, 2);

            double diviBy765 = sumOfRGB / 765.0;
 
            char visibleCharacter = 'N';
            if (diviBy765 >= 1.0){
                visibleCharacter = '@';
            }
            else if (diviBy765 >= 0.9){
                visibleCharacter = '#';
            }
            else if (diviBy765 >= 0.8){
                visibleCharacter = '%';
            }            
            else if (diviBy765 >= 0.7){
                visibleCharacter = '*';
            }            
            else if (diviBy765 >= 0.6){
                visibleCharacter = '|';
            }            
            else if (diviBy765 >= 0.5){
                visibleCharacter = '+';
            }            
            else if (diviBy765 >= 0.4){
                visibleCharacter = ';';
            }            
            else if (diviBy765 >= 0.3){
                visibleCharacter = '~';
            }            
            else if (diviBy765 >= 0.2){
                visibleCharacter = '-';
            }            
            else if (diviBy765 >= 0.1){
                visibleCharacter = '.';
            }            
            else if (diviBy765 >= 0.0){
                visibleCharacter = ' ';
            }
            else{
                std::cerr << "NULL" << std::endl;
            }
            action_data.getOS() << visibleCharacter;            
        }
        action_data.getOS() << std::endl;
    }
//This function will display a rectangle of ASCII (text) characters in an attempt to represent the strength of each pixel. The strength of a pixel is calculated as the sum of the red, green, and blue values of the pixel, divided by 765.0. 
//This division, and its result, must be floating point values (think double). 
//>= 1.0 -> @, >= 0.9 -> #, >= 0.8 -> %, >= 0.7 -> *, >= 0.6 -> |, >= 0.5 -> +, >= 0.4 -> ;, >= 0.3 -> ~, >= 0.2 -> -, >= 0.1 -> ., >= 0.0 -> Space.
//Display each row of the image as a line of text. Display all rows of the image.
}

void writeUserImage( ActionData& action_data ){
    std::string fileName = getString(action_data, "Output filename? ");
    std::ofstream file(fileName, std::ios::binary);

    action_data.getOutputImage().writeStream(file);
    file.close();
}

void copyImage(ActionData& action_data){
    action_data.getOutputImage() = action_data.getInputImage1();
}

void readUserImage1( ActionData& action_data ){
    std::string fileName = getString(action_data, "Input filename? "); 
    std::ifstream file(fileName);
    if(file.is_open()){
        action_data.getInputImage1().readStream(file);
        file.close();
    }
    else{
        action_data.getOS() << "'" << fileName << "' could not be opened." << std::endl;
    }
}
//Uses getString to ask the user for the name of an existing PPM file to be read, using “Input filename? ” as the prompt. Opens the file as an std::ifstream, 
//then uses readStream() to read the file into the input image 1. If the file does not open correctly, report to the that the file could not be opened. 
//For example, if the file was named “foo.ppm”, then the message should be “‘foo.ppm’ could not be opened.”

void readUserImage2( ActionData& action_data ){
    std::string fileName = getString(action_data, "Input filename? "); 
    std::ifstream file(fileName);
    if(file.is_open()){
        action_data.getInputImage2().readStream(file);
        file.close();
    }
    else{
        action_data.getOS() << "'" << fileName << "' could not be opened." << std::endl;
    }
}

void copyOutputImageToImage1(ActionData& action_data){
    action_data.getInputImage1() = action_data.getOutputImage();
}