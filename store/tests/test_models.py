from django.test import TestCase
from store.models import Customer, Product, Order, OrderItem, ShippingAddress
import time


class TestModels(TestCase):
    
    def test_product_imageURL(self):

        self.product1 = Product.objects.create(
            name='product 1',
            price= 100,
            digital= True,
            image = ''
        )

        self.assertEquals(self.product1.image, '')


    def test_orderitem_get_cart_total(self):
        
        self.customer1 = Customer.objects.create(
            name= 'test',
            email= 'test@gmail.com',
        )

        self.product1 = Product.objects.create(
            name='product 1',
            price= 100,
            digital= True,
            image = ''
        )

        self.order1 = Order.objects.create(
            customer= self.customer1,
            date_ordered= time.time(),
            complete= True,
            transaction_id='12345',
        )

        self.orderitem1 = OrderItem.objects.create(
            product= self.product1,
            order= self.order1,
            quantity= 5,
            date_added=time.time(),
        )

        self.assertEquals(self.orderitem1.quantity * self.product1.price, 500)
