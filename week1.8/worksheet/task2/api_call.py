
import httpx

base_url = "https://dummyjson.com/"

#content = "posts/1"
content = "products/search?q=phone"
content = "recipe/meal-type/snack"

content="posts/5"


url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)
print(len(content))
