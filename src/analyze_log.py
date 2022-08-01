import csv


def get_csv(path):
    file = open(path, 'r')
    reader = csv.reader(file)
    orders = []
    for row in reader:
        orders.append({
            "name": row[0],
            "food": row[1],
            "day": row[2],
        })
    return orders
        
def most_requested_food_by_maria(orders):
    count = {}
    most_frequent = orders[0]
    for order in orders:
        if order["food"] in count:
            count[order["food"]] += 1
        else:
            count[order["food"]] = 1
        if count[order["food"]] > count[most_frequent["food"]]:
            most_frequent = order
    return most_frequent["food"]

def quantity_arnaldo_ordered_hamburgers(orders):
    count = 0
    for order in orders:
        if order["food"] == "hamburguer" and order["name"] == "arnaldo":
            count += 1
    return count

def list_foods(orders):
    foods = []
    for order in orders:
        if order["food"] not in foods:
            foods.append(order["food"])
    return foods

def orders_joao_never_ordered(orders):
    foods = list_foods(orders)
    foods_never_ordered = set()
    for food in foods:
        count = 0
        for order in orders:
            if order["food"] == food and order["name"] == "joao":
                count += 1
        if count == 0:
            foods_never_ordered.add(food)
    return foods_never_ordered

def list_days(orders):
    days = []
    for order in orders:
        if order["day"] not in days:
            days.append(order["day"])
    return days


def day_joao_never_go_to_restaurant(orders):
    days = list_days(orders)
    days_never_go_to_restaurant = set()
    for day in days:
        count = 0
        for order in orders:
            if order["day"] == day and order["name"] == "joao":
                count += 1
        if count == 0:
            days_never_go_to_restaurant.add(day)
    return days_never_go_to_restaurant

def write_file(path_to_file):
    orders = get_csv(path_to_file)
    file = open("data/mkt_campaign.txt", "w")
    file.write(most_requested_food_by_maria(orders) + "\n")
    file.write(str(quantity_arnaldo_ordered_hamburgers(orders)) + "\n")
    file.write(str(orders_joao_never_ordered(orders)) + "\n")
    file.write(str(day_joao_never_go_to_restaurant(orders)) + "\n")
    file.close()

def analyze_log(path_to_file):
    file_extension = path_to_file.split(".")[1]
    if file_extension != 'csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        write_file(path_to_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
