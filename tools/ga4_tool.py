import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Dimension, Metric
)
from dotenv import load_dotenv

load_dotenv()

def get_ga4_report(metrics_list, dimensions_list, date_start="7daysAgo", date_end="today"):

    client = BetaAnalyticsDataClient()
    property_id = os.getenv("GA4_PROPERTY_ID")

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name=d) for d in dimensions_list],
        metrics=[Metric(name=m) for m in metrics_list],
        date_ranges=[DateRange(start_date=date_start, end_date=date_end)],
    )
    
    response = client.run_report(request)
    return response