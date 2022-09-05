# collect email from user
# split the email using the @, the first part as the user name, the second part is gonna be used as domain
# split domain using .,
# hello@codewithtomi.com
# hello
# codewithtomi.com

import email


def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Enter your email address: ")
    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


main()
