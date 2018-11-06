"""\
The average length (in tokens) of proper nouns (consecutive tokens tagged as
Proper Nouns), magnified by an order of 3. The motivation for this feature is
the same as :mod:`translationese.single_naming`.
"""

import os
if os.environ.get("READTHEDOCS", None) != 'True':
    import nltk

def quantify(analysis):
    """Quantify mean multiple naming."""

    if analysis.lang == 'en':
        from translationese.utils import is_proper_noun
    elif analysis.lang == 'zh':
        from translationese.utils import is_proper_noun_zh as is_proper_noun
    else:
        print('language "{}" not implemented yet for single naming'.format(analysis.lang))
        exit()

    num_proper_noun_runs = 0
    num_proper_noun_tokens = 0
    currently_in_run = False

    # pos_tags = nltk.pos_tag(analysis.case_tokens())
    # pos_tags = [word_tag_pair[1] for word_tag_pair in analysis.pos_tags()]
    pos_tags = analysis.pos_tags()

    for token in pos_tags:
        if is_proper_noun(token):
            currently_in_run = True
            num_proper_noun_tokens += 1
        elif currently_in_run:
            # Run just ended
            currently_in_run = False
            num_proper_noun_runs += 1

    if num_proper_noun_runs == 0:
        result = 0
    else:
        result = float(num_proper_noun_tokens) / num_proper_noun_runs
    
    return { "mean_multiple_naming": result }
