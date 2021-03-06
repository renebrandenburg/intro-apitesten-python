import requests
import json


def test_maak_reservering():
    url = "http://localhost:8080/user/reserve/1"
    payload = {"dateRange": "2021-03-11 tot 2021-03-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_terwijl_andere_user_al_heeft_geboekt():
    url = "http://localhost:8080/user/reserve/2"
    payload = {"dateRange": "2021-03-11 tot 2021-03-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == False
    print(response.text)


test_maak_reservering()
test_maak_reservering_terwijl_andere_user_al_heeft_geboekt()
