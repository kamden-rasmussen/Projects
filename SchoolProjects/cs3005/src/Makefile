all: questions_3 hello ascii_image image_file four_square ppm_menu
objects = MenuData.o ActionData.o image_drawing.o image_output.o controllers.o user_io.o Image.o PPM.o image_filters.o NumberGrid.o ColorTable.o ComplexFractal.o JuliaSet.o MandelbrotSet.o ThreadedGrid.o
headers = ActionData.h image_menu.h Image.h MenuData.h PPM.h NumberGrid.h ColorTable.h ComplexFractal.h JuliaSet.h MandelbrotSet.h ThreadedGrid.h

CXXFLAGS = -Wall -Werror -Wpedantic -std=c++11 -Wextra -g

# ---Hello World---
hello: hello.o
	g++ -pthread $(CXXFLAGS) -o hello hello.o

hello.o: hello.cpp
	g++ $(CXXFLAGS) -c hello.cpp

# ---Q's 3---
questions_3: questions_3.o $(objects)
	g++ -pthread $(CXXFLAGS) -o questions_3 $^

questions_3.o: questions_3.cpp $(headers)
	g++ $(CXXFLAGS) -c questions_3.cpp

controllers.o: controllers.cpp 
	g++ $(CXXFLAGS) -c controllers.cpp 

user_io.o: user_io.cpp $(headers)
	g++ $(CXXFLAGS) -c user_io.cpp 

# ---ASCII Image---
ascii_image: ascii_image.o $(objects)
	g++ -pthread $(CXXFLAGS) -o ascii_image $^

ascii_image.o: ascii_image.cpp $(headers)
	g++ $(CXXFLAGS) -c ascii_image.cpp 

image_drawing.o: image_drawing.cpp $(headers)
	g++ $(CXXFLAGS) -c image_drawing.cpp

image_output.o: image_output.cpp $(headers)
	g++ $(CXXFLAGS) -c image_output.cpp

Image.o: Image.cpp $(headers)
	g++ $(CXXFLAGS) -c Image.cpp 

# ---Image File---
image_file: image_file.o $(objects)
	g++ -pthread $(CXXFLAGS) -o image_file $^

image_file.o: image_file.cpp $(headers)
	g++ $(CXXFLAGS) -c image_file.cpp

PPM.o: PPM.cpp $(headers)
	g++ $(CXXFLAGS) -c PPM.cpp

# ---Four Square---
four_square:four_square.o $(objects)
	g++ -pthread $(CXXFLAGS) -o four_square $^

four_square.o: four_square.cpp $(headers)
	g++ $(CXXFLAGS) -c four_square.cpp

# ---Menu and Action Data

MenuData.o: MenuData.cpp $(headers)
	g++ $(CXXFLAGS) -c MenuData.cpp

ActionData.o: ActionData.cpp $(headers)
	g++ $(CXXFLAGS) -c ActionData.cpp

# ---ppm menu----
ppm_menu: ppm_menu.o $(objects)
	g++ -pthread $(CXXFLAGS) -o ppm_menu $^

ppm_menu.o: ppm_menu.cpp $(headers)
	g++ $(CXXFLAGS) -c ppm_menu.cpp

# ---image filters---
image_filters.o: image_filters.cpp $(headers)
	g++ $(CXXFLAGS) -c image_filters.cpp

# ---NumberGrid---
NumberGrid.o: NumberGrid.cpp $(headers)
	g++ $(CXXFLAGS) -c NumberGrid.cpp

ColorTable.o: ColorTable.cpp $(headers)
	g++ $(CXXFLAGS) -c ColorTable.cpp

# ---ComplexFractal---
ComplexFractal.o: ComplexFractal.cpp $(headers)
	g++ $(CXXFLAGS) -c ComplexFractal.cpp

# ---JuliaSet---
JuliaSet.o: JuliaSet.cpp $(headers)
	g++ $(CXXFLAGS) -c JuliaSet.cpp

MandelbrotSet.o: MandelbrotSet.cpp $(headers)
	g++ $(CXXFLAGS) -c MandelbrotSet.cpp

ThreadedGrid.o: ThreadedGrid.cpp $(headers)
	g++ $(CXXFLAGS) -c ThreadedGrid.cpp

clean: 
	-rm -f *.o
	-rm -f .*.swp
	-rm -f *.gch
	-rm -f *.json
	-rm -r .vscode
	-rm -f *.gch
	-rm questions_3	
	-rm hello
	-rm ascii_image
	-rm -f *.ppm
	-rm image_file
	-rm four_square
	-rm ppm_menu


