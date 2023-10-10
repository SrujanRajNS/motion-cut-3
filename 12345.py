from forex_python.converter import CurrencyRates

c = CurrencyRates()

def convert_currency():
    try:
        
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the source currency code (e.g., USD): ").upper()
        to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

        
        exchange_rate = c.get_rate(from_currency, to_currency)


        converted_amount = amount * exchange_rate


        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Currency Conversion Tool")
    while True:
        convert_currency()
        another_conversion = input("Do you want to convert another currency? (yes/no): ").lower()
        if another_conversion != "yes":
            break

