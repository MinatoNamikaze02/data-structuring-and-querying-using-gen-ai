# Generative AI Integration for LongShot AI assessment

This repository contains the code for the LongShot AI assessment. The code is written in Python 3. 

### Overview
This is a simple app that has integrated the scraping of this [page](https://en.wikipedia.org/wiki/List_of_2023_box_office_number-one_films_in_the_United_States) to the subsequent usage of its data through LLM APIs to filter based on query inputs.

### Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

### Usage

To run the code, run the following command:

```bash
python app.py
```

Then go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the results.

## Explanation

### Scraper
- Used beautiful soup to parse, scrape and format the data.
- Used pydantic to handle objects. The sample of the data is dumped at films.json.

### LLMs
- Used the openai python library to create and handle the llms access for GPTs
- For other Open Source LLMs, used the together AI python library to handle Mistral LLMs or any other open source LLMs.

## How it works
- Flask api hosts the frontend and communicates with the LLM API and returns a Jsonified response which is rendered in the frontend.
