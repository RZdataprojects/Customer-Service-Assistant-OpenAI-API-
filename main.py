import chatbot, functions
import time
import os


def main():
    # Initialize the chatbot client with an API key
    client = chatbot.Chatbot(openai_api_key=os.getenv(['OPENAI_KEY']))

    # Create a new thread for the chat session
    thread = client.client.beta.threads.create()

    # Prompt the user for input
    user_input = input("assistant: Hello, how could I assist you today?\nuser: ")

    # Loop to handle continuous interaction
    while True:
        # Create a new message in the thread with the user's input
        message = client.client.beta.threads.messages.create(
            thread_id=thread.id,
            role='user',
            content=user_input
        )

        # Create a new run for the assistant to process the message
        run = client.client.beta.threads.runs.create(
            assistant_id=client.assistant.id,
            thread_id=thread.id
        )

        flag = True  # Flag to control the loop
        start_time = time.time()  # Record the start time

        # Loop to wait for the assistant to complete processing the message
        while run.status not in ['completed', 'requires_action'] and flag:
            print('please wait, retrieving answer.' + "." * int(time.time() - start_time), end='\r')
            time.sleep(3.5)  # Wait for a short period before checking the status again

            # Retrieve the updated run status
            run = client.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )

        if run.status == 'requires_action':
            # Step 2: Check if the response from the model includes a tool call
            tool_calls = run.required_action.submit_tool_outputs.tool_calls
            if tool_calls:
                # If there are tool calls, retrieve the tool call ID and function name
                tool_call_id = tool_calls[0].id
                tool_function_name = tool_calls[0].function.name

                # Step 3: Call the appropriate function and retrieve results
                if tool_function_name == 'get_order_status':
                    order_id = input("Please provide an order ID: ")
                    response = functions.get_order_status(order_id)
                    print(response)
                elif tool_function_name == 'request_human_representative':
                    full_name = input("Please provide your full name: ")
                    email = input("Please provide your email address: ")
                    phone = input("Please provide your phone number: ")
                    response = functions.request_human_representative(full_name, email, phone)
                    print(response)
                    # Note: User's personal information is not recorded in model messages to ensure privacy and GDPR compliance.

                # Step 4: Submit the tool outputs back to the assistant
                run = client.client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread.id,
                    run_id=run.id,
                    tool_outputs=[
                        {
                            "tool_call_id": tool_call_id,
                            "output": response
                        }
                    ]
                )
        else:
            # If the model did not identify a function to call, return the result to the user
            messages = client.get_messages_in_chat(thread.id)
            output = messages.data[-1].content[0].text.value
            print(output)

        # Prompt the user for more input
        user_input = input("user: ")

        # Break the loop if the user says "goodbye!" or if the flag is False
        if user_input.lower() == "goodbye!" or flag is False:
            break

    # Display the entire chat thread at the end of the session
    print("Displaying thread:\n\n")
    messages = client.get_messages_in_chat(thread.id)

    for message in messages:
        print(message.role + ": " + message.content[0].text.value)
        print('\n')


# Entry point of the script
if __name__ == "__main__":
    main()