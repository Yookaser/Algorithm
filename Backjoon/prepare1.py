import requests, json


headers = {
    'X-Auth-Token': '956af49225cacd4054cec28bfc962547',
    'Content-Type': 'application/json'
}
data = {"problem": 1}
BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'

response = requests.post(BASE_URL + '/start', headers=headers, data=json.dumps(data))

headers = {
    'Authorization': response.json()['auth_key'],
    'Content-Type': 'application/json'
}

response = requests.get(BASE_URL + '/locations', headers=headers)

bike = [[0] * 5 for _ in range(5)]
for dic in response.json()['locations']:
    r, c = divmod(dic['id'], 5)
    bike[r][c] = dic['located_bikes_count']

response = requests.get(BASE_URL + '/trucks', headers=headers)

truck = [[0] * 5 for _ in range(5)]
for dic in response.json()['trucks']:
    r, c = divmod(dic['loaded_bikes_count'], 5)
    truck[r][c] += 1

for _ in range(720):
    data = {'commands': []}
    response = requests.put(BASE_URL + '/simulate', headers=headers, data=json.dumps(data))

print(response.json())

response = requests.get(BASE_URL + '/score', headers=headers)
print(response.json())
