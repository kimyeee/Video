from django.test import TestCase

# Create your tests here.
import requests

res = requests.get('https://code.jquery.com/jquery-3.3.1.js')
open('jquery-3.3.1.js','wb').write(res.content)