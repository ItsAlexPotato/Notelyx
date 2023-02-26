import datetime


class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags or []
        self.creation_date = datetime.datetime.now()

    def match(self, query):
        return query in self.title or query in self.content or query in " ".join(self.tags)