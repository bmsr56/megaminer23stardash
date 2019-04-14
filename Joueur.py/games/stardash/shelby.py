from scipy.spatial import distance



# given a list of bodies, return target x, target y
def findTargetMiner(bodies, miner):
    # take a slice of the bodies so we dont move to the sun or our planet
    asteroids = bodies[3:len(bodies)]
    # minerX = miner.x
    # minerY = miner.y


    # find the closest asteroid in the list
    for asteroid in range(len(asteroids)):

        #get the x and the y of the asteroid
        astX = asteroids[asteroid].x
        astY = asteroids[asteroid].y

       # check it against the x and y of our miner
       


# a = (x1, y1)
# b = (x2, y2)
# dst = distance.euclidean(a, b)

