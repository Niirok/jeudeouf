#-*- coding: utf-8 -*-

import threading

class ParseMessageWorker(threading.Thread):
    """
        Ajoute deux nombres l'un à l'autre et retourne
        le résultat.
    """
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.messagetoparse = message

    def run(self):
        #TODO put here the method to parse messages
        print(self.messagetoparse)