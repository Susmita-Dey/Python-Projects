# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url and returns a response

import urllib.request as urllib


def main(url):
    print("Checking connectivity in progress...")
    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully.")
    print("The response status code is:", response.getcode())


print("This is a site connectivity checker program\n")
input_url = input("Input the url of the site you want to check:")

main(input_url)
