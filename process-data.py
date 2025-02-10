import urllib.request, json,urllib.error

def get_forces():
    force_list = []
    url = "https://data.police.uk/api/forces"
    with urllib.request.urlopen(url) as url:
        data = json.load(url)
        for item in data:
            force_list.append(item["id"])
        return force_list
            
def get_events(force):
    events = []
    url = "https://data.police.uk/api/crimes-no-location?category=all-crime&force={0}".format(force)

    with urllib.request.urlopen(url) as url:
        data = json.load(url)
        for event in data:
            events.append(event)
        return events


all_events = []
for force in get_forces():
    all_events.append (get_events(force))

#dump to stdout
print(json.dumps(all_events))