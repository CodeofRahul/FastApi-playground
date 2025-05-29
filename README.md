# FastApi-playground
A FastAPI lab for prototyping ideas, testing features, and deepening API knowledge.

![Fastapi 8](https://github.com/user-attachments/assets/cf28c33f-eba2-4562-a1f8-ce02e09c1afa)

![Fastapi 7](https://github.com/user-attachments/assets/de5730b6-9fbe-4f2d-a061-c5eba6731f1d)

![Fastapi 6](https://github.com/user-attachments/assets/574a192d-2d68-4a30-af85-d6817e5bdf43)

![Fastapi 5](https://github.com/user-attachments/assets/08d4b9ec-d6ff-43ea-86cb-dd7061c71e3e)

![Fastapi 4](https://github.com/user-attachments/assets/380c1b44-e4ca-4c5e-af6d-47009bbad433)

![Fastapi 3](https://github.com/user-attachments/assets/21a25096-17e5-4288-b238-8dfe5c542ca2)

![Fastapi 2](https://github.com/user-attachments/assets/65a5d86e-b424-4d42-a9c8-154176f7fab9)

![Fastapi 1](https://github.com/user-attachments/assets/5bf32338-a69c-48b3-b597-fd32351ead8e)

## Why FastAPI is fast to code?

1. Automatic input Validation <br>
2. Auto-Generated interactive Documentation <br>
3. Seamless Integration with Modern Ecosystem (ML/DL libraries, OAuth, JWT, SQL Alchemy, Docker, Kubernetes etc) 

#### Run the Server:

```bash
uvicorn main:app --reload
fastapi dev main.py
```


## **HTTP Requests:**

## Real-world analogy:

GET is like reading a book in a library.
Post is like writing a note and handing it to the librarian.

-	When you GET, you’re just requesting to see something
-	When you POST, you’re sending data to be processed or saved.

### Technical Difference

| Feature | GET | POST |
| -------- | ------- | ------- |
| Purpose | Retrieve data | Submit data |
| Data location | In URL (query string) | In the request body |
| Visibility | Data is visible in URL | Data is hidden from URL |
| Use for | Reading/fetching resources | Creating/updating resources |
| Bookmarkable | Yes | No |
| Idempotent | Yes (repeating gives same result) | Not necessarily (can cause changes |

### Get request:

```http
GET /search?query=shoes HTTP/1.1
```

-	You’re asking: “Hey server, show me all the shoes.”

### POST request:

```http
POST /add-to-cart HTTP/1.1
Body: { “item_id”: 123, “quantity”: 2}
```

-	You’re saying: “Hey server, please add this item to my cart.”

## Think of it like a conversation with a website:

### 1. GET = “Just give me info”

-	You’re asking the server for something.
-	Example: “Show me all blog posts tagged with ‘travel’.”
-	You don’t change anything on the server.
-	The server responds with that info.

**In the browser: **

-	You type in a URL or click a link – that’s a GET request.
-	Example: `https://example.com/posts?tag=travel`

### 2. POST = “I’m giving you something to do”

-	You’re sending data to the server to do something with it.
-	Example: “Here is my comment on this blog post.”
-	The server might save that comment to a database.

**In the browser: **

-	You fill out a form and click “Submit” – that’s a POST request.
-	Example: You post a review, submit login info, or upload a photo.

## Why does it matter?

-	GET is for viewing. (safe, can be cached, can be bookmarked.)
-	POST is for doing. (Sends new data, not cached, not bookmarkable.)

## GET Scenarios (Read-only actions)

These are situations where the client just wants to retrieve data, without making any changes:

### 1. Loading a web page

-	URL: `https://news.com/latest`
-	You want to view the latest news.
-	No data is sent except in the URL.

### 2. Search queries

-	URL: `https://store.com/search?q=laptop`
-	You are searching for laptop”.
-	The search term is passed as a query string.

### 3. Viewing a user profile

-	URL: `https://site.com/user/john`
-	Just displays John’s profile
-	Doesn’t change anything.

### 4. Pagination

-	URL: `https://blog.com/posts?page=3`
-	You’re just asking for page 3 of the blog.

### 5. Filtering results

-	URL: `https://shop.com/products?category=shoes&price=low`
-	You’re applying filters to what you see.

## POST Scenarios (Write/Submit actions)

These are situations where the client is sending data to the server to create, modify, or trigger actions.

### 1. Submitting a login form

-	URL: `https://site.com/login`
-	Sends your username and password.
-	Server checks and starts your session.

### 2. Creating a new user/account

-	URL: `https://site.com/signup`
-	Sends your name, email, password, etc.

### 3. Submitting a contact form

-	Sends message, name, email to the server to be saved or emailed.

### 4. Uploading a file or image

-	Sends the file data as part of the request body.

### 5. Adding to a shopping cart

-	You click “Add to Cart” – the item ID and quantity are sent to the server.

### 6. Placing an order

-	URL: `https://shop.com/checkout`
-	Sends the cart items, payment detail, shipping info.

### 7. Posting a comment or message

-	Submits text, maybe with a post ID or thread ID.


## Summary Table:

| Scenario | Method |
| --- |--- |
| View a blog post | GET |
| Search for a products | GET |
| Login to a site | POST |
| Sign up for a new account | POST |
| Add an item to cart | POST |
| Submit a contact form | POST |
| View a list of product | GET |
| Filter products by price | GET |
| Post a review | GET |
| Get weather info by city | GET |
| Upload a profile picture | POST |
| View user profile | GET |

## GET Request on Flipkart (Viewing or fetching data)

These happen when you’re just browsing or searching without changing anything on the server.

### 1. Homepage Load

-	When you go to `https://www.flipkart.com`, your browser sends a GET request.
-	You’re just asking to view the homepage.

### 2. Searching for a product 

-	You type “mobile phone” in the search bar and hit Enter.
-	URL becomes: `https://www.flipkart.com/search?q=mobile+phones`
-	That’s a GET request with the query `q=mobile+phones`
-	You are just requesting info.

### 3. Filtering products

-	Apply a filter like “Price: Low to High” or select a brand.
-	URL updates to something like: `https://www.flipkart.com/search?q=mobile+phones&sort=price_asc&brand=Samsung`
-	Still a GET request – just showing filtered results.

### 4. Viewing a product

-	Click on a phone to see its details.
-	URL: `https://www.flipkart.com/Samsung-galaxy/product-id`
-	Again, it’s just fetching info – so it’s a GET.

## POST Requests on Flipkart (Sending data or changing state)

These happen when you interact in a way that changes something – like logging in, adding to cart, or checking out.

### 1. Logging in

-	You enter your phone/email and password.
-	Your browser sends a POST request to `https://www.flipkart.com/api/login`
-	Flipkart checks your credentials and starts a session.

### 2. Adding a product to cart

-	You click “Add to Cart”.
-	A POST request is sent to something like: `https://www.flipkart.com/api/add-to-cart`
-	Data sent: `{ product_id: 12345, quantity: 1 }`

### 3. Placing an order

-	After selecting items, address, and payment, you click “Place Order”.
-	A POST request sends your order details to Flipkart’s servers to process.

### 4. Submitting a review

-	You rate a product and write a review.
-	Flipkart uses a POST request to store that review in their database.















## Bash Environment Commands

- To Create a file

```bash

touch <file_name>
# Example: touch Test_Excercise.py
```

- Run python (.py) file:

```bash
python file_name.py

```

- To Create a virtual environment

```bash

python -m venv <env_name>
# Example: python -m venv playground
```

- Activate the virtual environment

```bash

source <env_name>/bin/activate  # for macos
source <env_name>/Scripts/activate  # for windows
# Example for macos: source playground/bin/activate
# Example for window bash: source playground/Scripts/activate
```
- Deactivate the virtual environment

```bash

deactivate
```

- Delete the environment

```bash

rm -rf <env_name>
# Example: rm -rf playground
```

- Useful Bash Tips for Environment Management

List Python virtual environments if stored in a folder (e.g., `~/venvs`)

```bash

ls ~/venvs
```

Find all virtual environments on your system (search for `activate` scripts)

```bash

find ~ -type f -name "activate"
```

Quick script to list venv env names inside `~/venvs`

```bash

for dir in ~/venvs/*; do
  if [ -f "$dir/bin/activate" ]; then
    echo "$(basename "$dir")"
  fi
done
```

## Pip Commands

- To install requirements.txt = `pip install -r requirements.txt`
- To check install packages = `pip list`
- To check detailed about package = `pip show package_name`
- To install package = `pip install package_name`
- To uninstall package = `pip uninstall package_name`
- To save all packages of env to a requirements.txt file = `pip freeze > requirements.txt`

## Git commands

- To add all file = `git add .`
- To add any particular file = `git add <file_name>`
- To commit = `git commit -m "commit message"`
- To push the code = `git push origin main`

Docs:

- Documentation: https://fastapi.tiangolo.com
- Source Code: https://github.com/fastapi/fastapi

-  Swagger UI:

```bash
localhost:8000/docs
http://127.0.0.1:8000/docs
```

