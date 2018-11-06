"""
dependency triples involving at least one pronoun
want to look at subj, obj pro-drop

"""

__author__ = 'Hai Hu'
__email__ = 'huhai@indiana.edu'

VARIANTS = [0, 1, 2, 3, 4, 5]
# 0: all depTripleLex2 with a pronoun in it
# 1: depTripleLex2 with a personal pronoun in it

PERSON_PN = {"我", "我们", "咱", "咱们", "俺", "俺们",
             "你", "您", "你们", "您们",
             "他", "他们", "她", "她们", "它", "它们",
             "吾", "其",}

# relations I want
RELATIONS = {"nsubj", "nobj", "cop", "dep",}
             # ["", "", "", "", "", "", "", ]

class depPronounQuantifier:
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

                if self.k == 0:
                    # depTripleLex2:
                    # only want depTripleLex2 if there is PN pronoun in it
                    if (head[1] == 'PN') or (dependent[1] == 'PN'):
                        if head[1] == 'PN':
                            newHead = head[0]  # lexical item
                        else:
                            newHead = head[1]  # pos
                        if dependent[1] == 'PN':
                            newDependent = dependent[0]  # lexical item
                        else:
                            newDependent = dependent[1]  # pos
                        depTriple_Lex2 = '_'.join([newHead, relation, newDependent])
                        res[depTriple_Lex2] = res.get(depTriple_Lex2, 0) + 1

                elif self.k == 1:
                    # only personal pronoun
                    if (head[0] in PERSON_PN) or (dependent[0] in PERSON_PN):
                        if head[1] == 'PN':
                            newHead = head[0]  # lexical item
                        else:
                            newHead = head[1]  # pos
                        if dependent[1] == 'PN':
                            newDependent = dependent[0]  # lexical item
                        else:
                            newDependent = dependent[1]  # pos
                        depTriple_Lex2 = '_'.join([newHead, relation, newDependent])
                        res[depTriple_Lex2] = res.get(depTriple_Lex2, 0) + 1

                elif self.k == 2:
                    # only personal pronoun and simple relations
                    if (relation in RELATIONS) and \
                            ((head[0] in PERSON_PN) or (dependent[0] in PERSON_PN)):
                        if head[1] == 'PN':
                            newHead = head[0]  # lexical item
                        else:
                            newHead = head[1]  # pos
                        if dependent[1] == 'PN':
                            newDependent = dependent[0]  # lexical item
                        else:
                            newDependent = dependent[1]  # pos
                        depTriple_Lex2 = '_'.join([newHead, relation, newDependent])
                        res[depTriple_Lex2] = res.get(depTriple_Lex2, 0) + 1

                elif self.k == 3:
                    # only personal pronoun and nsubj of VA, VC, VE, VV
                    if (relation == "nsubj") and \
                            (head[1] in {"VA", "VC", "VE", "VV"}) and (dependent[0] in PERSON_PN):
                        newHead = head[1]  # pos
                        newDependent = dependent[0]  # lexical item
                        depTriple_Lex2 = '_'.join([newHead, relation, newDependent])
                        res[depTriple_Lex2] = res.get(depTriple_Lex2, 0) + 1

                elif self.k == 4:
                    # only personal pronoun that are nsubj, nobj, cop, dep of VA, VC, VE, VV
                    # all pronouns collapsed
                    if (relation in ["nsubj", "dobj", "cop", "dep"]) and \
                            (head[1] in {"VA", "VC", "VE", "VV"}) and (dependent[0] in PERSON_PN):
                        newHead = head[1]  # pos
                        # newDependent = dependent[0]  # lexical item
                        depTriple_Lex2 = '_'.join([newHead, relation, "PERSON_PN"])
                        res[depTriple_Lex2] = res.get(depTriple_Lex2, 0) + 1

                elif self.k == 5:
                    # pronoun as the head depTriple1
                    if head[1] == "PN":
                        depTriple = '_'.join([head[1], relation, dependent[1]])
                        res[depTriple] = res.get(depTriple, 0) + 1

        # normalized count
        return {k : v/len(depParses) for k, v in res.items()}

def quantify_variant(analysis, variant):
    """Quantify depPronoun."""
    quantifier = depPronounQuantifier(variant)
    return quantifier.quantify(analysis)


