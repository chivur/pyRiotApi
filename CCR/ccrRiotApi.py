import requests
import time

api_key = "RGAPI-75966C38-D2B1-4E8A-AF05-BDB617631C74"
id = "33485411"
region = "eune"
name = 'jocasuna'
platformID = "EUN1"

BLUE_TEAM = "blue"
BLUE_TEAM_ID = 100
BLUE_TEAM_IDX = 0
PURPLE_TEAM = "purple"
PURPLE_TEAM_ID = 200
PURPLE_TEAM_IDX = 1

#######################################
#   request summoner by name
#   GET /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
#######################################
def requestSummonerDataByName(summonerName):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + api_key
    response = requests.get(URL)
    return response.json()

def getSummonerID(summonerName,jsonData):
    return jsonData[summonerName]['id']

def getSummonerLevel(summonerName,jsonData):
    return jsonData[summonerName]['summonerLevel']

def getSummonerName(summonerName,jsonData):
    return jsonData[summonerName]['name']

#######################################
#   usage example:
#
#   getSummonerID('name',requestSummonerDataByName('name'))
#
#######################################
#   end request summoner by name
#######################################



#######################################
#   request matchlist (predefined SEASON2016)
#   optional : begin_time, end_time <TODO>
#   GET /api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}}
#######################################
def requestMatchList(summonerID):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.2/matchlist/by-summoner/" + summonerID + "?seasons=SEASON2016" +"&api_key=" + api_key
    response = requests.get(URL)
    return response.json()
    
def getAllMatchIDs(jsonData):
    ids = []
    for i in range(0,len(jsonData['matches'])):
        ids.append(jsonData['matches'][i]['matchId'])
    return ids
    
def getLastMatchIDs(jsonData,noMatches):
    ids = []
    for i in range(0,noMatches):
        ids.append(jsonData['matches'][i]['matchId'])
    return ids
    
def getNoMatches(jsonData):
    return jsonData['totalGames']
    
    
#######################################
#   usage example:
#
#   getLastMatchIDs(requestMatchList(id),5) - matchIDs for the last 5 games   
#
#######################################
#   end request matchlist
#######################################


#######################################
#   request challenger league information
#   GET /api/lol/{region}/v2.5/league/challenger
#######################################

def getChallengerLeague():
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/challenger?type=RANKED_SOLO_5x5&api_key=" + api_key 
    response = requests.get(URL)
    return response.json()
    
def getChallengerPlayerIDs(jsonData):
    ids = []
    for i in range(0,len(jsonData['entries'])):
        ids.append(jsonData['entries'][i]['playerOrTeamId'])
    return ids


#######################################
#   usage example:
#
#   getChallengerPlayerIDs(getChallengerLeague())
#
#######################################
#   end challenger league information
#######################################



#######################################
#   request match information
#   GET /api/lol/{region}/v2.2/match/{matchId}
#######################################

def getMatchInfo(matchID):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.2/match/" + matchID +"?includeTimeline=yes&api_key=" + api_key
    response = requests.get(URL)
    return response.json()
    
    
def getMatchParticipantID(jsonData,summonerName):
    for i in range(0,len(jsonData['participantIdentities'])):
        if jsonData['participantIdentities'][i]['player']['summonerName'] == summonerName:
            return i
			
def getParticipantKDA(jsonData,participantID):
    kda=[] #kda[0] = k, etc
    kda.append(jsonData['participants'][participantID]['stats']['kills'])
    kda.append(jsonData['participants'][participantID]['stats']['deaths'])
    kda.append(jsonData['participants'][participantID]['stats']['assists'])
    return kda
    
def getWardsPlaced(jsonData,participantID):
    return jsonData['participants'][participantID]['stats']['wardsPlaced']
    
def getParticipantLane(jsonData,participantID):
    return jsonData['participants'][participantID]['timeline']['lane']
    
