import requests

# https://stackoverflow.com/questions/12601316/how-to-make-python-requests-work-via-socks-proxy
# pip install pysocks

proxies = {
    'http': 'socks5h://72.210.208.101:4145',
    'https': 'socks5h://72.210.208.101:4145',
}

session = requests.Session()
session.proxies.update(proxies)

res = session.get('http://ident.me/', timeout=300)

print(res.text)
