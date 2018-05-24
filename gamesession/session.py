#-*- coding: utf-8 -*-

class GameSession:

    def __init__(self):
        self.gamesessionID = GenerateGameSessionID()
        self.objectlist = GenerateObjectSpawn()
        self.ennemylist = GenerateEnemySpawn()
        self.playerlist = {}

    
