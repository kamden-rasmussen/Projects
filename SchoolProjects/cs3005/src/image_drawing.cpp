#include "Image.h"
#include "image_menu.h"
#include <cmath>

void diagonalQuadPattern( ActionData& action_data ){

    int height = getInteger(action_data, "Image height? ");
    int width = getInteger(action_data, "Image width? ");
    //os << height << width;
    action_data.getInputImage1().setWidth(width);
    action_data.getInputImage1().setHeight(height);
    action_data.getInputImage1().setMaxColorValue(255);

    for (int row = 0; row < action_data.getInputImage1().getHeight();row++){
        for (int column = 0; column < action_data.getInputImage1().getWidth();column++){
            
            int channel = 0;
            for (;channel < 3;channel++){
                
                //Red color set
                if(channel == 0){
                    if(row < (action_data.getInputImage1().getHeight() / 2)){
                        action_data.getInputImage1().setChannel(row, column, channel, 0);
                    }
                    else{
                        action_data.getInputImage1().setChannel(row, column, channel, 255);    
                    }
                }

                //Green color Set
                else if(channel == 1){
                    action_data.getInputImage1().setChannel(row, column, channel,( ( (2 * row) + (2 * column) ) % 256));
                }
                
                //Blue color set
                else if(channel == 2){
                    if(column < (action_data.getInputImage1().getWidth() / 2)){
                        action_data.getInputImage1().setChannel(row, column, channel, 0);
                    }
                    else{
                        action_data.getInputImage1().setChannel(row, column, channel, 255);    
                                       
                    }
                }
            }   
        }
    }
}

void stripedDiagonalPattern( ActionData& action_data ){

    int height = getInteger(action_data, "Image height? ");
    int width = getInteger(action_data, "Image width? ");
    action_data.getInputImage1().setWidth(width);
    action_data.getInputImage1().setHeight(height);

    int tempMaxValue = (height + width) / 3 ;

    if( tempMaxValue > 255){
        action_data.getInputImage1().setMaxColorValue(255);
    }
    else{
        action_data.getInputImage1().setMaxColorValue(tempMaxValue);
    }
    for (int row = 0; row < action_data.getInputImage1().getHeight();row++){
        for (int column = 0; column < action_data.getInputImage1().getWidth();column++){
            
            for (int channel = 0;channel < 3;channel++){

                // Red Color Set
                if(channel == 0){
                    if(row < (action_data.getInputImage1().getHeight() / 2)){
                        action_data.getInputImage1().setChannel(row, column, channel, 0);
                    }
                    else if(row >= (action_data.getInputImage1().getHeight() / 2) && row % 3 == 0 ){ // double check logic here
                        action_data.getInputImage1().setChannel(row, column, channel, 0);
                    }
                    else if(row >= (action_data.getInputImage1().getHeight() / 2) && row % 3 != 0){
                        action_data.getInputImage1().setChannel(row, column, channel, action_data.getInputImage1().getMaxColorValue());
                    }
                    else{
                        std::cerr << "Error: red set channel failure \n";
                        break;
                    }
                }

                //Green Color Set
                else if(channel == 1){
                    int greenColor = ((row + width - column - 1) % (action_data.getInputImage1().getMaxColorValue() + 1));
                    action_data.getInputImage1().setChannel(row, column, channel, greenColor);
                }

                //Blue Color Set
                else if(channel == 2){
                    if(column < row){
                        action_data.getInputImage1().setChannel(row, column, channel, 0);
                    }
                    else if (column >= row){
                        action_data.getInputImage1().setChannel(row, column, channel, action_data.getInputImage1().getMaxColorValue());
                    }
                    else{
                        std::cerr << "Error: blue set channel failure \n";
                        break;
                    }

                }

            }

        }

    }

}

void fourSquarePattern( ActionData& action_data ){

    int tempVar = getInteger(action_data, "Image size? ");
    action_data.getInputImage1().setHeight(tempVar);
    action_data.getInputImage1().setWidth(tempVar);
    action_data.getInputImage1().setMaxColorValue(100);

    for (int row = 0; row < action_data.getInputImage1().getHeight();row++){
        for (int column = 0; column < action_data.getInputImage1().getWidth();column++){
            if(row < (action_data.getInputImage1().getHeight() / 2)){
                if(column < action_data.getInputImage1().getWidth() / 2){
                    action_data.getInputImage1().setPixel(row, column, 100, 0, 66 );
                }
                else if( column >= action_data.getInputImage1().getWidth() / 2 ){
                    action_data.getInputImage1().setPixel(row, column, 0, 100, 33 );
                
                }
            }

            else if (row >= action_data.getInputImage1().getHeight() / 2){
                if(column < action_data.getInputImage1().getWidth() / 2){
                    action_data.getInputImage1().setPixel(row, column, 66, 33, 100 );
                }
                else if( column >= action_data.getInputImage1().getWidth() / 2 ){
                    action_data.getInputImage1().setPixel(row, column, 33, 66, 0 );
                
                }

            }       

        }
    }

}

