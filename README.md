# E-Chef 🧑‍🍳

This is the  Demo implementation of E-Chef. That helps the Restaurant Operation team  with data-analysis using OpenAI's `GPT-3.5 LLM` and `langchain`

## Instructions

1. Install Requirements:
   - Make sure you have Python 3.x installed on your system.
   - Install the required packages by running the following command:
     ```
     pip install -r requirements.txt
     ```

2. Run the Server:
   - Start the server by running the following command:
     ```
     python main.py
     ```

3. Initial Data Analysis:
   - To perform an initial data analysis from CSV file, send a GET request to the following URL:
     ```
     http://0.0.0.0:8080/start_analysis
     ```

4. Interacting with E-Chef:
   - To interact with E-Chef , send a POST request to the following URL:
     ```
     http://0.0.0.0:8080/ask_e_chef
     ```
   - Include the following JSON body in the request:
     ```json
     {
         "user": "user_message"
     }
     ```
     Replace "user_message" with your actual message/question.

Please note that the server is expected to be running on your local machine (localhost) at port 8080 (http://0.0.0.0:8080). Adjust the URL accordingly if you have configured it differently.


