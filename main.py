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

