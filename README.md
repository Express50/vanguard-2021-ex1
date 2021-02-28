## NER on FIGER dataset using spaCy

This work attempts to use a simple NER model from spaCy to predict correct NER tags
from the FIGER dataset. We first convert each input sentence into (potentially multiple)
sentence(s), tagged with B, I, O tags corresponding to the hierarchial tags from the provided labels.

### Installation

1. Install spaCy and required packages by running ```pip install requirements.txt```
2. Install spaCy's English model by running ```python -m spacy download en_core_web_sm```
3. Place the FIGER training/test/dev JSON files in a folder called ```FIGER```

You should now be able to run the `ner.ipynb` notebook in order to process the data and run the model.
An example output of the training process can be seen in `output.txt`.