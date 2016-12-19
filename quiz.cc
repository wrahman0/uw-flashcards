// basic file operations
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void readFile(string *filename) {
    cout << "Reading: " << filename << endl;

    ifstream quiz;
    quiz.open(filename);
    string in;

    while ( quiz >> in ){
        cout << in << endl;
    }

    quiz.close();
}

int main (int argc, char **argv) {
    cout << argv[1] << endl;
    // if (argc >= 2) readFile(argv[1]);
    return 0;
}
