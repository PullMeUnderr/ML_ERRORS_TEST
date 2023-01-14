import openpyxl

error_list_xlsx = openpyxl.open("stanok_error_list.xlsx", read_only=True)
cycle = True
def machine_selection():
   while True:
        ktf = ["ktf", "KTF", "КТФ", "ктф", "rna", "RNF", "ЛЕА", "леа"]
        ml = ["ML", "ml", "мл", "МЛ", "ьд", "ЬД", "vk", "VK", "TBT", "tbt", "тбт", "ТБТ", "n,n", "N,N", "ЕИЕ", "еие"]
        machine = input("Выберите ваш станок: ")
        if machine.lower() in ml:
            return error_list_xlsx.worksheets[0]
        elif machine.lower() in ktf:
            return error_list_xlsx.worksheets[1]
        else:
            print("Станок не найден")

error_list = machine_selection()
if error_list != error_list_xlsx.worksheets[0] and error_list != error_list_xlsx.worksheets[1]:
    cycle = False
while cycle == True:

    number = input("Введите номер вашей ошибки: ")


    def error_search(error_number):
        flag = False
        for i in range(1, error_list.max_row + 1):
            error_line = error_list[i][0].value
            if str(error_number).isdigit() == False:
                return "Это не номер ошибки"
            elif str(error_number) in error_line[:6] and str(error_number) == error_line[:6] and str(error_number).isdigit() == True:
                    error_text = error_list[i][0].value
                    flag = True
                    return f"Ваша ошибка:{error_text[6:].title()}"

        if flag == False:
            return "Такой ошибки не существует!"


    print()
    print(error_search(number))
    print()
