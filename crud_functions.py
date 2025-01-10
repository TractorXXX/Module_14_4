import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Эта функция создаёт таблицу Products, если она ещё не создана

def initiate_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
)
''')

    connection.commit()

# Эта функция возвращает все записи из таблицы Products

def get_all_products():
    connection_1 = sqlite3.connect('database.db')
    cursor_1 = connection_1.cursor()
    cursor_1.execute('SELECT * FROM Products')
    products = cursor_1.fetchall()
    connection_1.close()
    return products

# Эта функция заполняет нашу базу данных продуктами. Используется один раз.

def add_products():
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
                       (f'Продукт{i}', f'Описание{i}', i * 100))

    connection.commit()

# Запускаем один раз при создании и заполнении базы данных Products
# initiate_db()
# add_products()

connection.commit()
connection.close()
