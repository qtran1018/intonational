```
intonational
├─ .dockerignore
├─ app
│  ├─ data
│  │  ├─ country_data.csv
│  │  ├─ country_links.csv
│  │  └─ __init__.py
│  ├─ db
│  │  ├─ mongo.py
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ models
│  │  ├─ country.py
│  │  └─ __init__.py
│  ├─ repositories
│  │  ├─ country_repository.py
│  │  └─ __init__.py
│  ├─ routes
│  │  ├─ api.py
│  │  ├─ web.py
│  │  └─ __init__.py
│  ├─ services
│  │  ├─ country_factory.py
│  │  ├─ country_pipeline.py
│  │  ├─ scrape.py
│  │  └─ __init__.py
│  ├─ templates
│  │  └─ index.html
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
└─ requirements.txt

```

app/
├─ ingestion/                 # Batch, scheduled jobs
│  ├─ travel_gov/
│  │  ├─ scraper.py
│  │  ├─ parser.py
│  │  ├─ pipeline.py
│  │  └─ __init__.py
│  └─ __init__.py
│
├─ geocoding/                 # Lazy, on-demand
│  ├─ client.py               # Open-Meteo + Nominatim
│  ├─ service.py              # cache + normalize
│  ├─ repository.py
│  ├─ models.py
│  └─ __init__.py
│
├─ historical_weather/        # Lazy, on-demand
│  ├─ client.py               # Open-Meteo ERA5
│  ├─ service.py
│  ├─ repository.py
│  ├─ models.py
│  └─ __init__.py
│
├─ shared/                    # Cross-cutting concerns
│  ├─ db/
│  │  └─ mongo.py
│  ├─ rate_limiters.py
│  ├─ http.py
│  └─ __init__.py
│
├─ api/                       # FastAPI routes
│  ├─ locations.py
│  ├─ weather.py
│  ├─ countries.py
│  └─ __init__.py
│
├─ main.py
└─ __init__.py
