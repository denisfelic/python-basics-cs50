teams = [
    {"name": "Palmeiras", "year": 2018},
    {"name": "Flamengo", "year": 2019},
    {"name": "Corinthians", "year": 2017},
]

def sort_by_name(values):
    return values['name']

print(teams)
# teams.sort(key=sort_by_name)
teams.sort(key= lambda team: team["name"])
print(teams)