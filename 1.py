import datetime


def apply_discount(price, discount_percent):
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    if final_price < 0:
        final_price = 0
    return final_pric


def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

    print("Проверка завершена")


products = [
    {"name": "Apple", "price": 100, "stock": 10},
    {"name": "Banana", "price": "50", "stock": 5},
    {"name": "Cherry", "price": 75, "stock": -3},
    {"name": "Date", "price": None, "stock": 2},
    {"name": "Elderberry", "stock": 4},
    {"name": "Fig", "price": 80, "count": 6},
]


total_sum = 0


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
