"""
Subordinate conjunctions in Chinese as feats
"""

__author__ = 'Hai Hu'

VARIANTS = [0, 1, 2] #: Possible variants


from collections import Counter

class SubConjQuantifier:
    def __init__(self, variant):
        self.k = variant

    def quantify(self, analysis):
        """Quantify determiners."""
        if analysis.lang != 'zh':
            print('language "{}" not implemented yet for Subordinate conjunctions'.format(analysis.lang))
            exit()
        pos_tags = analysis.pos_tags()

        if self.k == 0:

            appropriate_tokens = (token.lower() for token, tag in pos_tags \
                                      if tag == 'CS')

            counter = Counter(appropriate_tokens)
            numTokens = len(pos_tags)

            result = { key: value * 3 / numTokens for key, value in counter.items() }

            return result

        elif self.k == 1:
            result = {}
            return result


def quantify_variant(analysis, variant):
    """Quantify SubConj """
    quantifier = SubConjQuantifier(variant)
    return quantifier.quantify(analysis)