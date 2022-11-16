# importing libraries

import demoji
import json
import pandas as pd
import re
import os

from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

# IMPORT DATASET PATHS

CURRENT_DIR = os.getcwd()
print(CURRENT_DIR)
PARENT_DIR = CURRENT_DIR.replace("/notebooks/visualizations", "")
RAW_DATA_DIR = PARENT_DIR + "/data/raw"
CLEAN_DATA_DIR = PARENT_DIR + "/data/preprocessed/clean"
LOCATION_DATA_DIR = PARENT_DIR + "/data/preprocessed/location"

# print(RAW_DATA)
JSON_DATA = ...

stop_word = stopwords.words("english")
df = pd.read_csv("../data/raw/cyberbullying_tweets.csv")


def super_clean(df):

    # Opening JSON file
    f = open("../data/external/profanity_list.json")
    profanity_data = json.load(f)

    # extract emojis
    def extract_emoji(txt):
        emoji_txt = demoji.findall(txt)
        emoji_keys = emoji_txt.keys()
        emoji_values = emoji_txt.values()
        return " ".join(list(map(str, emoji_keys))), " ".join(
            list(map(str, emoji_values))
        )

    # extract hashtags
    def hashtags(txt):
        txt = re.findall("#([a-zA-Z0-9_]{1,50})", txt)
        return " ".join(list(map(str, txt)))

    # extract mentions
    def mentions(txt):
        txt = re.findall("@([a-zA-Z0-9_]{1,50})", txt)
        return " ".join(list(map(str, txt)))

    # lookup profanity manually
    def find_profanity(text):
        profanity_set = set()
        for word in text.split():
            if word in profanity_data:
                profanity_set.add(word)
        return " ".join(list(map(str, profanity_set)))

    def lemma(words):
        lemmatizer = WordNetLemmatizer()
        lemma_list = [
            lemmatizer.lemmatize(token, "v") for token in word_tokenize(words)
        ]
        sentence = " ".join(lemma_list)
        return sentence

    df["profanity_list"] = df["tweet_text"].apply(lambda x: find_profanity(x))
    df["hashtags"] = df["tweet_text"].apply(lambda x: hashtags(x))
    df["mentions"] = df["tweet_text"].apply(lambda x: mentions(x))
    df["emoji_face"] = df["tweet_text"].apply(lambda x: extract_emoji(x)[0])
    df["emoji_names"] = df["tweet_text"].apply(lambda x: extract_emoji(x)[1])

    # remove stopwords
    df["clean_txt"] = df["tweet_text"].apply(
        lambda x: " ".join(
            word for word in x.split() if word not in stop_word or len(word) > 2
        )
    )
    df["clean_txt"] = df["clean_txt"].apply(lambda x: re.sub("@[A-Za-z0-9_]+", "", x))
    # remove hashtags
    df["clean_txt"] = df["clean_txt"].apply(lambda x: re.sub("#[A-Za-z0-9_]+", "", x))
    # to lowercases
    df["clean_txt"] = df["clean_txt"].str.lower()

    df["clean_txt"] = df["clean_txt"].apply(
        lambda x: " ".join(word for word in x.split() if word not in stop_word)
    )
    df["clean_txt"] = df["clean_txt"].apply(lambda x: re.sub(r"http\S+", "", x))  #
    df["clean_txt"] = df["clean_txt"].str.replace("[^a-zA-Z#]", " ")  # z3 puntuation
    df["clean_txt"] = df["clean_txt"].apply(
        lambda x: " ".join(word for word in x.split() if len(word) > 2)
    )
    df["clean_txt_lemma"] = df["clean_txt"].apply(lambda x: lemma(x))  # lemmatize

    df["clean_txt_emoji"] = df["clean_txt_emoji"] + df["emoji_names"]
    df["clean_txt_emoji"] = df["clean_txt_emoji"].apply(
        lambda x: " ".join(word for word in x.split() if word not in stop_word)
    )
    df["clean_txt_emoji"] = df["clean_txt_emoji"].apply(
        lambda x: re.sub(r"http\S+", "", x)
    )  #
    df["clean_txt_emoji"] = df["clean_txt_emoji"].str.replace(
        "[^a-zA-Z#]", " "
    )  # z3 puntuation
    df["clean_txt_emoji"] = df["clean_txt_emoji"].apply(
        lambda x: " ".join(word for word in x.split() if len(word) > 2)
    )
    df["clean_txt_emoji_lemma"] = df["clean_txt_emoji"].apply(
        lambda x: lemma(x)
    )  # lemmatize

    return df


clean_df = super_clean(df)
clean_df.to_csv("../data/external/processed/clean_df.csv")
