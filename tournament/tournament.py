'''
Introduction
Tally the results of a small football competition.

Based on an input file containing which team played against which and what the outcome was, create a file with a table like this:

Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1
What do those abbreviations mean?

MP: Matches Played
W: Matches Won
D: Matches Drawn (Tied)
L: Matches Lost
P: Points
A win earns a team 3 points. A draw earns 1. A loss earns 0.

The outcome should be ordered by points, descending. In case of a tie, teams are ordered alphabetically.

Input

Your tallying program will receive input that looks like:

Allegoric Alaskans;Blithering Badgers;win
Devastating Donkeys;Courageous Californians;draw
Devastating Donkeys;Allegoric Alaskans;win
Courageous Californians;Blithering Badgers;loss
Blithering Badgers;Devastating Donkeys;loss
Allegoric Alaskans;Courageous Californians;win
The result of the match refers to the first team listed. So this line

Allegoric Alaskans;Blithering Badgers;win
Means that the Allegoric Alaskans beat the Blithering Badgers.

This line:

Courageous Californians;Blithering Badgers;loss
Means that the Blithering Badgers beat the Courageous Californians.

And this line:

Devastating Donkeys;Courageous Californians;draw
Means that the Devastating Donkeys and Courageous Californians tied.
'''

# from collections import OrderedDict
# from operator import itemgetter, attrgetter

class Team:

    def __init__(self, name):
        self.name = name
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0
        return

    def __repr__(self):
        # return self.name.ljust(31) + f'|  {self.matches} |  {self.wins} |  {self.draws} |  {self.losses} |  {self.points}'
        return repr((self.name, self.points))

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.points < other.points

    def __le__(self, other): 
        return self.points <= other.points

    def __eq__(self, other): 
        return self.points == other.points

    def __ne__(self, other): 
        return self.points != other.points

    def __gt__(self, other): 
        return self.points > other.points

    def __ge__(self, other):
        return self.points >= other.points

    def win(self):
        self.matches += 1
        self.wins += 1
        self.points += 3
    
    def loss(self):
        self.matches += 1
        self.losses += 1

    def draw(self):
        self.matches += 1
        self.draws += 1
        self.points += 1

class Tourney:

    def __init__(self, rows):
        self.rows = rows
        self.teams = {}
        return

    def __get_team(self, name):
        if name not in self.teams:
            self.teams[name] = Team(name)
            
        return self.teams[name]

    def get_team(self):
        return []

    def get_teams(self):
        return self.teams

    def parse_contest(self):
        for line in self.rows:
            matchresult = line.split(';')
            team1 = self.__get_team(matchresult[0])
            team2 = self.__get_team(matchresult[1])
            if matchresult[2] == 'win':
                team1.win()
                team2.loss()
            elif matchresult[2] == 'loss':
                team1.loss()
                team2.win()
            elif matchresult[2] == 'draw':
                team1.draw()
                team2.draw()
            else:
                # ????
                pass
            
        return

def tally(rows):
    '''
    Test says to make a file... so create and send it's contents?
    '''
    tournament = Tourney(rows)
    tournament.parse_contest()
    # sortedTeams = sorted(tournament.get_teams().values(), key=attrgetter('points', 'name'), reverse=True)
    sortedTeams = sorted(tournament.get_teams().values(), key=lambda team: (-team.points, team.name)) 
    # print(sortedTeams)
    f = open('tournament_results.txt', 'w')
    f.write('Team'.ljust(31) + '| MP |  W |  D |  L |  P\n')
    for team in sortedTeams:
        # f.write(str(team) + '\n')
        # print(team)
        f.write(team.name.ljust(31) + f'|  {team.matches} |  {team.wins} |  {team.draws} |  {team.losses} |  {team.points} \n')
    
    f.close()

    f = open('tournament_results.txt', 'r')
    buffer = []
    for line in f:
        buffer.append(line.rstrip())
    
    f.close()
    return buffer

# results = []
# print(tally(results)) #["Team                           | MP |  W |  D |  L |  P"]
# results = ["Allegoric Alaskans;Blithering Badgers;win"]
# print(tally(results))
# tally(results)
# results = [
#             "Courageous Californians;Devastating Donkeys;win",
#             "Allegoric Alaskans;Blithering Badgers;win",
#             "Devastating Donkeys;Allegoric Alaskans;loss",
#             "Courageous Californians;Blithering Badgers;win",
#             "Blithering Badgers;Devastating Donkeys;draw",
#             "Allegoric Alaskans;Courageous Californians;draw",
#         ]
# tally(results)