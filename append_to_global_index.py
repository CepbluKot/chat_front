import base64
import torch
import os
from byaldi import RAGMultiModalModel
from os import listdir
from os.path import isfile, join


RAG_with_index = RAGMultiModalModel.from_index(
    index_path="./global_index",  # Путь к папке с индексом
    verbose=1,
    device="cuda",  # Укажите устройство, например "cuda" или "cpu"
)

saved_filenames = set()
doc_ids_to_file_names_copy = RAG_with_index.get_doc_ids_to_file_names()
for key in doc_ids_to_file_names_copy:
    filename = doc_ids_to_file_names_copy[key]
    filename = filename.split("/")[-1]
    saved_filenames.add(filename)

mypath = "./docs"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print('onlyfiels', onlyfiles)
# print('saved_filenames', saved_filenames)
for filename in onlyfiles:
    curr_path = mypath + "/" + filename
    if filename not in saved_filenames:
        print("adding ", curr_path)
        RAG_with_index.add_to_index(
            input_item=curr_path, store_collection_with_index=False
        )
