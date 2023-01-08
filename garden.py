import spacy
# Create a list of garden path sentences and assign the list to a variable called garden path
garden_path = ["The old man the boat.", "The complex houses married and single soldiers and their families.", "The horse raced past the barn fell.", "The florist sent the flowers was pleased.","We painted the wall with cracks."]
nlp = spacy.load("en_core_web_sm")

for sample in garden_path:
    doc = nlp(sample)
    # Tokenisation of each of the sentences
    print([token.orth_ for token in doc])
    # Entitity recognition of each of the sentences
    print([(i, i.label_, i.label) for i in doc.ents])