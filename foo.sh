wget --no-check-certificate https://www.eff.org/torchallenge/list/ -O index.html
#wget --no-check-certificate http://www./torchallenge/list/ -O index.html

if [ $? != 0 ]; then
    echo "\nERROR: The EFF server is currently down. Try again later"
    exit -1
fi

grep view-content-torchallenge index.html > content
python scrape.py content > prints
