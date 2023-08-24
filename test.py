import os

file_path = 'd:\\Arxiv\\Programming\\Python\\Bookbot\\book\\book2.txt'
if os.path.exists(file_path):
    print("Файл существует")
else:
    print("Файл не существует")
