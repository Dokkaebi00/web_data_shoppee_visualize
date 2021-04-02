import pandas as pd 
import numpy as np 
import os

data_frame = pd.read_csv('./Data_shoppee/train.csv')

def list_label_group():  
    list_label = data_frame["label_group"].unique()
    return list_label

def information_retrieval(label_group):
    data_retrieval = data_frame.loc[data_frame["label_group"] == label_group]
    
    list_image_paths = data_retrieval['image'].to_numpy()
    list_titles = data_retrieval['title'].to_numpy()
    return list_image_paths, list_titles

def search_by_label(label_search):
    list_label = list_label_group()
    for i in range(0, len(list_label)):
        list_label[i] = str(list_label[i])
    labels_founded = [lf for lf in list_label if label_founded in lf]
    return list(sorted(label_founded))