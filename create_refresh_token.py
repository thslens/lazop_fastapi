from setup import lazop

from client import LazopClient

def generate_token(code):
  client = lazop.LazopClient()
  request = lazop.LazopRequest("/auth/token/create")
  request.add_api_param("code", code)
  request.add_api_param("uuid", "This field is currently invalid, do not use this field please")
  response = client.execute(request)
  return response

def main():
  access_token_response = generate_token('0_100132_2DL4DV3jcU1UOT7WGI1A4rY91')  # Replace 'YOUR_AUTHORIZATION_CODE' with the actual code
  if access_token_response.type == 'error':
    print("Error while generating the access token:", access_token_response.body)
    return

  print(access_token_response.type)
  print(access_token_response.body)

if __name__ == '__main__':
  main()










"""from client import LazopClient, LazopClientRequest

def generate_token(code):
  request = LazopClientRequest("/auth/token/create")
  request.add_api_param("code", code)
  response = client.execute(request)
  return response

def refresh_token(refresh_token):
  client = LazopClient()
  request = LazopClientRequest(client, "/auth/token/refresh")
  request.add_api_param("refresh_token", refresh_token)
  response = client.execute(request)
  return response"""