import json
from loader import LoaderData
from processor import Processor
import pandas as pd
from pprint import pprint
import os

URI = os.getenv("HOST", "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
DB_NAME = os.getenv("DB_NAME", "IranMalDB")
# PATH_TO_WEAPON_FILE = os.getenv("PATH", "..\data\weapon_list.txt")
# for testing
path = "..\data\weapon_list.txt"


class Manager:



    def __init__(self):
        self.loader = LoaderData(URI, DB_NAME)
        self.processor = Processor()
        self.DF = self.processor.DF
        self.cleaning_and_process(path)





    def cleaning_and_process(self, path_to_weapons ):

        # set the weapons list to check
        self.processor.set_blacklist(path_to_weapons)
        weapon_list = self.processor.blacklist

        result_dict = {}
        for index, row in self.DF.iterrows():


            # extract column from dataframe
            text = self.processor.get_text(row)
            # pprint(text)

            # find the rarest word
            reare_word = self.processor.find_the_rarest_word(text)
            self.DF["rarest_word"] = reare_word

            # define the Sentiment of text
            score = self.processor.score_Sentiment_to_df(self.processor.score_text_Sentiment(text))
            self.DF["score_Sentiment"] = score

            # add a weapon if there is
            weapon = self.processor.find_weapon(weapon_list,text)
            if weapon:
                self.DF["weapons"] = weapon

        # pprint(self.DF)


    def get_df_as_list_of_json(self):
        df = self.DF
        json_lst = []
        for i in range(len(df)):
            d = json.loads(df.iloc[i, :].to_json())
            json_lst.append(d)
        return json_lst




# m = Manager()
# pprint(m.get_df_as_list_of_json())






















