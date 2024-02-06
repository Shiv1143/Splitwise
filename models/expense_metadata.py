class ExpenseMetadata:
    def __init__(self, name, imgUrl, notes):
        self.name = name
        self.imgUrl = imgUrl
        self.notes = notes

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_img_url(self):
        return self.imgUrl

    def set_img_url(self, imgUrl):
        self.imgUrl = imgUrl

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes
