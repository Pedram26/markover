from distutils.core import setup
setup(
  name = 'markover',
  packages = ['markover'], # this must be the same as the name above
  scripts = ['markover/markover'],
  version = '0.3',
  description = 'Text Processing with Markov',
  author = 'Pedram Pourdavood',
  author_email = 'pedrampourdavood@gmail.com',
  url = 'https://github.com/Pedram26/pyMarkov', # use the URL to the github repo
  download_url = 'https://github.com/pedram26/pyMarkov/tarball/0.1',
  keywords = ['file', 'text processing', 'markov'], # arbitrary keywords
  classifiers = [],
)
