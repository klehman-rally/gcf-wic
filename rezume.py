# rezume.py  -- an example script to illustrate how to instantiate a class with
#               some state information and then serialize it and later resurrect
#               an instance of that class that can do operations with dynamic
#               data via method calls that use the saved state information
#               to produce useful results.

import sys, os
import pickle

sys.path.insert(0, '.')

import whackiness
import bokati

WO_PKL = 'whacko.pkl' 

#####################################################################################

def main(args):

    # the epithet mappings
    epi_map = {'goofy'  : 'giggle', 
               'snooty' : 'sneezy', 
               'venal'  : 'meanie' 
              }
    # an instance of our class intended to transform epithets in some way
    proto = whackiness.Whacko('pranks', epi_map)

    chill(proto, WO_PKL)         # serialize the proto into a file
    rezu_proto = thaw(WO_PKL)    # resurrect the proto from the serialized file

    print("An instance of the Whacko class has been resurrected with state info")
    #print(f'rezu_proto.__dict__ has {repr(rezu_proto.__dict__)}')

    binky = bokati.Blado('Roscoe and Zoroaster were skinning', 4)

    nub = 'snooty'
    bun = None
    bun = rezu_proto.txin(nub)
    print(f"transformed {nub} to {bun}")

    fuz = 'venal'
    funky = rezu_proto.txout(binky, fuz)
    result = funky.stuffit(2)
    print(f'Blado.blend XXX-{result}-YYYY for your cup filled with {funky.epi}')

    print('All DONE!')

#####################################################################################

def chill(instance, cooler):
    with open(cooler, 'wb') as cf:
        pickle.dump(instance, cf, -1)

def thaw(cooler):
    cf = open(cooler, 'rb')
    thawed = pickle.load(cf)
    cf.close()
    
    return thawed

#####################################################################################
#####################################################################################


if __name__ == '__main__':
    main(sys.argv[1:])
