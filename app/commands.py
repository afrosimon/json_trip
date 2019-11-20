import json
import click
from app import app, db
from app.models import Destination


@app.cli.command("generate_json")
def generate_json():
    dests = Destination.query.all()
    json_res = []

    with open("./destination.json", "w") as output_file:
        for d in dests:
            obj = {
                'city_name': d.city_name,
                'country_name': d.country_name,
                'latitude': str(d.latitude),
                'longitude': str(d.longitude),
                'arrival_date': str(d.arrival_date),
                'departure_date': str(d.departure_date)
            }

            json_res.append(obj)

        output_file.write(json.dumps(json_res))

    print(f'Wrote {len(json_res)} destinations to ./destination.json')
