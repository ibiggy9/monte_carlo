import numpy as np
from matplotlib import pyplot
from multiprocessing import Process
import seaborn as sns
import pickle
import threading

#Globals 
lists = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
final_list = []
minimum = 0
maximum = 0
mode =  0
runs = 0

def inputs():
    global minimum
    global maximum
    global runs
    global mode
    

    maximum = int(input("What is the maximum value of your estimate?\n"))
    minumum = int(input("What is the minimum value of your estimate?\n"))
    mode = int(input("What is the most frequent number you'd expect to see? \n"))
    runs = int(input("How many runs would you like?\n"))
    



def monte_carlo():
    global lists
    for i in range(runs):
        monte = np.random.triangular(minimum, mode, maximum)
        lists.append(monte)    

    else:
        with open('dump.pkl', 'wb') as l:
            pickle.dump(lists, l)

def monte_carlo2():
    global l2
    for i in range(runs):
        monte = np.random.triangular(minimum, mode, maximum)
        l2.append(monte)    

    else:
        with open('dump2.pkl', 'wb') as l2:
            pickle.dump(l2, l2)
            
def monte_carlo3():
    global l3
    for i in range(runs):
        monte = np.random.triangular(minimum, mode, maximum)
        l3.append(monte)    

    else:
        with open('dump.pkl', 'wb') as l3:
            pickle.dump(l3, l3)

def monte_carlo4():
    global l4
    for i in range(runs):
        monte = np.random.triangular(minimum, mode, maximum)
        l4.append(monte)    

    else:
        with open('dump.pkl', 'wb') as l4:
            pickle.dump(l4, l4)


def monte_carlo5():
    global l5
    for i in range(runs):
        monte = np.random.triangular(minimum, mode, maximum)
        l5.append(monte)    

    else:
        with open('dump.pkl', 'wb') as l5:
            pickle.dump(l5, l5)

def monte_carlo6():
    global l6
    for i in range(runs):
        monte = np.random.triangular(minimum, mode, maximum)
        l6.append(monte)    

    else:
        with open('dump.pkl', 'wb') as l6:
            pickle.dump(l6, l6)                        

def combined():
    global final_list
    with open('dump.pkl', 'rb') as l:
        lists = pickle.load(l)
    
    with open('dump.pkl', 'rb') as l2:
        l2 = pickle.load(l2)

    with open('dump.pkl', 'rb') as l3:
        l3 = pickle.load(l3)

    with open('dump.pkl', 'rb') as l4:
        l4 = pickle.load(l4)

    with open('dump.pkl', 'rb') as l5:
        l5 = pickle.load(l5)

    with open('dump.pkl', 'rb') as l6:
        l6 = pickle.load(l6)
    
    final_list = lists+l2+l3+l4+l5+l6
    print(len(final_list))

def finish():
    
    #pyplot.hist(lists, bins=20)
    #pyplot.show()
    sns.set()
    pyplot.xlabel("Metric We Care About")
    pyplot.ylabel("Frequency")
    pyplot.hist(final_list, bins=20)
    pyplot.show()        



def execute():

    thread = threading.Thread(target=inputs)
    thread.start()
    thread.join()
    p1 = Process(target=monte_carlo)
    p2 = Process(target=monte_carlo)
    p3 = Process(target=monte_carlo)
    p4 = Process(target=monte_carlo)
    p5 = Process(target=monte_carlo)
    p6 = Process(target=monte_carlo)


    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()

    combined()
    finish()   


execute()
