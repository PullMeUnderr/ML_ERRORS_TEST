import openpyxl

error_list_xlsx = openpyxl.open("Spisok_oshibok_ML_dlya_programmy_Python.xlsx", read_only=True)

sheet = error_list_xlsx.active
error_list = sheet
error_text = ''


print("Введите номер вашей ошибки:")
number = int(input())


def error_search(error_number):
    flag = False
    for i in range(1, error_list.max_row + 1):
        error_line = error_list[i][0].value
        if str(error_number) in error_list[i][0].value and str(error_number) == error_line[:6]:
            error_text = error_list[i][0].value
            flag = True
            return f"Ваша ошибка:{error_text[6:].title()}"
    if flag == False:
        return "Такой ошибки не существует!"


print(error_search(number))
