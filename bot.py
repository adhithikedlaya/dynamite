from random import randint

moves = ['R', 'P', 'S']



def make_move(previous_rounds):
    dynamites_used = count_dynamites("p1", previous_rounds)
    if dynamites_used < 100:
        return 'D'
    return moves[randint(0,2)]

def count_dynamites(player, previous_rounds):
    dynamites = 0
    for round in previous_rounds:
        if round[player] == "D":
            dynamites += 1
    return dynamites
