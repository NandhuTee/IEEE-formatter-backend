class DocumentModel:
    def __init__(self):
        self.title = ""
        self.authors = []
        self.affiliations = []
        self.abstract = ""
        self.keywords = ""
        self.sections = []
        self.tables = []
        self.figures = []
        self.references = []

class Section:
    def __init__(self):
        self.level = 1
        self.title = ""
        self.content = []