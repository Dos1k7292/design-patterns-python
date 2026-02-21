class Report:
    def __init__(self):
        self.header = ""
        self.content = ""
        self.footer = ""

    def show(self):
        print(self.header)
        print(self.content)
        print(self.footer)
