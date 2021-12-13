#include "ThreadedGrid.h"
#include <thread>
#include <vector>

ThreadedGrid::ThreadedGrid(){
}

ThreadedGrid::ThreadedGrid(const int& height, const int& width)
: NumberGrid(height, width){

}

ThreadedGrid::~ThreadedGrid(){
}

void ThreadedGrid::calculateAllNumbers(){  
    std::vector<std::thread> threads;

    unsigned int max_cores = std::thread::hardware_concurrency();
    unsigned int i;
    
    int row;
    for(row = 0; row < getHeight(); row++) {
        mThreadedVector.push_back(row);
    }

    for(i = 0; i < max_cores; i++) {
        threads.push_back(std::thread(&ThreadedGrid::worker, this));
    }

    for(i = 0; i < threads.size(); i++) {
        threads[i].join();
    }
}

void ThreadedGrid::worker(){
    std::vector<int> this_workers_tasks;

    while(mThreadedVector.size() > 0) {
        this_workers_tasks.resize(0);
        mThreadedVector.pop_back(this_workers_tasks, 1);
        
        if(this_workers_tasks.size() > 0){
            int row = this_workers_tasks[0];

            for(int column = 0; column < getWidth(); column++) {

                double val = calculateNumber(row, column);
                setNumber(row, column, val);

            } 
        }
    }
}