'''
Introduction
Rest Api
Implement a RESTful API for tracking IOUs.

Four roommates have a habit of borrowing money from each other frequently, and have trouble remembering who owes whom, and how much.

Your task is to implement a simple RESTful API that receives IOUs as POST requests, and can deliver specified summary information via GET requests.

API Specification
User object
{
  "name": "Adam",
  "owes": {
    "Bob": 12.0,
    "Chuck": 4.0,
    "Dan": 9.5
  },
  "owed_by": {
    "Bob": 6.5,
    "Dan": 2.75,
  },
  "balance": "<(total owed by other users) - (total owed to other users)>"
}
Methods
Description	HTTP Method	URL	Payload Format	Response w/o Payload	Response w/ Payload
List of user information	GET	/users	{"users":["Adam","Bob"]}	{"users":<List of all User objects>}	{"users":<List of User objects for <users> (sorted by name)}
Create user	POST	/add	{"user":<name of new user (unique)>}	N/A	<User object for new user>
Create IOU	POST	/iou	{"lender":<name of lender>,"borrower":<name of borrower>,"amount":5.25}	N/A	{"users":<updated User objects for <lender> and <borrower> (sorted by name)>}
Other Resources:
https://restfulapi.net/
Example RESTful APIs
GitHub https://developer.github.com/v3/
Reddit https://www.reddit.com/dev/api/
'''

import json
from collections import OrderedDict

class RestAPI:

    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users':
            if payload == None:
                return json.dumps(self.database)
            else:
                request = self.decode_payload(payload)
                userscopy = self.database.copy()
                for user in self.database['users']:
                    if user['name'] not in request['users']:
                        userscopy['users'].remove(user)
                        
                return json.dumps(userscopy)
            
        else:
            return error("Invalid URL in GET REQUEST")

    def post(self, url, payload=None):
        if url == '/add':
            if payload == None:
                return error("No user provided in /add POST REQUEST")
            else:
                request = self.decode_payload(payload)
                return json.dumps(self.add_user(request))

            return self.get('/users', payload)
        elif url == '/iou':
            if payload == None:
                return error("No changes provided in /iou POST REQUEST")
            else:
                request = self.decode_payload(payload)
                self.handle_balance_change(request)

            return self.get('/users')
        else:
            return error("Invalid method in POST REQUEST")
    
    def decode_payload(self, payload):
        # Error handling?
        request = json.loads(payload)
        return request

    def add_user(self, request):
        newuser = {"name": request['user'], "owes": {}, "owed_by": {}, "balance": 0.0}
        self.database['users'].append(newuser)
        return newuser

    def handle_balance_change(self, request):
        # user in users database
        # {"name": 'Adam', "owes": {}, "owed_by": {}, "balance": 0.0}
        # iou request
        # "lender": "Adam", "borrower": "Bob", "amount": 3.0
        
        lender = request['lender']
        borrower = request['borrower']
        amount = request['amount']
        for user in self.database['users']:
            if user['name'] in [borrower, lender]:
                # Case where A already owes B money: increment debt
                if lender in user['owes']:
                    user['owes'][lender] += amount
                elif borrower in user['owed_by']:
                    user['owed_by'][borrower] += amount
                elif lender in user['owed_by']:
                    # Case where B already owed A money: reduce debt (when amount is not more than already owed)
                    if user['owed_by'][lender] > amount:
                        user['owed_by'][lender] -= amount
                    elif user['owed_by'][lender] == amount:
                        user['owed_by'].pop(lender)
                    else:
                        # Case where B already owed A money, but not as much as A now owes B
                        newamount = amount - user['owed_by'][lender]
                        user['owes'][lender] = newamount
                        user['owes'] = OrderedDict(sorted(user['owes'].items())) 
                        user['owed_by'].pop(lender)
                elif borrower in user['owes']:
                    # Case where B already owed A money: reduce debt (when amount is not more than already owed)
                    if user['owes'][borrower] > amount:
                        user['owes'][borrower] -= amount
                    elif user['owes'][borrower] == amount:
                        user['owes'].pop(borrower)
                    else:
                        # Case where B already owed A money, but not as much as A now owes B
                        newamount = amount - user['owes'][borrower]
                        user['owed_by'][borrower] = newamount
                        user['owed_by'] = OrderedDict(sorted(user['owed_by'].items())) 
                        user['owes'].pop(borrower)
                else:
                    # new debt
                    if user['name'] == borrower:
                        user['owes'][lender] = amount
                        user['owes'] = OrderedDict(sorted(user['owes'].items())) 
                    elif user['name'] == lender:
                        user['owed_by'][borrower] = amount
                        user['owed_by'] = OrderedDict(sorted(user['owed_by'].items()))

                # balance
                if user['name'] == lender:
                    user['balance'] += amount
                elif user['name'] == borrower:
                    user['balance'] -= amount

        payload = json.dumps({"users": [lender, borrower]})
        return self.get('/users', payload)
            
    def error(self, message):
        return json.dumps({ "error": message })
