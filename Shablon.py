def machine_selection():
    ktf = ["ktf", "KTF", "КТФ", "ктф", "rna", "RNF", "ЛЕА", "леа"]
    ml = ["ML", "ml", "мл", "МЛ", "ьд", "ЬД", "vk", "VK"]
    machine = input("Выберите ваш станок")
    if machine.lowcase() in ml:
        return "ML"
    elif machine.lowcase() in ktf:
        return "KTF"
error_list = error_list_xlsx.worksheet[machine_selection()]