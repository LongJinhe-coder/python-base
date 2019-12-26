# encoding: UTF-8
# book_list = []
# info_dict = {"name": "小明", "borrowed_book": book_list}
# print(info_dict)

student_list = []


def borrow_books(num):
    for i in range(num):
        name = input("输入你的名字")
        n = int(input("你想借几本书"))
        info_dict = {}
        student_list.append(info_dict)
        student_list[i]["name"] = name
        book_list = []
        student_list[i]["borrowed_book"] = book_list
        for x in range(n):
            student_list[i]["borrowed_book"].append(input("输入你借的书名"))


def show_info():
    for i in range(len(student_list)):
        print("{}借了".format(student_list[i]["name"]))
        for j in range(len(student_list[i]["borrowed_book"])):
            print(student_list[i]["borrowed_book"][j])


borrow_books(2)
show_info()
