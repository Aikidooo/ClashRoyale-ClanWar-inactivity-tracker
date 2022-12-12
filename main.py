import urllib.request
import json

def get_my_clan_only(raw, clanname):
    my_clan = []

    for cwar in raw["items"]:
        for cclan in cwar["standings"]:
            if cclan["clan"]["name"]  == clanname:
                log = cclan
                log["warDate"] = cwar["createdDate"]
                my_clan.append(log)
                break
    return my_clan


def get_inactive_members_since(my_clan, since_wars: int, currentmembers):
    all_time_inactives = []

    if since_wars > 10:
        raise Exception("Maximum backview is 10. Please type in a valid numer!")
    participants = []
    war_inactives = []

    #loop through wars and break when last requested war was scanned
    for index, war in enumerate(my_clan):
        if index == since_wars:
            break
        #loop through participants
        for i in range(len(war["clan"]["participants"])):
            #extract inactive members
            if war["clan"]["participants"][i]["fame"] <= 400 and war["clan"]["participants"][i]["repairPoints"] <= 300:
                player = {"name":war["clan"]["participants"][i]["name"], 
                        "fame": war["clan"]["participants"][i]["fame"], 
                        "repairPoints": war["clan"]["participants"][i]["repairPoints"]}

                participants.append(player)
        #append inactives to war dependend list
        war_inactives.append(participants)
        participants = [] #reset inactives for next war

    
    names_only = []
    #extract all names from all lists
    for i in war_inactives:
        for j in i:
            names_only.append(j["name"])

    all_time_inactives_names = []
    #loop through all inactives in first war
    for member in war_inactives[0]:
        #if name of current member loop occurs in every war add to all_time_inactives_names
        if names_only.count(member["name"]) == since_wars and member["name"] in currentmembers: 
            all_time_inactives_names.append(member["name"])
    
    tmp_war_inactives = []
    #loop through all members and if the name equals an inactive add to tmp_war_inactives
    for war in war_inactives:
        for member in war:
            if member["name"] in all_time_inactives_names:
                tmp_war_inactives.append(member)
        #append tmp_war_inactives to the final list
        all_time_inactives.append(tmp_war_inactives)
        tmp_war_inactives = []

    #write it to the file
    with open("inactives.json", "w") as p:
            json.dump(all_time_inactives, p, indent=2)
    
    return all_time_inactives



with open("token.txt") as token:
    WAR_BACKVIEW = int(input("War Backview: "))
    CLANTAG = "%23YGY8G8VC" #don't paste '#' sign, instead use '%23'
    CLANNAME = "Honor"

    my_token = token.read().rstrip("\n")

    #base_url = "https://proxy.royaleapi.dev/v1"
    base_url = "https://api.clashroyale.com/v1"

    appending_warlog = "/clans/" + CLANTAG + "/riverracelog?limit=5"
    appending_clanmembers = "/clans/" + CLANTAG + "/members"

    #prepare request the data from url
    request_warlog = urllib.request.Request(
        base_url + appending_warlog,
        None,
        {
            "Authorization": "Bearer %s" %my_token #sending the token for authorization
        }
    )
    request_clanmembers = urllib.request.Request(
        base_url + appending_clanmembers,
        None,
        {
            "Authorization": "Bearer %s" %my_token #sending the token for authorization
        }
    )


    #request
    response_warlog = urllib.request.urlopen(request_warlog).read().decode("utf-8")
    response_clanmembers = urllib.request.urlopen(request_clanmembers).read().decode("utf-8")


    content_raw = json.loads(response_warlog) #raw answer of api
    my_clan = get_my_clan_only(content_raw, CLANNAME) #extract my clan
    print(json.dumps(get_inactive_members_since(my_clan, WAR_BACKVIEW, response_clanmembers), indent=2)) #extract inactive members from my clan
    
    



