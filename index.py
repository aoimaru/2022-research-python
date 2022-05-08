

def test():
    lines = []
    with open("index.txt", mode="r") as f:
        for line in f:
            lines.append(line)
    
    for line in lines:
        print(line)



def main():
    test()

if __name__ == "__main__":
    main()