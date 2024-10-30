
import time


def find_coins_greedy(change):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = change // coin
        if count > 0:  # Додаємо тільки номінали, які потрібні
            result[coin] = count
        change %= coin
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]

    # Ініціалізація таблиці для зберігання мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Нуль монет для суми 0
    # Ініціалізація допоміжної таблиці для збереження останньої монети, доданої для досягнення певної суми
    last_coin = [-1] * (amount + 1)
    
    # Заповнення таблиці мінімальних кількостей монет
    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                last_coin[x] = coin

    # Якщо сума недосяжна, повернемо порожній словник
    if min_coins[amount] == float('inf'):
        return {}

    # Відновлення кількості кожної монети для досягнення суми
    coins_count = {coin: 0 for coin in coins}
    while amount > 0:
        coin = last_coin[amount]
        coins_count[coin] += 1
        amount -= coin

    return {k: v for k, v in coins_count.items() if v > 0}

# Тестування функцій
amount = 1234567

# Жадібний алгоритм
start_time = time.time()
greedy_change = find_coins_greedy(amount)
greedy_time = time.time() - start_time

# Динамічне програмування
start_time = time.time()
min_coins_change = find_min_coins(amount)
dp_time = time.time() - start_time

print("Жадібний алгоритм:", greedy_change)
print("Час виконання (жадібний алгоритм):", greedy_time)

print("Динамічне програмування:", min_coins_change)
print("Час виконання (Динамічне програмування):", dp_time)