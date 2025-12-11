import pandas as pd
import string
from pathlib import Path

class Model:
    def __init__(self, training_text):
        """
        Reads through an text and determins the rate of occurance of letter pairs within the text.
        Args:
            training_text ("file.txt"): The text that will be read to determin the frequency of letter pairs.
        """
        text_file = open(training_text, "r")
        self.training_text = text_file.read().lower()
        self.possible_keys = {k:0 for k in range(0, 26)}
        self.adj_pairs = {}
        self.pair_count = 0
        self.alpha = list(string.ascii_lowercase)

    def make_model(self, csv_file):
        """
        Reads the text and writes the letter pair frequencies to a csv file.
        Args:
            csv_file ("file/csv"): The csv file that the data will be written to.
        """
        for i, char in enumerate(self.training_text):
            try:
                if (char not in self.alpha) or (self.training_text[i + 1] not in self.alpha): #The current carecter or th one that fallows is not a letter.
                    continue
                elif (char  + self.training_text[i + 1]) not in self.adj_pairs: #The current pair has not been added yet
                    self.adj_pairs[char + self.training_text[i + 1]] = 1
                    self.pair_count += 1
                else:
                    self.adj_pairs[char + self.training_text[i + 1]] += 1 #The currnet pair has been added
                    self.pair_count += 1
            except IndexError: #IndexError on last char
                break
        self.adj_pairs = {k:(self.adj_pairs[k]/self.pair_count) for k in self.adj_pairs} #Convert from pair count to pari frequency
        self.adj_pairs = dict(sorted(self.adj_pairs.items(), key=lambda i: i[1], reverse=True)) #Order pairs by frequency
        lables = ["Pairs", "Freq"] #Lables for columns of DataFrame
        columns = [list(self.adj_pairs), list(self.adj_pairs.values())] #Columns of DataFrame
        self.pair_df = pd.DataFrame({k:v for (k, v) in zip(lables, columns)}) #Make DataFrame of pairs and frequencies
        self.pair_df.to_csv(csv_file, index=False) #Write DataFrame to csv file

def main():
    while True: #Get training text
        training_text = input("Enter the name of the training text file: ")
        file_path = Path(training_text) #Check if the file exists
        if file_path.is_path():
            break
        else:
            print(f"{traing_text} does not exist\nEnsure that you've included the full path to your file.")
    while True: #Get location to put the model
        csv_file = input("Enter the name of the csv file that you would like tor write the model to: ")
        file_path = Path(csv_file):
        if file_path.is_path(): #If the file alredy exists
            overwrite_check = input(f"{csv_file} already exists. Would you like to overwrite this file?[y/n]: ") #Check if they want to overwrite it
        if overwrite_check == "y":
            break
        else:
            continue
    model = Model(training_text)
    model.make_model("model.csv")


    # m1 = Model("training_text.txt")
    # m1.make_model("model.csv")
    # print(m1.pair_df, f"\nTotal Pairs: {m1.pair_count}\nUnique Pairs: {len(m1.adj_pairs)}")



if __name__ == "__main__":
    main()
