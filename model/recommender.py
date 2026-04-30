import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/topics.csv")

df['content'] = df['Topic'] + " " + df['Tags'] + " " + df['Difficulty']

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['content'])

def recommend(subject, level):
    filtered = df[(df['Subject'] == subject) & (df['Difficulty'] == level)]
    return filtered[['Topic', 'Resource']].to_dict(orient='records')

def recommend_similar(topic_name):
    idx = df[df['Topic'] == topic_name].index[0]
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = sim_scores.argsort()[-4:-1][::-1]
    return df.iloc[similar_indices][['Topic', 'Resource']].to_dict(orient='records')