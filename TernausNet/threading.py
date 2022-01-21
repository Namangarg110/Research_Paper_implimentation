
from queue import Queue
from threading import Thread
  
# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        data = 'str'
        out_q.append(data)
          
# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q
        print(in_q)
        # Process the data
        ...
          
# Create the shared queue and launch both threads
q = []
t1 = Thread(target = consumer, args =(q, ))
t2 = Thread(target = producer, args =(q, ))
t1.start()
t2.start()