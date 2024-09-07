import webbrowser


urls = {
    "Google": "https://www.google.com",
    "Facebook": "https://www.facebook.com",
    "Instagram": "https://www.instagram.com",
    "LinkedIn": "https://www.linkedin.com",
    "Fantasy Premier League": "https://fantasy.premierleague.com",
    "Udemy": "https://www.udemy.com",
    "Mozilla Firefox": "https://www.mozilla.org/firefox"
}



def firefox(name):
     url = urls.get(name)
     if url in urls.values():
          webbrowser.open(url)
     else : 
          print("website not found")    



