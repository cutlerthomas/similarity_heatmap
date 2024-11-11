import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

data = []
with open('articles/part-00000', 'r') as f:
    for line in f:
        data.append(json.loads(line))

sources = list(set([entry["source1"] for entry in data] + [entry["source2"] for entry in data]))
matrix = pd.DataFrame(1.0, index=sources, columns=sources, dtype=float)

for entry in data:
    matrix.loc[entry["source1"], entry["source2"]] = entry["similarity"]
    matrix.loc[entry["source2"], entry["source1"]] = entry["similarity"]

plt.figure(figsize=(10, 8))
sns.heatmap(matrix, annot=True, cmap="coolwarm", cbar=True, square=True)
plt.title("Cosine Similarity Heatmap of News Sources")
plt.savefig("cosine_similarity_heatmap.pdf", format="pdf", bbox_inches="tight")
plt.show()
