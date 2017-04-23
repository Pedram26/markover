Markover
========

Makover is natural language generation, where you'll train a model how to speak and have it generate new text for you. You may use the simplest possible model, but the results may still surprise you in their sophistication.

.. image:: https://github.com/Pedram26/markover/blob/master/example.png?raw=true
    :height: 170px
    :align: center
    :alt: Sample Image

Dependencies
------------
- Python 2.7

Install
-------
- Install via pip: `$ pip install markover`

Usage
-----
- ``$ markover -t ABS_PATH_TO_YOUR_TEXT_FILE -n LENGTH_OF_TEXT_TO_BE_GENERATED -c (optional)LENGTH_OF_CHUNKS_TO_BE_PROCESSED_AT_A_TIME``


The last argument (-c) is optional. The default value for it is 10 characters per chunk. Try generating texts using various chunks. You should observe that for small c (c= 1, 2, 3), the generated text resembles but is not quite English (or whatever language utilized by your modeled text). For higher order c, the text should start looking more and more like the original text.

Enjoy!
------
- A new text file called "output.txt" is created in the same folder as the file you selected.
