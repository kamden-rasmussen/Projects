#include "MenuData.h"
#include <string>
#include <vector>

MenuData::MenuData(){

}

void MenuData::addAction(const std::string& name, ActionFunctionType func, const std::string& description){
    menuVector.push_back(name);
    actionFuction[name] = func;
    commandDescription[name] = description;
}
//Append name to the collection of names, insert func in the action function map, with name as the key, 
//and insert description into the description map with name as the key.

const std::vector<std::string>&  MenuData::getNames() const{
    return menuVector;
}
ActionFunctionType MenuData::getFunction(const std::string& name){
    if (actionFuction[name]){
        return actionFuction[name];
    }
    else{
        return 0;
    }
}
const std::string& MenuData::getDescription(const std::string& name){
    static std::string uhh = "";
    if (commandDescription[name].empty()){
        return uhh;
    }
    else{
        return commandDescription[name];
    }
}