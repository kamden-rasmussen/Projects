#ifndef _ACTIONDATA_H
#define _ACTIONDATA_H
#include <iostream>
#include "PPM.h"
#include "NumberGrid.h"

class ActionData
{
public:
    ActionData(std::istream& is, std::ostream& os); 
    ~ActionData();
    std::istream& getIS();
    std::ostream& getOS();
    PPM& getInputImage1();
    PPM& getInputImage2();
    PPM& getOutputImage();
    bool getDone() const;
    void setDone();
    NumberGrid& getGrid();
    void setGrid(NumberGrid *grid);
    ColorTable& getTable();


private:

    NumberGrid * mNumberGrid;
    std::istream& inputStream;
    std::ostream& outputStream;
    PPM inputImage1;
    PPM inputImage2;
    PPM outputImage;
    bool quitApplication;
    ColorTable newColorTable;
    
};
#endif