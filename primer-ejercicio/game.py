from random import randint
from enum import Enum

class Coin(Enum):
    HEADS = 0
    TAILS = 1

def flip_coin():
    return randint(0,1)

def bet(bet_amount):
    return bet_amount*2 if flip_coin() == Coin.HEADS.value else 0

def play_betting_bame(initial_cash, attempt_cost):
    cash = initial_cash
    max_cash = 0

    if initial_cash > 0:
        has_cash = True
    else:
        has_cash = False

    attempts = 0
    successful_attempts = 0
    unsuccessful_attempts = 0

    if(initial_cash >= attempt_cost):
        while has_cash:
            attempts = attempts + 1
            cash = cash - attempt_cost
            cash_increase = bet(attempt_cost)

            if cash_increase > 0:
                successful_attempts = successful_attempts + 1
            else:
                unsuccessful_attempts = unsuccessful_attempts + 1

            cash = cash + cash_increase
            if (cash > max_cash):
                max_cash = cash
            
            if cash < attempt_cost:
                has_cash = False

    if (attempts > 0):
        win_average = (successful_attempts/attempts)*100
        loss_average = (unsuccessful_attempts/attempts)*100
    
    game_results = {
        "attempts": attempts,
        "successful_attempts": successful_attempts,
        "unsuccessful_attempts": unsuccessful_attempts,
        "win_average": win_average if attempts > 0 else 0,
        "loss_average": loss_average if attempts > 0 else 0,
        "max_cash":max_cash
    }

    return game_results
