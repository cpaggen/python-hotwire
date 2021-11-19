# What is this?

A very simple [Turbo-Flask](https://github.com/miguelgrinberg/turbo-flask) Python example.
Turbo-Flask uses the [HotWIRE JS (turbo.js)](https://turbo.hotwired.dev/) library to update sections/divs using WebSockets.
As I am not particularly good with JS or front-end frameworks, I looked for a Python-based alternative.
Turbo-Flask does the job: no need for tons of front-end JS code on the page - inspect the code and see for yourself.
This app just generates a random person's name every 3 seconds using Faker in a div.
This code can be used by Python programmers as a reference template for Web-app projects that require async update from various threads.

## Demo
[!Demo TurboFlask](https://raw.githubusercontent.com/cpaggen/python-hotwire/master/demo.gif)

## Installation

Just satisfy requirements.txt; code tested with Python3 on Chrome

```bash
pip install -r requirements.txt
```

## Usage

```bash
flask run
```

## Contributing
Pull requests are welcome. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
