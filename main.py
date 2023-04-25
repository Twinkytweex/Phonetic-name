
with open('file.txt') as f:
    data = [line.strip() for line in f.readlines()]
def natocode(new_file):
    alphabets = []
    names = []
    nato_code = {}

    temporaly_save = []
    # ფაილი გადავიყვანეთ ლისტად
    for val in new_file:
        temporaly_save.append(val)
    sep = '|'
    # გადავანაწილეთ
    for value in temporaly_save[1:]:
        new_alphabet = value.split(sep, 1)[0]
        new_names = value.split(sep , 1)[1]
        alphabets.append(new_alphabet)
        names.append(new_names)

    for key in alphabets:
        for value in names:
            nato_code[key] = value
            names.remove(value)
            break

    return nato_code

phonetic_dict = natocode(data)


inputed_name = input("ONLY ENGLISH შეიყვანე სახელი: ").upper()

phonetic_name = []
for key, value in phonetic_dict.items():
    for i in inputed_name:
        if i == key:
            phonetic_name.append(value)

print(f"ბატონო ჯარისკაცო {inputed_name}, შენი ნატოს კოდური სახელია {phonetic_name}")
