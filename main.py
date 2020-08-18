import re
import os
import tokenize_to_counter

TEST_PATH = "../data/supreme/134.txt"


if __name__ == '__main__':
    counter = tokenize_to_counter.solve(TEST_PATH)
    
