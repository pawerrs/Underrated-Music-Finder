class Song:
    
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def to_string(self):
        return self.title + ": " + self.url