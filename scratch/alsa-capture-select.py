#!/bin/env python

import alsaaudio

CARD = 0 # Audio device -default-

def get_mixers(kwargs):
    '''
    Generate and return dictionary of {mixer: capabilities}
    '''
    mixers = {}
    for m in alsaaudio.mixers(**kwargs):
        mixer = alsaaudio.Mixer(m, **kwargs)
        capabilities = [ mixer.mixerid() ]  # THIS DOESN'T WORK only returns 0 , can't set it to anything
        for c in mixer.volumecap() + mixer.switchcap():
            capabilities.append(c)
        mixers[m] = capabilities
    return mixers

def list_mixers(kwargs):
    '''
    Input {mixer:capabilities} and print nicely
    '''
    for m, c in kwargs.items():
        print(f'{m} : {c}')

    

if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--card", help="Card number to use") 
    args = parser.parse_args()

    if args.card:
        card = args.card
    else:
        card = CARD
    
    kwargs = { 'cardindex': int(card) }
    print(f'card={card}')       
    #print(get_mixers(kwargs))

    list_mixers(get_mixers(kwargs))
        
