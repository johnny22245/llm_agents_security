import autogen

# GeneralKnowledgeAgent - Answer general queries using GPT/LLM
class GeneralKnowledgeAgent:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        """
        Initializes the GeneralKnowledgeAgent with GPT agent.

        Args:
            api_key (str): The API key for accessing the GPT model.
            model (str): The GPT model to use (default: gpt-4o-mini).
        """
        config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
        )

        # Configure an agent with GPT model
        self.agent = autogen.AssistantAgent(
            name="query_paraphraser",
            llm_config={
            "config_list": config_list
        }
        )

    def answer_query(self, query: str):
        print("Answering general query:", query)
        result = self.agent.generate_reply(messages=[{"role": "user", "content": query}])
        return result