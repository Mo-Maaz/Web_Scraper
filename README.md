# Scraper Service 

The Scraper Service is a web service designed to fetch the HTTP status code of a given URL and expose Prometheus metrics. 
This service is implemented using Python and Flask, and it can be run as a standalone service or within a Docker container.

## Setup and Usage 

To run the Scraper Service, you need the following dependencies:

- Python 3.x
- Docker

### Running the Service Locally 

- Extract the contents of the provided zip file to a directory on your local machine.
- Install dependencies: `pip install -r requirements.txt`
- Run the service: `python scraper_service.py`
- To stop the service, press `Ctrl + C`.

### Running the Service with Docker 

- Extract the contents of the provided zip file to a directory on your local machine.
- Build the Docker image: `docker build -t scraper_service.py .`
- Run the Docker container: `docker run -d -p 8080:8080 -p 9095:9095 scraper_service.py`
- To stop the container, use the `docker stop` command.

## Components and Functions

1. **Client (Sender of POST Requests)**
   - Sends a JSON POST request to the Scraper Service with the URL to be scraped.
   - Example: `curl -X POST -H "Content-Type: application/json" -d '{"url": "http://google.com"}' http://localhost:8080`

2. **Scraper Service (WebService)**
   - Listens on port 8080 for incoming POST requests.
   - Parses the JSON payload to extract the URL.
   - Makes an HTTP GET request to the provided URL.
   - Captures the HTTP status code of the response.
   - Increments a Prometheus counter for the HTTP GET requests, with labels for URL and status code.
   - Exposes Prometheus metrics at `/metrics` endpoint on port 9095.
   - Handles exceptions such as request failures and sets appropriate status codes.
   - Runs as a Flask app.

3. **Prometheus Server**
   - Configured to scrape metrics from specified endpoints at regular intervals. (prometheus.yml)
   - Queries the `/metrics` endpoint of the Scraper Service.
   - Stores scraped metrics in its time-series database.

   *Note*: Please refer to the `workflow diagram.pdf` file in the same folder to get the complete end-to-end workflow.

### Functional Tests

The functional tests cover the following aspects of the Scraper Service:

1. **Scraping URLs and Validating Status Codes:**
   - Tests verify that the Scraper Service correctly retrieves URLs and their respective status codes.
   - The Scraper Service is expected to make GET requests to the provided URLs and return their status codes in the response JSON.

2. **Prometheus Metrics Endpoint:**
   - Tests ensure that the `/metrics` endpoint of the Scraper Service is accessible.
   - This validates that the Scraper Service exposes Prometheus metrics as intended.

To run the tests, execute: `python3 test_scraper_service.py`.

#### Monitoring and Visualization

1. Prometheus can be configured to scrape metrics from the Scraper Service's endpoint by running the following command: `prometheus --config.file=prometheus.yml`

   *Note*: The `prometheus.yml` configuration file is provided. Users only need to run the command to start Prometheus. 
   If additional configuration is required, users can modify `prometheus.yml` according to their requirements.

2. Prometheus UI can be accessed on http://localhost:9090 to visualize the collected metrics for monitoring and analysis.

##### PromQL Query 

PromQL queries are used to analyze the metrics exposed by the Scraper Service. Below is an example query to retrieve the total count of HTTP GET requests:

- `http_get_total`: This query sums the metric grouped by the `url` label, giving you the total count of HTTP GET requests for each URL.

   To execute this query in Prometheus:
   1. Open the Prometheus UI in your web browser.
   2. Navigate to the "Graph" page.
   3. Enter the PromQL query in the query input box.
   4. Click "Execute" to execute the query.
   5. You will see the result graph and can further customize it as needed.

###### Future Enhancements

- Implementing CI/CD

   To further streamline the deployment and maintenance of the Scraper Service, implementing a Continuous Integration and Continuous Deployment (CI/CD) pipeline would be beneficial. 

   1. **Continuous Integration (CI):**
      - Build the Docker Image: Automatically build the Docker image whenever changes are pushed to the repository.
      - Run Tests: Execute the provided functional tests to ensure the service works as expected.
      - Code Quality Checks: Use tools like flake8 for Python to maintain code quality.

   2. **Continuous Deployment (CD):**
      - Push Docker Image to Registry: If the tests pass, push the Docker image to Docker Hub.
      - Deploy to Kubernetes: Use kubectl to deploy the new image to the Kubernetes cluster.# Web_Scraper
