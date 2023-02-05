student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict()) # zo krijgen we niet het gewenste resultaat.



#TODO 1. Create a dictionary in this format:

nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
#print(nato_alphabet) # dit is het resultaat dat we willen.

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_phonic()
    else:
        print(output_list)

generate_phonic()