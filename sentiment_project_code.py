# Sentiment Analysis Mini-Project (Proof of Work)
import random, io, textwrap
from collections import defaultdict, Counter
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

random.seed(42)
positive_templates = [
    "I absolutely love this movie, it was fantastic",
    "Great product, exceeded my expectations",
    "Amazing quality and very easy to use",
    "Brilliant performance, would definitely recommend",
    "I am very satisfied, the experience was wonderful",
    "Loved it, superb value for money",
    "The design is elegant and the results are impressive",
    "Everything worked perfectly for me",
    "Customer support was helpful and responsive",
    "Five stars, flawless from start to finish",
]
negative_templates = [
    "I hate this, it was terrible",
    "Very disappointing and a complete waste",
    "Poor quality and hard to use",
    "Awful performance, I would not recommend",
    "I am not satisfied, the experience was horrible",
    "Did not like it at all, bad value",
    "The design is ugly and the results are weak",
    "Nothing worked properly for me",
    "Customer support was unhelpful and slow",
    "One star, problems from start to finish",
]
neutral_templates = [
    "It was okay, nothing special",
    "Average experience, neither good nor bad",
    "The product works as expected",
    "I tried it briefly and it seemed fine",
    "Service was acceptable overall",
    "Standard features and normal performance",
    "I have mixed feelings about this",
    "Decent but could be better",
    "Not sure yet, still testing",
    "Typical results, nothing to highlight",
]
def jitter_sentence(s):
    import random
    tails = ["", ".", "!", " :)", " :(", " ..."]
    return s + random.choice(tails)
def make_dataset(n_pos=40, n_neg=35, n_neu=25):
    data = []
    import random
    for _ in range(n_pos):
        data.append(jitter_sentence(random.choice(positive_templates)))
    for _ in range(n_neg):
        data.append(jitter_sentence(random.choice(negative_templates)))
    for _ in range(n_neu):
        data.append(jitter_sentence(random.choice(neutral_templates)))
    random.shuffle(data)
    return data
comments = make_dataset()

positive_words = {
    "love","fantastic","great","exceeded","amazing","easy","brilliant","recommend",
    "satisfied","wonderful","superb","value","elegant","impressive","perfectly",
    "helpful","responsive","five","flawless"
}
negative_words = {
    "hate","terrible","disappointing","waste","poor","hard","awful","not","horrible",
    "bad","ugly","weak","nothing","unhelpful","slow","problems","one"
}
def sentiment_score(text):
    tokens = [t.strip(".,!?():;").lower() for t in text.split()]
    score = 0
    for t in tokens:
        if t in positive_words:
            score += 1
        if t in negative_words:
            score -= 1
    return score
def classify(score, pos_th=1, neg_th=-1):
    if score >= pos_th:
        return "Positive"
    elif score <= neg_th:
        return "Negative"
    else:
        return "Neutral"
records = []
for i, c in enumerate(comments, start=1):
    s = sentiment_score(c)
    label = classify(s)
    records.append({"id": i, "comment": c, "score": s, "label": label})
df = pd.DataFrame(records)
df.to_csv("/mnt/data/sentiment_labeled_dataset.csv", index=False)
# create a simple bar chart as proof
counts = df["label"].value_counts()
plt.figure()
plt.bar(counts.index.tolist(), counts.values.tolist())
plt.title("Sentiment Counts")
plt.xlabel("Class"); plt.ylabel("Count")
plt.savefig("/mnt/data/sentiment_counts.png", bbox_inches="tight")
print("Saved: /mnt/data/sentiment_labeled_dataset.csv and /mnt/data/sentiment_counts.png")
