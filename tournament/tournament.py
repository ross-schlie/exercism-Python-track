"""exercism tournament module."""


class Team:

    def __init__(self, name):
        """A Team in a football tournament.

        Keeps track of a teams matches, wins, draws, losses and points.

        Parameters
        ----------
        arg1 : string
            Name of the Team.
        """
        self.name = name
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0

    def __repr__(self):
        # return self.name.ljust(31) + f'|
        #   {self.matches} |
        #   {self.wins} |
        #   {self.draws} |
        #   {self.losses} |
        #   {self.points}'
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
        """The team Won! Updates the teams matches, wins and points."""
        self.matches += 1
        self.wins += 1
        self.points += 3

    def loss(self):
        """The team Lost! Updates the teams matches and losses."""
        self.matches += 1
        self.losses += 1

    def draw(self):
        """The team drew! Updates the teams draws, matches and points."""
        self.matches += 1
        self.draws += 1
        self.points += 1

class Tourney:

    def __init__(self):
        """A football Tournament that tracks teams that take part."""
        self.teams = {}

    def _get_team(self, name):
        if name not in self.teams:
            self.teams[name] = Team(name)

        return self.teams[name]

    def get_teams(self):
        """A Dictionary of the teams in the Tournament"""
        return self.teams

    def parse_contest(self, rows):
        """Determine the teams and their results in a Tournament.

        Parse lines in text (rows) to find the teams and their results
        in a Tournament.
        """
        for line in rows:
            matchresult = line.split(';')
            team1 = self._get_team(matchresult[0])
            team2 = self._get_team(matchresult[1])
            if matchresult[2] == 'win':
                team1.win()
                team2.loss()
            elif matchresult[2] == 'loss':
                team1.loss()
                team2.win()
            elif matchresult[2] == 'draw':
                team1.draw()
                team2.draw()
            #else:
                # ????

def tally(rows):
    """Tally the results of a small football competition.

    Parameters
    ----------
    arg1 : list
        A list of the results of matches in the competition
        Example: "Allegoric Alaskans;Blithering Badgers;win"

    Returns
    ------
    string
        The results of the Tournament.
        # containing the lines in the file

    Test says to make a file... so create and send it's contents?
    """
    tournament = Tourney()
    tournament.parse_contest(rows)
    sortedTeams = sorted(tournament.get_teams().values(),
                        key=lambda team: (-team.points, team.name))

    f = open('tournament_results.txt', 'w')
    f.write('Team'.ljust(31) + '| MP |  W |  D |  L |  P\n')
    for team in sortedTeams:
        f.write(team.name.ljust(31)
            + f'|  {team.matches} '
            + f'|  {team.wins} '
            + f'|  {team.draws} '
            + f'|  {team.losses} '
            + f'|  {team.points} \n')

    f.close()

    # ...
    f = open('tournament_results.txt', 'r')
    buffer = []
    for line in f:
        buffer.append(line.rstrip())

    f.close()
    return buffer
