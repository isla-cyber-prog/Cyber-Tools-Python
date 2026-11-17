from urllib.parse import urlparse

url = input("Enter URL: ")

parsed = urlparse(url)

print("Scheme:", parsed.scheme)
print("Domain:", parsed.netloc)
print("Path:", parsed.path)
