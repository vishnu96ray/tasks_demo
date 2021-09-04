
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample',#os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER':'root',
        'PASSWORD':'Vikash@1096',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
