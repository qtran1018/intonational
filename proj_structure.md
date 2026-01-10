intonational
├─ .dockerignore
├─ aggregator-service
│  └─ app
│     ├─ api
│     │  ├─ v1
│     │  │  ├─ routes.py
│     │  │  └─ __init__.py
│     │  └─ __init__.py
│     ├─ clients
│     │  ├─ dynamic_client.py
│     │  └─ static_client.py
│     ├─ main.py
│     ├─ models
│     │  ├─ aggregator_model.py
│     │  └─ aggregator_model_maker.py
│     ├─ repository
│     │  └─ repository.py
│     ├─ routes
│     │  └─ routes.py
│     ├─ services
│     │  └─ aggregator_service.py
│     └─ shared
│        ├─ http.py
│        ├─ redis
│        │  ├─ connection.py
│        │  ├─ redis_repository.py
│        │  └─ __init__.py
│        └─ utils
│           ├─ cache_keygen.py
│           └─ wmo_converter.py
├─ docker-compose.yml
├─ dynamic-data-service
│  ├─ app
│  │  ├─ api
│  │  │  ├─ v1
│  │  │  │  ├─ routes.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ config.py
│  │  ├─ fx_rates
│  │  │  ├─ client.py
│  │  │  ├─ model.py
│  │  │  ├─ model_maker.py
│  │  │  ├─ repository.py
│  │  │  ├─ routes.py
│  │  │  ├─ service.py
│  │  │  └─ __init__.py
│  │  ├─ main.py
│  │  ├─ shared
│  │  │  ├─ http.py
│  │  │  ├─ redis
│  │  │  │  ├─ connection.py
│  │  │  │  ├─ redis_repository.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ utils
│  │  │  │  └─ cache_keygen.py
│  │  │  └─ __init__.py
│  │  ├─ weather_forecast
│  │  │  ├─ client.py
│  │  │  ├─ model.py
│  │  │  ├─ model_maker.py
│  │  │  ├─ repository.py
│  │  │  ├─ routes.py
│  │  │  ├─ service.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  └─ Dockerfile
├─ proj_structure.md
├─ README.md
├─ requirements.txt
└─ static-data-service
   ├─ app
   │  ├─ advisories
   │  │  ├─ data
   │  │  │  ├─ country_data.csv
   │  │  │  ├─ country_links.csv
   │  │  │  └─ __init__.py
   │  │  ├─ model.py
   │  │  ├─ model_maker.py
   │  │  ├─ repository.py
   │  │  ├─ routes.py
   │  │  ├─ run_scrape.py
   │  │  ├─ scrape.py
   │  │  ├─ service.py
   │  │  └─ __init__.py
   │  ├─ api
   │  │  ├─ v1
   │  │  │  ├─ routes.py
   │  │  │  └─ __init__.py
   │  │  └─ __init__.py
   │  ├─ geocoding
   │  │  ├─ client.py
   │  │  ├─ model.py
   │  │  ├─ model_maker.py
   │  │  ├─ repository.py
   │  │  ├─ routes.py
   │  │  ├─ service.py
   │  │  └─ __init__.py
   │  ├─ main.py
   │  ├─ shared
   │  │  ├─ db
   │  │  │  ├─ mongo.py
   │  │  │  └─ __init__.py
   │  │  ├─ http.py
   │  │  └─ __init__.py
   │  ├─ tests
   │  │  ├─ geocoding
   │  │  │  ├─ test_repository.py
   │  │  │  └─ test_service.py
   │  │  └─ weather_historical
   │  ├─ weather_historical
   │  │  ├─ client.py
   │  │  ├─ model.py
   │  │  ├─ model_maker.py
   │  │  ├─ repository.py
   │  │  ├─ routes.py
   │  │  ├─ service.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ Dockerfile
   └─ static_structure.md
