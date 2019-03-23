from difflib import SequenceMatcher


class StringMathing:
    def __init__(self, stock_items):
        self.stock_items = stock_items

    @staticmethod
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def get_closest_item_from_string(self, string):
        best_item = self.stock_items[0].name
        max_value = self.similar(best_item, string)

        for item in self.stock_items:
            value = self.similar(item.name, string)

            if value > max_value:
                max_value = value
                best_item = item

        return item

if __name__ == "__main__":
    a = "oioioi"
    b = "oioioy"
    c = "cachorro"

    print(StringMathing.similar(a, b))
    print(StringMathing.similar(a, c))
