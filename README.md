# site-connectivity-checker

### Pings a website and checks to see if the website is up and running. Lil project similar to the ping command

    Make sure you have Python 3 installed!

Currently:
- Create env by doing `python3 venv env` and activate it
- Install packages by doing `python3 -m pip install -r requirements.txt`
- Created a CLI app. Pass your chosen website to `python main.py <url>`
- Makes 4 HTTP requests to chosen website
- Prints out the results in the terminal
- Prints the average time taken to complete all 4 requests

Ideas:
- Check a website every e.g. 10 seconds (polling)
- Add e.g. desktop notification system, so if the website goes down we are alerted