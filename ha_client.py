import urequests

from config import TOKEN
from config import HA_IP
from config import HA_PORT

URL = (
    "http://%s:%d/api/conversation/process"
    % (HA_IP, HA_PORT)
)

HEADERS = {
    "Authorization":
        "Bearer " + TOKEN,
    "Content-Type":
        "application/json"
}

def ask(text):

    payload = {
        "text": text
    }

    r = urequests.post(
        URL,
        json=payload,
        headers=HEADERS
    )

    data = r.json()

    r.close()

    try:
        return data["response"]["speech"]["plain"]["speech"]
    except:
        return "Viga"