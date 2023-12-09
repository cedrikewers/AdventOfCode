#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <string.h>

short is_end_node(short* node, short* end_nodes, int end_nodes_len){
    for(short* end_node = end_nodes; end_node < end_nodes + end_nodes_len; end_node++){
        if(*node == *end_node){
            return 1;            
        }
    }
    return 0;
}

short all_zs(short* current_nodes, int current_nodes_len, short* end_nodes, int end_nodes_len){
    for(short* current_node = current_nodes; current_node < (current_nodes + current_nodes_len); current_node++){
        if(!is_end_node(current_node, end_nodes, end_nodes_len)){
            return 0;
        }
    }
    return 1;
}

void print_current_nodes(short* current_nodes, int current_nodes_len){
    for(short* current_node = current_nodes; current_node < current_nodes + current_nodes_len; current_node++){
        printf("%hd, ", *current_node);
    }
    printf("\n");
}

long do_the_hard_part(short* directions, int directions_len, short* nodes, int nodes_len, short* start_nodes, int start_nodes_len,short* end_nodes, int end_nodes_len){

    // for(short* direction = directions; direction < directions + directions_len; direction++){
    //     printf("%s", *direction == 1 ? "R" : "L");
    // }
    // printf("\n");

    // for(short* node = nodes; node < nodes + nodes_len; node += 2){
    //     printf("(%hd, %hd), ", *node, *(node + 1));
    // }
    // printf("\n");

    // for(short* start_node = start_nodes; start_node < start_nodes + start_nodes_len; start_node++){
    //     printf("%hd, ", *start_node);
    // }
    // printf("\n");

    // for(short* end_node = end_nodes; end_node < end_nodes + end_nodes_len; end_node++){
    //     printf("%hd, ", *end_node);
    // }
    // printf("\n");

    short* current_nodes = malloc(start_nodes_len * sizeof(short));
    memcpy(current_nodes, start_nodes, start_nodes_len * sizeof(short));
    //print_current_nodes(current_nodes, start_nodes_len);    


    return 0L;
}