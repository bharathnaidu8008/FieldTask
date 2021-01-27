# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import datetime
app = Flask(__name__)


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

# Credit card check Luhn algorithm
def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer list
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0


def CheapPaymentGateWay(amount):
    """
    Parameters
    ----------
    amount : decimal
        It will call when amount less than 20

    Returns
    -------
    None.
    
    """
    print("Payment done using cheapPayment Gateway")

def ExpensivePaymentGateway(amount):
    """
    Parameters
    ----------
    amount : decimal
        It will call when amount more than 21 and less than 500

    Returns
    -------
    None.
    
    """
    print("Payment done using Expensive Payment Gateway")

def PremiumPaymentGateway(amount, maxretries=3):
    """
    Parameters
    ----------
    amount : decimal
        It will call when amount more than 500

    Returns
    -------
    None.
    
    """
    try:
        print("Payment done using Premium Payment Gateway")
    except Exception as e:
        if maxretries >= 0:
            PremiumPaymentGateway(amount, maxretries-1)
    

@app.route("/processpayment", methods = ["Post"])
def ProcessPayment():
    """
    Parameters
    ----------
    CreditCardNumber, CardHolder, SecurityCode, ExpireDateOnCard, Amount
    Take this parameter as input and execute the functionality as assignment info

    Raises
    ------
    Exception
        If any mandatory param is missing in params

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    params = request.get_json()
    credit_card_number = params.get("credit_card_number", None)
    card_holder = params.get("card_holder", None)
    expiration__date = params.get("expiration_date", None)
    security_code = params.get("security_code", None)
    amount = params.get("amount", None)
    try:
        month, year = expiration__date.split("/")
        if credit_card_number == None or card_holder == None or expiration__date == None or amount == None:
            raise Exception("Oops! Missing mandatory filed values'")
        if not validate(credit_card_number):
            raise Exception("Oops! Not a valid credit card number")
        if (int(month) < 1 and int(month) > 12) and int(year) < datetime.datetime.now().year:
            raise Exception("Oops! Not a valid expiration")
        if (amount<0):
            raise Exception("Oops! Amount should not be negative")
        if security_code != None and len(security_code) != 3:
            raise Exception("Oops! Invalid security code")
        
        # Payment Method
        if amount < 20:
            CheapPaymentGateWay(amount)
        elif amount >= 21 and amount <= 500:
            ExpensivePaymentGateway(amount)
        elif amount > 500:
            PremiumPaymentGateway(amount)
        return jsonify({"Message" : "OK", "Status" : 200})
    except:
        return jsonify({"Message" : "bad request", "Status" : 400})


if __name__ == '__main__':
   app.run()