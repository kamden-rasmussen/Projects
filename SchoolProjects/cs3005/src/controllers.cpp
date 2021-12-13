#include <iostream>
#include <string>
#include "image_menu.h"
#include "Image.h"
#include "PPM.h"
#include "MenuData.h"

int assignment1( std::istream& is, std::ostream& os ){
    ActionData action_data(is, os);
    int val = askQuestions3(action_data);
    return val;
}

int assignment2(std::istream& is, std::ostream& os ){
    ActionData action_data(is, os);

    diagonalQuadPattern(action_data);
    copyImage(action_data);
    drawAsciiImage(action_data);
    return 0;
}

int assignment3( std::istream& is, std::ostream& os ){  
    ActionData action_data(is, os);

    stripedDiagonalPattern(action_data);
    copyImage(action_data);
    writeUserImage(action_data);
    return 0;
}

int four_square( std::istream& is, std::ostream& os ){
    ActionData action_data(is, os);

    fourSquarePattern(action_data);
    copyImage(action_data);
    writeUserImage(action_data);
    return 0;
}

void showMenu( MenuData& menu_data, ActionData& action_data ){
    std::vector<std::string> name = menu_data.getNames();
    for( std::vector<std::string>::iterator i = name.begin(); i != name.end(); i++){
        std::string name = *i;
        action_data.getOS() << name << ") " << menu_data.getDescription(name) << std::endl;
    }

}
//For each command that was added to MenuData via addAction(), displays one line of text to the output stream of the ActionData. 
//The lines are formatted like this: “command-name) command description”. See the ShowMenu() example below.

void takeAction(const std::string& choice, MenuData& menu_data, ActionData& action_data){
    if( menu_data.getFunction(choice) != 0){
        //ActionFunctionType
        menu_data.getFunction(choice)(action_data);
    }
    else if( choice == "menu" ){
        showMenu(menu_data, action_data);
    }
    else{
        action_data.getOS() << "Unknown action '" << choice << "'." << std::endl;
    }
}


