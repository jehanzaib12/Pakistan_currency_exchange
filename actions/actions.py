import json
from datetime import datetime, timedelta

import requests
import os
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from itertools import islice
import re
from rasa_sdk.events import ReminderScheduled, ReminderCancelled, FollowupAction


class Action_irrelevant_response(Action):

    def name(self):
        return 'action_irrelevant_response'

    def run(self, dispatcher, tracker, domain):

        try:
            #id = tracker.sender_id
            id = 2769228663176300
            print("getting id")
            id = int(id)
            print(type(id))
            userid = requests.get(
                "https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token=EAAK0HoR2qbwBAI7MadZAejB9aru082t8Oiy8NdLuxLE7lSBHVmYGXbOvQxhMrq4jzYUA7z3JzAIt2G5yZAvnvCsmT9hOlVe2HIM90KQ1hwzy23EbIbOBxGxi1yoHrkqpjtNpQ7tYKBBRT41ZBgAt6VhxYcemAYgZAktXDOpELwZDZD".format(
                    id)).json()
            print(userid)
            print("getting userid")
            fn = ""
            for key, value in userid.items():
                fn = value
                print(fn)
                break
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")

            res1 = {
                "text": "Welcome to Pakistan Currency Assistant {}. Get started by clicking the button given below\n For Customer Support, you can join this link to talk to our Customer Representative\n m.me/arsalan.virgo".format(
                    fn),

                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Rates of Currency",
                        "payload": "Rates of Currency"
                    },
                    {
                        "content_type": "text",
                        "title": "Currency Conversion",
                        "payload": "Currency Conversion"
                    },
                    {
                        "content_type": "text",
                        "title": "Transfer rates",
                        "payload": "Transfer rates"
                    },
                    {
                        "content_type": "text",
                        "title": "Loc in Pakistan",
                        "payload": "Loc in Pakistan"
                    },
                    {
                        "content_type": "text",
                        "title": "Duration of Transfer",
                        "payload": "Duration of Transfer"
                    },
                    {
                        "content_type": "text",
                        "title": "Receiver Requirements",
                        "payload": "Receiver Requirements"
                    },
                    {
                        "content_type": "text",
                        "title": "Sender Requirement",
                        "payload": "Sender Requirement"
                    },
                    {
                        "content_type": "text",
                        "title": "Complaint",
                        "payload": "Complaint"
                    }

                ]
            }
            dispatcher.utter_custom_json(res1)
            print(res1)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]


class Actiongreet(Action):

    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):

        try:

            #id = tracker.sender_id
            id = 2769228663176300

            print("getting id")
            id = int(id)
            print(type(id))
            userid = requests.get(
                "https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token=EAAK0HoR2qbwBAI7MadZAejB9aru082t8Oiy8NdLuxLE7lSBHVmYGXbOvQxhMrq4jzYUA7z3JzAIt2G5yZAvnvCsmT9hOlVe2HIM90KQ1hwzy23EbIbOBxGxi1yoHrkqpjtNpQ7tYKBBRT41ZBgAt6VhxYcemAYgZAktXDOpELwZDZD".format(
                    id)).json()
            print(userid)
            print("getting userid")

            body = {
                "recipient": {
                    "id": id
                },
                "sender_action": "typing_on"
            }
            print(body)
            headers = {'content-type': 'application/json'}
            url = "https://graph.facebook.com/v5.0/me/messages?access_token=EAAK0HoR2qbwBAI7MadZAejB9aru082t8Oiy8NdLuxLE7lSBHVmYGXbOvQxhMrq4jzYUA7z3JzAIt2G5yZAvnvCsmT9hOlVe2HIM90KQ1hwzy23EbIbOBxGxi1yoHrkqpjtNpQ7tYKBBRT41ZBgAt6VhxYcemAYgZAktXDOpELwZDZD"

            requests.post(url=url, data=json.dumps(body), headers=headers)

            # get started button
            get_started = {
                "get_started": {
                    "payload": "GET STARTED"
                }
            }
            print(get_started)
            headers = {'content-type': 'application/json'}

            url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAK0HoR2qbwBAI7MadZAejB9aru082t8Oiy8NdLuxLE7lSBHVmYGXbOvQxhMrq4jzYUA7z3JzAIt2G5yZAvnvCsmT9hOlVe2HIM90KQ1hwzy23EbIbOBxGxi1yoHrkqpjtNpQ7tYKBBRT41ZBgAt6VhxYcemAYgZAktXDOpELwZDZD"

            requests.post(url=url, data=json.dumps(get_started), headers=headers)



            fn = ""
            for key, value in userid.items():
                fn = value
                print(fn)
                break
            res1 = {
                "text": "Welcome to Pakistan Currency Assistant {}. Get started by clicking the button given below\n For Customer Support, you can join this link to talk to our Customer Representative\n m.me/arsalan.virgo".format(fn),

                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Rates of Currency",
                        "payload": "Rates of Currency"
                    },
                    {
                        "content_type": "text",
                        "title": "Currency Conversion",
                        "payload": "Currency Conversion"
                    },
                    {
                        "content_type": "text",
                        "title": "Transfer rates",
                        "payload": "Transfer rates"
                    },
                    {
                        "content_type": "text",
                        "title": "Loc in Pakistan",
                        "payload": "Loc in Pakistan"
                    },
                    {
                        "content_type": "text",
                        "title": "Duration of Transfer",
                        "payload": "Duration of Transfer"
                    },
                    {
                        "content_type": "text",
                        "title": "Receiver Requirements",
                        "payload": "Receiver Requirements"
                    },
                    {
                        "content_type": "text",
                        "title": "Sender Requirement",
                        "payload": "Sender Requirement"
                    },
                    {
                        "content_type": "text",
                        "title": "Complaint",
                        "payload": "Complaint"
                    }

                ]
            }
            dispatcher.utter_custom_json(res1)
            print(res1)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]

