Stanford Politeness API
=======================

#### Adaptation developed for Hajin's study

Working with Version 3.00 linked below, I made adaptations in order to search and mark keywords that are part of word groups specified in strategies.py. Feel free to add more word groups to the strategy dictionary if you would like to identify more words. Integrating this with JavaScript browser rendering for the HTML form is a work in progress.

#### Version 3.00 (released June 2017)

[Base Code / Version](https://github.com/PureMath86/politeness)

In this version, the codebase has been refactored into a package-able state so it can be pushed to PyPi.

### Description

Python implementation of a politeness classifier for requests, based on the work described in:

	A computational approach to politeness with application to social factors.
	Cristian Danescu-Niculescu-Mizil, Moritz Sudhof, Dan Jurafsky, Jure Leskovec, Christopher Potts.
	Proceedings of ACL, 2013.

We release this code hoping that others will use and improve on our work.

NOTE: If you use this API in your work please send an email to cristian@cs.cornell.edu so we can add you to our list of users.  Thanks!

### Install & Setup

``` bash
pip install politeness
```

In order to classify documents that have not been preprocessed, we rely on the [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) for generating dependency parses.

However, this codebase does not come packaged with CoreNLP; you will need to download and run a CoreNLP server and tell the politeness API where it is. See the previous link for details on setting up a CoreNLP server. There are two ways to tell the politeness API where the server is running:

**bash**:

``` bash
python3 main.py url -u some-url.org:1234
```

**python**:

``` python
from politeness.helpers import set_corenlp_url
set_corenlp_url('some-url.org:1234')
```

When you set the URL, it will persist until another call to `politeness.helpers.set_corenlp_url()` is made. To see what the current URL is run `python3 main.py url -l`.

### Usage

#### Bash

``` bash
$ python3 main.py --help
usage: main.py [-h] {train,predict,download,url} ...

Command line access to the Stanford Politeness API.

optional arguments:
  -h, --help            show this help message and exit

Commands:
  {train,predict,download,url}
    train               Train politeness classifier.
    predict             Predict politeness of a sentence.
    download            Download training data.
    url                 Set the URL for the Stanford CoreNLP Server.
```

#### Python

``` python
import politeness
from politeness.classifier import Classifier

cls = Classifier()

# String Input
cls.predict("This is a sample sentence for prediction.")
# File Input
cls.predict("sample_sentences.txt")
# Dictionary Input
data_dict = {'sentence': 'If yes would you please share it?',
             'parses': ['ROOT(root-0, please-5)', 'dep(please-5, If-1)',
                        'dep(please-5, yes-2)', 'aux(please-5, would-3)',
                        'nsubj(please-5, you-4)', 'dobj(please-5, share-6)',
                        'dep(please-5, it-7)', 'punct(please-5, ?-8)']}
cls.predict(data_dict)
```

### Contact

For questions regarding this lab iterations, contact hl934@cornell.edu (Hajin Lim) or rmd252@cornell.edu (Ryan Davila).

For questions regarding versions 3.00 and 2.00, please email bsm9339@rit.edu (Benjamin Meyers) or nm6061@rit.edu (Nuthan Munaiah). Please direct questions regarding the port from Python2 to Python3 to Benjamin Meyers.

For questions regarding the implementation and the theory behind the politeness classifier, please email cristian@cs.cornell.edu (Cristian Danescu-Niculescu-Mizil) or sudhof@stanford.edu (Moritz Sudhof).

## Lab Notes & Adaptations
In order to properly run the program, you need to run a version of StanfordCoreNLP server ([link to version used](https://stanfordnlp.github.io/CoreNLP/history.html)), and link the ports, which has instructions in the previous part of the readme. The command used to start the server while in the directory of the NLP folder is

``` bash
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```

The default port is 9000. Then in order to run the program, run
``` bash
python3 app.py
```
And then you will be prompted to open the form with a url, and you should be able to input the sentence / request there.

The in-depth results can be displayed in the terminal, along with part of the values from the process with use of the commented out print statements. This information is displayed on the webpage. In the future, displaying the information with color codes for different groupings of phrases, as well as a bar that serves as a gradient to indicate the level of politeness is the goal.

### Noted Issues / Struggles

Problem: Working with the JavaScript to render the information appropriately was difficult. One specific instance is when matching the dictionary to the text in browser, if a word appeared as a substring before the specific word in question, the wrong text would be emphasized.

Example) Do they think I know what I am doing? Results in the "i" in "think" being highlighted instead of "I".

Resolution: Regular Expressions. I have code written there that works in certain RegEx testers but not in the browser code. This should be a relatively straightforward fix with some tinkering, but similar bugs may present themselves, as it is difficult to transfer object information in between languages into a browser and I've found out.

This is the main thing I was struggling with as I am writing this, as conveying accurate information is the most important. Beyond this, it is mostly stylistic choices as to how once chooses to display the information for the sentences.
