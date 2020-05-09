import numpy as np
from matplotlib import pyplot
from multiprocessing import Process
import seaborn as sns
import pandas as pd
import pickle
import threading


class Setup:
    def __init__(self):
        self.x = False

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
    runs = 167
    range_output = 0

    bin10v = 1
    bin20v = 0
    bin30v = 0
    bin40v = 0
    bin50v = 0
    bin60v = 0
    bin70v = 0
    bin80v = 0
    bin90v = 0
    bin100v = 0

    bin10l = []
    bin20l = []
    bin30l = []
    bin40l = []
    bin50l = []
    bin60l = []
    bin70l = []
    bin80l = []
    bin90l = []
    bin100l = []


    rangebin10 = 0
    rangebin20 = 0
    rangebin30 = 0
    rangebin40 = 0
    rangebin50 = 0
    rangebin60 = 0
    rangebin70 = 0
    rangebin80 = 0
    rangebin90 = 0
    rangebin100 = 0
    

attempt_1 = Setup()

def inputs():
    attempt_1.maximum = int(input("What is the maximum value of your estimate?\n"))
    attempt_1.minimum = int(input("What is the minimum value of your estimate?\n"))
    attempt_1.mode = int(input("What is the most frequent number you'd expect to see? \n"))
    

def monte_carlo():
    for i in range(attempt_1.runs):
        monte = np.random.triangular(attempt_1.minimum, attempt_1.mode, attempt_1.maximum)
        attempt_1.lists.append(monte)    

    else:
        with open('dump.pkl', 'wb') as l:
            pickle.dump(attempt_1.lists, l)

def monte_carlo2():
    for i in range(attempt_1.runs):
        monte = np.random.triangular(attempt_1.minimum, attempt_1.mode, attempt_1.maximum)
        attempt_1.l2.append(monte)    

    else:
        with open('dump2.pkl', 'wb') as attempt_1.l2:
            pickle.dump(attempt_1.l2, attempt_1.l2)
            
def monte_carlo3():
    for i in range(attempt_1.runs):
        monte = np.random.triangular(attempt_1.minimum, attempt_1.mode, attempt_1.maximum)
        attempt_1.l3.append(monte)    

    else:
        with open('dump.pkl', 'wb') as attempt_1.l3:
            pickle.dump(attempt_1.l3, attempt_1.l3)

def monte_carlo4():
    for i in range(attempt_1.runs):
        monte = np.random.triangular(attempt_1.minimum, attempt_1.mode, attempt_1.maximum)
        attempt_1.l4.append(monte)    

    else:
        with open('dump.pkl', 'wb') as attempt_1.l4:
            pickle.dump(attempt_1.l4, attempt_1.l4)


def monte_carlo5():
    for i in range(attempt_1.runs):
        monte = np.random.triangular(attempt_1.minimum, attempt_1.mode, attempt_1.maximum)
        attempt_1.l5.append(monte)    

    else:
        with open('dump.pkl', 'wb') as attempt_1.l5:
            pickle.dump(attempt_1.l5, attempt_1.l5)

def monte_carlo6():
    for i in range(attempt_1.runs):
        monte = np.random.triangular(attempt_1.minimum, attempt_1.mode, attempt_1.maximum)
        attempt_1.l6.append(monte)    

    else:
        with open('dump.pkl', 'wb') as attempt_1.l6:
            pickle.dump(attempt_1.l6, attempt_1.l6)                        

def combined():
    with open('dump.pkl', 'rb') as l:
        attempt_1.lists = pickle.load(l)
    
    with open('dump.pkl', 'rb') as attempt_1.l2:
        attempt_1.l2 = pickle.load(attempt_1.l2)

    with open('dump.pkl', 'rb') as attempt_1.l3:
        attempt_1.l3 = pickle.load(attempt_1.l3)

    with open('dump.pkl', 'rb') as attempt_1.l4:
        attempt_1.l4 = pickle.load(attempt_1.l4)

    with open('dump.pkl', 'rb') as attempt_1.l5:
        attempt_1.l5 = pickle.load(attempt_1.l5)

    with open('dump.pkl', 'rb') as attempt_1.l6:
        attempt_1.l6 = pickle.load(attempt_1.l6)
    
    attempt_1.final_list = attempt_1.lists+attempt_1.l2+attempt_1.l3+attempt_1.l4+attempt_1.l5+attempt_1.l6
   

