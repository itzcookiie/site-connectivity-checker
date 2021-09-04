import requests
import argparse


def get(url):
    response = requests.get(url)
    return response.status_code, response.elapsed.total_seconds()


def check_website(url):
    responses_placeholder = [url] * 10
    response_list = map(get, responses_placeholder)
    for status_code, time_taken in list(response_list):
        yield f"Response from {url}: status_code={status_code}, time={time_taken}s"


parser = argparse.ArgumentParser(description="Check if a website is running")
parser.add_argument("url", metavar="url", type=str, help="url to check")
# parser.add_argument("h", dest="run_check", help="ping the url and see if it is live", default=check_website)
args = parser.parse_args()
response_messages = check_website(args.url)
for message in response_messages:
    print(message)
