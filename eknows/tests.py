from django.test import TestCase
from .models import CustomerInformation
from eknows.views import MainPage

class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'mainpage.html')

    def test_save_post_request(self):
        response = self.client.post('/', {
            'first_name':'Angel', 
            'surname':'Diaday',
            'location': 'Cavite',
            'number': 639691428480})
        self.assertEqual(CustomerInformation.objects.count(), 1)
        newCustomerInfo = CustomerInformation.objects.first()
        self.assertEqual(newCustomerInfo.first_name, 'Angel')
        self.assertEqual(newCustomerInfo.last_name, 'Diaday')
        self.assertEqual(newCustomerInfo.location, 'Cavite')
        self.assertEqual(newCustomerInfo.phone, 639691428480)

    def test_redirect_POST(self):
        response = self.client.post('/', {
            'first_name':'Angel', 
            'surname':'Diaday',
            'location': 'Cavite',
            'number': 639691428480})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_if_necessary(self):
        self.client.get('/')
        self.assertEqual(CustomerInformation.objects.count(), 0)

    # def test_responding_POST_request(self):
    #     resp = self.client.post('/', data={'name':'Angel','surname':'Diaday', 'location':'Dasmarinas,Cavite', 'number': '09691428480', 'date': '04--22-2022', 'time': '03:00', 
    #         'checkbox_disaster1': 'Earthquake', 'checkbox_disaster4': 'Landslide', 'checkbox_disaster5': 'Tsunami', 'victim': '8', 'checkbox_equipment1': 'Ambulance', 'checkbox_equipment2': 'Crane', 'checkbox_equipment3': 'Rescueboats'})
    #     self.assertIn('name', resp.content.decode())
    #     self.assertTemplateUsed(resp,'mainpage.html')

class ORMTEST(TestCase):
    def test_saving_retriving(self):
        sampleCustomerInfo = CustomerInformation()
        sampleCustomerInfo.first_name = 'Angel'
        sampleCustomerInfo.last_name = 'Diaday'
        sampleCustomerInfo.location = 'Cavite'
        sampleCustomerInfo.phone = 639691428480
        sampleCustomerInfo.save()

        lists = CustomerInformation.objects.all()
        self.assertEqual(lists.count(), 1)

        lists1 = lists[0]
        self.assertEqual(lists1.first_name, 'Angel')
        self.assertEqual(lists1.last_name, 'Diaday')
        self.assertEqual(lists1.location, 'Cavite')
        self.assertEqual(lists1.phone, 639691428480)

    def test_template_display_list(self):
        CustomerInformation.objects.create(
            first_name= 'Angel',
            last_name= 'Diaday',
            location= 'Cavite',
            phone= 639691428480)
        response = self.client.get('/')
        self.assertIn('1: Diaday, Angel, Cavite, 639691428480', response.content.decode())