void configureMenu( MenuData& menu_data ){
    menu_data.addAction("draw-ascii", drawAsciiImage, "Write output image to terminal as ASCII art.");
    menu_data.addAction("write", writeUserImage, "Write output image to file.");
    menu_data.addAction("copy", copyImage, "Copy input image 1 to output image.");
    menu_data.addAction("read1", readUserImage1, "Read file into input image 1.");
    menu_data.addAction("#", commentLine, "Comment to end of line.");
    menu_data.addAction("size", setSize, "Set the size of input image 1.");
    menu_data.addAction("max-color-value", setMaxColorValue, "Set the max color value of input image 1.");
    menu_data.addAction("channel", setChannel, "Set a channel value in input image 1.");
    //menu_data.addAction("pixel", setPixel, "Set a pixel\u0027s 3 values in input image 1.");
    menu_data.addAction("pixel", setPixel, "Set a pixel's 3 values in input image 1.");
    
    //what is going on.
    menu_data.addAction("clear", clearAll, "Set all pixels to 0,0,0 in input image 1.");
    menu_data.addAction("quit", quit, "Quit.");

    //PPM Opperators
    menu_data.addAction("read2", readUserImage2, "Read file into input image 2.");
    menu_data.addAction("+", plus, "Set output image from sum of input image 1 and input image 2.");
    menu_data.addAction("+=", plusEquals, "Set input image 1 by adding in input image 2.");
    menu_data.addAction("-", minus, "Set output image from difference of input image 1 and input image 2.");
    menu_data.addAction("-=", minusEquals, "Set input image 1 by subtracting input image 2.");
    menu_data.addAction("*", times, "Set output image from input image 1 multiplied by a number.");
    menu_data.addAction("*=", timesEquals, "Set input image 1 by multiplying by a number.");
    menu_data.addAction("/", divide, "Set output image from input image 1 divided by a number.");
    menu_data.addAction("/=", divideEquals, "Set input image 1 by dividing by a number.");

    //image filters
    menu_data.addAction("red-gray", grayFromRed, "Set output image by grayscale from red on input image 1.");
    menu_data.addAction("green-gray", grayFromGreen, "Set output image by grayscale from green on input image 1.");
    menu_data.addAction("blue-gray", grayFromBlue, "Set output image by grayscale from blue on input image 1.");
    menu_data.addAction("linear-gray", grayFromLinearColorimetric, "Set output image by linear colorimetric grayscale on input image 1.");
    menu_data.addAction("circle", drawCircle, "Draw a circle shape in input image 1.");
    menu_data.addAction("box", drawBox, "Draw a box shape in input image 1.");

    //draw square
    menu_data.addAction("square", drawSquare, "Draw a square shape in input image 1.");

    //draw orange
    menu_data.addAction("orange", orangeFilter, "Set output image from orange filter on input image 1.");

    //number grid
    menu_data.addAction("grid", configureGrid, "Configure the grid.");
    menu_data.addAction("grid-set", setGrid, "Set a single value in the grid.");
    menu_data.addAction("grid-apply", applyGrid, "Use the grid values to set colors in the output image.");

    //color table
    menu_data.addAction("set-color-table-size", setColorTableSize, "Change the number of slots in the color table.");
    menu_data.addAction("set-color", setColor, "Set the RGB values for one slot in the color table.");
    menu_data.addAction("set-random-color", setRandomColor, "Randomly set the RGB values for one slot in the color table.");
    menu_data.addAction("set-color-gradient", setColorGradient, "Smoothly set the RGB values for a range of slots in the color table.");
    menu_data.addAction("grid-apply-color-table", applyGridColorTable, "Use the grid values to set colors in the output image using the color table.");

    //Complex Fractal
    menu_data.addAction("fractal-plane-size", setFractalPlaneSize, "Set the dimensions of the grid in the complex plane.");
    menu_data.addAction("fractal-calculate", calculateFractal, "Calculate the escape values for the fractal.");

    //JuliaSet
    menu_data.addAction("julia-parameters", setJuliaParameters, "Set the parameters of the Julia Set function.");
    menu_data.addAction("complex-fractal", setComplexFractal, "Choose to make a complex plane.");
    menu_data.addAction("julia", setJuliaFractal, "Choose to make a Julia set.");

    //Mandelbrot Set
    menu_data.addAction("mandelbrot", setMandelbrotFractal, "Choose to make a Mandelbrot set.");

    //Julia Set Four
    menu_data.addAction("julia-four", setJuliaFourFractal, "Choose to make a Julia set with the fourth power function.");

    //zoom Factor
    menu_data.addAction("fractal-zoom", zoomPlane, "Zoom in or out of the complex plane.");

    //Threaded Grid
    //menu_data.addAction("fractal-calculate", calculateFractal, "Calculate the escape values for the fractal.");
    menu_data.addAction("fractal-calculate-single-thread", calculateFractalSingleThread, "Calculate the escape values for the fractal, single-thread.");
    
    //AntiAliasing
    menu_data.addAction("anti-alias", antiAliasFilter, "Set output image from Anti-alias filter on input image 1.");
    menu_data.addAction("copyo1", copyOutputImageToImage1, "Copy output image to input image 1.");
}

int imageMenu(std::istream& is, std::ostream& os){
    ActionData action_data(is, os);
    MenuData menu_data;
    configureMenu(menu_data);
    
    //NumberGrid *tempNumGrid = new NumberGrid;
    ComplexFractal *complexfractal = new ComplexFractal;
    action_data.setGrid(complexfractal);

    while(not action_data.getDone() && action_data.getIS().good()){
        std::string choice = getChoice(action_data);
        takeAction(choice, menu_data, action_data);
    }
    return 0;
}

void setComplexFractal( ActionData& action_data ){
    ComplexFractal *complexfractal = new ComplexFractal;
    action_data.setGrid(complexfractal);
}

void setJuliaFractal( ActionData& action_data ){
    JuliaSet *juliaSet = new JuliaSet;
    action_data.setGrid(juliaSet);
}

void setMandelbrotFractal( ActionData& action_data ){
    MandelbrotSet *mandelbrotSet = new MandelbrotSet;
    action_data.setGrid(mandelbrotSet);
}

void setJuliaFourFractal(ActionData& action_data){
    JuliaSetFour *juliaSetFour = new JuliaSetFour;
    action_data.setGrid(juliaSetFour);
}
