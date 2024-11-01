print ('lesson6')

class Ticket:
    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

    def __str__(self):
        return f"Квиток на фільм '{self.movie_title}', місце {self.seat_number}, ціна: {self.price} грн."

class StandardTicket(Ticket):
    def __init__(self, movie_title, seat_number, price, discount=0):
        super().__init__(movie_title, seat_number, price)
        self.discount = discount

    def __str__(self):
        return f"Стандартний квиток. {super().__str__()}" + \
               f" Знижка: {self.discount}%" if self.discount else ""

class VIPticket(Ticket):
    def __init__(self, movie_title, seat_number, price, lounge_access=True, complimentary_drinks=2):
        super().__init__(movie_title, seat_number, price)
        self.lounge_access = lounge_access
        self.complimentary_drinks = complimentary_drinks

    def __str__(self):
        return f"VIP-квиток. {super().__str__()}" + \
               f" Доступ до VIP-зони: {self.lounge_access}. Безкоштовні напої: {self.complimentary_drinks}"

class InvalidSeatNumberError(Exception):
    pass

class Cinema:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        if 1 <= ticket.seat_number <= 100:
            self.tickets.append(ticket)
        else:
            raise InvalidSeatNumberError("Некоректний номер місця")

    def display_all_tickets(self):
        for ticket in self.tickets:
            print(ticket)

cinema = Cinema()

standard_ticket = StandardTicket("Аватар 2", 25, 150, 10)
vip_ticket = VIPticket("Барбі", 5, 200)

try:
    cinema.add_ticket(standard_ticket)
    cinema.add_ticket(vip_ticket)
    cinema.add_ticket(Ticket("Оппенгеймер", 120, 180))  # Викличе виняток
except InvalidSeatNumberError as e:
    print(e)

cinema.display_all_tickets()