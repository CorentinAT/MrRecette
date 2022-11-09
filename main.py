import requests

webhook = "https://discord.com/api/webhooks/1039873910302310463/5dRCWhSTc4snYlHGL4twNhWEUQcrb2tUOTMXFwvcKbppwzdpZaG6afDVfy_dGs_7V-Jm"
url="http://cumometer.games"
r = requests.get(url, allow_redirects=True)

message = {
    "content" : "test"
}

requests.post(webhook, json=message)