import json

class MyBooks:
    def __init__(self):
        try:
            with open("mybooks.json", "r") as f:
                self.mybooks = json.load(f)
        except FileNotFoundError:
            self.mybooks = []
        
    def all(self):
        return self.mybooks

    def get(self, id):
        return self.mybooks[id]

    def create(self, data):
        data.pop('csrf_token')
        self.mybooks.append(data)

    def save_all(self):
        with open("mybooks.json", "w") as f:
            json.dump(self.mybooks, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.mybooks[id] = data
        self.save_all()

mybooks = MyBooks()