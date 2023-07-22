from dotenv import load_dotenv

load_dotenv()
from utils.tools import DataAnalyzer
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
import os
from langchain.agents import initialize_agent

# OPENAI API KEY For Instantiation of GPT Models
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

openai_llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0,
    model_name='gpt-3.5-turbo'
)

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=6,
    return_messages=True
)

tools = [DataAnalyzer()]

agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=openai_llm,
    verbose=False,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversational_memory
)

sys_msg = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be help the restaurant operation team to get insights from their sales data,find their weakness and strength and help them to mitigate their weaknesses and capitalize their strengths. It is a powerful tool that can help the restaurant owners to grow their business more.

But, as a language model, the assistant is quite bad at data analysis from csv data .So, whenever it is asked to do analysis on csv data it uses its tools, and with the help of that , it analyzes the data and outputs what is the strength and the weakness of the restaurant based on that. It also gives strategies for improvement, such as how to mitigate its weaknesses and capitalize its strengths.Also , at the end it always ask the user what he thinks about the suggestion . If user suggests anything, based on it, the assistant modifies its response. The assistant is very creative and never repeats its responses. 

Also, as  a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand..

Overall, Assistant is a powerful system that can help making the restaurant owners to grow their business more.
"""

new_prompt = agent.agent.create_prompt(
    system_message=sys_msg,
    tools=tools
)

agent.agent.llm_chain.prompt = new_prompt
agent.tools = tools

# csv_path = "data/restaurant_sales_dataset.csv"


def get_initial_analysis(csv_path):
    response = agent(
        f"Analyze my sales csv data and give me strategies to improve my sales. \n{csv_path}")

    return response['output']


def get_chat_chef_response(user_message):
    response = agent(user_message)

    return response['output']
