# Create your views here.
import lxml
import requests
from lxml import html

# To grab the URL and convert into an lxml object ...

r = requests.get('http://www.mnd.uscourts.gov/calendars/mpls/index.html')

root = lxml.html.fromstring(r.content)
