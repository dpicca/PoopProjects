import senticnet

class Emo_extractor():

    def __init__(self, disambiguated_df):
        self.emotions_df = disambiguated_df
        self.list_1st_emotion = []
        self.list_2nd_emotion = []

    def extract_emotion(self):
        self.emotions_df = self.emotions_df.astype('string')
        for each in self.emotions_df:
            for word, synset in each:
                self.emotions_df['1st emotion'] = self.emotions_df.disambiguated[word].senticnet.senticnet[word][4]
                self.emotions_df['2nd emotion'] = self.emotions_df.disambiguated[word].senticnet.senticnet[word][5]

    def get_number_of_words(self):
        pass

    def get_the_average(self):
        pass