# AI Customer Service Assistant

## Overview

This repository contains a basic setup for an AI assistant for a generic e-commerce company. The assistant is designed to handle customer inquiries about order status, return policies, and request human representative contact.

## Features

- **Order Status**: Retrieve and display the status of a specific order.
- **Human Representative**: Collect user contact details for follow-up by a human representative.
- **Return Policy**: Store and retrieve information about the company's return and refund policy using a vector database.

## Prerequisites

- **Python**: Ensure you have Python 3.10 or later installed.
- **OpenAI API Key**: Obtain an API key from OpenAI.
- **Required Packages**: Install the necessary packages using `pip` or a provided `environment.yaml` file.

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/ai-customer-service-assistant.git
   cd ai-customer-service-assistant
   ```
   
2. **Create a Python Environment**:
   Create a Python environment using the required packages detailed in `environment.yaml`:
   ```
   conda env create -f environment.yaml
   ```
   Or manually install the necessary package:
   ```
   pip install openai
   ```

## Usage

1. **Run the Main Script**:
   ```
   python main.py
   ```

2. **Interact with the Assistant**:
   - Ask about the status of an order: "What is the status of order 12345?"
   - Inquire about the return policy: "What is the return policy?"
   - Request a human representative: "I would like to speak to a human representative."

## Project Structure

```
├── chatbot.py            # Defines the Chatbot class
├── functions.py          # Helper functions
├── tools.py              # Tool definitions and return policy document creation
├── main.py               # Main script to run the chatbot
├── config.yaml           # Configuration file for API keys
├── environment.yaml      # Conda environment configuration file
└── README.md             # Project documentation
```

Basic evaluation:
| n | accuracy | relevance | user satisfaction |
|:-:|:--------:|:---------:|:-----------------:|
| 1 | 🟢 5.0 | 🟢 5.0 | 🟢 5.0 |
| 2 | 🟢 5.0 | 🟢 5.0 | 🔴 2.0 |
| 3 | 🟢 5.0 | 🟢 5.0 | 🟢 5.0 |
| 4 | 🟢 5.0 | 🟢 5.0 | 🟡 4.0 |
| 5 | 🔴 2.0 | 🟡 3.0 | 🟢 5.0 |
| 6 | 🟡 4.0 | 🟢 5.0 | 🔴 1.0 |
| mean | 🟡 4.33 | 🟢 4.67 | 🟡 3.67 |


Enjoy your AI customer service assistant! For any questions or issues, please open an issue on GitHub.
