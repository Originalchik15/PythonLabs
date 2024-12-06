'''Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
Ввод данных из файла с контролем правильности ввода. 
Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами. Для GUI и визуализации использовать библиотеку tkinter.
Объекты – договоры на трудоустройство
Функции: сегментация полного списка договоров по компаниям, обратившимся за специалистами
визуализация предыдущей функции в форме круговой диаграммы
сегментация полного списка договоров по профессиям
визуализация предыдущей функции в форме круговой диаграммы
'''
import tkinter as tk
from tkinter import messagebox
import csv
from collections import Counter
import matplotlib.pyplot as plt

class EmploymentContract:
    def __init__(self, company, profession, salary):
        self.company = company
        self.profession = profession
        self.salary = salary

class ContractManager:
    def __init__(self):
        self.contracts = []

    def load_contracts(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 3:
                        print(f"Ошибка: Неверный формат строки: {row}. Ожидалось 3 поля.")
                        continue 
                    company, profession, salary = row
                    if not company or not profession or not salary:
                        print(f"Ошибка: Пустое значение в строке: {row}.")
                        continue
                    try:
                        salary = float(salary)
                    except ValueError:
                        print(f"Ошибка: Зарплата не является числом в строке: {row}.")
                        continue
                    if salary < 0:
                        print(f"Ошибка: Отрицательная зарплата в строке: {row}.")
                        continue

                    self.contracts.append(EmploymentContract(company, profession, salary))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    def segment_by_company(self):
        company_salary = Counter()
        for contract in self.contracts:
            company_salary[contract.company] += contract.salary
        return company_salary
    def segment_by_profession(self):
        profession_salary = Counter()
        for contract in self.contracts:
            profession_salary[contract.profession] += contract.salary
        return profession_salary
    def visualize_data(self, data):
        labels = data.keys()
        sizes = data.values()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление договорами")
        self.manager = ContractManager()
        self.load_button = tk.Button(root, text="Загрузить контракты", command=self.load_contracts)
        self.load_button.pack()
        self.segment_company_button = tk.Button(root, text="Сегментация по компаниям", command=self.segment_by_company)
        self.segment_company_button.pack()
        self.segment_profession_button = tk.Button(root, text="Сегментация по профессиям", command=self.segment_by_profession)
        self.segment_profession_button.pack()

    def load_contracts(self):
        self.manager.load_contracts('Lab-8/input.csv')
    def segment_by_company(self):
        data = self.manager.segment_by_company()
        self.manager.visualize_data(data)
    def segment_by_profession(self):
        data = self.manager.segment_by_profession()
        self.manager.visualize_data(data)

root = tk.Tk()
root.geometry("500x350+400+200")
app = App(root)
root.mainloop()