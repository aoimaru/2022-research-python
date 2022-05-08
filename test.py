from gensim.models.doc2vec import Doc2Vec
import json
import sys

def main(args):
    model = Doc2Vec.load("./model/doc2vec.model")

    target = str(args[0])
    items = model.docvecs.most_similar(args[1], topn=10)
    with open("../2022-research-data/linked.json", mode="r") as f:
        data = json.load(f)
    
    print("src:", data[args[1]])
    print()
    for cnt, item in enumerate(items):
        print(cnt, ": ", item[1])
        print(item[0], ": " ,data[item[0]])
    
if __name__ == "__main__":
    main(sys.argv)
    