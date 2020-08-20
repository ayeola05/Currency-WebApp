from django.shortcuts import render, redirect

from .forms import UserInputForm

import requests

# "requests " is the library you need in order to communicate with an API
import requests

def index(request):
  return render(request, "index.html")


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

        # function to do a simple cross multiplication between

    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

            # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        result = ('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        return result

    # Driver code


'''if __name__ == "__main__":
    try:
        # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
        url = str.__add__('http://data.fixer.io/api/latest?access_key=', '5e6a6c2576bc2070e83a6426e6d812e4')
        c = Currency_convertor(url)

        from_country = input("From Currency: ")
        to_country = input("To Currency: ")
        amount = int(input("Amount: "))
        c.convert(from_country.upper(), to_country.upper(), amount)
    except KeyError:
        print("\nInvalid Input")'''


def convert_currency(request):
    form = UserInputForm(request.POST or None)
    if form.is_valid():
        currency1 = form.cleaned_data.get("currency1")
        currency2 = form.cleaned_data.get("currency2")
        value = form.cleaned_data.get("value")
        try:
            # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
            url = str.__add__('http://data.fixer.io/api/latest?access_key=', '5e6a6c2576bc2070e83a6426e6d812e4')
            c = Currency_convertor(url)

            from_country = currency1
            to_country = currency2
            amount = value
            result = c.convert(from_country.upper(), to_country.upper(), amount)
            context = {'result': result,
                       'error': 'wrong details provided',
                       }
            return redirect('/result', context)
        except KeyError:
            context = {'form': form}
            return render(request, 'input.html', context)
    else:
        context = {'form': form}
        return render(request, 'input.html', context)

def get_result(request):
    return render(request, 'result.html', {})