# Metadata Analyzer for Little Caesar's Enterprises

## Project Overview
This project involved scraping and collecting metadata from over 400 documents across various domains associated with Little Caesar's Enterprises. The data was sourced from publicly available information, primarily using advanced search queries or "Google Dorks." The primary goal was to analyze this metadata to identify and report any sensitive information to the client, along with recommendations for future metadata handling.

## Features and Functionality
- **Analysis**: Utilizes `exiftool` to generate a comprehensive JSON object for each document, aiding in detailed metadata analysis.
- **Visualization**: Employs libraries like `seaborn` and `matplotlib` in Python to graphically represent the findings, making the data more accessible and understandable.
- **Sensitive Data Identification**: The tool highlights potential sensitive information within the metadata, which can then be addressed by the client.

## Technologies Used
- **Python**: For the main programming logic.
- **ExifTool**: To extract metadata and generate JSON objects.
- **Seaborn and Matplotlib**: For data visualization and graphical representation of the analysis.
