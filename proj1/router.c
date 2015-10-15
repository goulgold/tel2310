/*
 * Project 1 of Application of Network (TELCOM 2310)
 * Date: Oct 14 2015
 * Author: Qiming Guo
 * Description: Simulation a simple router with queue<Plug>(neosnippet_expand)
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define INTERVAL 50000
FILE *file_in_q, *file_dropped;
struct Router {
    long pkt_in_q;
    long pkt_dropped;
    long buffer_size;
};

void Event(int in_rate, int out_rate, struct Router* router) {
    int y = rand() % 100;
    int prob_in = 100 * in_rate / (in_rate + out_rate);
    if (y <= prob_in) {
        if (router->pkt_in_q < router->buffer_size) {
            router->pkt_in_q++;
        } else {
            router->pkt_dropped++;
        }
    } else {
        if (router->pkt_in_q > 0) {
             router->pkt_in_q--;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        printf("Parameter: in_rate, out_rate, buffer_size\n");
        exit(1);
    }
    int in_rate = atoi(argv[1]);
    int out_rate = atoi(argv[2]);
    int buffer_size = atoi(argv[3]);
    struct Router router = {0, 0, buffer_size};
    char filename[50];
    sprintf(filename, "./result/%d_%d_%d_in.result", in_rate, out_rate, buffer_size);
    file_in_q = fopen(filename, "w");
    sprintf(filename, "./result/%d_%d_%d_dropped.result", in_rate, out_rate, buffer_size);
    file_dropped = fopen(filename, "w");

    // Start Simulating the events
    srand(in_rate * out_rate * buffer_size);
    for (int i = 0; i < 1000000; ++i) {
        Event(in_rate, out_rate, &router);
        if (i % INTERVAL == 0) {
        fprintf(file_in_q, "(%d, %ld)\n", i, router.pkt_in_q);
        fprintf(file_dropped, "(%d, %ld)\n", i, router.pkt_dropped);
        }
    }
    exit(0);
}
