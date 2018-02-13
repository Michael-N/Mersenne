from math import sqrt
from math import ceil
from datetime import datetime, timedelta
from time import time
now = datetime.now()
file_name = "mersenne_log_%s-%s-%s_%s.%s.%s.txt" %(str(now.month), str(now.day), str(now.year), str(now.hour), str(now.minute), str(now.second))
### DEFINING FUNCTIONS --> ORDER MATTERS! FUNCTIONS CALL EACH OTHER! ###
def is_prime(num):
    from math import sqrt
    from math import ceil
    num = int(num)
    for i in range(2, (ceil(sqrt(num))+1)):
        print("\n Testing " + str(num))
        if num % i == 0:
            print("False at " + str(num) + " % " + str(i) + " = " + str(num%i) )
            return False
        else:
            print("Iterating " + str(num) + " % " + str(i) + " = "+ str(num%i) )
    return True

def mers_seq(range_open, range_close):
    i = range_open
    range_close -= 1
    num_primes = 0
    current_time = "%s-%s-%s %s:%s:%s" % (str(now.month), str(now.day), str(now.year), str(now.hour), str(now.minute), str(now.second))
    print(current_time, file=open(file_name, "w"))
    print("Finding primes in range ["+str(range_open)+","+str(range_close)+"]", file=open(file_name, "a"))
    while i <= range_close:
        if i % 2 == 1 or i == 2:
            if is_prime(i) == True:
                num_primes += 1
                try:
                    print(i, file=open(file_name, "a"))
                    print(i)
                except:
                    print(i)
        i += 1
    try:
        print(str(num_primes) + " primes found!", file = open(file_name, "a"))
        print(str(num_primes) + " primes found!")
    except:
        print(str(num_primes) + " primes found!")


def mers_list(range_open, range_close):
    primes = []
    test_list = range(range_open, range_close)
    test_odds = [item for item in test_list if item % 2 ==1]
    if 2 in range(range_open, range_close):
        primes.append(2)
    for item in test_odds:
        if is_prime(item) == True:
            primes.append(item)
    print(str(len(primes)) + " primes found!")
    return primes

def elapsed_time(start_time, end_time):
    duration = end_time-start_time
    elapsed = timedelta(seconds = duration).__str__()
    return elapsed
### USER INTERFACE TO CALL FUNCTIONS ###
print("Welcome to the Mersenne Prime Number Calculator! This will calculate all prime numbers in the determined range.")
range_open, range_close = input("Input beginning and end range values, separated only by spaces:\n").split()
range_open = int(range_open)
range_close = int(range_close)+1
test_number = range_open
user_input = input("Would you like to store calulated primes to a list and return at the end,\n \
or print as each is found and store to log file?\n (options: list or sequential) ")
if user_input not in ["list", "sequential", "ls", "seq"]:
    print("Invalid selection!")
if user_input == "list" or user_input == "ls":
    print("list")
    start_time = time()
    print(mers_list(range_open, range_close))
    end_time = time()
    print("Elapsed time: " + str(elapsed_time(start_time,end_time)))
if user_input == "sequential" or user_input == "seq":
    print("seq")
    start_time = time()
    mers_seq(range_open, range_close)
    end_time = time()
    print("Elpased time: " + str(elapsed_time(start_time, end_time)), file=open(file_name, "a"))
    print("Elapsed time: " + str(elapsed_time(start_time, end_time)))







#try me!
#20988936657440586486151264256610222593863921
