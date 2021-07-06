# Modern Muckraker IHOP Episode Data

## Setup

Run the following on your command line to set up the environment for you current shell. If you start a new shell, you'll only need to run the `source env/bin/activate` command again.
```bash
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

## Run

### Scraper

Collect a list of all IHOP locations in a JSON Lines (`.jl`) format. 
```bash
scrapy runspider ihop_scraper.py -O ihop_list.jl
```

There is currently a copy of `ihop_list.jl` in this repository, so you can skip this step.

### Jupyter Notebook

View the IHOP data.
```bash
jupyter notebook ihop_notebook.ipynb
```
