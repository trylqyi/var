FROM python:2

MAINTAINER Oraclize "Danny@bcoffee.io"

ADD coinmarketcap_basket.py /

RUN pip install coinmarketcap json time pandas

CMD [ "python", "./coinmarketcap_basket.py " ]

