#include "image_menu.h"
#include <iostream>
#include <ctime>
#include <cstdlib>

int main(){
    std::srand(std::time(0));
    int val = imageMenu(std::cin, std::cout);
    return val;
}