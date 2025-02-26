class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        base_amount = amount / self.exchange_rates[from_currency]
        return base_amount * self.exchange_rates[to_currency]


class CurrencyConverterApp:
    def __init__(self):
        self.exchange_rates = {
            'USD': 1.0,       # Base currency
            'EUR': 0.85,
            'JPY': 139.9,
            'GBP': 0.75,
            'CAD': 1.36,
            'INR': 83.9,
            'HKD': 7.79,
            'RUB': 105.3,
            'MYR': 4.3015,
            'SGD': 1.2949

        }
        self.converter = CurrencyConverter(self.exchange_rates)

    def display_currencies(self):
        print("Available currencies:")
        for currency in self.exchange_rates.keys():
            print(f"- {currency}")

    def get_user_input(self):
        self.display_currencies()
        from_currency = input("Enter the currency you want to convert from: ").upper()
        to_currency = input("Enter the currency you want to convert to: ").upper()
        amount = float(input(f"Enter the amount in {from_currency}: "))
        return from_currency, to_currency, amount

    def perform_conversion(self):
        from_currency, to_currency, amount = self.get_user_input()
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates:
            converted_amount = self.converter.convert(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print("Invalid currency code. Please try again.")

    def run(self):
        while True:
            self.perform_conversion()
            cont = input("Do you want to perform another conversion? (yes/no): ").lower()
            if cont != 'yes':
                print("Thank you for using Currency Converter!")
                break


# Running the application
if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.run()