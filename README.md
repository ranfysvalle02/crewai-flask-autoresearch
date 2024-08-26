# AI Research Assistant

This is a Flask application that uses Azure OpenAI to perform research on a company and generate a report on its potential for partnership opportunities. The application uses the DuckDuckGo search engine to gather information about the company and then uses Azure OpenAI to analyze the data and generate a report. The report includes information on the company's reputation, financial stability, compliance, strategic goals, and innovation.

## Features

- Flask application with a single endpoint `/demo` that accepts both `GET` and `POST` requests.
- Uses Azure OpenAI for data analysis and report generation.
- Uses DuckDuckGo search engine to gather information about the company.
- Generates a report in HTML format that can be injected into a `<div>`.

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
