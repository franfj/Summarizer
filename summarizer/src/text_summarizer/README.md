# Text-Summarizer
Text summarization Python library (in progress)

#### Installation
pip install text-summarizer

#### Packages needed
- NLTK
- iso-639
- lang-detect

#### Usage
~~~~
# Import summarizer
from text_summarizer import summarizer

# Init summarizer parameters
summarizer.text = input_text
summarizer.algo = Summ.TEXT_RANK    # Summ.TEXT_RANK is equals to "textrank"
summarizer.percentage = 0.25

# Summarize with summarize() (returns a paragraph) or schematize() (returns a schema)
summarizer.summarize()
summarizer.schematize()

# You can also init the parameters in the summarize() / schematize() call
summarizer.summarize(text_to_be_summarized)
summarizer.summarize(text_to_be_summarized, "textrank", 0.5)
~~~~


[More info about Text summarization](https://github.com/icoxfog417/awesome-text-summarization)