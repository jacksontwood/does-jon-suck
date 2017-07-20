from RiotAPI import RiotAPI
import ctypes

def main():
    counter = 0
    #api key goes here
    api = RiotAPI('{key}')
    r = api.get_summoner_by_name('Luxclusive')
    #print r
    ml = api.get_matchlist_by_id(r['accountId'])
    #print ml
    matches = []
    for match in ml['matches']:
        matches.append(match['gameId'])
    #print matches
    pi = 0
    for match in matches:
        m = api.get_match_by_id(match)
        for p in m['participantIdentities']:
            if p['player']['currentAccountId'] == r['accountId']:
                pi = p['participantId']
                break
        pi -= 1
        if m['participants'][pi]['stats']['win'] == False:
            counter += 1

    if counter == 0:
        message = "Jon did not suck."
    elif counter in range(1, 5):
        message = "Jon sucked a little."
    elif counter == 5:
        message = "Eh."
    elif counter in range(6, 8):
        message = "Jon did a fair amount of sucking."
    elif counter in range(8, 10):
        message = "Jon sucked quite a lot."
    else:
        message = "Jon should start a gay porn company because of how much he's sucking."

    retval = "Luxclusive lost " + str(counter) + "/10 of his last 10 ranked games.\n" + message
    ctypes.windll.user32.MessageBoxA(0, retval, "Did Jon Suck?", 1)

if __name__ == "__main__":
    main()
