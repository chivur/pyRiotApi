from cassiopeia import riotapi
from cassiopeia.type.core.common import EventType

#if __name__ == "main":

riotapi.set_region("eune")
riotapi.set_api_key("RGAPI-75966C38-D2B1-4E8A-AF05-BDB617631C74")

summoner = riotapi.get_summoner_by_name("JoC Asuna")
print("{name} is a level {level} summoner on the EUNE server.".format(name=summoner.name, level=summoner.level))

challenger_league = riotapi.get_challenger() #for player:challenger_league -> player.name

timestamps = []
player_names = []

#for every player
for player in challenger_league:
    #match_list = player.match_list()
    match_list = summoner.match_list() #replace this line with the upper modified 
    #for every match of the last 2
    for match_idx in range(1,2):
        match_ref = match_list[-match_idx]
        match = match_ref.match()
        #for every frame
        if match is not None:
            for frame in match.timeline.frames:
                for event in frame:
                    if event.type == EventType.building_kill:
                        time = frame.timestamp #minute when first tower went down
                        #player = event.creator.summoner_name #who took the tower down
                        timestamps.append(time)
                        print time
                        #player_names.append(player)
                        break;#we want only FIRST tower timestamp

i=1
for t in timestamps:
    print("(name) took first tower @ (time)".format(name="p",time=t))
    i=i+1