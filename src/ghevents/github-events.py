#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    """url input is used to convert into json text string, then returns as python objects"""
    json_text = requests.get(url).text
    return json.loads(json_text)

def print_events(events,n=5):
    """Prints the first n events given list of recent GitHub events"""
    for x in events[:n]:
            event = x['type'] + ' :: ' + x['repo']['name']
            print(event) 
def main():
    """prints GHUSER, url, and  displays github events of that user"""
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)

if __name__ == "__main__":
    main()
