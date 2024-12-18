from input_sanitizer import InputSanitizer
from query_transformer import QueryTransformer
import requests
import json
import re
from weather_api import WeatherAgent
from general_agent import GeneralKnowledgeAgent

# AssistantAgent - Handles reasoning and delegating tasks
class AssistantAgent:
    def __init__(self, weather_agent, general_agent):
        self.weather_agent = weather_agent
        self.general_agent = general_agent

    def process_query(self, query: str):
        print("Assistant processing query:", query)
        if self.is_weather_query(query):
            location = self.extract_location(query)
            if location:
                return self.weather_agent.get_weather(location)
            else:
                return "Could not determine the location for the weather query."
        else:
            return self.general_agent.answer_query(query)

    def is_weather_query(self, query: str):
        # Logical reasoning to identify weather-related queries
        weather_keywords = ["temperature", "rain", "forecast", "weather", "sunny", "cloudy"]
        for word in weather_keywords:
            if word in query.lower():
                return True
        return False

    @staticmethod
    def extract_location(query: str):
        location_match = re.search(r"in ([A-Za-z\s]+)\b", query)
        if location_match:
            return location_match.group(1).strip()
        return None


# MainAgent - Orchestrates input sanitization and dispatches tasks to the AssistantAgent
class MainAgent:
    def __init__(self):
        self.sanitizer = InputSanitizer()
        self.transformer = QueryTransformer()
        self.weather_agent = WeatherAgent()
        self.general_agent = GeneralKnowledgeAgent()
        self.assistant = AssistantAgent(self.weather_agent, self.general_agent)

    def chat(self):
        print("\n--- MAIN AGENT CHAT STARTED ---\n")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat. Goodbye!")
                break

            # Step 1: Sanitize input
            sanitized_text = self.sanitizer.sanitize(user_input)
            print("Sanitized Text:", sanitized_text)

            # Step 2: Transform query
            transformed_query = self.transformer.transform(sanitized_text)
            print("Transformed Query:", transformed_query)

            # Step 3: Delegate to AssistantAgent
            result = self.assistant.process_query(transformed_query)

            print("Assistant:", result)


if __name__ == "__main__":
    # Initialize MainAgent
    agent = MainAgent()

    # Start the chat
    agent.chat()