class Action_complain(Action):

    def name(self):
        return 'action_complaint'

    def run(self, dispatcher, tracker, domain):
        try:
            print("If you have any complaint you can contact us at: info@pakistancurrency.com")
            dispatcher.utter_message("If you have any complaint you can contact us at: info@pakistancurrency.com")
            res_admin = {

                "text": "Do you want to ask more?, If yes then click on I want to ask more button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "I want to ask more",
                        "payload": "I want to ask more"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]

class Action_locations_in_pakistan(Action):

    def name(self):
        return 'action_locations_in_pakistan'

    def run(self, dispatcher, tracker, domain):
        try:
            rq = requests.get("http://pak.hashlob.com/api/getBranches").json()
            #print(rq)
            ls = []
            count = 0
            for i in rq['data']:
                print(i['name'])
                if count <= 10:
                    ls.append({"content_type": "text",
                               "title": i["name"],
                               "payload": i["name"]})
                    count += 1

            res_admin = {

                "text": "Select your city from the button given below",
                "quick_replies": ls
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]



class Action_get_address(Action):

    def name(self):
        return 'action_get_address'

    def run(self, dispatcher, tracker, domain):
        try:
            city = tracker.get_slot('ask_city')
            city = city.lower()
            if city == None:
                print("city not coming")
            else:
                print("city coming" + city)
            #inputt = str(input("Enter your city name"))
            count = 0
            rq = requests.get("http://pak.hashlob.com/api/getBranches").json()
            ls = []
            ls1 = []
            for i in rq['data']:
                for j in i['locations']:
                    if i['name'].lower() == city:
                        # print(i['name'])
                        # print(i['locations'])
                        count += 1
                        # print("There are total {} branches in {}".format(count,i["name"]))
                        ls.append(j['address'])
                        ls1.append(j['phone'])
                        # print(j['address'])
            print("There are total {} branches in {} which are as follows: ".format(count, city))
            dispatcher.utter_message("There are total {} branches in {}".format(count, city))
            count1 = 0
            for i in ls:
                count1 += 1
                print("Address # {}: {} ".format(count1,i))
                dispatcher.utter_message("Address # {}: {} ".format(count1,i))
            for j in ls1:
                dispatcher.utter_message("Contact Number: {}".format(j))
                print("Contact Number: {}".format(j))
                break
            res_admin = {

                "text": "Do you want to ask more?, If yes then click on I want to ask more button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "I want to ask more",
                        "payload": "I want to ask more"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]


