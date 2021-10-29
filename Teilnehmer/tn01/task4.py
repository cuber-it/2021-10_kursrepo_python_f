import pandas as pd

#"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"

class Quotes:

        def __init__(self, filepath):
            self.filepath = filepath

        def read_file(self):
            df = pd.read_csv()
            print(self.df.head())
            return self.df

       

if __name__ == "__main__":
    quotes = Quotes.read_file()