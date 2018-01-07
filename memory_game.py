import json
import logging
from random import randint
import requests
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

r2 = requests.post("http://intelycare.net/isystem/pages/partcare.php", data={'uid': 155, 'section': 'Dashboard'})
##print(r2.content)
content = r2.content


def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.items()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    else:
        return input


articles = convert(json.loads(content))
json_file = open("a.json", 'wb')
json_file.write(content)
json_file.close()
with open('a.json') as provJson:
    data = provJson.read()
    apiData = json.loads(data)
TOTALCOUNT = apiData["TOTAL"]

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launch():
    welcome_msg=render_template('welcome')
    return statement(welcome_msg)

@ask.intent("CreateStaffIntent")
def CREATE_STAFF():
    schedule_msg1 = render_template('CURRENT WEEK TOTAL', schedule=CURRENT_WEEK_TOTAL)

    return statement(schedule_msg1)


@ask.intent("CurrentWeekTotalIntent")
def CURRENT_WEEK_TOTAL():
    keys = []
    values = []
    string_to_be_add = ""
    CURRENT_WEEK_FLOOR = TOTALCOUNT["CURRENT_WEEK"]
    text1 = " total number of employees working for current week is "
    for k, v in CURRENT_WEEK_FLOOR.items():
        if k == "total":
            value1 = str(v)
            CURRENT_WEEK_TOTAL = text1 + value1

    schedule_msg1 = render_template('CURRENT WEEK TOTAL', schedule=CURRENT_WEEK_TOTAL)

    return statement(schedule_msg1)


@ask.intent("CurrentWeekFloorIntent")
def CURRENT_WEEK_FLOOR_WISE_DETAILS():
    keys = []
    values = []
    string_to_be_add = ""
    CURRENT_WEEK_FLOOR = TOTALCOUNT["CURRENT_WEEK"]
    text2 = " number of employees working for current week in the floor "
    for k, v in CURRENT_WEEK_FLOOR.items():
        if k != "total":
            keys.append(k)
            values.append(v)

    for i in range(0, 2):
        string_to_be_add += str(keys[i]) + " is " + str(values[i]) + " , "

    CURRENT_WEEK_FLOORWISE_DETAILS = text2 + string_to_be_add

    schedule_msg2 = render_template('CURRENT WEEK FLOOR WISE TOTAL', schedule2=CURRENT_WEEK_FLOORWISE_DETAILS)

    return statement(schedule_msg2)


@ask.intent("LastWeekTotalIntent")
def LAST_WEEK_TOTAL():
    keys = []
    values = []
    LAST_WEEK_FLOOR = TOTALCOUNT["LAST_WEEK"]
    text1 = " total number of employees working for last week is "
    for k, v in LAST_WEEK_FLOOR.items():
        if k == "total":
            value1 = str(v)
            LAST_WEEK_TOTAL = text1 + value1

    schedule_msg3 = render_template('LAST WEEK TOTAL', schedule3=LAST_WEEK_TOTAL)

    return statement(schedule_msg3)


@ask.intent("LastWeekFloorIntent")
def LAST_WEEK_FLOOR_WISE_DETAILS():
    keys = []
    values = []
    string_to_be_add = ""
    LAST_WEEK_FLOOR = TOTALCOUNT["LAST_WEEK"]
    text2 = " number of employees working for last week in the floor "
    for k, v in LAST_WEEK_FLOOR.items():
        if k != "total":
            keys.append(k)
            values.append(v)

    for i in range(0, 2):
        string_to_be_add += str(keys[i]) + " is " + str(values[i]) + " , "

    LAST_WEEK_FLOORWISE_DETAILS = text2 + string_to_be_add

    schedule_msg4 = render_template('LAST WEEK FLOOR WISE TOTAL', schedule4=LAST_WEEK_FLOORWISE_DETAILS)

    return statement(schedule_msg4)


@ask.intent("NextWeekTotalIntent")
def NEXT_WEEK_TOTAL():
    keys = []
    values = []
    NEXT_WEEK_FLOOR = TOTALCOUNT["NEXT_WEEK"]
    text1 = " total number of employees working for the NEXT week is "
    for k, v in NEXT_WEEK_FLOOR.items():
        if k == "total":
            value1 = str(v)
            NEXT_WEEK_TOTAL = text1 + value1

    schedule_msg5 = render_template('NEXT WEEK TOTAL', schedule5=NEXT_WEEK_TOTAL)

    return statement(schedule_msg5)


