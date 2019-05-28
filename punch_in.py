import requests

cookies = {
    'cookie: _ga': 'GA1.2.982115016.1553089365',
    'Subdomain': 'myoperator.keka.com',
    'ai_user': '5EK2L|2019-03-20T13:43:09.349Z',
    'lc_sso8563323': '1554353128126',
    'ASP.NET_SessionId': 'e3xxfqxa4hgqyrntqe3hkqcq',
    'ThemeIndex': '1',
    '__RequestVerificationToken': 'yeZyBfYwkBp9yuX5R0KfxcEfPn9fnQCF3z8dJb1eLe8lPbl_jZIZ_8yDrXk4WgTgYfUwZAl0KgDvF8Xw1Xa1F7XjS52GlPdxkgbH2K1hC701',
    '.AspNet.Cookies': 'WUfzpOd_d3suR7JnyeGjCaVDlEA6tX_EtdJFkcuWd79VNCpwjNZtjqDD1Yl9WHykubxtUcHq7kENgoC7FKu55BaBrXrQh0LdkMjAM2ZTHxA4r65GkzNbqCEoLHkC5d84wie_yGNCCcI1UiqT6mY-U0l874pOyaJ6uTNZ7lE7umi66Jh8L-2yX-b1TfW_xVTDGcJIewVKHTcwkywXn7MytSGKWMSTTBThpcD8TC_ccX48spIhmjIL2iwIX6OskLGqH_iUkCVHsRKTQuEDYgzg5MjcTjJrJBj0gFkW83PRKn6spZeqg0R4gPNvq53PWrIYwKXDzRAkHoSEuLKlALzDnZFgmYtueug7xZyp-NzxPHZLFCx7O-V_YNMSiUySfAOp-M__CrEogitWVb6dOET4yKfMocgRxSv83C6L1q7XBUP9OhxIaCkZrNW8pjCwsWdDcjbbATZfVhBSYt0x87GZ9fx7-xd4gPow3IxnKhdF3iKjC9aqq8L7kq4-TCMI-_HIioH3lYWlHuKxqi5Kdkxy-H4oHdw0EALflvCnSQckJYhY4LgTJNLknRBB9-6wGnFO4VcAkglbRDGZ2KUs5RvXjqn-VZ_nEJ41XW00_S1cHZ28nOb7JHNlufBkywhBfZnSap1yxHx2oWxcLo5oArKvAeR_-2q_XQKN-Wc1NrnNC-UbXUjKouopy6AsTo7SPuHqxok0daYZSSh9KWeC7-NhubGezbrb2TwBgo_h4TeK3m3AHT1Dw_8iHdAFiLCxKTBG2dpVHQjrAZZ6QpuU9NmlpFug2dzIG6aqnv_qsTl96pNZVwu6ZeA8-3QtxyttiBL0sjxBMJf04lNt24ipdstV7ezLcmfqtLzH24WzqhXHuWFLodr_WHUgPRO5qzeYjU0iYia7Km8LZyRWMRnQnwHmFukQp0ZecBJQcgX-oVl2VU9GbPA_0DRTM16YN9CDXs2ILcOHfAgP5mvoN0J0_qNWRD9irON8rH3q9sVQzSEIe-b_JrznApeZAUfbc-Hb6G-K_-9XTnDxms4VNh8QjjbD93BzynBgT0JLVXOzed-vAfU4UL4CoZ0lCD-_SHoA4I0LtxxgNVtiDJnVYRACwjHTo7hXTU46vk1EjoOy1F9SGP-2DW94PhlP-T8BLcEk3fl_vxM6KiHzT-uSHutcvJgYjrp22lMt14hs_FysbM7EJhjhi0Xl6l156CGjw2FxEzw0JD5k9T5N6YPyTrrK0q-tQ3Pcxm9zxwm9X2_d0vrC5T5zWyYwRVNgNWlQjmV_ljLrLL_onkxKfv0YOEk2S4S6tKWacDj5JWg2j-csjyOP6DN1oIr3Q0_LK-K_mV0rtgopVA8RFwGc4iYdpY2rm3Mi8pyaBFE-CxoY4THUgn6II8V6O_HffknOzZbNJlq0J0F9DxWtC1Sru6sPhzJtMskmywYOb75agbLAaCQdjpI81GQ7DJ27S1oiMzlApDkyh7GPpf79bUWW-KL7407PdAGLuJxCYAVN0yXtfMMZoeJxUZwGZ2gWLnXl4J1k_X2G2XDeDsIFZnPG16taBebzAc9LsgU9bnaYW2Wwtr4THLg7IuGJpfhCTgMmgSdcdgzhI7ArkHvTXDB6BI8nOZ9bUHrINcsAXYwwqpZeGTXXok3rUr7ssTnxk772iiu8__K3y6oe2SLv8wLI3A-Ob74a31_HRdBtBpwZxQJtoj52CjOA2WnSHiLy8Ww-eiHNe9l2G4JI0-NlYV_IsAnNvK9d5R9K-ZOJqGwYN-MTN3JbvpqEqmEDJqI0VocNcENEjEGAmb59bTwT90qQ-sNsD5tMrlJCynUQdunPCHZUviN8Ak_L7vj-LHCGUpqjXndaoXwDjyqDgpu03NE0ZjhXduAO3EFX_ZJrbvDIrYAolv6mfKTg_oIgPAf9sFvE6NUjBBr-6rVpnM1g_h7s2WcFp50UWa55DbeANSOtummEcqgC411oXwzxRQ2qrUl4FXIIQmB1RhQsff8ARcNeq7cQOvfHe_Dix4SXjgeLeDU3Jli4WLv_fZrQ77d7OS6QfzKomb8Mn0kPJxEUx0x2cSI3iGkc2VTZb-v2JrSzPMKfYty2gLgCNASnm_tp7CssZ0CRbofkddeBmwnx7i6yxNfpM-6mBhgM9ydxoN6Wyiu8rm7k2ppTNsc',
    'ai_session': 'FUZDt|1557409659964|1557409716167.575',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://myoperator.keka.com/',
    'Origin': 'https://myoperator.keka.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    'origin': 'https://myoperator.keka.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'x-requested-with': 'XMLHttpRequest',
    'request-id': '|yn7bD.YkS/1',
    'request-context': 'appId=cid-v1:aecd77d6-a75f-425d-8560-ec8cb839064c',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://myoperator.keka.com/',
    'authority': 'myoperator.keka.com',
    'Sdk-Context': 'appId',
    'Content-type': 'application/json',
}

