from game import play_betting_bame
from plotting import plot_average_turns_before_losing

if __name__ == "__main__":
    initial_cash = 100
    attempt_cost = initial_cash
    threshold = 600
    results = []

    for i in range(0,100):
        result = play_betting_bame(initial_cash, attempt_cost)
        results.append(result)
    
    plot_average_turns_before_losing(results)