@ask.intent("NextWeekFloorIntent")
def NEXT_WEEK_FLOOR_WISE_DETAILS():
    keys = []
    values = []
    string_to_be_add = ""
    NEXT_WEEK_FLOOR = TOTALCOUNT["NEXT_WEEK"]
    text2 = " number of employees working for NEXT week in the floor "
    for k, v in NEXT_WEEK_FLOOR.items():
        if k != "total":
            keys.append(k)
            values.append(v)

    for i in range(0, 2):
        string_to_be_add += str(keys[i]) + " is " + str(values[i]) + " , "

    NEXT_WEEK_FLOORWISE_DETAILS = text2 + string_to_be_add

    schedule_msg6 = render_template('NEXT WEEK FLOOR WISE TOTAL', schedule6=NEXT_WEEK_FLOORWISE_DETAILS)

    return statement(schedule_msg6)


@ask.intent("TodayTotalIntent")
def TODAY_TOTAL():
    keys = []
    values = []
    TODAY_FLOOR = TOTALCOUNT["TODAY"]
    text1 = " total number of employees working for TODAY is "
    for k, v in TODAY_FLOOR.items():
        if k == "total":
            value1 = str(v)
            TODAY_TOTAL = text1 + value1

    schedule_msg7 = render_template('TODAY TOTAL', schedule7=TODAY_TOTAL)

    return statement(schedule_msg7)


@ask.intent("TodayFloorIntent")
def TODAY_FLOOR_WISE_DETAILS():
    keys = []
    values = []
    string_to_be_add = ""
    TODAY_FLOOR = TOTALCOUNT["TODAY"]
    text2 = " number of employees working for TODAY in the floor "
    for k, v in TODAY_FLOOR.items():
        if k != "total":
            keys.append(k)
            values.append(v)

    for i in range(0, 2):
        string_to_be_add += str(keys[i]) + " is " + str(values[i]) + " , "

    TODAY_FLOORWISE_DETAILS = text2 + string_to_be_add

    schedule_msg8 = render_template('TODAY FLOOR WISE TOTAL', schedule8=TODAY_FLOORWISE_DETAILS)

    return statement(schedule_msg8)


@ask.intent("TomorrowTotalIntent")
def TOMORROW_TOTAL():
    keys = []
    values = []
    TOMORROW_FLOOR = TOTALCOUNT["TOMORROW"]
    text1 = " total number of employees working for TOMORROW are "
    for k, v in TOMORROW_FLOOR.items():
        if k == "total":
            value1 = str(v)
            TOMORROW_TOTAL = text1 + value1

    schedule_msg9 = render_template('TOMORROW TOTAL', schedule9=TOMORROW_TOTAL)

    return statement(schedule_msg9)


@ask.intent("TomorrowFloorIntent")
def TOMORROW_FLOOR_WISE_DETAILS():
    keys = []
    values = []
    string_to_be_add = ""
    TOMORROW_FLOOR = TOTALCOUNT["TOMORROW"]
    text2 = " number of employees working for TOMORROW in the floor "
    for k, v in TOMORROW_FLOOR.items():
        if k != "total":
            keys.append(k)
            values.append(v)

    for i in range(0, 2):
        string_to_be_add += str(keys[i]) + " is " + str(values[i]) + " , "

    TOMORROW_FLOORWISE_DETAILS = text2 + string_to_be_add

    schedule_msg10 = render_template('TOMORROW FLOOR WISE TOTAL', schedule10=TOMORROW_FLOORWISE_DETAILS)

    return statement(schedule_msg10)


@ask.intent("YesterdayTotalIntent")
def YESTERDAY_TOTAL():
    keys = []
    values = []
    YESTERDAY_FLOOR = TOTALCOUNT["YESTERDAY"]
    text1 = " total number of employees who were working YESTERDAY are  "
    for k, v in YESTERDAY_FLOOR.items():
        if k == "total":
            value1 = str(v)
            YESTERDAY_TOTAL = text1 + value1

    schedule_msg11 = render_template('YESTERDAY TOTAL', schedule11=YESTERDAY_TOTAL)

    return statement(schedule_msg11)


