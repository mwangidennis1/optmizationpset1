###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import os

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):

    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows= open(filename,'r')
       
    d={}
    for i in cows:

        y=i.split(",")
        #print(y)
        d[y[0]] = int(y[1])
    #print(d)
    #print(dir({}))
    return d

    
p=load_cows("ps1_cow_data.txt")
print(p)
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    output=[]
    def  getItems(item):
        return item[1];
    
    cowsSorted = sorted(cows.items(),key=getItems,reverse=True)
    # function to call the trips
    def trips(cowsSorted,limit):
        weight=0
        q=[]
        for i in cowsSorted:
            if i[1] + weight <= limit:
                weight += i[1]
                q.append(i[0])
        return q
    #to kill of elements
    while len(cowsSorted) > 0:
        c= trips(cowsSorted,limit)
        output.append(c)

        if c:

            for i in c:
                for j in cowsSorted:
                    if  i == j[0]:
                        cowsSorted.remove(j)

    return output
#o=greedy_cow_transport(p)
#print(o)
# Problem 3

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    output = []
    worstcase = len(cows)
    print(worstcase)
    for i in (get_partitions(cows)):
        weight = 0
        for j in i:
            tempw=0
            for p in j:
                tempw += cows[p]
                if tempw > weight:
                    weight = tempw

        if weight <= limit:
            if len(i) < worstcase:
                output=[]
                worstcase = len(i)
                output.append(i)
            elif len(i) == worstcase:
                output.append(i)
    return output
                 
        



v=brute_force_cow_transport(p,limit)  
print(v) 

       
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
