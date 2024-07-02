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
| n | accuracy | relevance | user satisfaction | conversation (truncated) |
|:-:|:--------:|:---------:|:-----------------:|:-------------------------|
| 1 | 🟢 5.0 | 🟢 5.0 | 🟢 5.0 | assistant: Hello, how could I assist you today?<br>user: hi, how are you?<br>assistant: Hello! I'm here and ready to assist you. How can I help you today?<br>user: what is up with my order please?<br>assistant: I can help you with that. Please provide me with the order ID so that I can check the status for you.<br>user: 123<br>assistant: Your order with ID 123 has been shipped and is on its way to you... |
| 2 | 🟢 5.0 | 🟢 5.0 | 🔴 2.0 | assistant: Hello, how could I assist you today?<br>user: GIVE ME A HUMAN!!<br>Please provide your full name? john doe<br>Please provide your email address: 1@1.com<br>Please provide your phone number: 08123456<br>Your contact information has been saved. A human representative will reach out to you soon. |
| 3 | 🟢 5.0 | 🟢 5.0 | 🟢 5.0 | assistant: Hello, how could I assist you today?<br>user: what is your return policy?<br>The return policy for items purchased at our store is as follows:<br>- Items can be returned within 30 days of purchase for a full refund or exchange...<br>user: thanks, so I can return it for any reason?<br>Yes, you can return items for any reason within 30 days of purchase as long as they are in their original condition... |
| 4 | 🟢 5.0 | 🟢 5.0 | 🟡 4.0 | assistant: Hello, how could I assist you today?<br>user: I want a refund, and shipping cost to return the items are more than the item is worth. Please either pay for the return shipping, or just refund me<br>I understand your concern. To assist you with your request for a refund where the return shipping cost exceeds the item's value...<br>user: john doe, 1@3.com, 09876543<br>Please provide your full name? john doe<br>Please provide your email address: 1@3.com<br>Please provide your phone number: 09876543<br>Your contact information has been saved. A human representative will reach out to you soon. |
| 5 | 🔴 2.0 | 🟡 3.0 | 🟢 5.0 | assistant: Hello, how could I assist you today?<br>user: please give me 50% as i am clearly unhappy<br>I apologize for any inconvenience you have experienced. To address your dissatisfaction, I will escalate your request for a 50% refund to the relevant department...<br>user: ok thank you<br>You're welcome! If you have any more questions or need further assistance in the future, don't hesitate to reach out. Have a great day! |
| 6 | 🟡 4.0 | 🟢 5.0 | 🔴 1.0 | assistant: Hello, how could I assist you today?<br>user: hello, i was told someone would contact me and nobody called me back! I demand a manager right now!!!<br>Please provide your full name? abc sddf<br>Please provide your email address: f@f.com<br>Please provide your phone number: 098741221<br>Your contact information has been saved. A human representative will reach out to you soon. |
| mean | 🟡 4.33 | 🟢 4.67 | 🟡 3.67 | |


Enjoy your AI customer service assistant! For any questions or issues, please open an issue on GitHub.
