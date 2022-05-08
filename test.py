from gensim.models.doc2vec import Doc2Vec
import json
import sys

def main(args):
    model = Doc2Vec.load("./model/doc2vec.model")

    target = str(args[0])
    
    items = model.docvecs.most_similar("276726589:1:1", topn=10)
    with open("../2022-research-data/linked.json", mode="r") as f:
        data = json.load(f)
    
    print("target:", data["276726589:1:1"])
    for cnt, item in enumerate(items):
        print(cnt, ": ", item[1])
        print(data[item[0]])
    
if __name__ == "__main__":
    main(sys.argv)
    