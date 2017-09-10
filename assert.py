BET = 25
def eat_piece():
    pass

def eat_ravioly(helping):
    """
    Devour the helping
    :param helping:
    :type list
    :return: number of eaten pieces
    :type int
    """

    if len(helping) < 25:
        raise ValueError('Недостаточно пельмений!')

    # Your code goes here.
    pieces = 0
    for __ in helping:
        pieces -= 1

    assert pieces >= 0
    return pieces

def announce_winner(eaten_pieces):
    if eaten_pieces < 25:
        print ('Grandmom win')
    else:
        print ('Grandson win')
# Your code goes here.
helping_for_grandson = ["piece" for __ in range(25)]
eaten_pieces = eat_ravioly(helping_for_grandson)
announce_winner(eaten_pieces)