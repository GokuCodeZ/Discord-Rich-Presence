import pypresence
import time

rpc = pypresence.Presence("BOT ID") # BOT ID
rpc.connect()
rpc.update(state="GoKu on top bxby", details="https://feds.lol/GokuCodeZ", large_image="lol", start=time.time(), buttons=[{
    "label": "lol", "url": "https://feds.lol/GokuCodeZ"
}])
print("started..")

while True:
    time.sleep(60)
