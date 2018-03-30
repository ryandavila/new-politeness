Stanford Politeness API
=======================

#### Version 3.00 (released June 2017)

In this version, the codebase has been refactored into a package-able state so it can be pushed to PyPi.

#### Version 2.00 (released March 2017)

[Details](https://github.com/meyersbs/politeness/tree/eee3c5f8397c422825d5a76a4e8ff4bbfc17a310)

#### Version 1.01 (released October 2014)

[Details](https://github.com/sudhof/politeness/tree/89506585fbd70afa265c773a68b71cf3e3fd0a64)


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

For questions regarding versions 3.00 and 2.00, please email bsm9339@rit.edu (Benjamin Meyers) or nm6061@rit.edu (Nuthan Munaiah). Please direct questions regarding the port from Python2 to Python3 to Benjamin Meyers.

For questions regarding the implementation and the theory behind the politeness classifier, please email cristian@cs.cornell.edu (Cristian Danescu-Niculescu-Mizil) or sudhof@stanford.edu (Moritz Sudhof).

# new-politeness
In order to properly run the program, you need to run a version of StanfordCoreNLP server, and link the ports, which has instructions in the previous part of the readme.
The default port is 9000. Then in order to run the program, run
``` bash
python3 app.py
```
And then you will be prompted to open the form with a url, and you should be able to input the sentence / request there.
The in-depth results will be displayed in the terminal, along with part of the values from the process. This is being
adapted to work on the webpage, with a cleaner display.
