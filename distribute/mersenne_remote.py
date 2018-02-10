def mers_list(range_open, range_close):
    from datetime import datetime, timedelta
    from time import time
    def elapsed_time(start_time, end_time):
        duration = end_time - start_time
        elapsed = timedelta(seconds=duration).__str__()
        return elapsed
    def is_prime(num):
        from math import sqrt
        from math import ceil
        num = int(num)
        for i in range(2, (ceil(sqrt(num)) + 1)):
           # print("\n Testing " + str(num))
            if num % i == 0:
                print("False at " + str(num) + " % " + str(i) + " = " + str(num % i))
                return False
            else:
                x=""#THE CODE DOES NOT WORK WITHOUT THIS....
                print("Iterating " + str(num) + " % " + str(i) + " = " + str(num % i))
        return True;

    now = time()
    primes = []
    test_list = range(range_open, range_close)
    test_odds = [item for item in test_list if item % 2 ==1]
    if 2 in range(range_open, range_close):
        primes.append(2)
    for item in test_odds:
        #print("IN LOOP")
        if is_prime(item) == True:
            primes.append(item)
    #print(str(len(primes)) + " primes found!")
    endOfC = time()

    delTime = elapsed_time(now,endOfC)
    ret =  [primes,delTime]
    return ret

print('loaded');