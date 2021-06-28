import argparse
import json
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def main(in_file, out_file):
    # The Nominatim Usage Policy requests to keep the request slower:
    #   No heavy uses (an absolute maximum of 1 request per second).
    # https://operations.osmfoundation.org/policies/nominatim/
    geolocator = Nominatim(user_agent="ihop_geocode")
    rate_limited_geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    with open(in_file, 'r') as in_file:
        with open(out_file, 'w') as out_file:
            for line in in_file:
                ihop = json.loads(line)

                try:
                    location = rate_limited_geocode(query=ihop['address'], country_codes='us')
                except geopy.exc.GeocoderTimedOut:
                    location = None

                if location is None:
                    ihop['coordinates'] = None
                else:
                    ihop['coordinates'] = (location.latitude, location.longitude)

                json.dump(ihop, out_file)
                out_file.write("\n")
                print(ihop)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='JSON Line input file of addresses', nargs=1)
    parser.add_argument('--output', help='JSON Line output file with lat/lon', nargs=1)
    args = parser.parse_args()
    main(args.input[0], args.output[0])
