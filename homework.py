import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.count_today = 0
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        for summ in self.records:
            if summ.date == dt.date.today():
                self.count_today += summ.amount
        return self.count_today


    def get_week_stats(self):
        for summ in self.records:
            if summ.date >= dt.date.today() - dt.timedelta(days=7):
                self.count_today += summ.amount
        return self.count_today


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_cal = self.get_today_stats()
        if today_cal < self.limit:
            count_cal = self.limit - today_cal
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {count_cal} кКал'
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 62.10
    EURO_RATE = 69.31

    def get_today_cash_remained(self, currency):
        today_cash = self.get_today_stats()
        limit = self.limit
        """Добавляю val к text"""
        if currency == 'usd':
            val = 'USD'
        elif currency == 'eur':
            val = 'Euro'
        else:
            val = 'руб'
        """Проверка на лимит"""
        if today_cash < limit:
            balance = limit - today_cash
            if currency == 'usd':
                balance /= self.USD_RATE
            elif currency == 'eur':
                balance /= self.EURO_RATE
            text = f'На сегодня осталось {round(balance, 2)} {val}'

        elif today_cash == limit:
            text = 'Денег нет, держись'

        elif today_cash > limit:
            balance = today_cash - limit
            if currency == 'usd':
                balance /= self.USD_RATE
            elif currency == 'eur':
                balance /= self.EURO_RATE
            text = f'Денег нет, держись: твой долг - {round(balance, 2)} {val}'
        return text








class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()



