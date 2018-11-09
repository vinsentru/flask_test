# Clone the repository
Go to the cloned folder

# Install the requirements:

pip install -r requirements.txt

# Run the application in the DEBUG mode:

python3 src/app.py

# Tests:

Open another terminal and run:

Standard request:

curl -X GET http://127.0.0.1:5000/

You should see `'<p>Hello, World</p>'` replay

Request with 'Accept header'

curl -X GET -H "Accept: application/json" http://127.0.0.1:5000/

You should see this replay:
{
  "message": "Good morning"
}

For unit tests run:

pytest --disable-warnings

You should see that 2 tests are passed

# To install the application run:
python setup.py install
