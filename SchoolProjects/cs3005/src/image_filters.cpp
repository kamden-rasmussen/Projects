#include "image_menu.h"

void plusEquals( ActionData& action_data ){
    action_data.getInputImage1() += action_data.getInputImage2();
}
//Modifies input image 1 by adding input image 2 to it.

void minusEquals( ActionData& action_data ){
    action_data.getInputImage1() -= action_data.getInputImage2();
} 
//Modifies input image 1 by subtracting input image 2 from it.

void timesEquals( ActionData& action_data ){
    action_data.getInputImage1() *= getDouble(action_data, "Factor? ");
}
//Modifies input image 1 by multiplying it by the double obtained by calling getDouble with a prompt of “Factor? “.

void divideEquals( ActionData& action_data ){
    action_data.getInputImage1() /= getDouble(action_data, "Factor? ");
}
//Modifies input image 1 by dividing it by the double obtained by calling getDouble with a prompt of “Factor? “.

void plus( ActionData& action_data ){
    action_data.getOutputImage() = action_data.getInputImage1() + action_data.getInputImage2();
}
//Sets output image to be the sum of input image 1 and input image 2.

void minus( ActionData& action_data ){
    action_data.getOutputImage() = action_data.getInputImage1() - action_data.getInputImage2();
}
//Sets output image to be the difference of input image 1 and input image 2.

void times( ActionData& action_data ){
    action_data.getOutputImage() = action_data.getInputImage1() * getDouble(action_data, "Factor? ");
}
//Sets output image to input image1 times the double obtained by calling getDouble with a prompt of “Factor? “.

void divide( ActionData& action_data ){
    action_data.getOutputImage() = action_data.getInputImage1() / getDouble(action_data, "Factor? ");
}

//image filters
void grayFromRed(ActionData& action_data){
    PPM grey;
    action_data.getInputImage1().grayFromRed(grey);
    action_data.getOutputImage() = grey;
}

void grayFromGreen(ActionData& action_data){
    PPM grey;
    action_data.getInputImage1().grayFromGreen(grey);
    action_data.getOutputImage() = grey;
}

void grayFromBlue(ActionData& action_data){
    PPM grey;
    action_data.getInputImage1().grayFromBlue(grey);
    action_data.getOutputImage() = grey;
}

void grayFromLinearColorimetric(ActionData& action_data){
    PPM grey;
    action_data.getInputImage1().grayFromLinearColorimetric(grey);
    action_data.getOutputImage() = grey;
}

void orangeFilter(ActionData& action_data){
    PPM orange;
    action_data.getInputImage1().orangeFilter(orange);
    action_data.getOutputImage() = orange;
}

void antiAliasFilter(ActionData& action_data){
    PPM antiAliasing;
    int changeValue = getInteger(action_data, "Reduction count? ");
    action_data.getInputImage1().antiAlias(changeValue, antiAliasing);
    action_data.getOutputImage() = antiAliasing;

}