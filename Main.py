from data import Data

if __name__ == "__main__":
    data = Data('Vasya.bd', 'tehnick')
    buf = 1
    while int(buf) != 7:
        print("Що ви хочете зробити!")
        print("Вивести всі дані - 1")
        print("Вивести техніку якій потрібен ремонт - 2")
        print("Змінити стан техніки - 3")
        print("Pемонтувати техніку - 4")
        print("Видалити техніку - 5")
        print("Додати техніку - 6")
        print("Вийти - 7")
        buf = input("Цифра - ")
        print("=====================\n")
        if int(buf) == 1:
            data.FullDataMachinery()
        if int(buf) == 2:
            data.show_machinery_for_repair()
        if int(buf) == 3:
            id = input("id - ")
            status = input("Дыйсний стан - ")
            data.setStatusMachinery(int(id), status)
        if int(buf) == 4:
            id = input("id - ")
            data.repairMachinery(int(id))
        if int(buf) == 5:
            id = input("id - ")
            data.delMachinery(id)
        if int(buf) == 6:
            model = input("Модель техніки - ")
            status = input("Стан техніки - ")
            data.addMachinery(model, status)
        print("\n=====================\n")