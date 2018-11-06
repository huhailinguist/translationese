"""\
Splitting sentences is a common strategy in translation, which is also
considered a form of simplification. Long and complicated sentences may be
simplified and split into short, simple sentences. Hence we assume that
translations contain shorter sentences than original texts.

For Chinese, measured by num of characters, instead of words
"""

def quantify(analysis):
    """Quantify mean sentence length."""
    result = len(analysis.chars()) / float(len(analysis.sentences()))
    return { "mean_sentence_length": result }
