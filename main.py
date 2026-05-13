from src.utils import load_data, clean_data,data_summary

#load dataset
df= load_data("data/Titanic-Dataset.csv")

#remove dublicates
df= clean_data(df)

# data summary
df= data_summary(df)