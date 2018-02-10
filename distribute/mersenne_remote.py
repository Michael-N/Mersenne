def mers_list(range_open, range_close):
    def is_prime(num):
        from math import sqrt
        from math import ceil
        num = int(num)
        for i in range(2, (ceil(sqrt(num)) + 1)):
           # print("\n Testing " + str(num))
            if num % i == 0:
                #print("False at " + str(num) + " % " + str(i) + " = " + str(num % i))
                return False
            else:
                x=""#THE CODE DOES NOT WORK WITHOUT THIS....
                #print("Iterating " + str(num) + " % " + str(i) + " = " + str(num % i))
        return True;

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
    return primes

print('loaded');