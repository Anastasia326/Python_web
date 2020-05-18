from django.test import TestCase
from .get import get_something
from .models import City
from .forms import CityForm

class TestSite(TestCase):
    def test_all(self):
        appid = '60762f39833d5027ecddd7ce126a7ee6'
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
        req = {'csrfmiddlewaretoken': ['isoskVblkFvpdhlxddWx0vRqavf24ckj4WKEAojmozZ3wnk17Px41GW8EDlUv4vB'],
 'name': 'Saint Petersburg', 'send': ['Find']}
        form = CityForm(req)
        form.save()
        context = get_something(url, form)
        self.assertEqual(context['all_info'][0]['city'], 'Saint Petersburg' )