@ask.intent("YesterdayFloorIntent")
def YESTERDAY_FLOOR_WISE_DETAILS():
    keys = []
    values = []
    string_to_be_add = ""
    YESTERDAY_FLOOR = TOTALCOUNT["YESTERDAY"]
    text2 = " number of employees who were working YESTERDAY in the floor "
    for k, v in YESTERDAY_FLOOR.items():
        if k != "total":
            keys.append(k)
            values.append(v)

    for i in range(0, 2):
        string_to_be_add += str(keys[i]) + " is " + str(values[i]) + ", "
    YESTERDAY_FLOORWISE_DETAILS = text2 + string_to_be_add
    schedule_msg12 = render_template('YESTERDAY FLOOR WISE TOTAL', schedule12=YESTERDAY_FLOORWISE_DETAILS)

    return statement(schedule_msg12)


DATASS = apiData['DATA']
DATA = DATASS
CURRENT_WEEK = DATA['CURRENT_WEEK']


@ask.intent("CurrentWeekNurseIntent")
def CURRENT_WEEK_NURSENAME_PID():
    CURRENT_WEEK = DATA['CURRENT_WEEK']
    usernames = []
    pids = []
    dstring_to_be_add = ""
    dtext1 = "the current week, the nurse name and their P.I.D. number are following, "
    if len(CURRENT_WEEK) == 0:
        lvalue1 = "the current week, there are no records of providers working"
    else:
        for i in range(0, len(CURRENT_WEEK)):
            username = DATA['CURRENT_WEEK'][i]['pfname']

            if username != "Pending":
                usernames.append(username)
            else:
                usernames.append('Blank')

            pid = DATA['CURRENT_WEEK'][i]['pid']
            if pid is not None:
                pids.append(pid)
            else:
                pids.append('0')
        if len(usernames) > 1:
            for i in range(0, len(usernames)):
                dstring_to_be_add += "name " + str(usernames[i]) + ", P.I.D. " + str(pids[i]) + " , "

            lvalue1 = dtext1 + dstring_to_be_add

        else:
            dstring_to_be_add += "name " + str(usernames[0]) + ", P.I.D. " + str(pids[0]) + " , "
            lvalue1 = dtext1 + dstring_to_be_add
    lvalue1

    schedule_msg13 = render_template('CURRENT WEEK NURSENAME PID', schedule13=lvalue1)

    return statement(schedule_msg13)


@ask.intent("LastWeekNurseIntent")
def LAST_WEEK_NURSENAME_PID():
    LAST_WEEK = DATA['LAST_WEEK']
    usernames = []
    pids = []
    dstring_to_be_add = ""
    dtext1 = "the LAST WEEK, the nurse name and their P.I.D. number are following, "
    if len(LAST_WEEK) == 0:
        lvalue1 = "the LAST WEEK, there are no records of providers working"
    else:
        for i in range(0, len(LAST_WEEK)):
            username = DATA['LAST_WEEK'][i]['pfname']

            if username != "Pending":
                usernames.append(username)
            else:
                usernames.append('Blank')

            pid = DATA['LAST_WEEK'][i]['pid']
            if pid is not None:
                pids.append(pid)
            else:
                pids.append('0')
        if len(usernames) > 1:
            for i in range(0, len(usernames)):
                dstring_to_be_add += "name " + str(usernames[i]) + ", P.I.D. " + str(pids[i]) + " , "

            lvalue1 = dtext1 + dstring_to_be_add

        else:
            dstring_to_be_add += "name " + str(usernames[0]) + ", P.I.D. " + str(pids[0]) + " , "
            lvalue1 = dtext1 + dstring_to_be_add
    lvalue1

    schedule_msg14 = render_template('LAST WEEK NURSENAME PID', schedule14=lvalue1)

    return statement(schedule_msg14)


@ask.intent("NextWeekNurseIntent")
def NEXT_WEEK_NURSENAME_PID():
    NEXT_WEEK = DATA['NEXT_WEEK']
    usernames = []
    pids = []
    dstring_to_be_add = ""
    dtext1 = "the NEXT WEEK, the nurse name and their P.I.D. number are following, "
    if len(NEXT_WEEK) == 0:
        lvalue1 = "the NEXT WEEK, there are no records of providers working"
    else:
        for i in range(0, len(NEXT_WEEK)):
            username = DATA['NEXT_WEEK'][i]['pfname']

            if username != "Pending":
                usernames.append(username)
            else:
                usernames.append('Blank')

            pid = DATA['NEXT_WEEK'][i]['pid']
            if pid is not None:
                pids.append(pid)
            else:
                pids.append('0')
        if len(usernames) > 1:
            for i in range(0, len(usernames)):
                dstring_to_be_add += "name " + str(usernames[i]) + ", P.I.D. " + str(pids[i]) + " , "

            lvalue1 = dtext1 + dstring_to_be_add

        else:
            dstring_to_be_add += "name " + str(usernames[0]) + ", P.I.D. " + str(pids[0]) + " , "
            lvalue1 = dtext1 + dstring_to_be_add
    lvalue1

    schedule_msg15 = render_template('NEXT WEEK NURSENAME PID', schedule15=lvalue1)

    return statement(schedule_msg15)


