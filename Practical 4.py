from abc import ABC, abstractmethod
import sqlite3
import os
import time



class Authentication(ABC):
    @abstractmethod
    def register(self, name, email, password, role):
        pass

    @abstractmethod
    def login(self, email, password, role):
        pass





class Product:
    def __init__(self, name, description, Price, Translator, id):
        self.name = name
        self.description = description
        self.Price = Price
        self.Translator = Translator
        self.id = id

    def save_to_database(self):
        database = Database("products.database")
        query = 'CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, name TEXT, description TEXT, Price REAL, Translator INT)'
        database.execute_query(query)
        query = 'INSERT INTO Products (name, description, Price, Translator) VALUES (?, ?, ?, ?)'
        values = (self.name, self.description, self.Price, self.Translator)
        database.execute_query(query, values)
        database.close()
        
    def update_database(self):
        database = Database("products.database")
        query = 'UPDATE Products SET name = ?, description = ?, Price = ?, Translator = ? WHERE id = ?'
        values = (self.name, self.description, self.Price, self.Translator, self.id)
        database.execute_query(query, values)
        database.close()
        
    def display_product(self):
        database = Database("products.database")
        query = 'SELECT * FROM Products ORDER BY name'
        products = database.execute_query(query)
        for product in products:
            print(product)
        database.close()
        


class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def save_to_database(self):
        database = Database('users.db')
        query = 'CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, role VARCHAR(20))'
        database.execute_query(query)
        query = 'INSERT INTO Users (name, email, password, role) VALUES (?, ?, ?, ?)'
        values = (self.name, self.email, self.password, self.role)
        database.execute_query(query, values)
        database.close()


def close(self):
        self.conn.close()

class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()





class UserAuthentication:
    

    def register(self, name, email, password, role):
        user = User(name, email, password, role)
        user.save_to_database()
        print('Вы успешно зарегистрированы!')
        Main.login(self, role)

    def login(self, email, password, role):
        database = Database('users.database')
        query = 'SELECT * FROM Users WHERE email=? AND password=? AND role=?'
        values = (email, password, role)
        result = database.fetch_data(query, values)
        database.close()
        if result:
            print('Вход выполнен успешно!')
            Main.login(self, role)
        else:
            print('Неверный email, пароль или роль \n Система заблокирована, перезапустите')
       
class Basket:
    def __init__(self, Full_name, ID_PRODUCT, Taste, status, id):
        self.Full_name = Full_name
        self.ID_PRODUCT = ID_PRODUCT
        self.Taste = Taste
        self.status = status
        self.id = id
        
    def save_to_database(self):
        database = Database("order.db")
        query = 'CREATE TABLE IF NOT EXISTS Order (id INTEGER PRIMARY KEY, Full_name TEXT, ID_PRODUCT TEXT, Taste TEXT, status TEXT)'
        database.execute_query(query)
        query = 'INSERT INTO Order (Full_name, ID_PRODUCT, Taste, status) VALUES (?, ?, ?,?)'
        values = (self.Full_name, self.ID_PRODUCT, self.Taste, self.status)
        database.execute_query(query, values)
        database.close()
        
    def update(self):
        database = Database("order.database")
        query = 'UPDATE Order SET status = ? WHERE id = ?'
        values = (self.status, self.id)
        database.execute_query(query, values)
        database.close()
         
