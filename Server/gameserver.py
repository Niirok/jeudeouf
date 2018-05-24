#-*- coding: utf-8 -*-

import zmq
import workers.parseworker

from multiprocessing.pool import ThreadPool
from multiprocessing import  Queue


TIMEOUT = 100000

context = zmq.Context()

pool = ThreadPool(processes=1)
Messq = Queue()

publishsocket = context.socket(zmq.PUB)
publishsocket.bind("tcp://*:12345")

receivesocket = context.socket(zmq.PULL)
receivesocket.bind("tcp://*:23456")

SessionList = {}

while True:
    poller = zmq.Poller()
    poller.register(receivesocket, zmq.POLLIN)
    event = dict(poller.poll(TIMEOUT))

    if event:
        if event.get(receivesocket) == zmq.POLLIN:
            received_message = receivesocket.recv_string()# blocking call
            #print("message received "+ received_message)
            result = pool.apply_async(workers.parseworker.getFlag(received_message, Messq))#, [received_message])
            React = Messq.get()
            print("THIS IS OUTSIDE THE THREAD " + React)
    else:
        print("Nothing yet")

    #publishsocket.send(worker.result)
