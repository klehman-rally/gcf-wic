
class Whacko:

    def __init__(self, field_name, field_mappings):
        self.field_name = field_name
        self.field_mappings = field_mappings

    def txin(self, value):
        tx_val = self.field_mappings[value]
        #print(f'You called me a {tx_val}')
        return tx_val

    def txout(self, item, value):
        setattr(item, 'epi', self.field_mappings[value])
        return item

    def pontificate(self, speaker, audience):
        return None

#
#    NB: If you don't have to exclude anything from Whacko.__dict__ to satisfy pickle limitations
#        then you don't need to have explicit __setstate__ or __getstate__ methods for this to work!
#
#    # If the Whacko class was a sub-class of GeneralChaos then we might be
#    # able to define __getstate__ and __setstate__ in GeneralChaos
#    def __getstate__(self):
#        # this method is called when you are
#        # going to pickle the class, to know what to pickle
#        state = self.__dict__.copy()
#        return state
#
#    def __setstate__(self, state):
#        self.__dict__.update(state)
