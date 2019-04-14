# This is where you build your AI for the Stardash game.

from joueur.base_ai import BaseAI
from scipy.spatial import distance

import math


# CONSTANTS
MAX_MOVE = 64

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Stardash. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.stardash.game.Game
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.stardash.player.Player
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "TheBirdsOfWar" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        # <<-- /Creer-Merge: start -->>

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are
        tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and
            dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won
            or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    
    def run_turn(self):

        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for runTurn

        # NOTE We start with 3 miners on our home planet
        
        # Organize our units so that we can manipulate them easier
        miners = []
        transports = []
        corvettes = []
        martyrs = []
        missileboats = []

        for unit in self.player.units:
            if unit.job.title == 'miner':
                miners.append(unit)
            elif unit.job.title == 'transport':
                transports.append(unit)
            elif unit.job.title == 'corvette':
                corvettes.append(unit)
            elif unit.job.title == 'martyr':
                martyrs.append(unit)
            elif unit.job.title == 'missileboat':
                missileboats.append(unit)
        
        
        # Move a miner
        miner = miners[0]
        vpAsteroid = self.game.bodies[4]
        sun = self.game.bodies[2]

        # move all the miners to the belt
        count = 0
        for miner in miners:
            needMine = False
            body = None


            x, y, body = findBestAsteroidforMiner(self.game.bodies, miner)

            if checkFullPayload(miner):
                # if payload is full go home
                x, y = getHomeValue(miner)
            else: 
                # means still has room to mine
                # head to "target location" -> closer to the asteroid belt
                print('miner.x: ', miner.x)
                if miner.x > 1600:
                    # this is the right side
                    print('miner.x: ', miner.x)
                    if miner.x < 2000:
                        print('looking for best asteroid -> right')
                        x, y, body = findBestAsteroidforMiner(self.game.bodies, miner)
                        needMine = True 
                        print('x:', x, '  y:', y)
                    else:
                        x, y = getAdvanceCoords(miner, 2000, 900)
                else:                     
                    # this is the left side
                    if miner.x > 1350:
                        print('looking for best asteroid -> left')
                        x, y, body = findBestAsteroidforMiner(self.game.bodies, miner)
                        needMine = True 
                    else:
                        x, y = getAdvanceCoords(miner, 1350, 900)
                        
            # make the miner move 
            miner.move(miner.x+x, miner.y+y)
            if needMine:
                miner.mine(body)
                print('asteroid has been mined!!!')
                print(miner.genarium + miner.legendarium + miner.mythicite + miner.rarium)

        if self.game.current_turn > 1:
            quit = 4/0

        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>

# NOTE how to spawn a piece
# call self.player.home_base.body.spawn(x, y, title)

# def mod_x(player, val):
#     """
#     """
#     if player.home_base.x < 1600:
        # we're on the left side, so return val
        # return val
    # else:
        #  return -val

def getAdvanceCoords(unit, targetX, targetY):
    # print('unit\t', unit.x, unit.y)
    # print('target\t', targetX, targetY)
    xDiff = targetX - unit.x
    yDiff = targetY - unit.y
    # print('diff:', xDiff, yDiff)
    theta = math.tan(float(yDiff)/float(xDiff))
    # print('theta:', theta)
    moveToX = MAX_MOVE * math.cos(theta)
    moveToY = MAX_MOVE * math.sin(theta)
    # print('moveTo:', moveToX, moveToY)
    if targetX < unit.x:
        moveToX *= -1
    return moveToX, moveToY

def checkFullPayload(miner):
    return 20 == (miner.genarium + miner.legendarium + miner.mythicite + miner.rarium)

# given a list of bodies, return target x, target y
def findBestAsteroidforMiner(bodies, miner):
    print("Attempting to find Best")
    # take a slice of the bodies so we dont move to the sun or our planet
    asteroids = bodies[3:len(bodies)]
    minerX = miner.x
    minerY = miner.y
    
    possibleTargets = []
    bestAsteroid = None
    bestValue = 0

    lowX = 100000
    highX = 0

    # find the asteroids in the list that are possible to move to in this turn
    for asteroid in range(len(asteroids)):

        #get the x and the y of the asteroid
        astX = asteroids[asteroid].x
        astY = asteroids[asteroid].y

        if astX > highX:
            highX = astX
        if astX < lowX:
            lowX = astX


        # check it against the x and y of our miner
        minerCoord = (minerX,minerY)
        astCoord = (astX, astY)
        dist = distance.euclidean(minerCoord, astCoord)
        
        #save this as a new dist, if this distance is smaller than previous dist, update it and save the asteroid x y
        if dist < 64:
            possibleTargets.append(asteroids[asteroid])

    print('\nlowest and highest ast values:', lowX, highX, '\n')

    for asteroid in range(len(possibleTargets)):
        #find the asteroid with the highest value, if equivalent, find the shorter distance one
        print(possibleTargets[asteroid].amount)
        print(possibleTargets[asteroid].material_type)
        #print the amount of whatever is on there
        # if bestValue < possibleTargets[asteroid].amount:
        #     bestValue = possibleTargets[asteroid].amount
        #     bestTargetX = possibleTargets[asteroid].x
        #     bestTargetY = possibleTargets[asteroid].y
        if possibleTargets[asteroid].material_type == 'mythicite':
            value = 1000
        elif possibleTargets[asteroid].material_type == 'legendarium':
            value = 10
        elif possibleTargets[asteroid].material_type == 'rarium':
            value = 5
        elif possibleTargets[asteroid].material_type == 'generium':
            value = 2
        
        if bestValue < value:
            bestValue = value
            bestTargetX = possibleTargets[asteroid].x
            bestTargetY = possibleTargets[asteroid].y
            bestAsteroid = possibleTargets[asteroid]
    
    return bestTargetX,bestTargetY, bestAsteroid

# returns x and y to go to to get home
def getHomeValue(miner):
    pass
    # move to the player's home
    print("\nthis is home base:", miner.owner.home_base, '\n')

    return 0, 0
    
         
    
