#include <stdio.h>
#include <omp.h>
#define CONV_COUNT 7
#define MAX_VALUE 100000000 //100.000.000
#define THREAD_COUNT 16

long convert(long source[], long dest[], long range_size[], int arr_size, long input){
    //printf("dest: %ld, source: %ld, range_size: %ld\n", dest[1], source[1], range_size[1]);
    for(int i = 0; i < arr_size; i++){
        if(input < source[i] || input >= source[i] + range_size[i]) continue;
        //printf("input %ld is in range %ld - %ld and gets mapped to %ld\n", input, source[i], source[i] + range_size[i], input + dest[i] - source[i]);
        return input + dest[i] - source[i];
    }       
    //printf("input %ld is not in any range\n", input);
    return input;
}

long do_the_hard_part(long source[], long dest[], long range_size[], int arr_sizes[], long seed_ranges[], int seed_ranges_len){
    
    int sdr_len = 0;//This calculates the length of the three arrays
    for(int i = 0; i < CONV_COUNT; i++){
        sdr_len += arr_sizes[i];
    }

    long global_minimum = MAX_VALUE;

    // for(int i = 0; i < seed_ranges_len; i += 2){
    //     printf("seed_range: %ld - %ld\n", seed_ranges[i], seed_ranges[i+1]);
    // }
    #pragma omp parallel num_threads(THREAD_COUNT) shared(global_minimum)
    {
        short done = 0;

        int thread_no = omp_get_thread_num();
        int from = (MAX_VALUE/THREAD_COUNT) * thread_no;
        int to = (MAX_VALUE/THREAD_COUNT) * (thread_no + 1);
        //printf("Thread %d is looking betweeen %i and %i\n", thread_no, from, to);
        for(int i = from; i < to; i++){
            
            long seed = i;
            int current_index = sdr_len - arr_sizes[CONV_COUNT - 1];
            for(int j = CONV_COUNT - 1; j >= 0; j--){
                seed = convert(&dest[current_index], &source[current_index], &range_size[current_index], arr_sizes[j], seed);
                //printf(" %ld", seed);
                if(j > 0) current_index -= arr_sizes[j - 1];
            }

            //printf("location_no: %d, seed: %ld\n", i, seed);

            for(int j = 0; j < seed_ranges_len; j += 2){
                if(seed >= seed_ranges[j] && seed < seed_ranges[j+1]){
                    //printf("Thread %d found a seed in range %ld - %ld. Its location is %d\n", thread_no, seed_ranges[j], seed_ranges[j+1], i);

                    #pragma omp critical
                    {
                        if(i < global_minimum) global_minimum = i;
                    }

                    done = 1;
                    break;
                };
            }
            if(done) break;
        }
        //if(!done) printf("Thread %d did not find a seed in range\n", thread_no);
    }

    return global_minimum;
}

