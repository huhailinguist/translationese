"""
Determiners in Chinese as feats
"""

__author__ = 'Hai Hu'

VARIANTS = [0, 1, 2] #: Possible variants

determiners = {'这', '那'}  #, '该', '此'} #, '这些', '那些'}

from collections import Counter

class DeterminerQuantifier:
    def __init__(self, variant):
        self.k = variant

    def quantify(self, analysis):
        """Quantify determiners."""
        if analysis.lang != 'zh':
            print('language "{}" not implemented yet for determiners'.format(analysis.lang))
            exit()
        pos_tags = analysis.pos_tags()

        if self.k == 0:

            appropriate_tokens = (token.lower() for token, tag in pos_tags \
                                      if tag == 'DT')

            counter = Counter(appropriate_tokens)

            result = sum(occurrences for token, occurrences in counter.items()
                         if occurrences > 1)

            result *= 3.0
            result /= len(pos_tags)

            return { "determiners": result }

        elif self.k == 1:
            result = {}
            for token, tag in pos_tags:
                if (tag == 'DT') and (token[0] in determiners):
                    result[token[0]] = result.get(token[0], 0) + 1
                # if (tag == 'DT') and (len(token) > 1) and (token[:2] in determiners):
                #     result[token[:2]] = result.get(token[:2], 0) + 1

            for key in result.keys():
                result[key] = result[key] * 3 / len(pos_tags)
            return result


def quantify_variant(analysis, variant):
    """Quantify determiners """
    quantifier = DeterminerQuantifier(variant)
    return quantifier.quantify(analysis)