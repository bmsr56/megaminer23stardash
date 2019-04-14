from scipy.spatial import distance

#modify this to stay within 64 units

# given a list of bodies, return target x, target y
def findTargetforMiner(bodies, miner):
    # take a slice of the bodies so we dont move to the sun or our planet
    asteroids = bodies[3:len(bodies)]
    minerX = miner.x
    minerY = miner.y

    bestTargetX = 0
    bestTargetY = 0
    bestDist = 10000 # infinity

    # find the closest asteroid in the list
    for asteroid in range(len(asteroids)):

        #get the x and the y of the asteroid
        astX = asteroids[asteroid].x
        astY = asteroids[asteroid].y

        # check it against the x and y of our miner
        minerCoord = (minerX,minerY)
        astCoord = (astX, astY)
        dist = distance.euclidean(minerCoord, astCoord)
        
        #save this as a new dist, if this distance is smaller than previous dist, update it and save the asteroid x y
        if dist < bestDist:
            bestTargetX = astX
            bestTargetY = astY
            bestDist = dist

    return bestTargetX,bestTargetY


