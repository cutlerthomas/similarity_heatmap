#!/bin/python3

import sys
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


sources = []
texts = []

for line in sys.stdin:
    data = json.loads(line.strip())
    sources.append(data["source"])
    texts.append(data["content"])

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

cosine_sim_matrix = cosine_similarity(tfidf_matrix)

for i, source1 in enumerate(sources):
    for j, source2 in enumerate(sources):
        if i < j: 
            similarity = cosine_sim_matrix[i, j]
            print(json.dumps({"source1": source1, "source2": source2, "similarity": similarity}))
