#ifndef _THREADEDGRID_H_
#define _THREADEDGRID_H_
#include <vector>
#include "NumberGrid.h"
#include "ThreadedVector.h"

class ThreadedGrid: public NumberGrid
{
private:
    ThreadedVector<int> mThreadedVector;

public:
    ThreadedGrid();
    ThreadedGrid(const int& height, const int& width); 
    virtual ~ThreadedGrid();
    virtual void calculateAllNumbers();
    virtual void worker();

};

#endif
