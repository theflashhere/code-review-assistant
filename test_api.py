# test_api.py
import requests

# Read the code file
with open('sample.py', 'rb') as f:
    # Send it to your API
    response = requests.post('http://127.0.0.1:8000/review', files={'file': f})

# Print the review results
if response.status_code == 200:
    result = response.json()
    print("\n" + "="*50)
    print("CODE REVIEW RESULTS")
    print("="*50)
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)