class Action_company_transfer_rates(Action):

    def name(self):
        return 'action_company_transfer_rates'

    def run(self, dispatcher, tracker, domain):
        try:
            print("Company transfer rates")
            # dispatcher.utter_message("Pakistan Currency has the following companies rates which are as follows: \n"
            #                          "Western Union")
            dispatcher.utter_message("The transfer rates of Money Gram and Western Union are attached above ")

           # id = tracker.sender_id
            print("getting id")
            id = 2769228663176300
            id = int(id)
            print(type(id))
            userid = requests.get(
                "https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token=EAAK0HoR2qbwBAI7MadZAejB9aru082t8Oiy8NdLuxLE7lSBHVmYGXbOvQxhMrq4jzYUA7z3JzAIt2G5yZAvnvCsmT9hOlVe2HIM90KQ1hwzy23EbIbOBxGxi1yoHrkqpjtNpQ7tYKBBRT41ZBgAt6VhxYcemAYgZAktXDOpELwZDZD".format(
                    id)).json()

            print(userid)
            print("getting userid")


            res = {
                "recipient": {
                    "id": id
                },
                "message": {
                    "attachment": {
                        "type": "file",
                        "payload": {
                            "url": "https://github.com/jehanzaib12/Hello-World/raw/master/Moneygrram%20charges%20slab.pdf",
                            "is_reusable": True
                        }
                    }
                }
            }
            # }

            headers = {'content-type': 'application/json'}

            url = "https://graph.facebook.com/v8.0/me/messages?access_token=EAAK0HoR2qbwBACpetk73NkRr0hiMZBi7q2Kpp2f6iW8EQgqvmPzS6SphJlF3v8G1y6AhxTwGare5CRZAEkvKSG37LINTKKAah4rcZAcip3zQHtVHFc6PZBtFu5J7Dn9bZC3OsQtcfh6oF6ZBuiCSMSWTGgpDOOwrQcZA62xp910RQZDZD"

            requests.post(url=url, data=json.dumps(res), headers=headers)
            dispatcher.utter_custom_json(res)
            print(res)

            res1 = {
                "recipient": {
                    "id": id
                },
                "message": {
                    "attachment": {
                        "type": "file",
                        "payload": {
                            "url": "https://github.com/jehanzaib12/Hello-World/raw/master/Charges%20Slabs%20For%20WU.xlsx",
                            "is_reusable": True
                        }
                    }
                }
            }
            # }

            headers = {'content-type': 'application/json'}

            url = "https://graph.facebook.com/v8.0/me/messages?access_token=EAAK0HoR2qbwBACpetk73NkRr0hiMZBi7q2Kpp2f6iW8EQgqvmPzS6SphJlF3v8G1y6AhxTwGare5CRZAEkvKSG37LINTKKAah4rcZAcip3zQHtVHFc6PZBtFu5J7Dn9bZC3OsQtcfh6oF6ZBuiCSMSWTGgpDOOwrQcZA62xp910RQZDZD"

            requests.post(url=url, data=json.dumps(res1), headers=headers)
            dispatcher.utter_custom_json(res1)
            print(res1)


            res_admin = {

                "text": "Do you want to ask more?, If yes then click on I want to ask more button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "I want to ask more",
                        "payload": "I want to ask more"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]

class Action_duration_of_transfer(Action):

    def name(self):
        return 'action_duration_of_transfer'

    def run(self, dispatcher, tracker, domain):

        try:
            print("printing duration of transfer")
            dispatcher.utter_message("* The duration of transfer for Cash Transaction is 5 Minutes\n"
                                     "* The duration of transfer for Bank Transaction is depend on your bank")
            res_admin = {

                "text": "Do you want to ask more?, If yes then click on I want to ask more button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "I want to ask more",
                        "payload": "I want to ask more"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]


