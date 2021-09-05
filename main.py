import requests
import argparse


def get(url):
    response = requests.get(url)
    return response.status_code, response.elapsed.total_seconds()


def check_website(url):
    responses_placeholder = [url] * 5
    return list(map(get, responses_placeholder))


def print_responses(data):
    for status_code, time_taken in data:
        print(f"Response: status_code={status_code}, time={time_taken}s")


def get_average_time(data):
    list_of_time_taken = map(lambda item: item[1], data)
    return sum(list(list_of_time_taken))


parser = argparse.ArgumentParser(description="Ping a website and Check if it is running")
parser.add_argument("url", metavar="url", type=str, help="url to ping and see if it is live")
args = parser.parse_args()
response_messages = check_website(args.url)
print(f"Pinging {args.url}...")
print("-" * 40)
print_responses(response_messages)
print("-" * 40)
print(f"Statistics:")
print(f"{' ' * 4} Average = {get_average_time(response_messages)}s")