void setSize( ActionData& action_data ){
    int height = getInteger(action_data, "Height? ");
    int width = getInteger(action_data, "Width? ");
    action_data.getInputImage1().setWidth(width);
    action_data.getInputImage1().setHeight(height);
    
}

void setMaxColorValue( ActionData& action_data ){
    int tempMaxValue = getInteger(action_data, "Max color value? ");
    action_data.getInputImage1().setMaxColorValue(tempMaxValue);
}

void setChannel( ActionData& action_data ){
    int row = getInteger(action_data, "Row? ");
    int column = getInteger(action_data, "Column? ");
    int channel = getInteger(action_data, "Channel? ");
    int value = getInteger(action_data, "Value? ");
    action_data.getInputImage1().setChannel(row, column, channel, value);
}

void setPixel( ActionData& action_data ){
    int row = getInteger(action_data, "Row? ");
    int column = getInteger(action_data, "Column? ");
    int red = getInteger(action_data, "Red? ");
    int green = getInteger(action_data, "Green? ");
    int blue = getInteger(action_data, "Blue? ");
    action_data.getInputImage1().setPixel(row, column,red, green, blue);
}

void clearAll( ActionData& action_data ){
    for (int row = 0; row < action_data.getInputImage1().getHeight();row++){
        for (int column = 0; column < action_data.getInputImage1().getWidth();column++){
            action_data.getInputImage1().setPixel(row, column, 0, 0, 0);
        }
    }
}

//Image Filters

void drawCircle(ActionData& action_data){
    int centerRow = getInteger(action_data, "Center Row? ");
    int centerColumn = getInteger(action_data, "Center Column? ");
    int radius = getInteger(action_data, "Radius? ");
    int red = getInteger(action_data, "Red? ");
    int green = getInteger(action_data, "Green? ");
    int blue = getInteger(action_data, "Blue? ");
    //double distance; = sqrt((x2 + x1) ** - (y2 - y1) **);

    int row, col;
    for(row = centerRow - radius; row <= centerRow + radius; row++){
        for(col = centerColumn - radius; col <= centerColumn + radius; col++){
            double distance = std::abs( sqrt(( ( row - centerRow ) * ( row - centerRow ) ) + ( ( col - centerColumn ) * ( col - centerColumn ) )) );
            if(distance <= radius){
                action_data.getInputImage1().setPixel(row, col, red, green, blue);
            }
            else{
                std::cerr << distance;
            }
        }
    }

    // int startRow = centerRow - radius;
    // int endRow = centerRow + radius;
    // int startColumn = centerColumn - radius;
    // int endColumn = centerColumn + radius;

    // if(startRow < 0){
    //     startRow = 0;
    // }
    // if(endRow > action_data.getInputImage1().getWidth()){
    //     endRow = action_data.getInputImage1().getHeight();
    // }

    // if(startColumn < 0){
    //     startColumn = 0;
    // }
    // if(endColumn > action_data.getInputImage1().getHeight()){
    //     endColumn = action_data.getInputImage1().getHeight();
    // }
    
    // for(;startRow <= endRow; startRow++){
    //     for(;startColumn <= endColumn; startColumn++){
    //         distance = sqrt(((startColumn + centerColumn) * (startColumn + centerColumn)) - ((startRow + centerRow) * (startRow + centerRow)));
    //         if( distance <= radius){
    //             action_data.getInputImage1().setPixel(startRow, startColumn, red, green, blue);
    //         }
    //     }
    // }
}

void drawBox(ActionData& action_data){
    int topRow = getInteger(action_data, "Top Row? ");
    int leftColumn = getInteger(action_data, "Left Column? ");
    int bottomRow = getInteger(action_data, "Bottom Row? ");
    int rightColumn = getInteger(action_data, "Right Column? ");
    int red = getInteger(action_data, "Red? ");
    int green = getInteger(action_data, "Green? ");
    int blue = getInteger(action_data, "Blue? ");

    int row, col;
    for(row = topRow; row <= bottomRow;row++){
        for(col = leftColumn; col <= rightColumn; col++){
        action_data.getInputImage1().setPixel(row, col, red, green, blue);
        }
   }
}

