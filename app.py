from flask import Flask
from flask import jsonify

app = Flask(__name__)

# load list into memory
f = open("email-providers.csv", "r")
providers = {}

for line in f:
    domain = line.rstrip()
    if domain in providers:
        providers[domain] += 1
    else:
        providers[domain] = 1

@app.route('/')
def listProviders():
    return jsonify(providers.keys())

@app.route('/<emailaddress>')
def check(emailaddress):
    providerToCheck = emailaddress
    domainIdx = providerToCheck.find('@')
    if domainIdx >= 0:
        providerToCheck = providerToCheck[domainIdx + 1:]
    
    if providerToCheck not in providers:
        return ('', 404)
    else:
        return ('', 200)
