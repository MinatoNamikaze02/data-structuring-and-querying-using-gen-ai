# Generative AI Integration for LongShot AI assessment

This repository contains the Python 3 code for the LongShot AI assessment, showcasing the integration of Generative AI with a Retrieval Augmented Generation (RAG) model. The application scrapes data from a specific Wikipedia page, processes it through a RAG system, and uses Large Language Models (LLMs) to generate informative responses based on user queries.


### Overview
This application integrates web scraping, RAG, and LLMs to provide enriched responses to queries related to the 2023 box office films in the United States. It scrapes data from this page, categorizes and formats the data using a custom GPT model, and then uses this structured data in tandem with LLMs to answer user queries more effectively.


### Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

### Usage

To start off, run

```bash
python formatting.py
```
This scrapes the data, uses LLMs to format the data to a pydantic object and is dumped to json which is later used to query.
1. Uses the Mistral LLM to get a summary of the table element from the wikipedia page.
2. This summarised data is sent over to the GPT model to categorize and structure the data into a JSON.
3. This JSON is then converted dumped to films.json which is later used to query.

Samples 
<br />
This file represents the initial summarisation output from Mistral
<img width="899" alt="Screenshot 2023-12-20 at 11 04 36 PM" src="https://github.com/MinatoNamikaze02/generative_ai/assets/85065053/9bac368b-e912-415a-97af-86b56bef96c8">
<br />
This represents the JSON conversion followed by the writing into pydantic objects.
<img width="1216" alt="Screenshot 2023-12-20 at 11 04 47 PM" src="https://github.com/MinatoNamikaze02/generative_ai/assets/85065053/447ab4da-97be-466f-8290-76ee3fe66a85">

```bash
python app.py
```

Then go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the interface to query the data.

## Explanation

### Scraper
- Used beautiful soup to parse, scrape and format the data.
- Used pydantic to handle objects. The sample of the data is dumped at films.json.

### LLMs
- Integrates OpenAI's python library for accessing GPT models.
- For open-source LLMs, uses the Together AI python library to handle models like Mistral.
- Implements a RAG system where GPT categorizes the scraped data into a structured format, which is then used to augment the query processing by the same or a different GPT model.

#### Function Calling
- Users interacting with the interface can choose if function calling can be used. 
- function calling for OpenAI is another way of prompting the LLMs.

## How it works
- Flask api hosts the frontend and communicates with the LLM API and returns a Jsonified response which is rendered in the frontend.
- RAG Integration: The application first uses a GPT model to categorize and structure the scraped data. When a user query is received, this structured data is used to augment the query processing, enabling more contextually rich and accurate responses.
<br />
<img width="883" alt="Screenshot 2023-12-20 at 11 14 08 PM" src="https://github.com/MinatoNamikaze02/generative_ai/assets/85065053/63c4f47b-d9e9-49cd-9feb-a219e57d3f18">