#only works if match lasted >30m - so 'thirtyToEnd' exists
def getParticipantCSDiffPerMin(jsonData,participantID):
    csDiff=[] #csDiff[0] = csDiff @ 10; [1] @[10-20]; [2] @[20-30], [3] @[30-end]
    csDiff.append(jsonData['participants'][participantID]['timeline']['csDiffPerMinDeltas']['zeroToTen'])
    csDiff.append(jsonData['participants'][participantID]['timeline']['csDiffPerMinDeltas']['tenToTwenty'])
    csDiff.append(jsonData['participants'][participantID]['timeline']['csDiffPerMinDeltas']['twentyToThirty'])
    csDiff.append(jsonData['participants'][participantID]['timeline']['csDiffPerMinDeltas']['thirtyToEnd'])
    return csDiff

#only works if match lasted >30m - so 'thirtyToEnd' exists
def getParticipantCreepsPerMin(jsonData,participantID):
    creeps=[] #creeps[0] = creeps @ 10; [1] @[10-20]; [2] @[20-30], [3] @[30-end]
    creeps.append(jsonData['participants'][participantID]['timeline']['creepsPerMinDeltas']['zeroToTen'])
    creeps.append(jsonData['participants'][participantID]['timeline']['creepsPerMinDeltas']['tenToTwenty'])
    creeps.append(jsonData['participants'][participantID]['timeline']['creepsPerMinDeltas']['twentyToThirty'])
    creeps.append(jsonData['participants'][participantID]['timeline']['creepsPerMinDeltas']['thirtyToEnd'])
    return creeps
        
#only works if match lasted >30m - so 'thirtyToEnd' exists
def getParticipantXPDiffPerMin(jsonData,participantID):
    xpDiff=[] #xpDiff[0] = xpDiff @ 10; [1] @[10-20]; [2] @[20-30], [3] @[30-end]
    xpDiff.append(jsonData['participants'][participantID]['timeline']['xpDiffPerMinDeltas']['zeroToTen'])
    xpDiff.append(jsonData['participants'][participantID]['timeline']['xpDiffPerMinDeltas']['tenToTwenty'])
    xpDiff.append(jsonData['participants'][participantID]['timeline']['xpDiffPerMinDeltas']['twentyToThirty'])
    xpDiff.append(jsonData['participants'][participantID]['timeline']['xpDiffPerMinDeltas']['thirtyToEnd'])
    return xpDiff
        
def getParticipantChampionID(jsonData,participantID):
    return jsonData['participants'][participantID]['championId']

def getParticipantDivision(jsonData,participantID):
    return jsonData['participants'][participantID]['highestAchievedSeasonTier']
    
def getParticipantsNames(jsonData):
    names=[]
    for i in range(0,len(jsonData['participantIdentities'])):
        names.append(jsonData['participantIdentities'][i]['player']['summonerName'])
    return names
	
def getParticipantsIds(jsonData):
    ids=[]
    for i in range(0,len(jsonData['participantIdentities'])):
        ids.append(jsonData['participantIdentities'][i]['player']['summonerId'])
    return ids
    
def getBlueBaronKills(jsonData):
    return jsonData['teams'][BLUE_TEAM_IDX]['baronKills']
    
def getPurpleBaronKills(jsonData):
    return jsonData['teams'][PURPLE_TEAM_IDX]['baronKills']
    
def getTeamFirstBlood(jsonData,strTrue):
    if jsonData['teams'][BLUE_TEAM_IDX]['firstBlood'] == strTrue:
        return BLUE_TEAM
    if jsonData['teams'][PURPLE_TEAM_IDX]['firstBlood'] == strTrue:
        return PURPLE_TEAM
    
#######################################
#   usage example:
#
#   strName = getSummonerName(name,requestSummonerDataByName(name))
#   getMatchParticipantID(getMatchInfo(id),strName)
#
#######################################
#   end match information
#######################################


#######################################
#   request current match information
#   platformID = EUN1 default - eune server
#   GET  /observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}
#######################################
def getCurrentMatchInfo(summonerID):
    URL = "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + platformID + "/" + summonerID + "?api_key=" + api_key
    response = requests.get(URL)
    return response.json()

