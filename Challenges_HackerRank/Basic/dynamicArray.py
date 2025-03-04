# HackerRank Mode:

import os

def processQueries(num_sequences, queries):
    sequences = [[] for _ in range(num_sequences)] 
    previous_result = 0  
    output_results = []  

    for query in queries:
        operation, index_value, data_value = query
        target_index = (index_value ^ previous_result) % num_sequences 

        if operation == 1:
            sequences[target_index].append(data_value)  
        elif operation == 2:
            chosen_list = sequences[target_index]  
            previous_result = chosen_list[data_value % len(chosen_list)]  
            output_results.append(previous_result)  

    return output_results  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_input = input().rstrip().split()
    num_sequences = int(first_input[0])
    num_queries = int(first_input[1])

    query_list = [list(map(int, input().rstrip().split())) for _ in range(num_queries)]

    final_result = processQueries(num_sequences, query_list)

    fptr.write('\n'.join(map(str, final_result)) + '\n')

    fptr.close()
