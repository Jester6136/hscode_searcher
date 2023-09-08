from ..utils.utils import TariffDatabase,ImExTariff
import pandas as pd
import json

data = pd.read_json('data/output.jsonl',lines=True)

tariff_db = TariffDatabase()
for index, row in data.iterrows():
    tariff = ImExTariff(
        row["_hscode"],
        row["_fatherhscode"],
        row["mota"],
        row["mota_xin"],
        row["deep"]
    )
    tariff_db.add_tariff(tariff)

# Get related tariffs by fatherhscode
related_tariffs = tariff_db.get_related_tariffs("FATHER112")
for tariff in related_tariffs:
    tariff.display()