class Action_ask_more(Action):

    def name(self):
        return 'action_ask_more'

    def run(self, dispatcher, tracker, domain):
        try:
            fn = "jehanzaib"
            res1 = {
                "text": "Welcome to Pakistan Currency Assistant {}. Get started by clicking the button given below\n For Customer Support, you can join this link to talk to our Customer Representative\n m.me/arsalan.virgo".format(
                    fn),

                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Rates of Currency",
                        "payload": "Rates of Currency"
                    },
                    {
                        "content_type": "text",
                        "title": "Currency Conversion",
                        "payload": "Currency Conversion"
                    },
                    {
                        "content_type": "text",
                        "title": "Transfer rates",
                        "payload": "Transfer rates"
                    },
                    {
                        "content_type": "text",
                        "title": "Loc in Pakistan",
                        "payload": "Loc in Pakistan"
                    },
                    {
                        "content_type": "text",
                        "title": "Duration of Transfer",
                        "payload": "Duration of Transfer"
                    },
                    {
                        "content_type": "text",
                        "title": "Receiver Requirements",
                        "payload": "Receiver Requirements"
                    },
                    {
                        "content_type": "text",
                        "title": "Sender Requirement",
                        "payload": "Sender Requirement"
                    },
                    {
                        "content_type": "text",
                        "title": "Complaint",
                        "payload": "Complaint"
                    }

                ]
            }
            dispatcher.utter_custom_json(res1)
            print(res1)

        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]


class Action_select_currency(Action):

    def name(self):
        return 'action_select_currency'

    def run(self, dispatcher, tracker, domain):

        try:
            print("select_currency_rates")
            rq = requests.get("http://pak.hashlob.com/api/getCurrencies").json()
           # print(rq)
            ls = []
            for i in rq['data']:
                #print(i['name'])
                first_conversion_rate = "The buying rate of {} is: ".format(i['name']) + i["buying_rate"]
                second_conversion_rate = "The selling rate of {} is: ".format(i['name']) + i["selling_rate"]
                ls.append(first_conversion_rate)
                ls.append(second_conversion_rate)
                ls.append("")
            iterator = islice(ls, 35)
            nf = "The Currency Rates are as follows: \n\n" + "\n".join(
                    iterator)
            print(nf)
            dispatcher.utter_message(nf)
            res_admin = {

                "text": "Do you want to ask more?, If yes then click on I want to ask more button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "I want to ask more",
                        "payload": "I want to ask more"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)

        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]


class Action_select_first_currency(Action):

    def name(self):
        return 'action_select_first_currency'

    def run(self, dispatcher, tracker, domain):

        try:
            res1 = {
                "text": "Please select the first currency to convert by clicking on the buttons below:",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "US Dollar",
                        "payload": "US Dollar"
                    },
                    {
                        "content_type": "text",
                        "title": "EURO",
                        "payload": "EURO"
                    },
                    {
                        "content_type": "text",
                        "title": "British Pound",
                        "payload": "British Pound"
                    },
                    {
                        "content_type": "text",
                        "title": "Saudi Riyal",
                        "payload": "Saudi Riyal"
                    },
                    {
                        "content_type": "text",
                        "title": "UAE Dirham",
                        "payload": "UAE Dirham"
                    },
                    {
                        "content_type": "text",
                        "title": "Australian Dollar",
                        "payload": "Australian Dollar"
                    },
                    {
                        "content_type": "text",
                        "title": "Canadian Dollar",
                        "payload": "Canadian Dollar"
                    },
                    {
                        "content_type": "text",
                        "title": "Singapore Dollar",
                        "payload": "Singapore Dollar"
                    },
                    {
                        "content_type": "text",
                        "title": "South africa Rand",
                        "payload": "South africa Rand"
                    },
                    {
                        "content_type": "text",
                        "title": "PKR",
                        "payload": "PKR"
                    }

                ]
            }
            dispatcher.utter_custom_json(res1)
            print(res1)

           # return [FollowupAction("action_add_first_currency_amount")]

        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]

class Action_add_first_currency_amount(Action):

    def name(self):
        return 'action_add_first_currency_amount'

    def run(self, dispatcher, tracker, domain):
        try:

            currency = tracker.get_slot('first_currency_to_conversion')
            currency = currency.lower()
            if currency == None:
                print("first currency not coming")
            else:
                print("first currency coming" + currency)
            dispatcher.utter_message("Enter the amount of {} to convert into".format(currency))
            #return [FollowupAction("action_select_second_currency")]
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]

