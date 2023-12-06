#include <stdio.h>
#include <omp.h>

#define THREAD_COUNT 16

 
long do_the_hard_part(long time, long record){

    printf("Time: %ld, Record: %ld\n", time, record);

    long out = 0;

    #pragma omp parallel num_threads(THREAD_COUNT) shared(out)
    {
        long no = 0;
        // int thread_no = omp_get_thread_num();
        // long from = (time/THREAD_COUNT) * thread_no;
        // long to = (time/THREAD_COUNT) * (thread_no + 1);
        // printf("Thread %d is looking betweeen %ld and %ld\n", thread_no, from, to);

        #pragma omp for
        for(long i = 0; i < time; i++){

            if((time - i) * i > record){
                no++;
            }
        }

        #pragma omp critical
        {
            out += no;
        }
    }

    return out;
}