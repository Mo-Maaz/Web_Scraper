from flask import Flask, request, jsonify
import requests
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, start_http_server
from flask.wrappers import Response

app = Flask(__name__)

# Create a Prometheus counter for HTTP GET requests
http_get_counter = Counter('http_get', 'Number of HTTP GET requests', ['url', 'code'])

@app.route('/', methods=['POST'])
def scrape_url():
    # Parse JSON data from the request
    data = request.json
    url = data.get('url')

    if not url:
        # Return a bad request response if URL is not provided
        return jsonify({'error': 'URL is required'}), 400

    # Make HTTP GET request to the provided URL
    try:
        response = requests.get(url)
        status_code = response.status_code
    except requests.RequestException as e:
        # Print the exception for debugging
        print(f"Request to {url} failed: {e}")
        # Handle request exceptions (e.g., connection error)
        status_code = 500

    # Increment Prometheus counter for HTTP GET requests
    http_get_counter.labels(url=url, code=str(status_code)).inc()

    # Construct the response with URL and status code
    response = {'url': url, 'status_code': status_code}

    return jsonify(response)

@app.route('/metrics')
def metrics():
    """
    Expose Prometheus metrics.
    """
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    # Start Prometheus metrics server on port 9095
    start_http_server(9095)

    # Start Flask app on port 8080
    app.run(host='0.0.0.0', port=8080)
