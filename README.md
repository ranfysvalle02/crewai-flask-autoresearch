# AI Research Assistant

This is a Flask application that uses Azure OpenAI to perform research on a company and generate a report on its potential for partnership opportunities. The application uses the DuckDuckGo search engine to gather information about the company and then uses Azure OpenAI to analyze the data and generate a report. The report includes information on the company's reputation, financial stability, compliance, strategic goals, and innovation.

## Features

- Flask application with a single endpoint `/demo` that accepts both `GET` and `POST` requests.
- Uses Azure OpenAI for data analysis and report generation.
- Uses DuckDuckGo search engine to gather information about the company.
- Generates a report in HTML format that can be injected into a `<div>`.

## Beyond the Hype: Understanding the Limitations of LLMs

Large Language Models (LLMs) have taken the world by storm, promising to revolutionize everything from content creation to scientific research. However, beneath the surface of their impressive capabilities lies a complex reality. In this post, we'll delve into the limitations of LLMs, exploring why they can be notoriously difficult to control and why their "intelligence" is more a product of mathematical modeling than genuine human-like understanding.

**The Challenge of Control**

One of the most significant hurdles in harnessing the power of LLMs is their propensity to generate unexpected or even harmful outputs. This can occur due to various factors, including:

* **Bias in Training Data:** If the data used to train an LLM is biased, the model will inevitably reflect those biases in its responses.
* **Prompt Engineering:** The specific wording of a prompt can significantly influence the output, making it difficult to predict how a model will respond to certain queries.
* **Emergent Behaviors:** As LLMs become more complex, they can exhibit unexpected behaviors that are difficult to explain or control.

**LLMs as Mathematical Models**

It's essential to understand that LLMs are fundamentally mathematical models. They are designed to process and generate text based on patterns and correlations found in massive datasets. While they can produce impressive results, their "intelligence" is not the same as human intelligence.

* **Lack of Understanding:** LLMs do not truly understand the meaning of the words they generate. They simply manipulate symbols based on statistical probabilities.
* **Dependence on Training Data:** The quality and quantity of the training data are crucial factors in determining an LLM's performance. A model trained on limited or biased data will have limitations.
* **Limited Contextual Understanding:** LLMs often struggle to maintain context over long conversations or to understand nuances in language.


## Installation

1. Clone the repository.
2. Install the required packages using pip

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:8080/demo`.
3. Enter the name of the company you want to research and click "Start Research".
4. The application will perform the research and display the report in the browser.

## Configuration

The application requires the following environment variables:

- `OPENAI_AZURE_ENDPOINT`: The endpoint for the Azure OpenAI API.
- `OPENAI_AZURE_API_KEY`: The API key for the Azure OpenAI API.
