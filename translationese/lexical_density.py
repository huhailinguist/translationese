"""\
The frequency of tokens that are `not` nouns, adjectives, adverbs or verbs.
"""

__author__ = "Gal Star"
__email__ = "gal.star3051@gmail.com"

def quantify(analysis):
    """Quantify lexical density."""
    all_tags = analysis.tokens()
    
    def is_lexical_density(letter):    
        is_not_verb = letter[0] !='V'
        is_not_noun = letter[0] !='N'
        is_not_adjective = letter[0] !='J'
        is_not_adverb = letter[0] !='R'

        return is_not_verb and is_not_noun and is_not_adverb and \
               is_not_adjective

    def is_lexical_density_zh(letter):
        is_not_verb = letter != 'VV'
        is_not_predAdj = letter != 'VA'
        is_not_noun = letter[0] != 'N'
        is_not_adjective = letter[0] != 'J'
        is_not_adverb = letter != 'AD'

        return is_not_verb and is_not_predAdj and is_not_noun and \
               is_not_adverb and is_not_adjective

    def count_all_lexical_pos_tags():
        text = analysis.pos_tags()
        if analysis.lang == 'en':
            return len([t for t in text if is_lexical_density(t[1])])
        elif analysis.lang == 'zh':
            return len([t for t in text if is_lexical_density_zh(t[1])])
        else:
            print('language "{}" not implemented yet for lexical_density'.format(analysis.lang))
            exit()

    result = float(count_all_lexical_pos_tags()) / len(all_tags)
    return { "lexical_density": result }
