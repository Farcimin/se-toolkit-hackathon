"""Jewish prayer times — computed locally via the `zmanim` Python library.

No external network is needed: sunrise/sunset and halachic times are
computed from latitude, longitude, and timezone for the given date.
"""
from datetime import date, datetime
import pytz
from zmanim.zmanim_calendar import ZmanimCalendar
from zmanim.util.geo_location import GeoLocation

# city -> (latitude, longitude, IANA timezone)
CITIES: dict[str, tuple[float, float, str]] = {
    "Jerusalem": (31.7683, 35.2137, "Asia/Jerusalem"),
    "Tel Aviv": (32.0853, 34.7818, "Asia/Jerusalem"),
    "New York": (40.7128, -74.0060, "America/New_York"),
    "Moscow": (55.7558, 37.6173, "Europe/Moscow"),
    "London": (51.5074, -0.1278, "Europe/London"),
    "Berlin": (52.5200, 13.4050, "Europe/Berlin"),
    "Paris": (48.8566, 2.3522, "Europe/Paris"),
    "Los Angeles": (34.0522, -118.2437, "America/Los_Angeles"),
    "Kazan": (55.7887, 49.1221, "Europe/Moscow"),
    "Innopolis": (55.7520, 48.7440, "Europe/Moscow"),
}


def _fmt(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    return dt.strftime("%H:%M")


def fetch_zmanim(city: str, for_date: str | None = None) -> dict:
    """Compute prayer times for a given city and date."""
    if city not in CITIES:
        city = "Jerusalem"

    lat, lng, tz_name = CITIES[city]
    tz = pytz.timezone(tz_name)

    if for_date is None:
        target = date.today()
    else:
        target = date.fromisoformat(for_date)

    location = GeoLocation(city, lat, lng, tz_name, elevation=0)
    cal = ZmanimCalendar(geo_location=location, date=target)

    sunrise = cal.sunrise()
    sunset = cal.sunset()
    shacharit = cal.sof_zman_tfila_gra()  # latest time for morning Amidah
    mincha = cal.mincha_gedola()
    maariv = cal.tzais()  # nightfall

    # convert UTC times to local tz for display
    def to_local(dt):
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = pytz.utc.localize(dt)
        return dt.astimezone(tz)

    return {
        "city": city,
        "date": target.isoformat(),
        "shacharit": _fmt(to_local(shacharit)),
        "mincha": _fmt(to_local(mincha)),
        "maariv": _fmt(to_local(maariv)),
        "sunrise": _fmt(to_local(sunrise)),
        "sunset": _fmt(to_local(sunset)),
    }


def list_cities() -> list[str]:
    return sorted(CITIES.keys())
