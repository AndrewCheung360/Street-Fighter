from settings import *

def createFighterState(playerId, name):
    return {
        "id": playerId,
        "name": name,
        "score" : 1,
        "health" : MAX_HEALTH,
    }