
class Blado:
    def __init__(self, bean, count):
        self.blad = bean
        self.calco = count * 7
        self.epi = 'initted'

    def stuffit(self, blend):
        self.blend = blend * self.calco
        return self.blend

