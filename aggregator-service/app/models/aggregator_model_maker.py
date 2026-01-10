from app.models.aggregator_model import AggregatedData, TempStats
from typing import List, Dict

def make_aggregate_model(
        

) -> AggregatedData:
    return AggregatedData(

    )

def make_temp_stats(mean: float, median: float) -> TempStats:
    return TempStats(
        mean = mean,
        median = median
    )