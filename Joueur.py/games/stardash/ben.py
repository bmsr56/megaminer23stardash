def find_mine_return(bodies, miner):
    # find the best asteroid for miner
    targetX, targetY = findBestAsteroidforMiner(bodies, miner)


    # execute move returned from move to target if diff not zero
    # if dif zero, mine and keep moving
    # 

def create_raven_party(player):
    """Creates a raven party (1 miner, 1 martyr, 1 corvette) if available.
    """
    # Martyrs cost 150
    # Corvettes cost 100
    # Miners cost 100
    
    # NOTE Check to see if a raven party needs to be balanced

    # corvettes = 0
    # martyrs = 0
    # for unit in player.units:
    #     if unit.job.title == 'corvette':
    #         corvettes += 1
    #     if unit.job.title == 'martyr':
    #         martyrs += 1
    # if corvettes <= martyrs:
    #     if player.money >= 100:
    #         # create corvette
    #         player.home_base.spawn(
    #             player.home_base.x, player.home_base.y, 'corvette')
    # else:
    #     if player.money >= 150:
    #         player.home_base.spawn(
    #             player.home_base.x, player.home_base.y, 'martyr')
    
    # NOTE Create all at once otherwise
    if player.money >= 350:
        player.home_base.spawn(
            player.home_base.x, player.home_base.y, 'corvette')
        player.home_base.spawn(
            player.home_base.x, player.home_base.y, 'martyr')
        player.home_base.spawn(
            player.home_base.x, player.home_base.y, 'miner')
    return

def escort_sparrow():
    # if at least 1 corvette and 1 martyr
    # find nearest sparrow and move to it
    # once in proximity to sparrow, follow it

