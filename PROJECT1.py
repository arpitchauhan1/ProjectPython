import requests
import json

def SendSms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        "authorization":'5Xp8RbLSO1UgM7hxyKWtNmsC4oQZil9qf0EGndjak2Yu6JBTDw3sOqUXD6lPAFjr0byJfovaMT79p8B2',
        "sender_id":'TXTIND',
        "message":message,
        "language":'english',
        "route":'v3',
        "numbers":number
    }

    response = requests.get(url, params=params)
    dict = response.json()
    print(dict)

SendSms("8770571259","Hi how are you Arpit")