class Action_select_second_currency(Action):

    def name(self):
        return 'action_select_second_currency'

    def run(self, dispatcher, tracker, domain):
        try:
            res1 = {
                "text": "Please select the second currency that is PKR by which your amount will be converted by clicking on the buttons below:",
                "quick_replies": [

                    {
                        "content_type": "text",
                        "title": "PKR",
                        "payload": "PKR"
                    }

                ]
            }
            dispatcher.utter_custom_json(res1)
            print(res1)

        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]



class Action_calculate_currency_conversion(Action):

    def name(self):
        return 'action_calculate_currency_conversion'

    def run(self, dispatcher, tracker, domain):

        try:
            first_currency = tracker.get_slot("first_currency_to_conversion")
            first_currency_amount = tracker.get_slot("first_currency_amount")
            second_currency = tracker.get_slot("second_currency_to_conversion")
            first_currency = first_currency.lower()
            second_currency = second_currency.lower()

            if first_currency == None:
                print("first currency not coming")
            else:
                print("The first currency to convert is " + first_currency)

            if first_currency_amount == None:
                print("first currency amount not coming")
            else:
                print("The first currency amount is" + first_currency_amount)

            if second_currency == None:
                print("second currency  not coming")
            else:
                print("The second currency to convert is {}".format(second_currency))
            rq = requests.get("http://pak.hashlob.com/api/getCurrencies").json()

            for i in rq['data']:
                for j in rq['data']:
                    if first_currency == i["name"].lower():
                        print(i['name'])
                        first_conversion_rate = int(float(i["buying_rate"]))
                        # print(type(first_conversion_rate))

                        # first_conversion_rate = intfirst_conversion_rate)
                        if second_currency == j["name"].lower():
                            total = 0
                            second_conversion_rate = int(float(j["buying_rate"]))
                            print("first conversion rate is {}".format(first_conversion_rate))
                            print(type(first_conversion_rate))
                            print("second conversion rate is {}".format(second_conversion_rate))
                            print(type(second_conversion_rate))
                            print("the rate is {}".format(first_currency_amount))
                            first_currency_amount = int(float(first_currency_amount))
                            print(type(first_currency_amount))
                            total = first_conversion_rate * first_currency_amount / second_conversion_rate
                            print("printing the total amount")
                            print("the total amount is {}".format(total))
                            dispatcher.utter_message("Your total amount is after converting {} to {} is {}".format(first_currency,
                                                                                                             second_currency,total))
                            print("the total amount is {}".format(total))
                            break
            res_admin = {

                "text": "Do you want to ask more?, If yes then click on I want to ask more button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "I want to ask more",
                        "payload": "I want to ask more"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)
        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]




class Actionrecevier(Action):

    def name(self):
        return 'action_receiver'

    def run(self, dispatcher, tracker, domain):

        try:
            dispatcher.utter_message("This is the following requirments for receiver: ")


            dispatcher.utter_message('Original NIC With Photocopy \n MTCH (Western Union)\n'
                                     'Reference Number (Money Gram)\n Pin Number (RIA)\n'
                    'Sender Name\n Receiver Name as per ID\n')
            print("receiver requirement printed")
            res_admin = {

                "text": "Do you want to ask more currency rates, If yes then click on currency rates button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Currency Rates",
                        "payload": "Currency Rates"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)

        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]

class Actionsender(Action):

    def name(self):
        return 'action_sender'

    def run(self, dispatcher, tracker, domain):

        try:
            dispatcher.utter_message("This is the following requirments for sender: ")


            dispatcher.utter_message('Original NIC With Photocopy \n Receiver name as per ID\n'
                                     'Contact Number\n Address)\n'
                    'Receiver Bank Account Details (If receiver has bank account)\n')
            print("sender requirement printed")
            res_admin = {

                "text": "Do you want to ask more currency rates, If yes then click on currency rates button given below? ",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Currency Rates",
                        "payload": "Currency Rates"

                    },
                    {
                        "content_type": "text",
                        "title": "No, thankyou",
                        "payload": "No, thankyou"

                    }
                ]
            }
            dispatcher.utter_custom_json(res_admin)
            print(res_admin)

        except:
            dispatcher.utter_message("Pakistan Currency Chatbot Didnt recognize the text! Try Again!")
            return [FollowupAction("action_greet")]