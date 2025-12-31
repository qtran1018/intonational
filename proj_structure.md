travel-platform/
├── aggregator-service/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── destination.py
│   │   ├── clients/
│   │   │   ├── static_client.py
│   │   │   └── dynamic_client.py
│   │   ├── schemas/
│   │   │   └── response.py
│   │   └── config.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── static-data-service/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── advisory.py
│   │   │   ├── geocoding.py
│   │   │   └── climate.py
│   │   ├── services/
│   │   │   ├── scrape_travel_gov.py
│   │   │   ├── geocode.py
│   │   │   └── historical_weather.py
│   │   ├── repositories/
│   │   │   └── mongo_repo.py
│   │   ├── models/
│   │   │   └── location.py
│   │   └── config.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── dynamic-data-service/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── weather.py
│   │   │   └── currency.py
│   │   ├── services/
│   │   │   ├── forecast_weather.py
│   │   │   └── exchange_rates.py
│   │   ├── cache/
│   │   │   └── redis_client.py
│   │   ├── schemas/
│   │   │   └── rates.py
│   │   └── config.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
└── infra/
    ├── docker-compose.yml
    ├── env.example
    └── README.md
