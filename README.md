[![PyPI version](https://badge.fury.io/py/text-summarizer.svg)](https://badge.fury.io/py/text-summarizer)
[![PyPI python version](https://img.shields.io/pypi/pyversions/text-summarizer.svg)](https://badge.fury.io/py/text-summarizer)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ffranfj%2FSummarizer.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Ffranfj%2FSummarizer?ref=badge_shield)

# Text-Summarizer
Text summarization Python library (in progress)

#### Installation
pip install text-summarizer

#### Packages needed
See requirements.txt

#### Usage
~~~~
# Import summarizer
from text_summarizer import summarizer

# Init summarizer parameters
summarizer.text = input_text
summarizer.algo = Summ.TEXT_RANK    # Summ.TEXT_RANK is equal to "textrank"
summarizer.percentage = 0.25

# Summarize with summarize() (returns a paragraph) or schematize() (returns a schema)
summarizer.summarize()
summarizer.schematize()

# You can also init the parameters in the summarize() / schematize() call
summarizer.summarize(text_to_be_summarized)
summarizer.summarize(text_to_be_summarized, "textrank", 0.5)
~~~~

#### More (theorical) information about text summarization

[More info in icoxfog417/awesome-text-summarization](https://github.com/icoxfog417/awesome-text-summarization)

#### License

Copyright 2018 Francisco Javier Rodrigo Ginés

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Ffranfj%2FSummarizer.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Ffranfj%2FSummarizer?ref=badge_large)