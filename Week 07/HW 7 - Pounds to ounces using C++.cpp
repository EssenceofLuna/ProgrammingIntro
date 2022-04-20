/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
//Original code: https://onlinegdb.com/7A0U2O-4I
//Turned in code: https://www.onlinegdb.com/fork/7A0U2O-4I

#include <iostream>

using namespace std;

int main()
{
    double lbs, ounces;
    cout << "Convert lbs to ounces" << endl;
    cout << "How many lbs? >";
    cin >> lbs;
    ounces = lbs * 16;
    cout << "That equals " << ounces << " ounces" << endl;

    return 0;
}

