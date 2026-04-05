
# Travel Platform Backend

A **microservices-based backend** built with **FastAPI** that aggregates static and dynamic travel-related data into a unified API. The platform is designed with clean architecture principles, Redis caching, and external API integrations, mirroring patterns used in production backend systems.

---

## Key Features

* Microservices-oriented FastAPI architecture
* Clear separation of **static data** and **dynamic data** services
* Redis caching with TTL for rate-limited APIs
* Strong domain modeling with Pydantic
* External API and web-scraped data integrations
* Dockerized for local development and deployment

---

## Architecture Overview

The backend is organized into multiple services, each responsible for a single domain. Services communicate via HTTP and share common infrastructure patterns.





---

## Static Data Services

Static data services provide **infrequently changing or historical datasets**. These services are optimized for read-heavy usage and long-lived caching.

###  Historical Weather Service

Provides long-term historical climate data for destinations.

**Responsibilities:**

* Monthly weather averages
* Historical temperature and precipitation statistics
* Precomputed datasets optimized for fast lookup

**Notes:**

* Data is stored as static datasets
* Ideal for travel planning and climate comparison

---

###  Geocodes Service

Resolves location-based metadata for destinations.

**Responsibilities:**

* Latitude / longitude lookup
* City, country, and region normalization
* Canonical destination identifiers

**Notes:**

* Acts as a foundational service for other domains
* Ensures consistent location resolution across services

---

###  Advisories Service (Playwright Scraped)

Provides travel advisories and safety-related information collected via automated web scraping.

**Responsibilities:**

* Scrape official advisory sources using **Playwright**
* Normalize and store advisory levels and descriptions
* Serve cleaned, structured advisory data via API

**Notes:**

* Scraping jobs run on a scheduled basis
* Data treated as semi-static with controlled refresh cycles

---

## Dynamic Data Services

Dynamic services provide **frequently changing, real-time or near-real-time data**. These services heavily leverage Redis caching to respect external API rate limits.

###  Weather Forecast Service

Provides short-term weather forecasts for destinations.

**Responsibilities:**

* Fetch 7-day weather forecasts from external APIs
* Align time-series data by date
* Cache responses in Redis with TTL

**Caching Strategy:**

* Lazy caching on request
* Time-based TTL to ensure freshness
* Prevents redundant external API calls

---

###  FX Rates Service

Provides foreign exchange rate data and currency conversion.

**Responsibilities:**

* Fetch base-currency FX rates from a rate-limited external API
* Convert between arbitrary currency pairs internally
* Cache FX data in Redis to minimize API usage

**Notes:**

* Designed around a single base currency to reduce call volume
* Supports deterministic and repeatable conversions

---

## Domain Modeling

* All services use **Pydantic models** for validation and serialization
* External API schemas are mapped to **internal domain models**
* Aggregated models combine static and dynamic data where appropriate

This approach ensures:

* Schema stability even if external APIs change
* Strong typing across service boundaries
* Predictable API responses

---

## Caching & Performance

* **Redis** used as a shared caching layer
* TTL values defined at the service level
* Cache keys generated in repository layers
* JSON serialization centralized to avoid duplication

Benefits:

* Reduced latency
* Significant reduction in external API calls
* Better fault tolerance when third-party APIs are unavailable



Each service will be exposed on its own port and documented via FastAPI's built-in Swagger UI.

---

## Testing (Planned / In Progress)

* Unit tests for service and repository layers
* Integration tests for API endpoints
* Mocked external API responses
* User accounts with SSO (Keycloak) to integrate with other travel apps

---

## Roadmap

* API Gateway for unified data aggregation
* Background jobs for scheduled cache refreshes
* Authentication and per-user rate limiting
* Observability (logging, metrics, tracing)

---

## Design Philosophy

This project emphasizes:

* Real-world backend patterns over monolithic design
* Explicit ownership of data domains
* Scalability through stateless services
* Clean separation of concerns

The goal is to mirror how production travel and data platforms are architected in industry.


```
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
├─ architecture.md
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
   │  │  │  ├─ advisory_review.json
   │  │  │  ├─ advisory_review_real.json
   │  │  │  ├─ CountryAdvisories.xml
   │  │  │  ├─ CountryTravelInformation.xml
   │  │  │  ├─ country_data.csv
   │  │  │  ├─ country_links - Copy.csv
   │  │  │  ├─ country_links.csv
   │  │  │  ├─ test advisory.py
   │  │  │  ├─ test info.py
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
   │  ├─ weather_historical
   │  │  ├─ client.py
   │  │  ├─ model.py
   │  │  ├─ repository.py
   │  │  ├─ routes.py
   │  │  ├─ service.py
   │  │  └─ __init__.py
   │  ├─ _deprecated_advisories
   │  └─ __init__.py
   ├─ Dockerfile
   └─ static_structure.md

```