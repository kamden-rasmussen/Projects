#ifndef _MENUDATA_H
#define _MENUDATA_H
#include "ActionData.h"
#include <iostream>
#include <map>

typedef void (*ActionFunctionType)(ActionData& action_data);

class MenuData
{
private:
    std::vector<std::string> menuVector;
    std::map<std::string, ActionFunctionType> actionFuction;
    std::map<std::string,std::string> commandDescription;
public:
    MenuData();
    void addAction(const std::string& name, ActionFunctionType func, const std::string& description);
    const std::vector<std::string>& getNames() const;
    ActionFunctionType getFunction(const std::string& name); 
    const std::string& getDescription(const std::string& name); 
};

#endif