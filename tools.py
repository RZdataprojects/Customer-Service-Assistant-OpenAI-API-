# Defining tools:
# [
# "get_order_status",
# "request_human_representative"
# ]
import json


def get_tools():
    """
    Returns a list of tool configurations for the chatbot.
    :return: list of dictionaries containing tool configurations
    """
    tools = [
        {"type": "file_search"},  # A tool for searching files (for the return policy)
        {
            "type": "function",
            "function": {
                "name": "get_order_status",
                "description": "Retrieve the status of an order. ONLY use this if the user queries over an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The unique identifier for the order."
                        }
                    },
                    "required": [
                        "order_id"  # The 'order_id' parameter is required
                    ]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "request_human_representative",
                "description": "Gather contact information for users who want to interact with a person.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "The full name of the user."
                        },
                        "email": {
                            "type": "string",
                            "description": "The email address of the user."
                        },
                        "phone": {
                            "type": "string",
                            "description": "The phone number of the user."
                        }
                    },
                    "required": [
                        "full_name",  # The 'full_name' parameter is required
                        "email",  # The 'email' parameter is required
                        "phone"  # The 'phone' parameter is required
                    ]
                }
            }
        }
    ]
    return tools


def return_policy_doc(client):
    """
    Creates a return policy document on OpenAI's API dashboard and uploads it to a vector store.
    :param client: OpenAI client instance
    :return: str - The ID of the newly created vector store containing the return policy document
    """
    # Define the return policy document
    doc = {
        "name": "return policy",
        "content": """Q: What is the return policy for items purchased at our store?
                   A: You can return most items within 30 days of purchase for a full refund or
                   exchange. Items must be in their original condition, with all tags and
                   packaging intact. Please bring your receipt or proof of purchase when
                   returning items.
                   Q: Are there any items that cannot be returned under this policy?
                   A: Yes, certain items such as clearance merchandise, perishable goods, and
                   personal care items are non-returnable. Please check the product description
                   or ask a store associate for more details.
                   Q: How will I receive my refund?
                   A: Refunds will be issued to the original form of payment. If you paid by
                   credit card, the refund will be credited to your card. If you paid by cash or
                   check, you will receive a cash refund."""
    }

    # Save the return policy document to a JSON file
    with open('return_policy.json', 'w') as fp:
        json.dump(doc, fp)

    # Create a new vector store called "Return Policy"
    vector_store = client.beta.vector_stores.create(name="Return Policy")

    # Prepare the file stream for upload
    file_streams = [open('return_policy.json', "rb")]

    # Upload the file to the vector store and poll the status until completion
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )

    return vector_store.id  # Return the ID of the vector store