#include<NucleonStructure.hpp>


#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <cmath>
#include "constants.hpp"

using namespace std;

int main(int argc, char* argv[]){
    string which_function(argv[1]);
    string parameterization(argv[2]);
    NucleonStructure test_object(parameterization);
    
    double x = strtod(argv[3],NULL);
    double Q2 = strtod(argv[4],NULL);
    bool proton=0;

    if(which_function == "f"){

        double F1=0.,F2=0.;
        test_object.getF_xQ(F1,F2,proton,x,Q2);

        cout  << F1 << " " << F2 << endl;
    }
    else if(which_function == "g"){
        double G1 = test_object.getG1_grsv2000(proton,x,Q2);
        double G1plusg2 = test_object.getG1plusg2_grsv2000(proton,x,Q2);
        double g2 = G1plusg2 - G1;

        cout << G1 << " " << g2 << endl;
    }




}
