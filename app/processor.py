from loader import  LoaderData
import data
import os
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# for testing
URI = os.getenv("URI", "mo/")
DB_NAME = os.getenv("DB_NAME", "IranMalDB")


class Processor:

    def __init__(self):
        self.data = self.bring_data(URI,DB_NAME)
        self.DF = pd.DataFrame(self.data)
        self.blacklist = None


    def set_blacklist(self,path):
        with open(path, "r") as weap:
            weapons = weap.read()
        self.blacklist = list(weapons)


    def bring_data(self, URI, db_name):
        loader = LoaderData(URI,db_name)
        data = loader.get_all()
        return list(data)

    def get_text(self, raw ):
        text = raw["Text"]
        return text

    def score_text_Sentiment(self, text):
        score=SentimentIntensityAnalyzer().polarity_scores(text)
        return score["compound"]

    def score_Sentiment_to_df(self, score):
        if score > 0.5 :
            return "positive"
        elif score == 0.49 :
            return "natural"
        elif score < -0.5:
            return "negative"


    def find_weapon(self, weapon_list: list, text: str):
        """ find if in the text there are a weapon mention """
        splited_text = text.split()
        for weapon in weapon_list:
            if weapon in splited_text:
                return weapon
        # return None


    def add_weapon_to_df(self, weapon):
        """ add a field to the df with the weapon name """
        self.DF["weapons"] = weapon


    def find_the_rarest_word(self, text):
        """find the rarest_word in the text """
        words = {}
        splited_text = text.split()
        for word in splited_text:
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
        rear = min(words.values())
        for key, val in words.items():
            if val == rear:
                return key









# # for testing
# uri = "t/"
# db_name = "IranMalDB"
# p = Processor()


