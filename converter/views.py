from django.shortcuts import render, redirect

from .forms import UserInputForm

import requests

def index(request):
  return render(request, "index.html")

def input(request):
    form = UserInputForm()
    context = {'form': form}
    return render(request, 'input.html', context)


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
        if from_currency != 'EUR' : 
            amount = amount / self.rates[from_currency] 
  
        # limiting the precision to 2 decimal places 
        amount = round(amount * self.rates[to_currency], 2) 
        result = ('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        return result

def result(request):
  
  if request.method == 'POST': 
    form = UserInputForm(request.POST)
    
    if form.is_valid():
        currency1 = form.cleaned_data.get("currency1")
        currency2 = form.cleaned_data.get("currency2")
        value = form.cleaned_data.get("value")
        url = str.__add__('http://data.fixer.io/api/latest?access_key=', '5e6a6c2576bc2070e83a6426e6d812e4')    
        c = Currency_convertor(url)
        output = c.convert(currency1.upper(), currency2.upper(), value)
        context = {'output': output} 
        return render(request, 'result.html', context)