def getCurrentMatchParticipantIDs(jsonData):
    participantIDs = []
    for i in range(0,len(jsonData['participants'])):
        participantIDs.append(jsonData['participants'][i]['summonerId'])
    return participantIDs

def getCurrentMatchParticipantNames(jsonData):
    participantNames = []
    for i in range(0,len(jsonData['participants'])):
        participantNames.append(jsonData['participants'][i]['summonerName'])
    return participantNames

def getCurrentMatchParticipantChampions(jsonData):
    participantChampions = []
    for i in range(0,len(jsonData['participants'])):
        participantChampions.append(jsonData['participants'][i]['championId'])
    return participantChampions


#######################################
#   usage example:
#
#   getCurrentMatchParticipantIDs(getCurrentMatchInfo(id))
#
#######################################
#   end match information
#######################################
    
def app():
    ###
    # IDEA
    #
    #
    #    1 - getCurrentMatchParticipantIDs
    #    2 - getLastMatchIDs of current participants
    #    3 - get necesary info from last X matches of specific participant (eg. enemy laner, whole enemy team, etc)
    #
    #    info example:
    #    cs diff @10,20,30+ from last 10 matches
    #    cs diff @10,20,30+ from last 10 matches playing the same role as in current game
    #    cs diff @10,20,30+ from last 5 matches 
    #    cs diff @10,20,30+ from last 5 matches playing same role
    #    cs diff @10,20,30+ from last 5 matches playing same champion
    #
    #    OBS: role info not available for current game - take it as INPUT
    #    champion played AVAILABLE for current game - ggetCurrentMatchParticipantChampions
    #
    ###
    print "aa"#delete this after implementing app()    
    
def main():
    #strTrue = getMatchInfo("1482668510")['teams'][PURPLE_TEAM_IDX]['firstBlood'] #"true" string
    str = getSummonerName(name,requestSummonerDataByName(name))
    #print getMatchParticipantID(getMatchInfo("1482668510"),str)
    #print getParticipants(getMatchInfo("1482668510"))
    #print getPurpleBaronKills(getMatchInfo("1482668510"))
    #print getBlueBaronKills(getMatchInfo("1482668510"))
    
    #print getCurrentMatchInfo(id)['participants']
    #req_id = getCurrentMatchParticipantIDs(getCurrentMatchInfo(id))[0]
    #print req_id
    #print getCurrentMatchParticipantNames(getCurrentMatchInfo(id))
    
    last_ids =  getLastMatchIDs(requestMatchList(id),5)
    
    match_info = getMatchInfo(`last_ids[2]`)
    summ_name = getSummonerName(name,requestSummonerDataByName(name))
    print summ_name
    
    part_id = getMatchParticipantID(match_info,summ_name)
    
    print part_id
    print getParticipantChampionID(match_info,part_id)

    print "________"
    time.sleep(10)
    print getParticipantKDA(match_info,part_id)
    print getWardsPlaced(match_info,part_id)
    print getParticipantLane(match_info,part_id)
    print getParticipantCSDiffPerMin(match_info,part_id)
    print getParticipantCreepsPerMin(match_info,part_id)
    time.sleep(10)
    print getParticipantXPDiffPerMin(match_info,part_id)
    print getParticipantDivision(match_info,part_id)
    print getParticipantsNames(match_info)

    
#     challengerPlayers = getChallengerPlayerIDs(getChallengerLeague())
#     matchIDs = []
#     firstBloods = []
#     for i in range(0,1):
#         matchIDs = getAllMatchIDs(requestMatchList(challengerPlayers[i]))
#         time.sleep(10)
#         for j in range(0,len(matchIDs)-1):
#             firstBloods.append(getTeamFirstBlood(getMatchInfo(`matchIDs[j]`),strTrue))
#             print firstBloods[-1]
#             if j%4==0:
#                 time.sleep(10)
#     print firstBloods
    
#entry point
if __name__ == "__main__":
    main() #<-- for testing purposes, comment it after implementing app()
    #app()  <-- insert this after implementing it