@ask.intent("TodayNurseIntent")
def TODAY_NURSENAME_PID():
    TODAY = DATA['TODAY']
    usernames = []
    pids = []
    dstring_to_be_add = ""
    dtext1 = "TODAY, the nurse name and their P.I.D. number are following, "
    if len(TODAY) == 0:
        lvalue1 = "TODAY, there are no records of providers working"
    else:
        for i in range(0, len(TODAY)):
            username = DATA['TODAY'][i]['pfname']

            if username != "Pending":
                usernames.append(username)
            else:
                usernames.append('Blank')

            pid = DATA['TODAY'][i]['pid']
            if pid is not None:
                pids.append(pid)
            else:
                pids.append('0')
        if len(usernames) > 1:
            for i in range(0, len(usernames)):
                dstring_to_be_add += "name " + str(usernames[i]) + ", P.I.D. " + str(pids[i]) + " , "

            lvalue1 = dtext1 + dstring_to_be_add

        else:
            dstring_to_be_add += "name " + str(usernames[0]) + ", P.I.D. " + str(pids[0]) + " , "
            lvalue1 = dtext1 + dstring_to_be_add
    lvalue1

    schedule_msg16 = render_template('TODAY NURSENAME PID', schedule16=lvalue1)

    return statement(schedule_msg16)


@ask.intent("TomorrowNurseIntent")
def TOMORROW_NURSENAME_PID():
    TOMORROW = DATA['TOMORROW']
    usernames = []
    pids = []
    dstring_to_be_add = ""
    dtext1 = "TOMORROW, the nurse name and their P.I.D. number are following, "
    if len(TOMORROW) == 0:
        lvalue1 = "TOMORROW, there are no records of providers working"
    else:
        for i in range(0, len(TOMORROW)):
            username = DATA['TOMORROW'][i]['pfname']

            if username != "Pending":
                usernames.append(username)
            else:
                usernames.append('Blank')

            pid = DATA['TOMORROW'][i]['pid']
            if pid is not None:
                pids.append(pid)
            else:
                pids.append('0')
        if len(usernames) > 1:
            for i in range(0, len(usernames)):
                dstring_to_be_add += "name " + str(usernames[i]) + ", P.I.D. " + str(pids[i]) + " , "

            lvalue1 = dtext1 + dstring_to_be_add

        else:
            dstring_to_be_add += "name " + str(usernames[0]) + ", P.I.D. " + str(pids[0]) + " , "
            lvalue1 = dtext1 + dstring_to_be_add
    lvalue1

    schedule_msg17 = render_template('TOMORROW NURSENAME PID', schedule17=lvalue1)

    return statement(schedule_msg17)


@ask.intent("YesterdayNurseIntent")
def YESTERDAY_NURSENAME_PID():
    YESTERDAY = DATA['YESTERDAY']
    usernames = []
    pids = []
    dstring_to_be_add = ""
    dtext1 = "YESTERDAY, the nurse name and their P.I.D. number are following, "
    if len(YESTERDAY) == 0:
        lvalue1 = "yesterday, there are no records of providers working"
    else:
        for i in range(0, len(YESTERDAY)):
            username = DATA['YESTERDAY'][i]['pfname']

            if username != "Pending":
                usernames.append(username)
            else:
                usernames.append('Blank')

            pid = DATA['YESTERDAY'][i]['pid']
            if pid is not None:
                pids.append(pid)
            else:
                pids.append('0')
        if len(usernames) > 1:
            for i in range(0, len(usernames)):
                dstring_to_be_add += "name " + str(usernames[i]) + ", P.I.D. " + str(pids[i]) + " , "

            lvalue1 = dtext1 + dstring_to_be_add

        else:
            dstring_to_be_add += "name " + str(usernames[0]) + ", P.I.D. " + str(pids[0]) + " , "
            lvalue1 = dtext1 + dstring_to_be_add
    lvalue1

    schedule_msg18 = render_template('YESTERDAY NURSENAME PID', schedule18=lvalue1)

    return statement(schedule_msg18)

