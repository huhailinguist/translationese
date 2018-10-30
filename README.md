# Chinese translationese 

Hai Hu, forked and modifed from https://github.com/lutzky/translationese

Documentation of the original implementation is available here: https://translationese.readthedocs.org/

I made the following modifications:

1. I extended it to use Stanford CoreNLP to process text data, rather than NLTK, which is quite inaccurate. You need to install and fire up a [CoreNLP server](https://stanfordnlp.github.io/CoreNLP/corenlp-server.html) locally and then process text data. You will also need a python wrapper for CoreNLP which is already in this folder. It is a modification of the wrapper from [here](https://github.com/Lynten/stanford-corenlp).

2. I also extend it to handle Chinese data, which means you will need to download the Chinese model from [CoreNLP webpage](https://stanfordnlp.github.io/CoreNLP/index.html#download). It can also easily be extended to handle other languages that CoreNLP can process.

3. Changed the code from python2 to python3.

4. Added features to the original module, some of which specific to Chinese. 



