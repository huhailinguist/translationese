"""
depth of constituency parse tree as feature
"""

__author__ = 'Hai Hu'

def quantify(analysis):
    """Quantify treedepth."""
    pcfg = analysis.PCFG()
    # pcfg.maxDepths = a list of maxDepths for each sentence
    meanMaxDepth = sum(pcfg.maxDepths) / len(pcfg.maxDepths)
    return {'meanMaxDepth' : meanMaxDepth}