B2 = requests.post("http://intelycare.net/isystem/manage/billing.php", data={'Section': 'main', 'cid': 151, 'uid': 155})
##print(r2.content)
B2content = B2.content
articles = convert(json.loads(B2content))
json_file = open("billing.json", 'wb')
json_file.write(B2content)
json_file.close()
with open('billing.json') as provJson:
    data = provJson.read()
    billingData = json.loads(data)
goodbilling = billingData['data']['Good To Go']
badbilling = billingData['data']['Missing Data']


@ask.intent("BillingEnterCountIntent")
def Billing_ENTERED_COUNT():
    enteredlst = []
    enterednamelst = []
    if len(goodbilling) == 0:
        lvalue1 = "NUMBER OF records Related to entered billing IS ZERO"
    else:
        for i in range(0, len(goodbilling)):
            aproved = goodbilling[i]['approved']
            if aproved == '0':
                lname = goodbilling[i]['fname']
                enterednamelst.append(lname)
                enteredlst.append('1')

        val = len(enterednamelst)
        lvalue1 = "total number of billing which is in entered status is " + str(val)
    lvalue1

    schedule_msg19 = render_template('Billing ENTERED COUNT', schedule19=lvalue1)

    return statement(schedule_msg19)


@ask.intent("BillingApprovedCountIntent")
def APPROVED_ENTERED_COUNT():
    approvedlst = []
    approvednamelst = []
    if len(goodbilling) == 0:
        lvalue1 = "NUMBER OF records Related to approved billing IS ZERO"
    else:
        for i in range(0, len(goodbilling)):
            aproved = goodbilling[i]['approved']
            if aproved != '0':
                lname = goodbilling[i]['fname']
                approvednamelst.append(lname)
                approvedlst.append(aproved)

        val = len(approvednamelst)
        lvalue1 = "total number of billing which is in approved status is " + str(val)
    lvalue1

    schedule_msg20 = render_template('APPROVED ENTERED COUNT', schedule20=lvalue1)

    return statement(schedule_msg20)


@ask.intent("BillingEnterNameIntent")
def Billing_ENTERED_NAME():
    enteredlst = []
    enterednamelst = []
    if len(goodbilling) == 0:
        lvalue1 = "NUMBER OF records Related to entered billing IS ZERO"
    else:
        for i in range(0, len(goodbilling)):
            aproved = goodbilling[i]['approved']
            if aproved == '0':
                lname = goodbilling[i]['fname']
                if lname == 'N/a':
                    lname = "Blank"
                    enterednamelst.append(lname)
                    enteredlst.append('1')
                else:
                    enterednamelst.append(lname)
                    enteredlst.append('1')

        val = ' , '.join(enterednamelst)
        lvalue1 = "name of the provider whose billing status is entered status are following " + str(val)
    lvalue1

    schedule_msg21 = render_template('Billing ENTERED NAME', schedule21=lvalue1)

    return statement(schedule_msg21)


@ask.intent("BillingApprovedNameIntent")
def APPROVED_ENTERED_NAME():
    approvedlst = []
    approvednamelst = []
    if len(goodbilling) == 0:
        lvalue1 = "NUMBER OF records Related to approved billing IS ZERO"
    else:
        for i in range(0, len(goodbilling)):
            aproved = goodbilling[i]['approved']
            if aproved != '0':
                lname = goodbilling[i]['fname']
                if lname == 'N/a':
                    lname = "Blank"
                    approvednamelst.append(lname)
                    approvedlst.append(aproved)
                else:
                    approvednamelst.append(lname)
                    approvedlst.append(aproved)

        val = ' , '.join(approvednamelst)
        lvalue1 = "name of the provider whose billing status is approved status are following " + str(val)
    lvalue1

    schedule_msg22 = render_template('APPROVED ENTERED NAME', schedule22=lvalue1)

    return statement(schedule_msg22)


@ask.intent("BillingMissingCountIntent")
def MISSING_COUNT():
    approvedlst = []
    approvednamelst = []
    if len(badbilling) == 0:
        lvalue1 = "NUMBER OF records Related to MISSING billing IS ZERO"
    else:
        for i in range(0, len(badbilling)):
            aproved = badbilling[i]['approved']
            if aproved == '0':
                lname = badbilling[i]['fname']
                approvednamelst.append(lname)
                approvedlst.append(aproved)

        val = len(approvednamelst)
        lvalue1 = "total number of billing which is in missing status is " + str(val)
    lvalue1

    schedule_msg23 = render_template('MISSING COUNT', schedule23=lvalue1)

    return statement(schedule_msg23)


