#include <stdio.h>
#include <stdlib.h>

int main() {
    double EstimatedRTT = 90.0;
    double DevRTT = 25.0;
    double TimeoutInterval;
    double a = 0.1;
    double b = 0.25;
    for (int i = 0; i < 100; ++i) {
        EstimatedRTT = (1-a)*EstimatedRTT + a*200.0;
        DevRTT = (1-b)*DevRTT + b*abs(200.0 - EstimatedRTT);
        TimeoutInterval = EstimatedRTT + 4.0*DevRTT;
        printf("After #%d measured, TimeoutInterval: %f\n", i, TimeoutInterval);
    }
    return 0;
}
