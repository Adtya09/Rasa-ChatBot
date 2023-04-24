Rasa with Flask Project

This project demonstrates how to integrate a Rasa chatbot with a Flask web application.
Setup

To get started with this project, follow these steps:

    Clone the repository

    Install the dependencies listed in requirements.txt by running the command:

pip install -r requirements.txt

Train the Rasa chatbot by running the command:

rasa train

Start the Rasa server by running the command:

css

rasa run --enable-api -p 5005 --cors "*" --debug

Start the Flask web application by running the command:

    python app.py

    Open your web browser and navigate to http://localhost:5000 to interact with the chatbot.

Training the Chatbot

To train the Rasa chatbot, you will need to create or modify the following files in the data directory:

    nlu.md: This file contains the examples of user messages and the intents they correspond to.
    stories.md: This file contains example conversations between the user and the chatbot.
    domain.yml: This file defines the intents, entities, actions, and templates used by the chatbot.

Once you have modified these files to your liking, you can train the chatbot by running the following command:

rasa train

This will create a new model based on the data in the data directory, which can be used to respond to user messages.
Requirements

The following dependencies are required to run this project:

    Rasa
    Flask
    Python 3.8

