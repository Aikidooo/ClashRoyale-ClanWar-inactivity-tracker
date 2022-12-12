# ClanWar inactivity tracker for ClashRoyale Clans

This is a simple Python script which will give you the members of your ClashRoyale clan that have been inactive in War for a given amount of Wars.

It uses the ClashRoyale API and has some pre-settings made that you will have to change before the script adapts to you.

## Usage

First you will need to sign up for the [ClashRoyale API](https://developer.clashroyale.com/#/register). It is free and needed to get access to it from your current IP-Adress.

After you created an account, sign in and go to My account, which is found in the dropdown menu under your Name.


Click `Create new Key` and enter a name and a description. Then click `Add IP Adress` and enter your devices IP, which you can find easily when you search for something like `How to find my IP?` in google.

Click `Create Key` and then click on your new Key where you need to copy the full token. 
Clone the repository and paste it into token.txt. Do not share this token.

Now open main.py in your favorite editor and locate the variables in caps. 
There you have to paste your Clans tag and the name of it which you can find [here](https://royaleapi.com/clans) via the search function.

You can optionally modify the `LIMIT` variable which represents the maximum amount of Wars that will be downloaded, and the`TOLERATION` variable which represents how many points a clan member must minimally have to not appear in the list of inactive people.

After all these steps you can now run the script and the output will be shown in the console and saved to the inactives.json file. 