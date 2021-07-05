# Modern Muckraker IHOP Episode Data

## Setup

Assuming `python` is Python 3.x
```bash
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

## Run

### Scraper

Collect a list of all IHOP locations in a JSON Lines (`.jl`) format.
```bash
scrapy runspider ihop_scraper.py -O ihop_list.jl
```