class Main:
    def __init__(self):
        self.authentication = UserAuthentication()
      
        
        

    def display_menu(self):
        print("Добро пожаловать в вейпшоп 'Ашкуди228'!")
        print("Войдите или зарегистрируйтесь ")
        print(" ")
        print("1. Зайти в уже созданный аккаунт и курить ашкуди")
        print(" ")
        print("2. Зарегистрировать новый аккаунт и потом курить ашкуди")
        print(" ")

    def menu_selection(self, choice ):
        if choice == "1":
            clear()
            print("Для входа введите свой пароль:)")
            print(" ")
            email = input("Введите email: ")
            password = input("Введите пароль: ")
            role = input("Введите вашу роль admin/client: ")
            self.authentication.login(email, password, role)
            
        elif choice == "2":
            clear()
            print("Добро пожалаловать в вейпшоп\n Чтобы купить свою ашкудишку - зарегистрируйтесь  ")
            print(" ")
            name = input("Введите имя: ")
            email = input("Введите email: ")
            password = input("Введите пароль: ")
            role = input("Введите свою роль admin/client: ")
            self.authentication.register(name, email, password, role)

    def login(self, role):
       
        if role == "admin":
            clear()
            print("Вы вошли в меню администратора!!!")
            print("=================================")
            print("Выберите нужный пункт: ")
            print("1. Добавление нового товара")
            print("2. Обновление товара")
            print("3. Вывести все товары магазина")
            print("4. Вывести все заказы")
            print("5. Изменить статус заказа")
            print("6. Выйти")
            vib = input("Ваш выбор: ")
            if vib == "1":
                clear()
                name = input("Введите название товара: ")
                description = input("Введите описание товара: ")
                Price = input("Введите цену товара: ")
                Translator = input("Введите количество: ")
                product = Product(name, description,  Price, Translator, 0)
                product.save_to_database()
                print("Товар сохранён!!!")
                time.sleep(2)
                Main.login(self, role)
            if vib == "2":
                clear()
                name = input("Измените имя товара: ")
                description = input("Измените описание товара: ")
                Price = input("Измените цену товара: ")
                Translator = input("Измените количество: ")
                id = input("Введите id товара: ")
                update = Product(name, description,  Price, Translator, id)
                update.update_database()
                print("Товар сохранён!!!")
                time.sleep(2)
                Main.login(self, role)
            if vib == "3":
                clear()
                connection = sqlite3.connect('products.db')
                cursor = connection.cursor()
                products = cursor.execute("SELECT * FROM products").fetchall()
                spisok = list()
                print("id | name | description | Price | Translator")
                for i in range(4):
                    for j in range(5):
                        spisok.append(products[i][j])
                    print(*spisok)
                    spisok = list()
                connection.close()
                time.sleep(2)
                Main.login(self, role)
            if vib == "4":
                clear()
                connection = sqlite3.connect('order.database')
                cursor = connection.cursor()
                products = cursor.execute("SELECT * FROM order").fetchall()
                print("ID заказа, ФИО клиента, ID товара, Адрес доставки, Cтатус Доставки")
                for product in products:
                    print(*product)  
                    
                connection.close()
                time.sleep(10)
                Main.login(self, role)
                
            if vib == "5":
                clear()
                id = input("Введите id заказа: ")
                status = input("Введите новый статус заказа: ")
                update1 = Basket(None, None, None, status, id)
                update1.update()
                print("Статус сохранен!!!")
                time.sleep(2)
                Main.login(self, role)
                
            if vib == "6":
                clear()
                print("До свидания! Перезапустите программу:)")
                
                
        elif role == "admin" :
            clear()
            print("Вы вошли в меню клиента!!!")
            print("=================================")
            print("Выберите нужный пункт: ")
            print("1. Ассортимент товаров и выбор")
            print("2. Данные о заказах")
            print("3. Выйти")

            vib = input("Ваш выбор: ")

            if vib == "1":
                clear()
                print("Вот наш ассортимент: ")
                print("ID товара, Наименование, Описание, Цена, Количество")
                connection = sqlite3.connect('products.database')
                cursor = connection.cursor()
                products = cursor.execute("SELECT * FROM products").fetchall()
                spisok = list()
                for i in range(1):
                    for j in range(5):
                        spisok.append(products[i][j])
                    print(*spisok)
                    spisok = list()
                connection.close()
                print("=========================================================")
                Full_name = input("Введите своё ФИО: ")    
                ID_PRODUCT = input("Введите ID товара, который  хотите заказать: ")
                Taste = input("Введити адрес доставки: ")
                status = input("Статус заказ (если вы клиент напишите '-'): ")
               
                order = Basket(Full_name, ID_PRODUCT, Taste, status, 0)
                order.save_to_database()
                print("Ваш заказ успешно сохранён!")
                time.sleep(2)
                Main.login(self, role)
                
            if vib == "2":
                clear()
                connection = sqlite3.connect('order.database')
                cursor = connection.cursor()
                products = cursor.execute("SELECT * FROM order").fetchall()
                print("ID заказа, ФИО клиента, ID товара, Адрес доставки, Cтатус Доставки")
                for product in products:
                    print(*product)  
        
                connection.close()
                time.sleep(2)
                Main.login(self, role)
                
            if vib == "3":
                clear()
                print("До свидания! Перезапустите программу:)")
                
                
def clear():
      os.system('cls')

if __name__ == "__main__":
    main = Main()
    main.display_menu()
    choice = input("Ваш выбор: ")
    main.menu_selection(choice)
   
    
   
    
    
