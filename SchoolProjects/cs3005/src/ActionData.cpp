#include "ActionData.h"
#include <iostream>

ActionData::ActionData(std::istream& is, std::ostream& os)
    : mNumberGrid(0), inputStream(is), outputStream(os), quitApplication(false), newColorTable(16) {
        Color startingColor(0, 255, 0);
        Color endingColor(255, 0, 255);
        newColorTable.insertGradient(startingColor, endingColor, 0, 15);
} 

ActionData::~ActionData(){
    if (mNumberGrid != 0){
        delete mNumberGrid;
    }
}
std::istream& ActionData::getIS(){
    return inputStream;
}
std::ostream& ActionData::getOS(){
    return outputStream;
}
PPM& ActionData::getInputImage1(){
    return inputImage1;
}
PPM& ActionData::getInputImage2(){
    return inputImage2;
}
PPM& ActionData::getOutputImage(){
    return outputImage;
}
bool ActionData::getDone() const{
    return quitApplication;
}
void ActionData::setDone(){
    quitApplication = true;
}
NumberGrid& ActionData::getGrid(){
    return *mNumberGrid;
}
void ActionData::setGrid(NumberGrid *grid){
    if(mNumberGrid != 0){
        delete mNumberGrid;  
    }
    mNumberGrid = grid;
}

ColorTable& ActionData::getTable(){
    return newColorTable;
}