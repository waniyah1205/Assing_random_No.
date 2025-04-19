import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate and print 10 random numbers in the specified range
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Print the random numbers separated by spaces
    print(" ".join(map(str, random_numbers)))

if __name__ == '__main__':
    main()