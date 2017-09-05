from distutils.core import setup

with open("README.rst", "rb") as f:
    long_description = f.read()

setup(
  name = 'markover',
  packages = ['markover'], # this must be the same as the name above
  scripts = ['markover/markover'],
  version = '1.0',
  description = 'Natural Language Generator with Markov',
  long_description = long_description,
  author = 'Pedram Pourdavood',
  author_email = 'pedrampourdavood@gmail.com',
  url = b'https://github.com/Pedram26/markover'.decode("utf-8"), # use the URL to the github repo
  download_url = b'https://github.com/pedram26/markover/archive/1.4.tar.gz'.decode("utf-8"),
  keywords = ["file", "text processing", "natural language", "markov"], # arbitrary keywords
  classifiers = []
)
