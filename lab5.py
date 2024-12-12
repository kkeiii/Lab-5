import re
import csv


#task_1
with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text = file.read()

numbers = re.findall(r'\b\d+(?:[.,]\d+)?\b', text)
six_letter_words = re.findall(r'\b\w{6}\b', text)
eight_letter_words = re.findall(r'\b\w{8}\b', text)


#task2
with open('task2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

content_values = re.findall(r'\bcontent=["\'](.*?)["\']', html_content)


#task3
output_file = 'new_data.csv'

with open('task3.txt', 'r') as file:
    data = file.read()

ids = re.findall(r'\b\d{1,3}\b', data)
names = re.findall(r'\b[A-Z][a-z]+\b', data)
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', data)
urls = re.findall(r'(https?://\S+)', data)

rows = zip(ids, names, emails, dates, urls)

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ID", "Name", "Email", "Date", "URL"])
    csvwriter.writerows(rows)


#add_task
with open('task_add.txt', 'r') as file:
    data = file.read()


dates = re.findall(r'\b(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})', data)
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', data)
urls = re.findall(r'\s(https?://[a-zA-Z0-9.-]+)', data)


if __name__ == "__main__":

    print(f'Задание 1')
    print(f"Числа (целые и дробные):\n{numbers}")
    print(f"\nСлова из 6 букв:\n{six_letter_words}")
    print(f"\nСлова из 8 букв:\n{eight_letter_words}") 

    print(f'\nЗадание 2')
    print(f'Найденные значения атрибута content:\n{content_values}')

    print(f'\nЗадание 3')
    print(f"Данные сохранены в файл {output_file}.")

    print(f'\nДоп задание')
    print(f"Dates:")
    for date in dates:
        print(f"{date}")

    print(f"\nEmails:")
    for email in emails:
        print(f"{email}")

    print(f"\nURLs:")
    for url in urls:
        print(f"{url}")




