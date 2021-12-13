#ifndef _IMAGE_MENU_H
#define _IMAGE_MENU_H

#include <iostream>
#include <string>
#include "Image.h"
#include "PPM.h"
#include "MenuData.h"
#include "NumberGrid.h"
#include "ComplexFractal.h"
#include "JuliaSet.h"
#include "MandelbrotSet.h"

std::string getString( ActionData& action_data, const std::string& prompt );

int getInteger( ActionData& action_data, const std::string& prompt );

double getDouble( ActionData& action_data, const std::string& prompt );

int askQuestions3(ActionData& action_data);

int assignment1( std::istream& is, std::ostream& os );

//Ascii Image
void drawAsciiImage(ActionData& action_data);

void diagonalQuadPattern( ActionData& action_data );

int assignment2( std::istream& is, std::ostream& os );

//DrawImage
void writeUserImage( ActionData& action_data );

void stripedDiagonalPattern( ActionData& action_data );

int assignment3( std::istream& is, std::ostream& os );

//FourSquare
void fourSquarePattern( ActionData& action_data );

int four_square( std::istream& is, std::ostream& os );

//PPM Menu
std::string getChoice( ActionData& action_data );

void commentLine( ActionData& action_data ); 

void quit(ActionData& action_data);

void setSize( ActionData& action_data );

void setMaxColorValue( ActionData& action_data );

void setChannel( ActionData& action_data );

void setPixel( ActionData& action_data ); 

void clearAll( ActionData& action_data );

void copyImage(ActionData& action_data);

void readUserImage1( ActionData& action_data );

void showMenu( MenuData& menu_data, ActionData& action_data );

void takeAction(const std::string& choice, MenuData& menu_data, ActionData& action_data);

void configureMenu( MenuData& menu_data );

int imageMenu(std::istream& is, std::ostream& os);

//PPM Opperators
void plusEquals( ActionData& action_data ); //Modifies input image 1 by adding input image 2 to it.

void minusEquals( ActionData& action_data ); //Modifies input image 1 by subtracting input image 2 from it.

void timesEquals( ActionData& action_data ); //Modifies input image 1 by multiplying it by the double obtained by calling getDouble with a prompt of “Factor? “.

void divideEquals( ActionData& action_data ); //Modifies input image 1 by dividing it by the double obtained by calling getDouble with a prompt of “Factor? “.

void plus( ActionData& action_data ); //Sets output image to be the sum of input image 1 and input image 2.

void minus( ActionData& action_data ); //Sets output image to be the difference of input image 1 and input image 2.

void times( ActionData& action_data ); //Sets output image to input image1 times the double obtained by calling getDouble with a prompt of “Factor? “.

void divide( ActionData& action_data ); //Sets output image to input image 1 divided by the double obtained by calling getDouble with a prompt of “Factor? “.

void readUserImage2( ActionData& action_data );

//Image Filters
void grayFromRed(ActionData& action_data);

void grayFromGreen(ActionData& action_data);

void grayFromBlue(ActionData& action_data);

void grayFromLinearColorimetric(ActionData& action_data);

void drawCircle(ActionData& action_data); 

void drawBox(ActionData& action_data);

void drawSquare(ActionData& action_data); 

void orangeFilter(ActionData& action_data); 

//number grid
void configureGrid(ActionData& action_data); 

void setGrid(ActionData& action_data);

void applyGrid(ActionData& action_data);

//Color Table
void setColorTableSize(ActionData& action_data);

void setColor(ActionData& action_data); 

void setRandomColor(ActionData& action_data);

void setColorGradient(ActionData& action_data);

void applyGridColorTable(ActionData& action_data);

//Complex Fractal
void setFractalPlaneSize(ActionData& action_data);

void calculateFractal(ActionData& action_data); 

//Julia Set
void setJuliaParameters(ActionData& action_data);

void setComplexFractal( ActionData& action_data );

void setJuliaFractal( ActionData& action_data ); 

//Mandelbrot Set
void setMandelbrotFractal( ActionData& action_data );

//Juia Set Four
void setJuliaFourFractal(ActionData& action_data);

//Zoom Factor
void zoomPlane(ActionData& action_data);

//Threaded Grid
void calculateFractalSingleThread(ActionData& action_data); 

//antiAliasing
void antiAliasFilter(ActionData& action_data);
void copyOutputImageToImage1(ActionData& action_data);

#endif