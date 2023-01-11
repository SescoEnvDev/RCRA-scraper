#!/usr/bin/python

import json
import logging
import math
import os

import requests
from progressbar import progressbar

OUTPUT_DIR = "tables"
BASE_URL = "https://data.epa.gov/efservice"
SDWIS_TABLES = [
    "water_system",
    "water_system_facility",
    "treatment",
    "geographic_area",
    "service_area",
]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def send_request(url: str) -> requests.Response:
    try:
        response = requests.get(url)
    except Exception:
        raise
    if not response.ok:
        raise Exception(f"Request returned code <{response.status_code}>")
    return response


def scrape_sdwis() -> None:
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    for idx, table in enumerate(SDWIS_TABLES):
        url = f"{BASE_URL}/{table}"
        num_records = json.loads(send_request(f"{url}/COUNT/JSON").content)[0][
            "TOTALQUERYRESULTS"
        ]
        logger.info(
            f"({idx}/{len(SDWIS_TABLES)}) Pulling {num_records} records for table {table}",
        )
        start_row = 0
        end_row = 10000 - 1
        filename = f"{table}.csv"
        output_file = os.path.join(OUTPUT_DIR, filename)
        with open(output_file, "w", encoding="utf8") as f:
            for chunk in progressbar(range(math.ceil(num_records / 10000))):
                content = send_request(f"{url}/rows/{start_row}:{end_row}/CSV").text
                if start_row == 0:
                    f.write(content)
                else:
                    rows = content.split("\n")
                    for idx, row in enumerate(rows):
                        if idx == 0:
                            continue
                        elif idx == len(rows) - 1:
                            f.write(f"{row}")
                        else:
                            f.write(f"{row}\n")
                start_row = end_row + 1
                end_row = end_row + 10000


if __name__ == "__main__":
    scrape_sdwis()
