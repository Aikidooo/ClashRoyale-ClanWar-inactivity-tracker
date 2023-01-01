import urllib.request
import json


CLANTAG = "" #don't paste '#' sign, instead use '%23', for example "%23YGY8G8VC"
CLANNAME = "" #For example "MyWonderfulClan"
LIMIT = 5
TOLERATION = 400

def get_my_clan_only(raw, clan_name):
    my_clan = []

    for cwar in raw["items"]:
        for cclan in cwar["standings"]:
            if cclan["clan"]["name"]  == clan_name:
                log = cclan
                log["warDate"] = cwar["createdDate"]
                my_clan.append(log)
                break
    return my_clan


def get_inactive_members_since(my_clan, since_wars, currentmembers):
    all_time_inactives = []

    if since_wars > 10:
        raise Exception("Maximum backview is 10. Please type in a valid numer!")
    participants = []
    war_inactives = []
    
    for index, war in enumerate(my_clan):# loop through wars and break when last requested war was scanned
        if index == since_wars:
            break
        
        for i in range(len(war["clan"]["participants"])):
            #extract inactive members
            if war["clan"]["participants"][i]["fame"] <= TOLERATION and war["clan"]["participants"][i]["repairPoints"] <= TOLERATION:
                player = {"name":war["clan"]["participants"][i]["name"], 
                        "fame": war["clan"]["participants"][i]["fame"], 
                        "repairPoints": war["clan"]["participants"][i]["repairPoints"]}
                participants.append(player)

        #append inactives to war dependend list
        war_inactives.append(participants)
        participants = [] #reset inactives for next war
    
    names_only = [[j["name"] for j in i] for i in war_inactives] #extract all names from all lists

    all_time_inactives_names = []
    for member in war_inactives[0]:# loop through all inactives in first war
        # if name of current member loop occurs in every war add to all_time_inactives_names
        if names_only.count(member["name"]) == since_wars and member["name"] in currentmembers: 
            all_time_inactives_names.append(member["name"])
    
    tmp_war_inactives = []
    # loop through all members and if the name equals an inactive add to tmp_war_inactives
    for war in war_inactives:
        for member in war:
            if member["name"] in all_time_inactives_names:
                tmp_war_inactives.append(member)
        #append tmp_war_inactives to the final list
        all_time_inactives.append(tmp_war_inactives)
        tmp_war_inactives = []

    with open("inactives.json", "w") as f:
            json.dump(all_time_inactives, f, indent=2)

    return all_time_inactives


def get_auth(token_file="token.txt"): # create http header with token fauth field
    with open(token_file, "r") as tokenf:
        token = tokenf.read().rstrip("\n")
    auth = {
            "Authorization": "Bearer " + token
        }
    return auth



if __name__ == "__main__":
    war_backview = int(input("War Backview: "))

    base_url = "https://api.clashroyale.com/v1" # "https://proxy.royaleapi.dev/v1"
    warlog_path = "/clans/" + CLANTAG + "/riverracelog?limit=" + str(LIMIT)
    clanmembers_path = "/clans/" + CLANTAG + "/members"
    auth = get_auth()
    request_warlog = urllib.request.Request(
        base_url + warlog_path,
        None,
        auth
    )
    request_clanmembers = urllib.request.Request(
        base_url + clanmembers_path,
        None,
        auth
    )

    # request
    response_warlog = urllib.request.urlopen(request_warlog).read().decode("utf-8")
    response_clanmembers = urllib.request.urlopen(request_clanmembers).read().decode("utf-8")

    content_raw = json.loads(response_warlog)
    my_clan = get_my_clan_only(content_raw, CLANNAME) #extract my clan

    inactive_members = get_inactive_members_since(my_clan, war_backview, response_clanmembers)
    print(inactive_members)