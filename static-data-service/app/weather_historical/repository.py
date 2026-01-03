from app.shared.db.mongo import db
from datetime import datetime, timezone

historical_weather = db["historical_weather"]