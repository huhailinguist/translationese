"""\
This hypothesis checks whether pronouns from
:mod:`translationese.function_words` alone can yield a high classification
accuracy. Each pronoun in the corpus is a feature, whose value is the
normalized frequency of its occurrences in the chunk.
"""

PRONOUNS = [
 "he", "her", "hers", "herself", "him",
 "himself", "i", "it", "itself", "me",
 "mine", "myself", "one", "oneself", "ours", "ourselves",
 "she", "theirs", "them", "themselves", "they",
 "us", "we", "you", "yourself"]

PRONOUNS_ZH = ["你","我","他","它","她","俺","自己",
            "你们","我们","咱们","她们","他们","它们","俺们","大家"]

"""List of pronouns"""

def quantify(analysis):
    """Quantify pronouns."""
    freq = analysis.histogram_normalized()
    if analysis.lang == 'en':
        pairs = [ (word, freq.get(word, 0.0)) for word in PRONOUNS ]
    elif analysis.lang == 'zh':
        pairs = [ (word, freq.get(word, 0.0)) for word in PRONOUNS_ZH ]
    else:
        print('language "{}" not implemented yet for pronouns'.format(analysis.lang))
        exit()

    return dict(pairs)
