import requests

api_key = "RGAPI-75966C38-D2B1-4E8A-AF05-BDB617631C74";
id = "33485411";
region = "eune"
name = 'jocasuna';

#######################################
#   request summoner by name
#   GET /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
#######################################
def requestSummonerDataByName(summonerName):
    URL = "https://" + region + ".api.pvp.net/api/lol/eune/v1.4/summoner/by-name/"+summonerName+ "?api_key="+api_key;
    response = requests.get(URL)
    return response.json()

def getSummonerID(summonerName,jsonData):
    return jsonData[summonerName]['id']

def getSummonerLevel(summonerName,jsonData):
    return jsonData[summonerName]['summonerLevel']

#######################################
#   usage example:
#
#   getSummonerID('name',requestSummonerData('name'))
#
#######################################
#   end request summoner by name
#######################################

    
    
def main():
    print getSummonerLevel(name,requestSummonerDataByName(name))
    
#entry point
if __name__ == "__main__":
    main()