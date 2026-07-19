import random
import string

def generate_email(total_length=255, subdomain="@dontwannacry.com", domain=""):
    if total_length <= len(subdomain):
        raise ValueError("total_length must be greater than the length of subdomain")

    random_characters = string.ascii_letters + string.digits
    prefix_length = total_length - len(subdomain)
    prefix = ''.join(random.choices(random_characters, k=prefix_length))

    return prefix + subdomain + '.' + domain

if __name__ == "__main__":
    user_input = input("Enter email domain: ")
    email = generate_email(domain=user_input)
    print(email)
    