# Use ELO rating to determine Smash Ultimate Player's rank

import csv, os
import operator

class Player:
    def __init__(self, name):
        self.name = name
        self.elo = 1000
        self.sets = 0
        self.sets_wins = 0
        self.games = 0
        self.games_wins = 0

class ELO:
    def __init__(self, k_value = 32):
        self.players = {} # key=Player Name, v=player object
        self.k = k_value
    def rate(self, p1, p2, win, p1_score, p2_score): # p1= player 1's name and win= 0 if player 1 won
        if(p1_score == -1 or p2_score == -1):
            return
        # Get the rating
        if(self.players.get(p1, -1) == -1):
            self.players[p1] = Player(name = p1)
        if(self.players.get(p2, -1) == -1):
            self.players[p2] = Player(name = p2)
        R_p1 = self.players[p1].elo
        R_p2 = self.players[p2].elo

        # Calculate Q values using the logisitic curve

        Q_p1 = 10 ** (R_p1/400)
        Q_p2 = 10 ** (R_p2/400)

        E_p1 = Q_p1 / (Q_p1 + Q_p2)
        E_p2 = 1 - E_p1

        # Calculate new ELO scores floored at 100

        self.players[p1].elo = max(R_p1 + self.k * (1 - win - E_p1), 100)
        self.players[p2].elo = max(R_p2 + self.k * (win - E_p2), 100)

        self.players[p1].sets += 1
        self.players[p2].sets += 1

        if(win):
            self.players[p2].sets_wins += 1
        else:
            self.players[p1].sets_wins += 1

        if(p1_score != -2 and p2_score != -2):
            self.players[p1].games += p1_score + p2_score
            self.players[p1].games_wins += p1_score
            self.players[p2].games += p1_score + p2_score
            self.players[p2].games_wins += p2_score

def main():
    os.chdir(r'')
    Ultimate_rater = ELO()
    file = open('tournaments.csv')
    Data = csv.reader(file)
    for i, row in enumerate(Data):
        if(i == 0): # skip the header row
            continue
        print(i, 'Rating '+row[1]+'-sets.csv')
        new_file = open(row[1]+'-sets.csv')
        new_data = csv.reader(new_file)
        for j, row in enumerate(new_data):
            if(j == 0):
                continue
            p1 = row[0].title().strip()
            p2 = row[1].title().strip()
            Ultimate_rater.rate(p1, p2, int(row[2]), int(row[3]), int(row[4]))
        new_file.close()

    print('Writing Data as Ultimate Results.csv')
    output_file = open('Ultimate Results.csv','w', newline='')
    output_writer = csv.writer(output_file)
    output_writer.writerow(['Rank', 'Player', 'ELO', 'Set Win %', 'Set Wins', 'Sets', 'Game Win %', 'Games Won', 'Games'])

    for i, p in Ultimate_rater.players.items():
        output_writer.writerow([0, p.name, p.elo, 0, p.sets_wins, p.sets, 0, p.games_wins, p.games])

    file.close()
    output_file.close()

main()
