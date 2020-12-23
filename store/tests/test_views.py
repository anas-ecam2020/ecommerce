from django.test import TestCase, Client
from django.urls import reverse


# TestViews tests that the response get from the server is 200
# TestViews tests that views render the exact html
class TestViews(TestCase):


    def test_store_GET(self):
        client = Client()
        response = client.get(reverse('store'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')


    def test_cart_GET(self):
        client = Client()
        response = client.get(reverse('cart'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')


    def test_checkout_GET(self):
        client = Client()
        response = client.get(reverse('checkout'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/checkout.html')