import requests


Pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"

def get_joke(mood):
    if mood == "pj":
        jokes = requests.get(url = Pj_url)
        final_joke = jokes.json()["setup"] + " " + jokes.json()["punchline"]
        print(final_joke)
    elif mood == "dad":
        jokes = requests.get(url = dad_joke_url, headers={"Accept": "application/json"})
        final_joke = jokes.json()["joke"]
        print(final_joke)
        

mood = input("what kind of joke you want ? (pj/dad) : ")
get_joke(mood)        

