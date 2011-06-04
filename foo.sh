wget --no-check-certificate https://www.eff.org/torchallenge/list/
grep view-content-torchallenge index.html > content
python scrape.py content
