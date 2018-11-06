"""\
We count the number of content words (words tagged as nouns, verbs, adjectives
or adverbs) that occur more than once in a chunk, and normalize by the number
of tokens in the chunk. Inflections of the verbs be and have are excluded
from the count since these verbs are commonly used as auxiliaries. This
feature's values are magnified by an order of 3.
"""

from collections import Counter

VARIANTS = [0, 1] #: Possible variants: 0: all, 1: only N repetitions

ignored_tokens = {
    # Inflections of 'be'
    "am", "is", "are", "was", "were", "be", "being", "been", 
    # Inflections of 'have'
    "have", "has", "had", 
}
"""Ignored tokens"""


def proper_pos(token, pos):
    if token.lower() in ignored_tokens: return False

    if pos.startswith("NN"): return True  # Noun
    if pos.startswith("VB"): return True  # Verb
    if pos.startswith("JJ"): return True  # Adjective
    if pos.startswith("RB"): return True  # Adverb

    return False


# chinese
def proper_pos_zh(pos):
    # if token.lower() in ignored_tokens: return False

    if pos.startswith("VC"): return False  # V copula 是
    if pos.startswith("VE"): return False  # V existential 有

    if pos.startswith("N"): return True  # Noun
    if pos.startswith("V"): return True  # Verb: VA, VV
    if pos.startswith("JJ"): return True  # Adjective
    # if pos.startswith("RB"): return True # Adverb

    return False

class RepetitionQuantifier:
    def __init__(self, variant):
        self.k = variant


    def quantify(self, analysis):
        """Quantify reptitions."""
        pos_tags = analysis.pos_tags()

        if self.k == 0:

            if analysis.lang == 'en':
                appropriate_tokens = (token.lower() for token, tag in pos_tags \
                                      if proper_pos(token, tag))
            elif analysis.lang == 'zh':
                appropriate_tokens = (token for token, tag in pos_tags \
                                      if proper_pos_zh(tag))
            else:
                print('language "{}" not implemented yet for repetitions'.format(analysis.lang))
                exit()


        elif self.k == 1:
            if analysis.lang == 'zh':
                appropriate_tokens = (token for token, tag in pos_tags \
                                      if tag.startswith("N"))
            else:
                print('language "{}" not implemented yet for repetitions'.format(analysis.lang))
                exit()

        counter = Counter(appropriate_tokens)

        result = sum(occurrences for token, occurrences in counter.items()
                     if occurrences > 1)

        result *= 3.0
        result /= len(pos_tags)

        if self.k == 0: return {"repetitions": result}
        elif self.k == 1: return {"repetitions-nouns": result}

def quantify_variant(analysis, variant):
    """ Quantify repetitions """
    quantifier = RepetitionQuantifier(variant)
    return quantifier.quantify(analysis)
