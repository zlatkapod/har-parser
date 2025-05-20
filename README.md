# HAR File Inspector

A streamlined tool for parsing and inspecting HAR (HTTP Archive) files, designed specifically for backend developers who want to quickly analyze network requests without the clutter.

## What is it?

HAR File Inspector is a web application that simplifies the process of analyzing HAR files by presenting the data in a clean, filterable, and developer-friendly format. HAR files contain detailed information about a web browser's interaction with a website, including HTTP requests and responses, timing data, and more.

## Who is it for?

This tool is primarily designed for:
- Backend developers who need to inspect API calls
- QA engineers debugging network issues
- Frontend developers troubleshooting API integrations
- DevOps professionals analyzing web traffic patterns

## Features

- **Upload and parse** HAR files with a simple drag-and-drop interface
- **Filter requests** by HTTP method or status code
- **Search requests** by URL content
- **Detailed view** of each request and response, including:
    - HTTP method and URL
    - Request and response headers
    - Request and response body (with JSON formatting)
    - Timestamp information

## How to Use

1. Run the app by command `streamlit run app.py`
2. Upload a HAR file using the file uploader
3. Use the filters to narrow down the requests you're interested in
4. Click on any request to expand and view its details
5. Toggle the display of headers and request/response bodies as needed

## Live Demo

The application is deployed and available at:
[https://har-parser.streamlit.app/](https://har-parser.streamlit.app/)

## Why Use This Tool?

Standard HAR viewers often include excessive information that most developers don't need when debugging API interactions. This tool focuses on presenting only the most relevant information in a clean, searchable interface, making it significantly faster to find and analyze specific requests.

---

Built with Streamlit | [Visit on Streamlit Cloud](https://har-parser.streamlit.app/)