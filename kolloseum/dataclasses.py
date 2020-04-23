class Event:
    def __init__(self, raw):
        self.id = raw['id']
        self.name = raw['name']
        self.numEntrants = raw['numEntrants']
        self.entrantSizeMax = raw['entrantSizeMax']
        self.entrantSizeMin = raw['entrantSizeMin']
        self.entrants = []
        for entrant in raw['entrants']['nodes']:
            self.entrants.append(Entrant(entrant))

class Entrant:
    def __init__(self, raw):
        self.id = raw['id']
        self.name = raw['name']
        self.participant = Participant(raw['participants'][0])

class Participant:
    def __init__(self, raw):
        self.id = raw['id']
        self.gamerTag = raw['gamerTag']
        self.email = raw['email']