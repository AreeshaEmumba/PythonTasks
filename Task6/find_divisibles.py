import time
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def find_divisibles(in_range, divisor):
    start_time = time.time()
    logging.info(f"find_divisibles called with range {in_range} and divisor {divisor}")
    
    result = [i for i in range(1, in_range + 1) if i % divisor == 0]
    
    end_time = time.time()
    logging.info(f"find_divisibles ended with range {in_range} and divisor {divisor}. It took {end_time - start_time} seconds")
    
    return result

def main():
    start_time = time.time()
    
    # First call
    find_divisibles(50800000, 34113)
    
    # Second call
    result2 = find_divisibles(100052, 3210)
    print(f"Result of second call: {result2}")
    
    # Third call
    result3 = find_divisibles(500, 3)
    print(f"Result of third call: {result3}")
    
    total_time = time.time() - start_time
    print(f"Total execution time: {total_time} seconds")

if __name__ == "__main__":
    main()
