'''
Created on Dec 5, 2012

@author: ohad
'''
import unittest

import analyze
import StringIO
import translationese.lexical_variety
import os.path

class TestAnalyze(unittest.TestCase):
    def cleanup(self):
        for root, dirs, files in os.walk(self.tests_dir):
            for f in files:
                if f.endswith(".analysis"):
                    os.unlink(os.path.join(root, f))

    def setUp(self):
        self.maxDiff = None
        self.tests_dir = os.path.join(os.path.dirname(__file__), "test_data")
        self.o_dir = os.path.join(self.tests_dir, "o")
        self.t_dir = os.path.join(self.tests_dir, "t")
        self.cleanup()

    def tearDown(self):
        self.cleanup()

    def assertResultForModule(self, module, expected, variant=None):
        s = StringIO.StringIO()
        analyze.main(module, self.o_dir, self.t_dir, s, variant, timer_stream=None)
        self.assertMultiLineEqual(expected, s.getvalue())

    def testWithPunctuation(self):
        self.assertResultForModule(translationese.contractions,
                                   contractions_result)

    def testWithLexicalVariety(self):
        self.assertResultForModule(translationese.lexical_variety,
                                   lexical_variety_result, 1)

    def testMissingVariant(self):
        def tryToQuantifyWithoutVariant():
            module = translationese.lexical_variety
            analyze.main(module, self.o_dir, self.t_dir)
        self.assertRaises(translationese.MissingVariant, \
                          tryToQuantifyWithoutVariant)

    def testExtraVariant(self):
        def tryToQuantifyWithVariant():
            module = translationese.contractions
            analyze.main(module, self.o_dir, self.t_dir, variant=0)
        self.assertRaises(translationese.NoVariants, \
                          tryToQuantifyWithVariant)

    def testUndefinedVariant(self):
        def tryToQuantifyWithVariant():
            module = translationese.lexical_variety
            analyze.main(module, self.o_dir, self.t_dir, variant=5)
        self.assertRaises(translationese.NoSuchVariant, \
                          tryToQuantifyWithVariant)

lexical_variety_result = """\
@relation translationese
@attribute 'TTR2' numeric
@attribute class { T, O }

@data
{0 4.82532632325, 1 O}
{0 4.96252485208, 1 O}
{0 6.0, 1 T}
{0 5.16811869688, 1 T}
"""

contractions_result = """\
@relation translationese
@attribute "can't" numeric
@attribute "couldn't" numeric
@attribute "didn't" numeric
@attribute "doesn't" numeric
@attribute "don't" numeric
@attribute "he'd" numeric
@attribute "he'll" numeric
@attribute "he's" numeric
@attribute "here's" numeric
@attribute "how's" numeric
@attribute "i'd" numeric
@attribute "i'll" numeric
@attribute "i'm" numeric
@attribute "i've" numeric
@attribute "it's" numeric
@attribute "let's" numeric
@attribute "must've" numeric
@attribute "she'd" numeric
@attribute "she'll" numeric
@attribute "she's" numeric
@attribute "should've" numeric
@attribute "there's" numeric
@attribute "they'd" numeric
@attribute "they'll" numeric
@attribute "they're" numeric
@attribute "they've" numeric
@attribute "we'd" numeric
@attribute "we'll" numeric
@attribute "we're" numeric
@attribute "we've" numeric
@attribute "what's" numeric
@attribute "where's" numeric
@attribute "who're" numeric
@attribute "who's" numeric
@attribute "who've" numeric
@attribute "would've" numeric
@attribute "wouldn't" numeric
@attribute "you'd" numeric
@attribute "you'll" numeric
@attribute "you're" numeric
@attribute "you've" numeric
@attribute class { T, O }

@data
{1 0.25, 9 0.5, 41 O}
{41 O}
{41 T}
{41 T}
"""
