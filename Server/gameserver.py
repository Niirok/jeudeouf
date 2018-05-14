#-*- coding: utf-8 -*-

import zmq

import workers.parseworker

context = zmq.Context()

publishsocket = context.socket(zmq.PUB)
publishsocket.bind("tcp://*:12345")

receivesocket = context.socket(zmq.PULL)
receivesocket.bind("tcp://*:12346")

while True:
    received_message = receivesocket.recv_string()# blocking call

    workerthread = workers.parseworker.ParseMessageWorker(received_message)
    workerthread.start()

    #publishsocket.send(worker.result)
