import os
SECRET_KEY = os.environ.get('SECRET_KEY', None)
if SECRET_KEY and len(SECRET_KEY)>1:
    print('Success')