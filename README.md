# Chinese translationese 
==================
Hai Hu, forked and modifed from https://github.com/lutzky/translationese

Documentation of the original implementation is available here: https://translationese.readthedocs.org/

I made the following modifications:

1. I extended it to use Stanford CoreNLP to process text data, rather than NLTK. So now you can fire up a CoreNLP server locally and then process text data.

2. I also extend it to handle Chinese data, which means you will need to download the Chinese model from [CoreNLP webpage](https://stanfordnlp.github.io/CoreNLP/index.html#download)
