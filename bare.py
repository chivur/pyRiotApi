import requests
import time

api_key = "RGAPI-75966C38-D2B1-4E8A-AF05-BDB617631C74";
id = "33485411";
region = "eune"
name = 'jocasuna';

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
    for i in range(1,len(jsonData['matches'])):
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
    for i in range(1,len(jsonData['entries'])):
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
    
def getParticipants(jsonData):
    names=[]
    for i in range(0,len(jsonData['participantIdentities'])):
        names.append(jsonData['participantIdentities'][i]['player']['summonerName'])
    return names
    
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
    
def main():
    strTrue = getMatchInfo("1482668510")['teams'][PURPLE_TEAM_IDX]['firstBlood'] #"true"
    str = getSummonerName(name,requestSummonerDataByName(name))
    #print getMatchParticipantID(getMatchInfo("1482668510"),str)
    #print getParticipants(getMatchInfo("1482668510"))
    #print getPurpleBaronKills(getMatchInfo("1482668510"))
    #print getBlueBaronKills(getMatchInfo("1482668510"))
    
    
    print getTeamFirstBlood(getMatchInfo("1482668510"),strTrue)
    
    challengerPlayers = getChallengerPlayerIDs(getChallengerLeague())
    matchIDs = []
    firstBloods = []
    for i in range(0,1):
        matchIDs = getAllMatchIDs(requestMatchList(challengerPlayers[i]))
        for j in range(0,len(matchIDs)-1):
            firstBloods.append(getTeamFirstBlood(getMatchInfo(`matchIDs[j]`),strTrue))
            
            
    print firstBloods
    
#entry point
if __name__ == "__main__":
    main()