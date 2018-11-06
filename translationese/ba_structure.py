"""
ba-structure in Chinese: freq(pos=BA) / len(analysis.sentences())
"""

__author__ = 'Hai Hu'
__email__ = 'huhai@indiana.edu'

def quantify(analysis):
    """ Quantify ba-structure """
    if analysis.lang != 'zh':
        print('language "{}" not implemented for ba-structure'.format(analysis.lang))
        exit()
    else:
        counter = 0
        for word_pos in analysis.pos_tags():
            if word_pos[1] == 'BA': counter += 1
        counter /= len(analysis.tokenized_sentences())

    return {'ba_structure' : counter}


