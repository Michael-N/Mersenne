def range_dist(r_open, r_close, n_dist):
    pre_range = []
    pre_range.extend(range(r_open,r_close))

    length = len(pre_range)
    each_length = int(length/n_dist)
    final_length = int(each_length+(length%n_dist))

    #for debugging
    """
    print("size of range=")
    print(str(length))

    print("length of each dist except final")
    print(str(each_length))

    print("length of final")
    print(str(final_length))
    """
    #creates distributions lists withing list_of_dists
    list_of_dists = []
    for i  in range(1,n_dist+1):
        list_of_dists.append([])

    #calculates all distributions to lists except final
    initial = r_open
    for i in range(0,n_dist-1):
        for x in range(initial, initial+each_length):
            if x == initial:
                list_of_dists[i].extend([x])
            elif x == (initial+each_length-1):
                list_of_dists[i].extend([x+1])
        initial += each_length

    #calculates final distribution of range / n_dist + remainder
    for x in range(initial, initial+final_length):
        if x == initial:
            list_of_dists[n_dist-1].extend([x])
        elif x == (initial+final_length-1):
            list_of_dists[n_dist-1].extend([x+1])
    print("")
    return list_of_dists

"""
r_open = int(input("open range?\n"))
r_close = int(input("close range?\n"))+1
n_dist = int(input("Times to distribute?\n"))
"""
