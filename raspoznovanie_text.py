import easyocr

def text_recognition(file_path):
    reader = easyocr.Reader(['ru'])# список языков для распознания
    result= reader.readtext(file_path)# путь расположения

    return result

def main():
    file_path = input('Введите название картинки с расширением: ')#картирнка хранится где сам проект
    print(text_recognition(file_path=file_path))

if __name__ =='__main__':
    main()
