import requests

"""
單純發送 Line Notify 文字訊息
"""
def send(token, msg):

    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    params = {'message': msg}
    response = requests.post(url, headers = headers, params = params)
    return response.status_code