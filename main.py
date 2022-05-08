import subprocess
import glob
import pprint
import json
import csv
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import os
import json
import subprocess
import pathlib


RESULT_FILE_PATH = "../results/**/*.json"

# RESULT_FILE_PATH = "../2022-research-data/**/*.json"

def get_contents(file_path: str):
    with open(file_path, mode="r") as f:
        data = json.load(f)
    return data

def get_commands(tokens):
    commands = []
    command = []
    _ = tokens.pop(0)
    while tokens:
        token = tokens.pop(0)
        if not token:
            continue
        if token == "AND":
            if command:
                commands.append(command)
            command = []
        else:
            command.append(token)
        
    return commands


def create_training_data():
    tr_datas = dict()
    for file_path in glob.glob(RESULT_FILE_PATH, recursive=True):
        # print(file_path)
        data = get_contents(file_path)
        results = data["Results"]
        file_path = os.path.basename(file_path)
        file_path = file_path.replace(".json", "")
        if not results:
            continue
        for hg, result in enumerate(results):
            commands = get_commands(result["Res"])
            for wd, command in enumerate(commands):
                tr_data = {
                   "{}:{}:{}".format(file_path, hg, wd): command
                   }
                tr_datas.update(tr_data)
    return tr_datas

def create_model(training_data):
    documents = [TaggedDocument(words=token, tags=[tag_name]) for tag_name, token in training_data.items()]
    model = Doc2Vec(
        documents=documents, 
        min_count=3, 
        dm=1,
        window=5
    )
    model.save("./model/doc2vec.model")

TO_JSON_FILE_PATH = "/data/"

def to_json(tag, contents):
    data = dict()
    data[tag] = contents

    return data

def test():
    trainings = create_training_data()
    # create_model(trainings)
    contents = {}
    for word, training in trainings.items():
        contents[word] = training
    print(json.dumps(contents))

def main():
    trainings = create_training_data()
    for training in trainings:
        print(training)


if __name__ == "__main__":
    main()