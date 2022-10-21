import sys
import requests

# import tldextract
# print(tldextract.extract('http://sangomargroup.com'))


import requests

# importing module
import requests


# function for scanning subdomains
def domain_scanner(domain_name, sub_domnames):
    print('----URL after scanning subdomains----')
    for subdomain in sub_domnames:
        url = f"https://{subdomain}.{domain_name}"
        try:
            requests.get(url)
            print(f'[+] {url}')
        except requests.ConnectionError:
            pass


# main function
if __name__ == '__main__':
    dom_name = input("Enter the Domain Name:")
    with open('subdomain_names1.txt', 'r') as file:
        name = file.read()
        sub_dom = name.splitlines()
    domain_scanner(dom_name, sub_dom)
# sangomargroup

# def sum1(n):
#     return (n * (n + 1)) / 2


# n = 10
# data = []
#
# for i in range(n):
#     a = len(data)
#     b = sys.getsizeof(data)
#     print('Length: {0:3d}; Size in bytes: {1:4d} '. format(a, b))
#     data.append(n)

# from turtle import *
# speed(10)
# color('cyan')
# bgcolor('black')
# b = 200
# while b > 0:
#     left(b)
#     forward(b * 3)
#     b = b - 1

import requests

url = "https://backend.ums.eaa.sn/api/v1/accounts"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjU3pDb3Q3ekkxc3MxNmdib29uTkplSTg4WTlBNl8weXE3dzFqdzBvSmxjIn0.eyJleHAiOjE2NjYzNTkzMjMsImlhdCI6MTY2NjM1OTAyMywiYXV0aF90aW1lIjoxNjY2MzU5MDIxLCJqdGkiOiI2MGI2MzEyMi1iOTBmLTQ4N2UtODJiNy01MjNkOGY4N2M2NTYiLCJpc3MiOiJodHRwczovL2F1dGguZWFhLnNuOjg0NDMvYXV0aC9yZWFsbXMvZWFhIiwiYXVkIjpbImNsaV91bXMiLCJhY2NvdW50Il0sInN1YiI6IjEzYjgyNzlhLWUxZDYtNDFhZi05ZTFiLTEzYTI0MjgzODk1OSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaV91bXNfZnJvbnQiLCJub25jZSI6IjcxZTU4MjRiLWM0ZWItNDdmYy05ODhhLTA3MzQxODM1NDJiOSIsInNlc3Npb25fc3RhdGUiOiI4OWQ2MWU4MS1mODIzLTRlZmEtOTk5OS03ZmZlOWQ2OTk4ZjQiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZWFhIiwidW1zX2FjY291bnRfYWRtaW4iLCJ1bXNfYWNjb3VudF9vd25lciIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJjbGlfdW1zIjp7InJvbGVzIjpbImNsaV91bXNfYWNjb3VudF9vd25lciIsImNsaV91bXNfYWNjb3VudF92aWV3ZXIiLCJjbGlfdW1zX2FjY291bnRfYWRtaW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiI4OWQ2MWU4MS1mODIzLTRlZmEtOTk5OS03ZmZlOWQ2OTk4ZjQiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJUaGlvcm8gVGhpYW0iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0aGlvcm8iLCJnaXZlbl9uYW1lIjoiVGhpb3JvIiwibG9jYWxlIjoiZnIiLCJmYW1pbHlfbmFtZSI6IlRoaWFtIiwiZW1haWwiOiJ0aGlvcm8udGhpYW1Ac2FuZ29tYXJncm91cC5jb20ifQ.YASJInutaSQWkRhge9-EZeOa726h_bZKJSBhsrWKxDC_yIiSXzFMkPauM-V4rWwG5FomYY5ylPWKnDfZHkEC60ljtXyDzQojkaHYPJz05RIVD387mtpI0Jeg7cyEPMKXfmXb7k_eTwaX_t33EMDgy11MWgTXT0ilzJXc_aKKOgEihhgXnqL6ak66_DdfLWuiiiTajas1D2rMdwxj5rqcWQTpADH3VKXC6D8xxQfZa95bJad4HUYlwJcjD4Dpb_c6OaUdQe7x91mz4c0_ddG1mPkA_PujYb_B8CKNZVOrhnd_5BJm4pHcSVNdvya8N7X1Yc9nWVOaDtnnBMeN5r1fTw'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


