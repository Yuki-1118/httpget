import requests

# Webサイトの情報を取得する
def HttpGet(url):
    print('Http Get at {0}'.format(url))
    res =  requests.get(url)
    print('Http Get :{0}'.format(res.status_code))
    return res.text