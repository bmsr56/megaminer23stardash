
# Defensive logic

def create_ravens(player):
    """
    """
    # Martyrs cost 150
    acceptableAmount = 5
    if len() < acceptableAmount:
        # NOTE here's an assumption that the following line evaluates the amount of 'money'
        # the player has that can be spent on ships
        # If resources available
        if player.money >= 150:
            # create martyr
            player.home_base.spawn(player.home_base.x, player.home_base.y, 'martyr')
            # move martyr to defense line

def escort_sparrows():
    