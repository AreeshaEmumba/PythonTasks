import time
import asyncio
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

async def async_find_divisibles(in_range, divisor):
    start_time = time.time()
    logging.info(f"async_find_divisibles called with range {in_range} and divisor {divisor}")
    
    result = []
    for i in range(1, in_range + 1):
        if i % divisor == 0:
            result.append(i)
        
        # Yield control less frequently (e.g., every 1000 iterations)
        if i % 1000 == 0:
            await asyncio.sleep(0)
    
    end_time = time.time()
    logging.info(f"async_find_divisibles ended with range {in_range} and divisor {divisor}. It took {end_time - start_time} seconds")
    
    return result


async def main():
    start_time = time.time()
    
    # Create async tasks
    task1 = asyncio.create_task(async_find_divisibles(50800000, 34113))
    task2 = asyncio.create_task(async_find_divisibles(100052, 3210))
    task3 = asyncio.create_task(async_find_divisibles(500, 3))
    
    # Await the tasks and print the results for the second and third task
    await task1
    result2 = await task2
    print(f"Result of second call: {result2}")
    
    result3 = await task3
    print(f"Result of third call: {result3}")
    
    total_time = time.time() - start_time
    print(f"Total execution time: {total_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())
