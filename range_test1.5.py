import math

r_open = int(input("open range?\n"))
r_close = int(input("close range?\n"))+1
n_dist = int(input("Times to distribute?\n"))
pre_range = []
pre_range.extend(range(r_open,r_close))

length = len(pre_range)
each_length = int(length/n_dist)
final_length = int(each_length+(length%n_dist))

print("size of range=")
print(str(length))

print("length of each dist except final")
print(str(each_length))

print("length of final")
print(str(final_length))

print("")
list_of_dists = []
for i  in range(1,n_dist+1):
    print(str(i))
    list_of_dists.append([])
"""
x = 1
for item_list in list_of_dists:
    item_list.append(x)
    print(item_list)
    x+=1
"""
print(list_of_dists)
#print(str(pre_range))

initial = r_open
for i in range(0,n_dist-1):
    print("item index")
    print(str(i))
    for x in range(initial, initial+each_length):
        list_of_dists[i].extend([x])
    print(list_of_dists[i])
    initial += each_length

#print(list_of_dists[n_dist-1])
