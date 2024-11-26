from .models import User, Address

class JSONPlaceholderTestData:
    EXPECTED_USER_COUNT = 10
    
    EXPECTED_USER_3 = User(
        id=3,
        name='Clementine Bauch',
        username='Samantha',
        email='Nathan@yesenia.net',
        address=Address(
            street='Douglas Extension',
            suite='Suite 847',
            city='McKenziehaven',
            zipcode='59590-4157',
            geo={'lat': -68.6102, 'lng': -47.0653}
        ),
        phone='1-463-123-4447',
        website='ramiro.info',
        company={
            'name': 'Romaguera-Jacobson',
            'catchPhrase': 'Face to face bifurcated interface',
            'bs': 'e-enable strategic applications'
        }
    )

    @staticmethod
    def get_expected_user_keys():
        return ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']

    @staticmethod
    def get_expected_address_keys():
        return ['street', 'suite', 'city', 'zipcode', 'geo'] 