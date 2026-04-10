"""Jewish prayer times via HebCal Zmanim API."""
import httpx
from datetime import date

# city -> either {"geonameid": id} or {"lat","lng","tzid"}
CITIES = {
    "Jerusalem": {"geonameid": 281184},
    "Tel Aviv": {"geonameid": 293397},
    "New York": {"geonameid": 5128581},
    "Moscow": {"geonameid": 524901},
    "London": {"geonameid": 2643743},
    "Berlin": {"geonameid": 2950159},
    "Paris": {"geonameid": 2988507},
    "Los Angeles": {"geonameid": 5368361},
    "Kazan": {"lat": 55.7887, "lng": 49.1221, "tzid": "Europe/Moscow"},
    "Innopolis": {"lat": 55.7520, "lng": 48.7440, "tzid": "Europe/Moscow"},
}


async def fetch_zmanim(city: str, for_date: str | None = None) -> dict:
    """Fetch prayer times for a given city from HebCal."""
    if city not in CITIES:
        city = "Jerusalem"

    loc = CITIES[city]
    if for_date is None:
        for_date = date.today().isoformat()

    params = {"cfg": "json", "date": for_date}
    if "geonameid" in loc:
        params["geonameid"] = loc["geonameid"]
    else:
        params["latitude"] = loc["lat"]
        params["longitude"] = loc["lng"]
        params["tzid"] = loc["tzid"]

    url = "https://www.hebcal.com/zmanim"
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(url, params=params)
        r.raise_for_status()
        data = r.json()

    times = data.get("times", {})

    def fmt(iso: str | None) -> str | None:
        if not iso:
            return None
        try:
            return iso.split("T")[1][:5]
        except (IndexError, AttributeError):
            return None

    return {
        "city": city,
        "date": for_date,
        "shacharit": fmt(times.get("sofZmanTfilla") or times.get("sunrise")),
        "mincha": fmt(times.get("minchaGedola")),
        "maariv": fmt(times.get("tzeit7083deg") or times.get("sunset")),
        "sunrise": fmt(times.get("sunrise")),
        "sunset": fmt(times.get("sunset")),
    }


def list_cities() -> list[str]:
    return sorted(CITIES.keys())
