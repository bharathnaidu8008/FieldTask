Install python
Install flask <pip install flask>
Clone this project and open cmd in project location
run <python Application.py>
It will start the application
  
---json format---
{'credit_card_number': <string>, 'card_holder': <string>, 'expiration_date': <string: format(mm/year ex: 05/2025> , 'security_code': <string>, 'amount': <decimal> }

---response--
{"Message":"OK","Status":200}
{"Message":"bad request","Status":400

---testcases---
Already few testcases are available in Test.py file
To test any new case scenario add your values to p.PayMoney method as follows in Test.py file existig scenarios
