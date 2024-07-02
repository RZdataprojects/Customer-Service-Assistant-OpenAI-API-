# Defining chatbot functionalities:
# [
# "get_order_status(order_id)",
# "request_human_representative(full_name, email, phone)"
# ]
from datetime import datetime
import csv


def get_order_status(order_id: str) -> str:
    """
    Returns the status of the order.
    :param order_id: str - The ID of the order to check
    :return: str - A fixed string for demonstration purposes
    """
    # Placeholder for the actual order status retrieval logic
    # Example response for demonstration
    return f"The status of order {order_id} is: Shipped.\nThe package is on its way and is expected to arrive in the coming days."

def request_human_representative(full_name: str, email: str, phone: str) -> str:
    """
    Records the user's contact information so a human customer service representative can contact them later.
    :param full_name: str - The full name of the user
    :param email: str - The email address of the user
    :param phone: str - The phone number of the user
    :return: str - A fixed string notifying the user that their request has been received
    """
    # Open the CSV file in append mode to add the user's contact information
    with open('contact_info.csv', 'a', newline='') as csvfile:
        # Define the field names for the CSV file
        fieldnames = ['timestamp', 'full_name', 'email', 'phone']
        # Create a DictWriter object to write the user's information
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write the user's information along with the current timestamp
        writer.writerow({
            'timestamp': datetime.now().isoformat(),
            'full_name': full_name,
            'email': email,
            'phone': phone
        })
    # Return a confirmation message to the user
    return "Your contact information has been saved. A human representative will reach out to you soon."