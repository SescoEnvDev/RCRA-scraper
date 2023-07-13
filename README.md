# RCRA-scraper

[![Docker](https://github.com/geocoug/sdwis-scraper/workflows/docker%20build/badge.svg)](https://github.com/geocoug/sdwis-scraper/actions/workflows/docker-build.yml)

This script pulls [RCRA data tables](https://www.epa.gov/enviro/rcra-info-model) from the [EPA Envirofacts RESTful API](https://www.epa.gov/enviro/web-services). Data are saved in CSV format. Note that a single API query can only return up to 10,000 records.

The Following modules can be queried:

- [Handler Module](https://www.epa.gov/node/238683)
  
- [Permitting Module](https://www.epa.gov/node/96229)
  
- [Corrective Action Module](https://www.epa.gov/node/238681)
    -Columns:
      `HANDLER_ID`
      `ACTIVITY_LOCATION`
      `ACTUAL_DATE`
      `AIR_RELEASE_IND`
      `AREA_FACILITYWIDE_IND`
      `AREA_HANDLER_ID`
      `AREA_NAME`
      `AREA_SEQ`
      `AUTHORITY_OWNER`
      `AUTHORITY_TYPE`
      `BEST_DATE`
      `CA_EVENT_CODE`
      `EFFECTIVE_DATE`
      `END_DATE`
      `EPA_OWNER`
      `EPA_PERSON_ID`
      `EVENT_HANDLER_ID`
      `EVENT_OWN`
      `EVENT_SEQ`
      `GROUNDWATER_RELEASE_IND`
      `HANDLER_NAME`
      `ISSUANCE_DATE`
      `OWNER`
      `PERSON_ID`
      `PERSON_OWNER`
      `REGION`
      `REGULATED_UNIT_IND`
      `REPOSITORY`
      `RESPONSIBLE_AGENCY`
      `RESPONSIBLE_PERSON`
      `RESPONSIBLE_PERSON_OWNER`
      `SCHEDULE_DATE_NEW`
      `SCHEDULE_DATE_ORIG`
      `SOIL_RELEASE_IND`
      `STATE`
      `STATE_OWNER`
      `STATE_PERSON_ID`
      `SUB_ORGANIZATION`
      `SUB_ORGANIZATION_OWNER`
      `SURFACE_WASTE_RELEASE_IND`
      `TRIBAL_ID`
      `UNIT_HANDLER_ID`
      `UNIT_SEQ`
  
- [Financial Assurance Module](https://www.epa.gov/node/238675)
    -Columns:
      `HANDLER_ID`
      `COST_ACTIVITY_LOCATION`
      `COST_FA_TYPE`
      `COST_AGENCY`
      `COST_COVERAGE_SEQ`
      `RESPONSIBLE_PERSON_OWNER`
      `RESPONSIBLE_PERSON`
      `COST_ESTIMATE_AMOUNT`
      `COST_ESTIMATE_DATE`
      `COST_ESTIMATE_REASON`
      `MECH_HANDLER_ID`
      `MECH_ACTIVITY_LOCATION`
      `MECH_AGENCY`
      `MECH_SEQ`
      `MECH_DETAIL_SEQ`
      `MECH_TYPE_OWNER`
      `MECH_TYPE`
      `PROVIDER`
      `PROVIDER_CONTACT_NAME`
      `PROVIDER_CONTACT_PHONE`
      `FACE_VALUE_AMOUNT`
      `EFFECTIVE_DATE`
      `EXPIRATION_DATE`
  
  ![image](https://github.com/SescoEnvDev/RCRA-scraper/assets/134627586/0c528d18-e80b-48a8-9785-05d8a557a924)

- [GIS Module](https://www.epa.gov/node/238679)

Each module consists of multiple tables; a list will be created here in the future, for now please reference the above links for a more detailed description.

This project is very much in its infancy; if you're reading this message, it is not currently updated to link to the correct resources. Please check back for future updates.

## Usage

```sh
docker run -it --rm -v $(pwd):/usr/local/app $(docker build -q -t rcra_scraper .)
```
