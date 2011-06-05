wget --no-check-certificate https://www.eff.org/torchallenge/list/ -O index.html
grep view-content-torchallenge index.html > content
python scrape.py conten > print
