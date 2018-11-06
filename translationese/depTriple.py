"""
dependency triples

"""

__author__ = 'Hai Hu'
__email__ = 'huhai@indiana.edu'

import math

VARIANTS = [0, 1, 2, 3, 4]

functionalPOS = {'AD','AS','BA','CC','CD','CS',
    'DEC','DEG','DER','DEV','DT','ETC',
    'IJ','LB','LC','MSP','OD','ON','P','PN','PU',
    'SB','SP','VC','VE'} # no M: measure word

class depTripleQuantifier:
    def __init__(self, variant):
        self.k = variant

    def quantify(self, analysis):
        res = {}

        depParses = analysis.depParses()

        assert len(analysis.pos_tags_by_sentence()) == len(depParses)
        for idx in range(len(depParses)):
            pos_tags = analysis.pos_tags_by_sentence()[idx]
            depParse = analysis.depParses()[idx]
            assert len(pos_tags) == len(depParse)

            for i in range(len(depParse)):
                # pos_tags: [('张三', 'NR'), ('买', 'VV'), ('了', 'AS'), ... ]
                # depTriple: [('ROOT', 0, 2), ('nsubj', 2, 1), ('aux:asp', 2, 3),  ... ]
                depTriple = depParse[i]  # ('nsubj', 2, 1)
                head = pos_tags[ depTriple[1] - 1 ]  # ('买', 'VV')
                dependent = pos_tags[ depTriple[2] - 1 ]  # ('张三', 'NR')
                relation = depTriple[0]  # nsubj
                # print(head, dependent, relation)

                # see below
                if self.k == 0:
                    depTriple1 = '_'.join([head[1], relation, dependent[1]])
                    res[depTriple1] = res.get(depTriple1, 0) + 1
                elif self.k == 1:
                    depTriple2 = '_'.join([head[1], dependent[1]])
                    res[depTriple2] = res.get(depTriple2, 0) + 1
                elif self.k == 2:
                    depTriple3 = relation
                    res[depTriple3] = res.get(depTriple3, 0) + 1
                elif self.k == 3:
                    depTriple_Lex1 = '_'.join([head[0], relation, dependent[0]])
                    res[depTriple_Lex1] = res.get(depTriple_Lex1, 0) + 1
                elif self.k == 4:
                    if head[1] in functionalPOS:
                        newHead = head[0]  # lexical item
                    else:
                        newHead = head[1]  # pos
                    if dependent[1] in functionalPOS:
                        newDependent = dependent[0]  # lexical item
                    else:
                        newDependent = dependent[1]  # pos
                    depTriple_Lex2 = '_'.join([newHead, relation, newDependent])
                    res[depTriple_Lex2] = res.get(depTriple_Lex2, 0) + 1

        '''
        we test many types of dep graph (or DAG):
        1. depGraph1:    pos1 --> rel1 --> pos2 --> rel2 --> pos3
        2. depGraph2:    pos1 --> pos2 --> pos3
        3. depGraph3:    rel1 --> rel2
        4. depGraphLex1: word1 --> rel1 --> word2 --> rel2 --> word3
        5. depGraphLex2: word1 --> rel1 --> word2 --> rel2 --> word3 # only if word is function word

        pos1 is the pos of the START_NODE, pos2 is the pos of the END_NODE

        For each depGraph, we can also define uni-depGraph, bi-depGraph, tri-depGraph,
        depending on the number of nodes in the graph (including the START_NODE and END_NODE)

        Therefore,
        uni-depGraph1: pos1 --> rel1 --> pos2, which is equavalent to depTriple

        for now, let's try:
            uni-, bi-, tri-depGraph1
            uni-, bi-, tri-depGraph2
            uni-, bi-, tri-depGraph3

        '''
        # print(res)
        # exit()
        return res

def quantify_variant(analysis, variant):
    """Quantify depTriple."""
    quantifier = depTripleQuantifier(variant)
    return quantifier.quantify(analysis)


