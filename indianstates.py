import json
States = {1:{"Uttar Pradesh":"Lucknow"},
          2:{"Rajasthan":"Jaipur"},
          3:{"Tamilnadu":"Chennai"},
          4:{"Jharkhand":"Ranchi"},
          5:{"Assam":"Dispur"}
          ,6:{"New Delhi":"New Delhi"},
          7:{"Madhya Pradesh":"Bhopal"},
          8:None}
print(States)
with open("States.json","w") as f:
    x= json.dump(States,f,indent=4)
    print(x)    