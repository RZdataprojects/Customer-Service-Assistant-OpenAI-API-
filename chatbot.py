from openai import OpenAI
import tools


class Chatbot:
    def __init__(self, openai_api_key: str):
        # Initialize the chatbot with the provided API key and set up the model and tools
        self.model = 'gpt-3.5-turbo'
        self.client = OpenAI(api_key=openai_api_key)
        self.tools = tools.get_tools()  # Retrieve the list of tools from the tools module
        self.vector_store_id = tools.return_policy_doc(
            self.get_client())  # Get the ID of the vector store for the return policy document
        self.assistant = self.create_assistant()  # Create an assistant instance

    def create_assistant(self):
        # Create an assistant with specific instructions and configurations
        assistant = self.client.beta.assistants.create(
            instructions="""You are a customer support representative for an e-commerce platform. 
            Provide accurate responses to customer inquiries about order status, return policies, and if you are requested a human representative,
            gather contact information so that they could be contacted in the near future.
            If a user requests information related to the return or refund policy of the company, you can look in the vectorDB.""",
            name="customer support",
            description="A customer support representative for an e-commerce platform.",
            tools=self.tools,
            tool_resources={"file_search": {"vector_store_ids": [self.vector_store_id]}},
            model=self.model,
            temperature=0.2  # Set a low temperature for more deterministic responses
        )
        return assistant

    def get_client(self):
        # Return the OpenAI client instance
        return self.client

    def get_assistant(self):
        # Return the assistant instance
        return self.assistant

    def start_new_chat(self):
        # Start a new chat thread
        empty_thread = self.client.beta.threads.create()
        return empty_thread

    def get_chat(self, thread_id: str):
        # Retrieve all messages in a chat thread, ordered ascending by creation time
        messages = self.client.beta.threads.messages.list(
            thread_id=thread_id,
            order='asc'
        )
        return messages

    def add_user_message(self, thread_id: str, content):
        # Add a user message to the chat thread
        thread_message = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=content,
        )
        return thread_message

    def add_assistant_message(self, thread_id: str, content):
        # Add an assistant message to the chat thread
        thread_message = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="assistant",
            content=content,
        )
        return thread_message

    def get_messages_in_chat(self, thread_id: str):
        # Retrieve all messages in a chat thread, ordered ascending by creation time
        messages = self.client.beta.threads.messages.list(
            thread_id=thread_id,
            order='asc'
        )
        return messages
