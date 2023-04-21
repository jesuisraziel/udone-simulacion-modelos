import matplotlib.pyplot as plt

def plot_individual_game_results(result):
    win_average_key = "win_average"
    loss_average_key = "loss_average"

    win_average = result[win_average_key]
    loss_average = result[loss_average_key]

    data = {f"Wins ({win_average:.2f}%)": win_average, f"Losses ({loss_average:.2f}%)":loss_average}
    labels = list(data.keys())
    results = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(labels, results, color ='maroon', width = 0.4)

    plt.xlabel("Possible results")
    plt.ylabel("Average (%)")
    plt.title("Results of a full betting game.")
    plt.show()

def plot_game_results(game_results, threshold):
    wins = 0
    losses = 0
    games = len(game_results)

    for result in game_results:
        max_cash = result["max_cash"]
        if max_cash >= threshold:
            wins = wins + 1
        else:
            losses = losses + 1
    
    data = {f"Above threshold ({wins})":wins, f"Below threshold ({losses})":losses}
    labels = list(data.keys())
    results = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(labels, results, color ='maroon', width = 0.4)

    plt.xlabel("Possible outcomes")
    plt.ylabel("Occurence")
    plt.title(f"Max cash earned before losing when playing {games} games (threshold = {threshold})")
    plt.show()

def plot_average_turns_before_losing(game_results):
    game_count = len(game_results)
    total_attempts = 0
    for result in game_results:
        total_attempts = total_attempts + result["attempts"]
    average = total_attempts/game_count 

    data = {f"Average ({average})":average}
    labels = list(data.keys())
    results = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(labels, results, color ='maroon', width = 0.4)

    # plt.xlabel("Possible outcomes")
    # plt.ylabel("Occurence")

    plt.title(f"Average of turns played before losing in {game_count} games")
    plt.show()