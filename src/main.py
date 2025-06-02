import argparse
import logging
from src.service.scraper import Scraper
from src.util.const import WAIT

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--postcode",
        help="The postcode to search for the bin collection for",
        required=True,
    )
    parser.add_argument(
        "-a",
        "--address",
        help="Your house number or name of your address",
        required=True,
    )
    parser.add_argument(
        "-w",
        "--wait",
        help="How long to wait whilst bin collections is loading your collections",
        default=WAIT,
    )
    parser.add_argument("-d", "--debug", help="Toggles on debug logging", default=DEBUG)
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    scraper = Scraper(args.postcode, args.address, args.wait)
    result = scraper.scrape()

    print("Bin Collections: " + str(result))
