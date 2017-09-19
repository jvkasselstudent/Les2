def get_ticker_data(filename):
    symbols = {}
    file = open(filename, 'r')
    file_lines = file.readlines()
    for line in file_lines:
        line_values = line.strip().split(":")
        key = line_values[0].lower()
        value = line_values[1]
        symbols[key] = value
    file.close()
    return symbols


def get_company_by_ticker(ticker_dictionary, ticker_value):
    for key in ticker_dictionary:
        if ticker_dictionary[key].lower() == ticker_value.lower():
            return ticker_dictionary[key]
    return None


def get_ticker_by_company(ticker_dictionary, company_value):
    if company_value.lower() in ticker_dictionary:
        return ticker_dictionary[company_value.lower()]
    else:
        return None


ticker_symbols = get_ticker_data("tickers.txt")

company = input("Enter Company name: ")
print("Ticker symbol: {0}".format(get_ticker_by_company(ticker_symbols, company)))

ticker = input("Enter Ticker symbol: ")
print("Company name: {0}".format(get_company_by_ticker(ticker_symbols, ticker)))
