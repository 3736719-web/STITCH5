import datetime


# Функция для расчёта скидки
def apply_discount(price, discount_percent):
    discount_amount = price * discount_percent / 100
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    if final_price < 0:
        final_price = 0
    return final_pric

    return final_price

# Функция для проверки возраста
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

    print("Проверка завершена")


# Список товаров с разными данными
products = [
    {"name": "Apple", "price": 100, "stock": 10},
    {"name": "Banana", "price": "50", "stock": 5},
    {"name": "Cherry", "price": 75, "stock": -3},
    {"name": "Date", "price": None, "stock": 2},
    {"name": "Elderberry", "stock": 4},
    {"name": "Fig", "price": 80, "count": 6},
    {"name": "Banana", "price": "50", "stock": 5},      # цена строкой
    {"name": "Cherry", "price": 75, "stock": -3},       # отрицательный остаток
    {"name": "Date", "price": None, "stock": 2},        # цена отсутствует
    {"name": "Elderberry", "stock": 4},                 # нет цены
    {"name": "Fig", "price": 80, "count": 6},           # ключ count вместо stock
]


# Переменная для общей суммы
total_sum = 0


# Цикл по товарам с обработкой ошибок
for product in products:

    price = product["price"]
    stock = product["stock"]


    price_float = float(price)


    discounted_price = apply_discount(price_float, "10")


    cost = discounted_price * stock


    total_sum += cost


    print(f"Товар: {product['name']}, Цена: {price}, Остаток: {stock}")


def calculate_tax(amount, rate):
    tax = amount * rate / 100
    return tax


tax_amount = calculate_tax(total_sum, tax_rate)


print("Итоговая сумма: " + total_sum)


age_check = is_adult("25")


unused_variable = "Это значение нигде не применяется"


print("Финальная сумма:", total_sum + tax_amount)


print(products[10]["name"])
    try:
        # Попытка получить цену и остаток с проверкой на наличие ключа
        price = product.get("price")
        if price is None:
            print(f"Товар {product['name']}: отсутствует цена, пропуск")
            continue

        stock = product.get("stock")
        if stock is None:
            print(f"Товар {product['name']}: отсутствует остаток, пропуск")
            continue

        # Преобразование цены в число
        price_float = float(price)

        # Применение скидки
        discounted_price = apply_discount(price_float, 10)

        # Расчёт стоимости партии
        cost = discounted_price * stock

        # Добавление стоимости к общей сумме
        total_sum += cost

        # Вывод информации о товаре
        print(f"Товар: {product['name']}, Цена: {price_float}, Остаток: {stock}")
    except ValueError:
        print(f"Ошибка: Некорректная цена для товара {product['name']}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Вычисление налога (предполагаем, что tax_rate определена ранее)
tax_rate = 10  # примерная ставка налога
tax_amount = calculate_tax(total_sum, tax_rate)

# Вывод итоговой суммы
print(f"Итоговая сумма: {total_sum}")
print(f"Финальная сумма с налогом: {total_sum + tax_amount}")

# Проверка возраста (логическая ошибка в вызове исправлена)
age_check = is_adult(25)  # передана корректная числовая величина
print(f"Проверка возраста: {age_check}")
