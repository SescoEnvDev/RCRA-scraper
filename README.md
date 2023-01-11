# sdwis-scraper

[![Docker](https://github.com/geocoug/sdwis-scraper/workflows/docker%20build/badge.svg)](https://github.com/geocoug/sdwis-scraper/actions/workflows/docker-build.yml)

This script pulls [SDWIS data tables](https://www.epa.gov/enviro/sdwis-model) from the [EPA Envirofacts RESTful API](https://www.epa.gov/enviro/web-services). Data are saved in CSV format. Note that a single API query can only return up to 10,000 records.

The following tables are queried:

- `water_system`
- `water_system_facility`
- `treatment`
- `service_area`
- `geographic_area`

## Usage

```sh
docker run -it --rm -v $(pwd):/usr/local/app $(docker build -q -t sdwis_scraper .)
```
