URL = {
    'base': 'https://{proxy}.api.riotgames.com/lol/{url}',
    'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
    'last_ten_ranked_by_acc': 'match/v{version}/matchlists/by-account/{accountId}',
    'match_by_id': 'match/v{version}/matches/{matchId}'
}

API_VERSIONS = {
    'summoner': '3',
    'match': '3'
}

REGIONS = {
    'north_america': 'na1'
}