@ask.intent("BillingMissingNameIntent")
def MISSING_NAME():
    enteredlst = []
    enterednamelst = []
    if len(badbilling) == 0:
        lvalue1 = "NUMBER OF records Related to MISSING billing IS ZERO"
    else:
        for i in range(0, len(badbilling)):
            aproved = badbilling[i]['approved']
            if aproved == '0':
                lname = badbilling[i]['fname']
                if lname == 'N/a':
                    lname = "Blank"
                    enterednamelst.append(lname)
                    enteredlst.append('1')
                else:
                    enterednamelst.append(lname)
                    enteredlst.append('1')

        val = ' , '.join(enterednamelst)
        lvalue1 = "name of the provider whose billing status is missing are following " + str(val)
    lvalue1

    schedule_msg24 = render_template('MISSING NAME', schedule24=lvalue1)

    return statement(schedule_msg24)


r22 = requests.post("http://intelycare.net/isystem/pages/partcare.php", data={'cid': 151, 'section': 'Providers'})
##print(r2.content)
content22 = r22.content

articles = convert(json.loads(content22))
json_file = open("PROVIDER.json", 'wb')
json_file.write(content22)
json_file.close()
with open('PROVIDER.json') as provJson:
    data = provJson.read()
    PROVIDERData = json.loads(data)


def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.items()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    else:
        return input


@ask.intent("NurseCountIntent")
def NURSE_COUNT():
    counterm = 0
    if len(PROVIDERData) == 0:
        lvalue1 = "Number of nurses is zero"
    else:
        for i in range(0, len(PROVIDERData)):
            types = PROVIDERData[i]['type']
            if types == 'Nurse':
                counterm = counterm + 1

        lvalue1 = "amount of nurses is " + str(counterm)

    schedule_msg25 = render_template('NURSE COUNT', schedule25=lvalue1)

    return statement(schedule_msg25)


@ask.intent("CNACountIntent")
def CNA_COUNT():
    counterm = 0
    if len(PROVIDERData) == 0:
        lvalue1 = "Number of CNA's is zero"
    else:
        for i in range(0, len(PROVIDERData)):
            types = PROVIDERData[i]['type']
            if types == 'CNA':
                counterm = counterm + 1

        lvalue1 = "amount of CNA is " + str(counterm)

    schedule_msg26 = render_template('CNA COUNT', schedule26=lvalue1)

    return statement(schedule_msg26)


@ask.intent("MaleFemaleIntent")
def MALE_FEMALE():
    counterm = 0
    counterf = 0

    if len(PROVIDERData) == 0:
        lvalue1 = "Number of providers is zero"
    else:
        for i in range(0, len(PROVIDERData)):
            sex = PROVIDERData[i]['sex']
            if sex == 'M':
                counterm = counterm + 1
            if sex == 'F':
                counterf = counterf + 1

        lvalue1 = "number of male providers is " + str(
            counterm) + " and female providers is " + str(counterf)

    schedule_msg27 = render_template('MALE FEMALE', schedule27=lvalue1)

    return statement(schedule_msg27)


@ask.intent("MaleCountIntent")
def MALE_PROVIDERS():
    counterm = 0
    if len(PROVIDERData) == 0:
        lvalue1 = "number of records for male providers is zero"
    else:
        for i in range(0, len(PROVIDERData)):
            sex = PROVIDERData[i]['sex']
            if sex == 'M':
                counterm = counterm + 1

        lvalue1 = "amount of male providers is " + str(counterm)

    schedule_msg28 = render_template('MALE PROVIDERS', schedule28=lvalue1)

    return statement(schedule_msg28)


@ask.intent("FemaleCountIntent")
def FEMALE_PROVIDERS():
    counterm = 0
    if len(PROVIDERData) == 0:
        lvalue1 = "number of records for female providers is zero"
    else:
        for i in range(0, len(PROVIDERData)):
            sex = PROVIDERData[i]['sex']
            if sex == 'F':
                counterm = counterm + 1

        lvalue1 = "amount of female providers is " + str(counterm)

    schedule_msg29 = render_template('FEMALE PROVIDERS', schedule29=lvalue1)

    return statement(schedule_msg29)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text=render_template('bye')
    return statement(bye_text)

@ask.intent('AMAZON.StopIntent')
def cancel():
    bye_text=render_template('bye')
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)