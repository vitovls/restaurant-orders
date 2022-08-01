class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})

    def get_days(self):
        days = []
        for order in self.orders:
            days.append(order["day"])

    def get_foods(self):
        foods = []
        for order in self.orders:
            if order["order"] not in foods:
                foods.append(order["order"])

    def get_most_ordered_dish_per_customer(self, customer):
        count = {}
        most_frequent = self.orders[0]
        for order in self.orders:
            if order["customer"] == customer:
                if order["order"] in count:
                    count[order["order"]] += 1
                else:
                    count[order["order"]] = 1
                if count[order["order"]] > count[most_frequent["order"]]:
                    most_frequent = order
        return most_frequent["order"]

    def get_never_ordered_per_customer(self, customer):
        foods = self.get_foods()
        foods_never_ordered = set()
        for food in foods:
            count = 0
            for order in self.orders:
                if order["order"] == food and order["customer"] == customer:
                    count += 1
            if count == 0:
                foods_never_ordered.add(food)
        return foods_never_ordered

    def get_days_never_visited_per_customer(self, customer):
        days = self.get_days()
        days_never_go_to_restaurant = set()
        for day in days:
            count = 0
            for order in self.orders:
                if order["day"] == day and order["customer"] == customer:
                    count += 1
            if count == 0:
                days_never_go_to_restaurant.add(day)
        return days_never_go_to_restaurant

    def get_busiest_day(self):
        days = self.get_days()
        days_busy = set()
        for day in days:
            count = 0
            for order in self.orders:
                if order["day"] == day:
                    count += 1
            if count > len(days_busy):
                days_busy = day
        return days_busy

    def get_least_busy_day(self):
        days = self.get_days()
        days_busy = days[0]
        for day in days:
            count = 0
            for order in self.orders:
                if order["day"] == day:
                    count += 1
            if count < len(days_busy):
                days_busy = day
        return days_busy