params = (
    ('latlng', '28.650389399999995,77.2002633'),
    ('key', 'AIzaSyBjMHjIjlGlKEWP1eVri2xxs7-juzdOVQA'),
)

data = '{"actualTimestamp":"2019-05-09T13:49:12.534Z","adjustedTimestamp":null,"originalPunchStatus":1,"modifiedPunchStatus":1,"punchStatus":1,"attendanceLogSource":1,"premiseId":0,"premiseName":null,"pairSubSequentLogs":false,"locationAddress":{"longitude":77.2002633,"latitude":28.650389399999995,"zip":"110005","countryCode":"IN","state":"Delhi","city":"Central Delhi","addressLine1":"16/525, Faiz Road","addressLine2":"Block A, Karol Bagh"},"ipAddress":"","manualClockinType":1,"isAdjusted":false,"isDeleted":false,"timestamp":"2019-05-09T13:49:12.534Z","isEditable":false,"isManuallyAdded":false}&[{"time":"2019-05-09T13:49:13.547Z","iKey":"52f1e3fb-9a00-4d6c-9dd6-01bcc0f68ec5","name":"Microsoft.ApplicationInsights.52f1e3fb9a004d6c9dd601bcc0f68ec5.RemoteDependency","tags":{"ai.session.id":"FUZDt","ai.device.id":"browser","ai.device.type":"Browser","ai.internal.sdkVersion":"javascript:1.0.20","ai.user.id":"5EK2L","ai.operation.id":"yn7bD","ai.operation.name":"/"},"data":{"baseType":"RemoteDependencyData","baseData":{"id":"|yn7bD.WpcCo","ver":2,"name":"GET /maps/api/geocode/json","resultCode":"200","duration":"00:00:00.045","success":true,"data":"GET https://maps.googleapis.com/maps/api/geocode/json?latlng=28.650389399999995,77.2002633&key=AIzaSyBjMHjIjlGlKEWP1eVri2xxs7-juzdOVQA","target":"maps.googleapis.com","type":"Ajax"}}},{"time":"2019-05-09T13:49:13.702Z","iKey":"52f1e3fb-9a00-4d6c-9dd6-01bcc0f68ec5","name":"Microsoft.ApplicationInsights.52f1e3fb9a004d6c9dd601bcc0f68ec5.RemoteDependency","tags":{"ai.session.id":"FUZDt","ai.device.id":"browser","ai.device.type":"Browser","ai.internal.sdkVersion":"javascript:1.0.20","ai.user.id":"5EK2L","ai.operation.id":"yn7bD","ai.operation.name":"/"},"data":{"baseType":"RemoteDependencyData","baseData":{"id":"|yn7bD.75ikR","ver":2,"name":"POST /api/mytime/attendance/webclockin","resultCode":"200","duration":"00:00:00.130","success":true,"data":"POST api/mytime/attendance/webclockin","target":"myoperator.keka.com | cid-v1:aecd77d6-a75f-425d-8560-ec8cb839064c","type":"Ajax"}}},{"time":"2019-05-09T13:49:13.833Z","iKey":"52f1e3fb-9a00-4d6c-9dd6-01bcc0f68ec5","name":"Microsoft.ApplicationInsights.52f1e3fb9a004d6c9dd601bcc0f68ec5.RemoteDependency","tags":{"ai.session.id":"FUZDt","ai.device.id":"browser","ai.device.type":"Browser","ai.internal.sdkVersion":"javascript:1.0.20","ai.user.id":"5EK2L","ai.operation.id":"yn7bD","ai.operation.name":"/"},"data":{"baseType":"RemoteDependencyData","baseData":{"id":"|yn7bD.YkS/1","ver":2,"name":"GET /api/mytime/attendance/attendancedayrequests","resultCode":"200","duration":"00:00:00.101","success":true,"data":"GET api/mytime/attendance/attendancedayrequests","target":"myoperator.keka.com | cid-v1:aecd77d6-a75f-425d-8560-ec8cb839064c","type":"Ajax"}}}]'

response = requests.post('https://maps.googleapis.com/maps/api/geocode/json', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://maps.googleapis.com/maps/api/geocode/json?latlng=28.650389399999995,77.2002633&key=AIzaSyBjMHjIjlGlKEWP1eVri2xxs7-juzdOVQA', headers=headers, cookies=cookies, data=data)