void drawSquare(ActionData& action_data){
    int startRow = getInteger(action_data, "Row? ");
    int startColumn = getInteger(action_data, "Column? ");
    int size = getInteger(action_data, "Size? ");
    int red = getInteger(action_data, "Red? ");
    int green = getInteger(action_data, "Green? ");
    int blue = getInteger(action_data, "Blue? ");

    int halfSize = size / 2;

    int row, col;
    for(row = startRow - halfSize; row <= startRow + halfSize;row++){
        for(col = startColumn - halfSize; col <= startColumn + halfSize; col++){
            action_data.getInputImage1().setPixel(row, col, red, green, blue);

        }
    }
}

void configureGrid(ActionData& action_data){
    int height = getInteger(action_data, "Grid Height? ");
    int width = getInteger(action_data, "Grid Width? ");
    int maxColor = getInteger(action_data, "Grid Max Value? ");
    
    action_data.getGrid().setGridSize(height, width);
    action_data.getGrid().setMaxNumber(maxColor);
}

void setGrid(ActionData& action_data){
    int row = getInteger(action_data, "Grid Row? ");
    int column = getInteger(action_data, "Grid Column? ");
    int value = getInteger(action_data, "Grid Value? ");

    action_data.getGrid().setNumber(row, column, value);
}

void applyGrid(ActionData& action_data){
    action_data.getGrid().setPPM(action_data.getOutputImage());
}

void setColorTableSize(ActionData& action_data){
    int size = getInteger(action_data, "Size? ");
    action_data.getTable().setNumberOfColors(size);
}

void setColor(ActionData& action_data){
    int position = getInteger(action_data, "Position? ");
    int red = getInteger(action_data, "Red? ");
    int green = getInteger(action_data, "Green? ");
    int blue = getInteger(action_data, "Blue? ");

    action_data.getTable()[position].setRed(red);
    action_data.getTable()[position].setGreen(green);
    action_data.getTable()[position].setBlue(blue);
}

void setRandomColor(ActionData& action_data){
    int position = getInteger(action_data, "Position? ");
    action_data.getTable().setRandomColor(255, position);
}

void setColorGradient(ActionData& action_data){
    int firstPosition = getInteger(action_data, "First position? ");
    int firstRed = getInteger(action_data, "First red? ");
    int firstGreen = getInteger(action_data, "First green? ");
    int firstBlue = getInteger(action_data, "First blue? ");    

    int secondPosition = getInteger(action_data, "Second position? ");
    int secondRed = getInteger(action_data, "Second red? ");
    int secondGreen = getInteger(action_data, "Second green? ");
    int secondBlue = getInteger(action_data, "Second blue? ");    

    Color color1(firstRed, firstGreen, firstBlue);
    Color color2(secondRed, secondGreen, secondBlue);

    action_data.getTable().insertGradient(color1, color2, firstPosition, secondPosition);

}

void applyGridColorTable(ActionData& action_data){
    action_data.getGrid().setPPM(action_data.getOutputImage(), action_data.getTable());
}

void setFractalPlaneSize(ActionData& action_data){
    double minX = getDouble(action_data, "Min X? ");
    double maxX = getDouble(action_data, "Max X? ");
    double minY = getDouble(action_data, "Min Y? ");
    double maxY = getDouble(action_data, "Max Y? ");

    ComplexFractal *test = dynamic_cast<ComplexFractal *>(&action_data.getGrid());

    if(test != 0){
        //int height = abs(maxY) - abs(minY);
        //int width = abs(maxX) - abs(minX);
        //action_data.getGrid().setGridSize(height, width);
        test->setPlaneSize(minX, maxX, minY, maxY);

    }
    else{
        action_data.getOS() << "Not a ComplexFractal object. Can't set plane size.";
    }
}

void calculateFractal(ActionData& action_data){
    action_data.getGrid().calculateAllNumbers();
}

void setJuliaParameters(ActionData& action_data){
    double paramA = getDouble(action_data, "Parameter a? ");
    double paramB = getDouble(action_data, "Parameter b? ");

    JuliaSet *test = dynamic_cast<JuliaSet *>(&action_data.getGrid());

    if(test != 0){
        test->setParameters(paramA, paramB);
    }
    else{
        action_data.getOS() << "Not a JuliaSet object. Can't set parameters.";
    }
}

//Zoom Factor
void zoomPlane(ActionData& action_data){
    double zoomFactor = getDouble(action_data, "Zoom Factor? ");

    ComplexFractal *test = dynamic_cast<ComplexFractal *>(&action_data.getGrid());

    if(test !=0){
        test->zoomPlane(zoomFactor);
    }
}

void calculateFractalSingleThread(ActionData& action_data){
    action_data.getGrid().NumberGrid::calculateAllNumbers();
}