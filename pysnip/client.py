import requests

def publish(name, password, code, author):
    r = requests.post("https://pysnip.marcusweinberger.repl.co/publish", data={
        'name':name,
        'password':password,
        'code':code,
        'author':author,
    })
    return r.json()