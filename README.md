# ClanWar inactivity tracker for ClashRoyale Clans

This is a simple Python script which will give you the members of your ClashRoyale clan that have been inactive in ClanWar for a given amount of Wars.

It uses the ClashRoyale API and has some pre-settings made that you will have to change before the script adapts to you and your clan.

## Usage

First you will need to sign up for the [ClashRoyale API](https://developer.clashroyale.com/#/register). It is free and required to get access to it from your current IP-Adress.

After you created an account, sign in and go to 'My account', which is found in the dropdown menu under your Name.


Click `Create new Key` and enter a name and a description. Then click `Add IP Adress` and enter your devices IP, which you can find easily [here](https://whatismyipaddress.com), [here](https://www.whatismyip.com), via [google](https://www.google.com/search?q=what+is+my+ip) or any other way you like.

Click `Create Key` and then click on your new Key in the now appearing overview, where you need to copy the full token. 
Clone the repository and paste the token into `token.txt`. Do not share this token.

Now open main.py in your favorite editor and locate a bunch of constant variables in caps. 
There you have to paste your clan's tag and the name of it which you can find at [royaleAPI](https://royaleapi.com/clans) via the search function or directly from your phone when you look at the clan overview.

You can optionally modify the `LIMIT` variable which represents the maximum amount of Wars that will be downloaded, and the `TOLERATION` variable which represents what minimum of points a clan member should have to not appear in the list of inactive people.

After all these steps you can now run the script and the output will be shown in the console and saved to the inactives.json file. 

Please note that your IP-Adress can change, which will result in a 403 forbidden error when requesting the API, since it only allows access for the IP you specified when creating your token. If this is the case just follow the steps above again and create a new key with your new IP-Adress. If this is too annoying for you you'll have to set up a static IP or use a proxy. In case you don't know how to do this, remember google is your best friend.


###### This is pretty bad code, please don't blame me for it, I am no professional and never really learned Python since I casually code most of my programs in Java. I thought this was a useful tool and as long as it works it should be shared. 
