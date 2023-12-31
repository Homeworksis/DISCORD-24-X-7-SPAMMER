from webserver import keep_alive
import requests

channelID = 977810977120747550/977927149489127454
headers = {
    "authorization":
    "6o8yeHhcvveOtOUxN3Fc"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
