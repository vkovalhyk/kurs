import sqlite3
import datetime
from machinery import Machinery


class Data:
    def __init__(self, nameDataBase, table):
        self.nameDataBase = nameDataBase
        self.table = table
        self.connect = sqlite3.connect(self.nameDataBase)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT * FROM {}".format(self.table))
        self.arr = self.cursor.fetchall()
        self.array = []
        for i in self.arr:
            self.array.append(Machinery(i[0], i[1], i[2], i[3]))

    def FullDataMachinery(self):
        print("id|Модель|Дата Останього ремонту|Стан техніки")
        for i in self.array:
            i.print()

    def addMachinery(self, model, status):
        self.array.append(Machinery(len(self.array), model, str(datetime.date.today()), status+"%"))

    def delMachinery(self, id):
        self.array.pop(int(id) - 1)

    def repairMachinery(self, id):
        id -= 1
        self.array[id].setStatus = "100%"
        self.array[id].setDateLastReview = datetime.date.today()

    def setStatusMachinery(self, id, status):
        id -= 1
        self.array[id].setStatus = status + "%"
        self.array[id].setDateLastReview = datetime.date.today()

    def show_machinery_for_repair(self):
        print("id|Модель|Дата Останього ремонту|Стан техніки")
        for i in self.array:
            temp = str(i.getStatus)
            if int(temp.replace('%', '')) < 60:
                i.print()

    def __del__(self):
        self.cursor.close()
        self.connect.close()








