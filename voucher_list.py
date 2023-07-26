from create_refresh_token import generate_token
from client import LazopClient, LazopClientRequest
import lazop

def get_voucher_list(access_token):
    client = LazopClient(access_token)
    request = client.request("/promotion/vouchers/get")
    request.add_api_param("cur_page", "1")
    request.add_api_param("voucher_type", "COLLECTIBLE_VOUCHER")
    request.add_api_param("name", "null")
    request.add_api_param("page_size", "10")
    request.add_api_param("status", "null")
    response = client.execute(request)
    return response

def main():
    access_token_response = generate_token('0_100132_2DL4DV3jcU1UOT7WGI1A4rY91')  # Replace 'YOUR_AUTHORIZATION_CODE' with the actual code
    if access_token_response.type == 'error':
        print("Error while generating the access token:", access_token_response.body)
        return

    access_token = access_token_response.body['access_token']
    response = get_voucher_list(access_token)
    print(response.type)
    print(response.body)

    if response.type == 'error':
        refresh_token_response = refresh_token(access_token_response.body['refresh_token'])
        if refresh_token_response.type == 'success':
            access_token = refresh_token_response.body['access_token']
            response = get_voucher_list(access_token)
            print("Refreshed access token response:")
            print(response.type)
            print(response.body)
        else:
            print("Error refreshing the access token:", refresh_token_response.body)

if __name__ == '__main__':
    main()
