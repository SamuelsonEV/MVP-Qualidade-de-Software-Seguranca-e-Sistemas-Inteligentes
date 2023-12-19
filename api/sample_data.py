import requests
import random

api_url = 'http://localhost:5000'

arrozs = [[14198.0,485.90301513671875,205.10435485839844,89.31971740722656,0.9001963138580322,14414.0,0.5658377408981323,22],
[10984.0,421.9599914550781,170.8734893798828,83.75952911376953,0.8716187477111816,11201.0,0.69554203748703,22],
[14734.0,498.7070007324219,211.00096130371094,90.11148071289062,0.9042201638221741,15171.0,0.7845998406410217,22],
[12188.0,435.8609924316406,182.0326690673828,85.78117370605469,0.8820047378540039,12363.0,0.7657703161239624,22],
[12022.0,431.2309875488281,176.25048828125,87.95137786865234,0.8665941953659058,12205.0,0.7853410243988037,22],
[13970.0,481.8840026855469,201.4725799560547,89.4972152709961,0.8959200382232666,14310.0,0.5678861737251282,22],
[11296.0,424.70098876953125,169.20689392089844,87.00450134277344,0.8576762676239014,11626.0,0.6110239624977112,22],
[14534.0,483.6409912109375,196.65081787109375,95.0506820678711,0.8754285573959351,14932.0,0.6496513485908508,22],
[11245.0,421.5480041503906,174.5754852294922,82.91380310058594,0.8800153136253357,11475.0,0.6819284558296204,22],
[15281.0,509.5169982910156,212.69688415527344,92.99383544921875,0.8993580341339111,15689.0,0.6402295827865601,22],
[13321.0,473.9930114746094,199.27256774902344,85.9288330078125,0.902250349521637,13758.0,0.5645687580108643,22],
[11626.0,433.2380065917969,178.07923889160156,84.56312561035156,0.880060076713562,11972.0,0.5896733403205872,22],
[11889.0,428.6969909667969,173.63134765625,88.43959045410156,0.8605578541755676,12113.0,0.6109455227851868,22],
[11883.0,448.21600341796875,191.74635314941406,79.46400451660156,0.91008460521698,12103.0,0.5503172278404236,22],
[14340.0,477.89599609375,196.47506713867188,94.2577896118164,0.8774083256721497,14700.0,0.6081424951553345,22],
[11955.0,454.08599853515625,196.8355255126953,78.12479400634766,0.9178601503372192,12127.0,0.5581232309341431,22],
[14011.0,493.8789978027344,212.63031005859375,85.02820587158203,0.9165642261505127,14336.0,0.6279861927032471,22]]

for arroz in arrozs:
    payload = {
                'name': 'T-'+ str(random.randint(1, 999)),
                'preg': arroz[0],
                'plas': arroz[1],
                'pres': arroz[2],
                'skin': arroz[3],
                'test': arroz[4],
                'mass': arroz[5],
                'pedi': arroz[6],
                'age': arroz[7],
                }
    response = requests.post(f"{api_url}/arroz", data=payload)

    if response.status_code == 200:
        print("adicionada com sucesso")
    elif response.status_code == 409:
        print("O mesmo título já existe !!!")
    else:
        print(f"Erro {response.status_code}: {response.text}")

print("Inserção de dados iniciais finalizada")