import os

BOOK_PATH = 'book\\book2.txt'
PAGE_SIZE = 100  # дефолтное значение 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation_list: tuple = (',', '.', '!', ':', ';', '?')
    text = text[start:start + size]
    i: int = len(text) - 1
    # print("text= ", text, "text[i]= ", text[i], "text[i-1]= ", text[i-1])
    if (text[i] in punctuation_list):
        while (text[i - 1] in punctuation_list):
            i -= 2
    if (text[i] not in punctuation_list):
        while (text[i] not in punctuation_list and (i >= 0)):
            # print("!!" + text[i] + " " + str(i))
            i -= 1
    if (text[i] == ' '):
        i -= 1
    # print(text[i] + " " + str(i+1))
    text = text[0:i + 1]

    result: tuple[str, int] = text, len(text)

    return result


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        tmp = _get_part_text(content, 0, PAGE_SIZE)
        book[1] = tmp[0]
    file.close()

    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))


if __name__ == '__main__':

    print(book)

    text = 'Раз. Два. Три. Четыре. Пять. Прием!'
    # print(*_get_part_text(text, 5, 9), sep='\n')
    # print("---")
    assert (_get_part_text('Раз. Два. Три. Четыре. Пять. Прием!', 5, 9)) == ('Два. Три.', 9)

    text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'
    # print("--2--")
    # print(*_get_part_text(text, 22, 145), sep='\n')
    assert (_get_part_text('Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!', 22, 145)) == ('Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит,', 139)

    text = '— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, в чём вопрос.'
    # print("--3--")
    # print(*_get_part_text(text, 54, 70), sep='\n')
    assert (_get_part_text('— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, в чём вопрос.', 54, 70)) == ('— и со всей определённостью заявляю, что это и есть ответ.', 58)

    # print("--4--")
    text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'
    # print(*_get_part_text(text, 0, 54), sep='\n')
    assert (_get_part_text('Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!', 0, 54)) == ('Да? Вы точно уверены? Может быть,', 33)

    # assert (prepare_book('d:\Arxiv\Programming\Python\Bookbot\book\book.txt')) == None
