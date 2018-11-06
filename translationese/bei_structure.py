"""
bei-structure in Chinese: freq(pos=BEI) / len(analysis.sentences())
"""

__author__ = 'Hai Hu'
__email__ = 'huhai@indiana.edu'

def quantify(analysis):
    """ Quantify bei-structure """
    if analysis.lang != 'zh':
        print('language "{}" not implemented for bei-structure'.format(analysis.lang))
        exit()
    else:
        counter = 0
        for word_pos in analysis.pos_tags():
            if word_pos[1] in ['LB', 'SB']: counter += 1
        counter /= len(analysis.tokenized_sentences())

    return { 'bei_structure' : counter}


