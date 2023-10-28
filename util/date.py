from datetime import datetime, date, time


def response_dates(response):
    data = response.json()
    if "AcsEvent" not in data:
        return []

    info_list = data["AcsEvent"].get("InfoList", [])
    filtered_data = [info for info in info_list if len(info.keys()) == 14]

    return filtered_data


def datetime_to_iso8601(datetime_object):
    return datetime_object.isoformat(timespec="seconds")


today = date.today()
start_time = f"{datetime_to_iso8601(datetime.combine(today, time.min))}+05:00"
end_time = f"{datetime_to_iso8601(datetime.combine(today, time.max))}+05:00"
