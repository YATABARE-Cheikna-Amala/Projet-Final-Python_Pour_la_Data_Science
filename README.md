## Utilisation des données via l'API de Hugging Face

---

```python
import requests
import pandas as pd

url = "https://datasets-server.huggingface.co/rows"

all_rows = []

for offset in range(0, 1000, 100):  # adapte si dataset plus grand
    params = {
        "dataset": "Uris001/credit-risk-eda",
        "config": "default",
        "split": "train",
        "offset": offset,
        "length": 100
    }

    r = requests.get(url, params=params).json()
    
    if "rows" not in r:
        break

    all_rows.extend([row["row"] for row in r["rows"]])

df = pd.DataFrame(all_rows)

df.head()