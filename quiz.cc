// basic file operations
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main (int argc, char *argv) {
    ifstream quiz;
    quiz.open (*argv[1]);
    string in;
    while ( quiz >> in ){
        cout << in << endl;
    }
    quiz.close();
    return 0;
}
