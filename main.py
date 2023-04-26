import time
import requests
from send_message import send_sachkhere


sachkhere = 'https://api-my.sa.gov.ge/api/v1/DrivingLicensePracticalExams2/DrivingLicenseExamsDates2?CategoryCode=4&CenterId=10'


def detect_change(file, dates):
    with open(file, 'r') as txt:
        if txt.read() != str(dates):
            with open(file, 'w') as txt1:
                txt1.write(str(dates))
            return True
    return False


def run():
    resS = requests.get(sachkhere)

    datesS = [i["bookingDate"] for i in resS.json()]
    if detect_change('sachkhere.txt', datesS):
        send_sachkhere(datesS)
        print("message sent")




