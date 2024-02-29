import random
import string

def generate_random_string():
    prefix = "https://discord.com/gift/"
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return prefix + suffix

# Generate the random string
random_string = generate_random_string()
print("Generated Nitro Gift:", random_string)