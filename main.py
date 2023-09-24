class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


class Bookcase:
    def __init__(self, sp):
        self.sp_books = sp

    def make_line(self, sp_books):  # возвращение строки из списка
        sp = []
        for i in sp_books:
            sp.append(f"{i.name} - {i.author}")
        return ', '.join(sp)

    def sort_by_author(self):  # сортировка по авторам
        sp_sort = list(sorted(self.sp_books, key=lambda x: x.author))
        return self.make_line(sp_sort)

    def sort_by_name(self):  # сортировка по названиям
        sp_sort = list(sorted(self.sp_books, key=lambda x: x.name))
        return self.make_line(sp_sort)

    def find_book(self, line):  # нахождение книги по подстроке
        sp_choose = list(filter(lambda x: line.lower() in x.name.lower(), self.sp_books))
        return self.make_line(sp_choose)


if __name__ == '__main__':
    sp = Bookcase([Book('Портрет Дориана Грея', 'Оскар Уайльд'), Book('Скотный двор', 'Джордж Оруэлл'),
                   Book('Гроза', 'Александр Островский')])
    print(sp.sort_by_author())
    print(sp.sort_by_name())
    print(sp.find_book('гроза'))
