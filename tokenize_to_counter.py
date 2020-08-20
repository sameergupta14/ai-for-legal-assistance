from collections import Counter
import resolve_abbrev
import spacy
import wordninja
nlp = spacy.load("en_core_web_lg")



def solve(doc):          
    clean_doc = resolve_abbrev.solve(doc)
    spacy_clean_doc = nlp(clean_doc)
    split_tokens = []
    for tk in spacy_clean_doc:
        if not tk.is_stop:
            for x in wordninja.split(tk.text):
                if len(x) > 2:
                    split_tokens.append(x)
    token_counter = Counter(split_tokens)
    return token_counter