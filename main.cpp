#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    int rdnum1, rdnum2, rdnum3;
    int total = 0;

    // TODO: seed the random number generator with time(0)
    srand(time(0));

    // TODO: generate 3 random numbers between 0 and 99
    rdnum1 = rand() % 100;
    rdnum2 = rand() % 100;
    rdnum3 = rand() % 100;

    // TODO: compute the total summation
    total = rdnum1 + rdnum2 + rdnum3;

    // TODO: print the 3 random numbers on the first line
    cout << rdnum1 << " " << rdnum2 << " " << rdnum3 << endl;

    // TODO: print the total and average (integer division) on the second line
    cout << total << " " << total / 3 << endl;

    return 0;
}
