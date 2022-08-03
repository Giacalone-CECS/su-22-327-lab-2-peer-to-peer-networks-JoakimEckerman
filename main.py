import zmq, time, pickle, sys

context = zmq.Context()
me = str(sys.argv[1])
s = context.socket(zmq.PUSH) # create a push socket
src = SRC1 if me == '1' else SRC2 # check task source host
prt = PORT1 if me == '1' else PORT2 # check task source port
p1 = "tcp://"+ SRC1 +":"+ PORT1 # address first task source
p2 = "tcp://"+ SRC2 +":"+ PORT2 # address second task source
s.bind(p1) # bind socket to address 1
s.bind(p2) # bind socket to address 2
s.connect(p1) # connect to task source 1
s.connect(p2) # connect to task source 2

while True: # do stuff
    pass
    #workload = random.randint(1, 100) # compute workload
    #s.send(pickle.dumps((me,workload))) # send workload to worker
    #work = pickle.loads(r.recv()) # receive work from a source
    #time.sleep(work[1]*0.01) # pretend to work