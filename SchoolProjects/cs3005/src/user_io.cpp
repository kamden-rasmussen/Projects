#include <iostream>
#include <string>
#include "image_menu.h"


std::string getString( ActionData& action_data, const std::string& prompt ){
    std::string userInput = "";

    action_data.getOS() << prompt ;
    action_data.getIS() >> userInput;

    return userInput ;
}

int getInteger( ActionData& action_data, const std::string& prompt ){
    int userInput = 0;

    action_data.getOS() << prompt;
    action_data.getIS() >> userInput;

    return userInput ;
}

double getDouble( ActionData& action_data, const std::string& prompt ){
    double userInput = 0.0;

    action_data.getOS() << prompt ;
    action_data.getIS() >> userInput;

    return userInput ;
}

int askQuestions3(ActionData& action_data){

    int i;

    std::string givenStr = getString(action_data, "What is your favorite color? " );

    int givenInt = getInteger( action_data, "What is your favorite integer? ");

    double givenDbl = getDouble( action_data, "What is your favorite number? ");

    if(givenInt > 0){    
        for(i = 0; i < givenInt; i++){
            action_data.getOS() << i + 1 <<  " " << givenStr <<  " " << givenDbl << std::endl;
        }
        //while( i < givenInt ){
        //    std::cout<< givenInt <<  " " << givenStr <<  " " << givenDbl << std::endl;
        //    i += 1;
        //}
    }
    
    return givenInt;
}

std::string getChoice( ActionData& action_data ){
    std::string choice = getString(action_data, "Choice? " );
    return choice;
}
//Uses getString to ask the user for a string, using “Choice? ” as the prompt. Returns the value returned by getString()

void commentLine( ActionData& action_data ){

    bool continueIfFalse = false;
    unsigned char isByte;
    while(not continueIfFalse){
        action_data.getIS().read((char *) &isByte, 1);
        if(not action_data.getIS().good() || isByte == '\n'){
            continueIfFalse = true;
        }
    }
    return;
}   

//Uses .read() to read a single character at a time from the input stream. If the input stream is .good() after the read, and if the character read is not the newline character, repeat. 
//Otherwise return. In other words, read from the input stream until the input stream has nothing to read, or a newline character is read. Do not do anything with the characters read.

void quit(ActionData& action_data){
    action_data.setDone();
}
//Set the ActionData object to be done