def analysis():
    attempt_1.range_output = attempt_1.maximum - attempt_1.minimum
    
    #pyplot.hist(attempt_1.lists, bins=20)
    #pyplot.show()

    attempt_1.bin10v = round(attempt_1.range_output*0.1) + attempt_1.minimum
    attempt_1.bin20v = round(attempt_1.range_output*0.2) + attempt_1.minimum 
    attempt_1.bin30v = round(attempt_1.range_output*0.3) + attempt_1.minimum
    attempt_1.bin40v = round(attempt_1.range_output*0.4) + attempt_1.minimum
    attempt_1.bin50v = round(attempt_1.range_output*0.5) + attempt_1.minimum
    attempt_1.bin60v = round(attempt_1.range_output*0.6) + attempt_1.minimum
    attempt_1.bin70v = round(attempt_1.range_output*0.7) + attempt_1.minimum
    attempt_1.bin80v = round(attempt_1.range_output*0.8) + attempt_1.minimum
    attempt_1.bin90v = round(attempt_1.range_output*0.9) + attempt_1.minimum
    attempt_1.bin100v = round(attempt_1.range_output) + attempt_1.minimum
    
    

    attempt_1.rangebin10 = range(0, attempt_1.bin10v)
    attempt_1.rangebin20 = range(attempt_1.bin10v, attempt_1.bin20v)
    attempt_1.rangebin30 = range(attempt_1.bin20v, attempt_1.bin30v)
    attempt_1.rangebin40 = range(attempt_1.bin30v, attempt_1.bin40v)
    attempt_1.rangebin50 = range(attempt_1.bin40v, attempt_1.bin50v)
    attempt_1.rangebin60 = range(attempt_1.bin50v, attempt_1.bin60v)
    attempt_1.rangebin70 = range(attempt_1.bin60v, attempt_1.bin70v)
    attempt_1.rangebin80 = range(attempt_1.bin70v, attempt_1.bin80v)
    attempt_1.rangebin90 = range(attempt_1.bin80v, attempt_1.bin90v)
    attempt_1.rangebin100 = range(attempt_1.bin90v, attempt_1.bin100v)


    for i in attempt_1.final_list:
        if i < attempt_1.bin10v:
            attempt_1.bin10l.append(i)
        elif i < attempt_1.bin20v and i > attempt_1.bin10v:
            attempt_1.bin20l.append(i)
        elif i < attempt_1.bin30v and i > attempt_1.bin20v:
            attempt_1.bin30l.append(i)
        elif i < attempt_1.bin40v and i > attempt_1.bin30v:
            attempt_1.bin40l.append(i) 
        elif i < attempt_1.bin50v and i > attempt_1.bin40v:
            attempt_1.bin50l.append(i)
        elif i < attempt_1.bin60v and i > attempt_1.bin50v:
            attempt_1.bin60l.append(i)
        elif i < attempt_1.bin70v and i > attempt_1.bin60v:
            attempt_1.bin70l.append(i)
        elif i < attempt_1.bin80v and i > attempt_1.bin70v:
            attempt_1.bin80l.append(i)
        elif i < attempt_1.bin90v and i > attempt_1.bin80v:
            attempt_1.bin90l.append(i)
        elif i < attempt_1.bin100v and i > attempt_1.bin90v:
            attempt_1.bin100l.append(i)
        

    prob10 = (len(attempt_1.bin10l)/(attempt_1.runs*6))*100
    prob20 = (len(attempt_1.bin20l)/(attempt_1.runs*6))*100
    prob30 = (len(attempt_1.bin30l)/(attempt_1.runs*6))*100
    prob40 = (len(attempt_1.bin40l)/(attempt_1.runs*6))*100
    prob50 = (len(attempt_1.bin50l)/(attempt_1.runs*6))*100
    prob60 = (len(attempt_1.bin60l)/(attempt_1.runs*6))*100
    prob70 = (len(attempt_1.bin70l)/(attempt_1.runs*6))*100
    prob80 = (len(attempt_1.bin80l)/(attempt_1.runs*6))*100
    prob90 = (len(attempt_1.bin90l)/(attempt_1.runs*6))*100
    prob100 = (len(attempt_1.bin100l)/(attempt_1.runs*6))*100

    print(f"The probability of the result being between 0 and {attempt_1.bin10v} is {prob10}%")
    print(f"The probability of the result being between {attempt_1.bin10v} and {attempt_1.bin20v} is {prob20}%")
    print(f"The probability of the result being between {attempt_1.bin20v} and {attempt_1.bin30v} is {prob30}%")
    print(f"The probability of the result being between {attempt_1.bin30v} and {attempt_1.bin40v} is {prob40}%")
    print(f"The probability of the result being between {attempt_1.bin40v}  and {attempt_1.bin50v} is {prob50}%")
    print(f"The probability of the result being between {attempt_1.bin50v} and {attempt_1.bin60v} is {prob60}%")
    print(f"The probability of the result being between {attempt_1.bin60v} and {attempt_1.bin70v} is {prob70}%")
    print(f"The probability of the result being between {attempt_1.bin70v} and {attempt_1.bin80v} is {prob80}%")
    print(f"The probability of the result being between {attempt_1.bin80v} and {attempt_1.bin90v} is {prob90}%")
    print(f"The probability of the result being between {attempt_1.bin90v} and {attempt_1.bin100v} is {prob100}%")

    sns.set()
    pyplot.xlabel("Metric We Care About")
    pyplot.ylabel("Frequency")
    pyplot.hist(attempt_1.final_list, bins=20)
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
    analysis()   


execute()