import json
employee = {1:{"name":"Sachin","DOB":"10/1/2000","Height":"5.4 Feet","City":"Gorakhpur","State":"Uttar Pradesh"},
            2:{"name":"Sammer","DOB":"27/8/2000","Height":"5.6 Feet","City":"Kanpur","State":"Uttar Pradesh"},
            3:{"name":"Prateek","DOB":"21/12/1999","Height":"5.8 Feet","City":"Noida","State":"Uttar Pradesh"},
            4:{"name":"Amit","DOB":"15/8/2000","Height":"5 Feet","City":"Delhi","State":"New Delhi"},
            5:{"name":"Aditya","DOB":"11/2/2000","Height":"6 Feet","City":"Chennai","State":"Tamilnadu"},
            6:None}
print(employee)
with open("employee.json","w") as f:
    x = json.dump(employee,f,indent=4)
    print(x)