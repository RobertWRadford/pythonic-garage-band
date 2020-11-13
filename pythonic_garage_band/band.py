class Band:

    bands = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.bands.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.bands


class Musician:

    def __init__(self, instrument, name=''):
        if not name:
            raise TypeError('Anonymous Musician')
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'{self.instrument} instance. Name = {self.name}'

class Guitarist(Musician):

    def __init__(self, name):
        super().__init__('Guitarist', name)

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'

class Bassist(Musician):

    def __init__(self, name):
        super().__init__('Bassist', name)

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):

    def __init__(self, name):
        super().__init__('Drummer', name)

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'