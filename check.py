from itertools import islice

import requests
rq = requests.get("http://pak.hashlob.com/api/getBranches").json()
print(rq)
ls = []
count = 0
for i in rq['data']:
                #print(i['name'])
                if count<=10:
                    ls.append({"content_type": "text",
                               "title": i["name"],
                               "payload": i["name"]})
                    count+=1


res_admin = {

                "text": "Select your city from the button given below",
                "quick_replies": ls
            }

print(res_admin)