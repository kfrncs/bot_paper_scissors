def emoji_to_num(emoji):
    lookup = {'🗿': 1, '📜': 2, '✂️': 3}
    return lookup.get(emoji)

def num_to_words(num):
    lookup = {1: 'rock', 2: 'paper', 3: 'scissors'}
    return lookup.get(num)
    
def evaluate(player, computer):
    outcomes = {
        (1, 3): 'win',  # rock beats scissors
        (1, 2): 'lose', # paper loses to rock
        (2, 1): 'win',  # paper beats rock
        (2, 3): 'lose', # paper loses to scissors
        (3, 1): 'lose', # scissors loses to rock
        (3, 2): 'win'   # scissors loses to paper
    }
    if player == computer:
        return 'tie'
    return outcomes[player, computer]
