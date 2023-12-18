# Imports

import pandas as pd


# Load question and answer dataset into dataframes
df1 = pd.read_csv('../input/qa_dataset/S08_question_answer_pairs.txt', sep='\t')
df2 = pd.read_csv('../input/qa_dataset/S09_question_answer_pairs.txt', sep='\t')
df3 = pd.read_csv('../input/qa_dataset/S10_question_answer_pairs.txt', sep='\t', encoding = 'ISO-8859-1')

# Combine into one dataframe
all_data = pd.concat([df1, df2, df3], ignore_index=True)

#Join topic (article title) to the question to keep context
all_data['Question'] = all_data['ArticleTitle'].str.replace('_', ' ') + ' ' + all_data['Question']
all_data = all_data[['Question', 'Answer']]

#Delete duplicates
all_data = all_data.drop_duplicates(subset='Question')

#Clean the text
def text_cleaning(text):
    if isinstance(text, str):  # Check if the value is a string
        text = "".join([char for char in text if char not in string.punctuation])
    return text

# Apply the text cleaning function to the "Questions" column, handling NaN values
all_data['Question'] = all_data['Question'].apply(text_cleaning)

#Drop Null vales
all_data = all_data.dropna()

