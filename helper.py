import constants
import requests

def get_access_token():
    base_response = requests.get(constants.BASE_URL_PET+'/animals', headers={'Authorization' : 'Bearer '+constants.ACCESS_TOKEN_PET}).json()
    if base_response.get("title", '') == 'Unauthorized':
        print("You need a new token.")
        data = {'grant_type': 'client_credentials', 'client_id': constants.API_KEY_PET, 'client_secret': constants.SECRET_PET }
        response = requests.post(constants.BASE_URL_PET+'oauth2/token', data=data).json()
        constants.ACCESS_TOKEN_PET = response["access_token"]
    else:
        print("Token is still valid.")