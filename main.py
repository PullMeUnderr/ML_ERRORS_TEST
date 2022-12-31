import openpyxl

error_list_xlsx = openpyxl.open("Spisok_oshibok_ML_dlya_programmy_Python.xlsx", read_only=True)

error_list = error_list_xlsx.active
while True:

    number = input("Введите номер вашей ошибки: ")


    def error_search(error_number):
        flag = False
        for i in range(1, error_list.max_row + 1):
            error_line = error_list[i][0].value
            if str(error_number).isdigit() == False:
                return "Это не номер ошибки"
            if str(error_number) in error_line[:6] and str(error_number) == error_line[:6] and str(error_number).isdigit() == True:
                    error_text = error_list[i][0].value
                    flag = True
                    return f"Ваша ошибка:{error_text[6:].title()}"

        if flag == False:
            return "Такой ошибки не существует!"


    print()
    print(error_search(number))
    print()
