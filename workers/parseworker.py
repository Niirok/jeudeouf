#-*- coding: utf-8 -*-

import threading
from multiprocessing import Process, Queue

class ParseMessageWorker(threading.Thread):
    """
        Ajoute deux nombres l'un à l'autre et retourne
        le résultat.
    """

def parse_update_mess(message):
    #TODO put here the method to parse messages
    print(message)


def getFlag(message, queue):

    Mess = message.split(" ")
    flagres = ""

    #print(Mess)

    if(Mess[0] == "INIT_MESS"):
        flagres = Mess[1]
        queue.put(flagres)

    elif(Mess[0] == "UPDATE_PLAYER_POS"):
        flagres = Mess[1]+ " " + Mess[2] + " " + Mess[3]
        queue.put(flagres)

    #print(flagres)