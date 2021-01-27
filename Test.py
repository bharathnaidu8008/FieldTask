# -*- coding: utf-8 -*-
import requests


class PaymentProcess:
    __url = 'http://127.0.0.1:5000/processpayment'
    __params = {'credit_card_number': None, 'card_holder': None, 'expiration_date': None, 'security_code': None, 'amount': None }
    
    def PayMoney(self, cardnumber, cardholder, expirationdate, securitycode, amount):
        self.__params["credit_card_number"] = cardnumber
        self.__params["card_holder"] = cardholder
        self.__params["expiration_date"] = expirationdate
        self.__params["security_code"] = securitycode
        self.__params["amount"] = amount
        x = requests.post(self.__url, json = self.__params)
        print(x.text)

# Testcases
p = PaymentProcess()
# Given correct details
p.PayMoney("5412753456789010", "ravi", "03/2025", "123", 20)  # {"Message":"OK","Status":200}
# Given creditcard number as wrong
p.PayMoney("45145700aa367707", "bharath", "03/2025", "123", 20)  # {"Message":"bad request","Status":400}
# Given security code as none
p.PayMoney("5412753456789010", "rajesh", "03/2025", None, 20)  # {"Message":"OK","Status":200}
# Given security code more than three digits
p.PayMoney("5412753456789010", "sai", "03/2025", "1233", 20)  # {"Message":"bad request","Status":400}
# Given security code more than three digits
p.PayMoney("5412753456789010", "king", "03/2025", "1233", 20)  # {"Message":"bad request","Status":400}
# Given amonut more than 500
p.PayMoney("5412753456789010", "sai", "03/2025", "123", 500.78)  # {"Message":"OK","Status":200}
# Given amonut more than 20
p.PayMoney("5412753456789010", "queen", "03/2025", "123", 228) #{"Message":"OK","Status":200}
# Given amonut negative -1
p.PayMoney("5412753456789010", "kishore", "03/2025", "123", -1) # {"Message":"bad request","Status":400}
