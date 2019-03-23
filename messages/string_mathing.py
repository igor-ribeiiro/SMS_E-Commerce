from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


if __name__ == "__main__":
    a = "oioioi"
    b = "oioioy"
    c = "cachorro"

    print(similar(a, b))
    print(similar(a, c))
