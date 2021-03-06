# Word Embeddings for Historical Text

### Author: William Hamilton (wleif@stanford.edu)
### [Project Website](http://nlp.stanford.edu/projects/histwords)


### Modification by Santiago Arconada (sarconada@gatech.edu)
### Forked to use in Meaning Change Historical Analysis

## Changes from original version
1. Modifications to use with python3.9
2. Example.py has been modified to retrieve neighbor set information

### How to use
#### Web Based
1. Download pre-trained word2vec vectors from links below
2. Include downloaded folder in project directory (i.e. Users/yourusername/Downloads/histwords/embeddings)
3. Run python3 viz/web/main.py
4. Go to localhost:5000 on your browser
5. Play around!

#### Terminal Based
1. Download pre-trained word2vec vectors from links below
2. Include downloaded folder in project directory (i.e. Users/yourusername/Downloads/histwords)
3. To alter the time period looking at adjust the range in the for-loop (i.e. range(1900, 2000, 20 to extract word embeddings from 20 year periods between 1900s and 2000s)
4. To change the pre-trained vector modify the variable in SequentialEmbedding.load("thepretrainedvectoryouchose")
5. To change the number of closest embeddings change the n variable in get_seq_neighbour_set("word",n=somenumber)


## Overview 

An eclectic collection of tools for analyzing historical language change using vector space semantics.

![alt text](https://github.com/williamleif/historical-embeddings/raw/master/wordpaths-final.png "Two-dimensional projections of some semantic changes computed using the English SGNS vectors. Check the appendix of my ACL 2016 paper (linked below) for details.")

## Pre-trained historical embeddings

Various embeddings (for many languages and using different embeddings approaches are available on the [project website](http://nlp.stanford.edu/projects/histwords).

Some pre-trained word2vec (i.e., SGNS) historical word vectors for multiple languages (constructed via Google N-grams) are also available here:
* [All English (eng-all)](http://snap.stanford.edu/historical_embeddings/eng-all_sgns.zip) 
* [English fiction (eng-fiction-all)](http://snap.stanford.edu/historical_embeddings/eng-fiction-all_sgns.zip) 
* [French (fre-all)](http://snap.stanford.edu/historical_embeddings/fre-all_sgns.zip) 
* [German (ger-all)](http://snap.stanford.edu/historical_embeddings/ger-all_sgns.zip) 
* [Chinese (chi-sim-all)](http://snap.stanford.edu/historical_embeddings/chi-sim-all_sgns.zip) 

All except Chinese contain embeddings for the decades in the range 1800s-1990s (2000s are excluded because of sampling changes in the N-grams corpus).
The Chinese data starts in 1950.

Embeddings constructed using the Corpus of Historical American English (COHA) are also available:
* [Raw words (coha-word)](http://snap.stanford.edu/historical_embeddings/coha-word_sgns.zip) 
* [Word lemmas (coha-lemma)](http://snap.stanford.edu/historical_embeddings/coha-lemma_sgns.zip) 

`example.sh` contains an example run, showing how to download and use the embeddings.
`example.py` shows how to use the vector representations in the Python code (assuming you have already run the `example.sh` script.)

[This paper](http://arxiv.org/abs/1605.09096) describes how the embeddings were constructed.
If you make use of these embeddings in your research, please cite the following:

@inproceedings{hamilton_diachronic_2016,
  title = {Diachronic {Word} {Embeddings} {Reveal} {Statistical} {Laws} of {Semantic} {Change}},
  url = {http://arxiv.org/abs/1605.09096},
  booktitle = {Proc. {Assoc}. {Comput}. {Ling}. ({ACL})},
  author = {Hamilton, William L. and Leskovec, Jure and Jurafsky, Dan},
  year = {2016}
}

## Training your own embeddings

You can use the provided code to train your own embeddings (see code organization below). However, thanks to Ryan Heuser you can also simply train embeddings with gensim (https://radimrehurek.com/gensim/) and use Ryan's port of my code to align the gensim models between time periods (https://gist.github.com/quadrismegistus/09a93e219a6ffc4f216fb85235535faf). Gensim contains many easy-to-use variants of word embeddings (e.g., LSI/SVD, word2vec, wordrank, ...), wrappers for using other packages like GloVe, and is very well maintained, so this solution is recommended. 


## Code organization

The structure of the code (in terms of folder organization) is as follows:

Main folder for using historical embeddings:
* `representations` contains code that provides a high-level interface to (historical) word vectors and is originally based upon Omer Levy's hyperwords package (https://bitbucket.org/omerlevy/hyperwords).

Folders with pre-processing code and active research code (potentially unstable):
* `googlengram` contains code for pulling and processing historical Google N-Gram Data (http://storage.googleapis.com/books/ngrams/books/datasetsv2.html).
* `coha` contains code for pulling and processing historical data from the COHA corpus (http://corpus.byu.edu/coha/).
* `statutils` contains helper code for common statistical tasks.
* `vecanalysis` contains code for evaluating and analyzing historical word vectors.
* `sgns` contains a modified version of Google's word2vec code (https://code.google.com/archive/p/word2vec/)

<!---`statistical-laws.ipynb` contains an IPython notebook with the main code necessary for replicating the key results of our [published work](http://arxiv.org/abs/1605.09096).--->

`example.py` shows how to compute the simlarity series for two words over time, which is how we evaluated different methods against the attested semantic shifts listed in our paper. 

If you want to learn historical embeddings for new data, the code in the `sgns` directory is recommended, which can be run with the default settings. As long as your corpora has at least 100 million words per time-period, this is the best method. For smaller corpora, using the `representations/ppmigen.py` code followed by the `vecanalysis/makelowdim.py` code (to learn SVD embeddings) is recommended. In either case, the `vecanalysis/seq_procrustes.py` code should be used to align the learned embeddings. The default hyperparameters should suffice for most use cases. 

However, as a caveat to the above, the code is somewhat messy, unstable, and specific to the historical corpora that it was originally designed for. If you are looking for a nice, off-the-shelf toolbox to run word2vec, I recommend you check out [gensim](https://radimrehurek.com/gensim/models/word2vec.html). 

<!--- * `notebooks` contains notebooks useful for replicating my published results-->

<!--- *See REPLICATION.md for detailed instructions on how to replicate specific published/submitted results.-->

## Dependencies

Core dependencies:
  * python 2.7
  * sklearn: http://scikit-learn.org/stable/
  * cython: http://docs.cython.org/src/quickstart/install.html
  * statsmodels: http://statsmodels.sourceforge.net/

You will also need Juptyer/IPython to run any IPython notebooks.
