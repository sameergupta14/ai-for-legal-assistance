#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 02:22:51 2020

@author: scream
"""


from collections import Counter
import resolve_abbrev
import spacy
nlp = spacy.load("en_core_web_lg")



def solve(path):
    doc = ""
    with open(path) as f:
        for line in f.readlines():
            doc += line
            
    clean_doc = resolve_abbrev.solve(doc)
    spacy_clean_doc = nlp(clean_doc)
    tokens = [token.text for token in spacy_clean_doc if not token.is_stop and len(token) > 2]
    token_counter = Counter(tokens)
    return token_counter