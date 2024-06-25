import requests

class Publication:
    __udc = "0.0.0"
    default_format = "hardcover"
    default_edition = "basic edition"


    def __init__(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher


    # Метод класса зависит от экземпляра
    def get_short_info(self):
        return f'{self.title} by {self.author} '


    # Метод класса, общий для всех
    @classmethod
    def get_default_edition(self):
        return self.default_edition, self.default_format

    # Публичный метод, работающий с приватным аттрибутом
    def get_udc(self):
        return self.__udc


    # Приватный метод класса
    def __set_udc(self, udc):
        self.__udc = udc





class Book(Publication):
    def get_book_udc(self):
        return self.__udc


    @staticmethod
    def get_random_phrase():
        r = requests.get("https://citbase.ru/random")
        txt = r.text
        tag_begin = "<pre>"
        tag_end = "</pre>"
        beg = txt.find(tag_begin) + len(tag_begin)
        end = txt.find(tag_end)
        txt = txt[beg:end]
        return txt
        # with open("response.html", "w") as f:
        #     f.write(r.text)


if __name__ == "__main__":
    pub = Publication("Статья", "Иванов И.И.", 2024, "Зеленоград24")
    book = Book("Мастер и Маргарита", "Булгаков М.А.", 2024, "АСТ")
    # print(pub.get_short_info())
    # print(Publication.get_default_edition())
    print(book.get_udc())
    #print(book.get_book_udc())
    print(Book.get_random_phrase())