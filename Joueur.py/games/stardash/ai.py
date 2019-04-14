# This is where you build your AI for the Stardash game.

from joueur.base_ai import BaseAI

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
            print('\ncount: ', count)
            count += 1
            targetX, targetY = findTarget(miner)

            x, y = moveToTarget(miner, targetX, targetY)
            if x > 32:
                x = 32
            if y > 32:
                y = 32
            # miner.move(x, y)
            miner.move(miner.x+64, miner.y+y)



        print(sun.x, sun.y)
        # miner.move(miner.x + 1, miner.y)
        
        if self.game.current_turn > 4:
            quit = 4/0

        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>

# NOTE how to spawn a piece
# call self.player.home_base.body.spawn(x, y, title)

def moveToCenter(unit):
    xCenter = 1600
    yCenter = 900
    
    # if we are on the left side
    if xCenter < unit.x:
        x = math.sqrt(unit.x - xCenter)
        y = math.sqrt(unit.y - yCenter)
    else:
        x = math.sqrt(unit.x + xCenter)
        y = math.sqrt(unit.y + yCenter)

    return x, y

def moveToTarget(unit, targetX, targetY):
    print('unit\t', unit.x, unit.y)
    print('target\t', targetX, targetY)
    xDiff = targetX - unit.x
    yDiff = targetY - unit.y
    print('diff:', xDiff, yDiff)
    try:
        theta = math.tan(float(xDiff)/float(yDiff))
    except ZeroDivisionError:
        theta = 0
    targetX = MAX_MOVE * math.acos(theta)
    targetY = MAX_MOVE * math.asin(theta)
    return targetX, targetY

def findTarget(unit):
    return 500, 900