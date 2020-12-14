from . import me
import datetime


class TrackedDatesEntity(me.Document):
    meta = {
        'abstract': True,
    }

    created = me.DateTimeField()
    modified = me.DateTimeField()

    def save(self, *args, **kwargs):
        if self.id is None:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        super().save(*args, **kwargs)


class User(me.Document):
    telegram_id = me.IntField(primary_key=True)
    username = me.StringField(min_length=2, max_length=128)
    first_name = me.StringField(min_length=2, max_length=128)
    phone_number = me.StringField(max_length=12)
    email = me.EmailField()
    is_blocked = me.BooleanField(default=False)

    def formatted_data(self):
        return f'Id - {self.telegram_id}\nUsername - {self.username}\nFirst name - {self.first_name}'\
               f'\nEmail - {self.email if self.email else ""}\nPhone number - {self.phone_number}'


class Category(me.Document):
    title = me.StringField(required=True)
    description = me.StringField(max_length=512)
    parent = me.ReferenceField('self')
    subcategories = me.ListField(me.ReferenceField('self'))

    @classmethod
    def get_root_categories(cls):
        return cls.objects(parent=None)

    def get_products(self):
        return Product.objects(category=self)

    def is_root(self):
        return not bool(self.parent)

    def add_subcategory(self, category):
        category.parent = self
        category.save()
        self.subcategories.append(category)
        self.save()


class Parameters(me.EmbeddedDocument):
    height = me.FloatField()
    width = me.FloatField()
    weight = me.FloatField()
    additional_description = me.StringField()


class Product(me.Document):
    title = me.StringField(required=True, max_length=256)
    description = me.StringField(max_length=512)
    in_stock = me.BooleanField(default=True)
    discount = me.IntField(min_value=0, max_value=100, default=0)
    price = me.FloatField(required=True)
    image = me.FileField()
    category = me.ReferenceField(Category, required=True)
    parameters = me.EmbeddedDocumentField(Parameters)

    #file = open('apole.jpeg','rb')
    #product.image.put(file, content_type='image/jpeg')
    #product.save()

    def formatted_data(self):
        if self.parameters:
            params = "\n"
            if self.parameters.height:
                params = params + 'Height - ' + str(self.parameters.height)
            if self.parameters.width:
                if params != '\n':
                    params = params + ' '
                params = params + 'Width - ' + str(self.parameters.width)
            if self.parameters.weight:
                if params != '\n':
                    params = params + ' '
                params = params + 'Weight - ' + str(self.parameters.weight)
            if self.parameters.additional_description:
                if params != '\n':
                    params = params + ' '
                params = params + str(self.parameters.additional_description)
        else:
            params = ""
        return f'{self.title}{" (" + self.description + ")" if self.description else ""}. Price: {str(self.price)}'\
               f'{params}'


class ProductInCart(me.EmbeddedDocument):
    product = me.ReferenceField(Product, required=True)
    amount = me.IntField(default=1)
    actual_price = me.FloatField(required=True)


class Cart(me.Document):
    user = me.ReferenceField(User, required=True)
    product_in_cart = me.ListField(ProductInCart, required=True)


class Order(me.Document):
    # user = me.ReferenceField(User, required=True)
    # product_ordered = me.ListField(ProductInCart, required=True)
    cart = me.ReferenceField(Cart, required=True)
    ordered_at = me.DateTimeField(default=datetime.datetime.now())
    delivery_address = me.StringField(min_length=2, max_length=256)

