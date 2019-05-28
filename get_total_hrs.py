import requests
import login
import datetime
import json


def get_month_summary(session, month, year):
    date_str = f"{year}-{month}-01"
    url = f"https://myoperator.keka.com/api/mytime/attendance/summary/{date_str}"
    print(url)
    response = session.get(url, headers={
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'referer': 'https://myoperator.keka.com/',
        'authority': 'myoperator.keka.com',
        'x-requested-with': 'XMLHttpRequest',
        'request-context': 'appId=cid-v1:aecd77d6-a75f-425d-8560-ec8cb839064c',
        'request-id': '|zR7p9.uf0wv',
    })
    print(response,response.text)
    attandance_data = json.loads(response.text)
    return attandance_data


if __name__ == "__main__":
    total_office_hrs = 0
    total_working_days = 0
    avg_required_hrs=9
    session, status = login.login()
    if not status:
        print("ERROR :: logging In")
        quit()
    
    attandances = get_month_summary(session, "05", "2019")
    for attandace in attandances:
        # print(attandace)
        if attandace.get('dayType') == 2: # skip if day is holiday
            continue
        
        print(attandace.get('attendanceDate'), attandace.get('totalEffectiveHours'))
        total_office_hrs = total_office_hrs + attandace.get('totalEffectiveHours')
        total_working_days = total_working_days + 1
    
    total_required_hrs = total_working_days * avg_required_hrs
    # avg_hrs = total_required_hrs // total_office_hrs

    print("Total Working Days: ", total_working_days)
    print("Total Office Hrs: ", total_office_hrs)
    print("Total Required Hrs: ", total_required_hrs)
    print("Mission Hrs: ", total_required_hrs - total_office_hrs)
    # print("Average Hrs Required: ", avg_hrs)


    # Logout User
    login.logout(session)

