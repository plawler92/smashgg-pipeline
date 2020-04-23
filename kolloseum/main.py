import configparser
import json

import requests

from dataclasses import Event

config = configparser.ConfigParser()
config.read('config.ini')
smash_token = config['smash.gg']['token']
smash_url = config['smash.gg']['url']

query = """query {
    tournament(slug: "the-kolosseum-1"){
        id
        name
        events {
            id
            name
        }
    }
}"""

def exec_query(query, variables):
    headers = {
        'X-Source': 'smashggpy',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(smash_token)
    }
    payload = {
        'query': query,
        'variables': json.dumps(variables)
    }
    return requests.post(smash_url, headers=headers, json=payload)

def get_event_info(event_slug):
    variables = {
        'slug': event_slug
    }
    query = """query EventQuery($slug: String){
        event(slug: $slug){
            id
            name
            numEntrants
            entrantSizeMin
            entrantSizeMax
        }
    }"""
    return exec_query(query, variables)

def get_event_entrants(event_slug, page, perPage):
    variables = {
        'slug': event_slug,
        'page': page,
        'perPage': perPage
    }
    query = """query EventQuery($slug: String, $page: Int, $perPage: Int){
        event(slug: $slug){
            id
            name
            numEntrants
            entrantSizeMax
            entrantSizeMin
            entrants(query: {
                page: $page
                perPage: $perPage
            }){
                nodes{
                    id
                    name
                    participants{
                        id
                        gamerTag
                        email
                    }
                }
            }
        }
    }"""
    return exec_query(query, variables)

event_slug = 'tournament/the-kolosseum-1/event/the-kolosseum-week-1'
#r = get_event_info('tournament/the-kolosseum-1/event/the-kolosseum-week-1')
r = get_event_entrants(event_slug, 1, 3)
e = Event(r.json()['data']['event'])