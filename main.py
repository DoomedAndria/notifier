import time
import requests
from send_message import send_kutaisi, send_sachkhere

kutaisi = 'https://api-my.sa.gov.ge/api/v1/DrivingLicensePracticalExams2/DrivingLicenseExamsDates2?CategoryCode=4' \
          '&CenterId=2 '
sachkhere = 'https://api-my.sa.gov.ge/api/v1/DrivingLicensePracticalExams2/DrivingLicenseExamsDates2?CategoryCode=4' \
            '&CenterId=10 '


def detect_change(file, dates):
    with open(file, 'r') as txt:
        if txt.read() != str(dates):
            with open(file, 'w') as txt1:
                txt1.write(str(dates))
            return True
    return False


def run():
    resK = requests.get(kutaisi)
    resS = requests.get(sachkhere)

    datesK = [i["bookingDate"] for i in resK.json()]
    datesS = [i["bookingDate"] for i in resS.json()]
    if detect_change('kutaisi.txt', datesK):
#         send_kutaisi(datesK)
        print("message sent")

    elif detect_change('sachkhere.txt', datesS):
        send_sachkhere(datesS)
        print("message sent")




