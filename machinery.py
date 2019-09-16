
class Machinery:
    def __init__(self, id, model,  dateLastReview, status):
        self.id = id
        self.model = model
        self.dataLastReview = dateLastReview
        self.status = status

    @property
    def getId(self):
        return int(self.id)

    @property
    def getModel(self):
        return self.model

    @property
    def getDateLastReview(self):
        return self.dataLastReview

    @property
    def getStatus(self):
        return self.status

    @getModel.setter
    def setModel(self, model):
        self.model = str(model)

    @getDateLastReview.setter
    def setDateLastReview(self, dateLastReview):
        self.dataLastReview = str(dateLastReview)

    @getStatus.setter
    def setStatus(self, status):
        self.status = str(status)

    def print(self):
        print("{} |{} |{}\t\t\t|{}".format(str(self.getId),
                                           self.getModel,
                                           self.getDateLastReview,
                                           self.getStatus))