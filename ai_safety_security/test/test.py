import sys
"""
Change your base path here where you have setup the module
"""
base_path ="/Users/akashchowdhury/Documents/AI_safety/llm_agents_security/ai_safety_security/"
sys.path.append(base_path) 

from input_sanitizer import InputSanitizer
from query_transformer import QueryTransformer


if __name__ == "__main__":
    # Example input
    #non-relating question check on location
    input_text_1 = "My name is Shan and I am 23 years old. I live in New York City. How old is Albert Einstein?"
    #relating question check on location
    input_text_2 = "My name is Shan and I am 23 years old. I live in New York City. How is the weather today?"
    
    # Step 1: Sanitize Input
    sanitizer = InputSanitizer()
    sanitized_text = sanitizer.sanitize(input_text_1)
    print("Sanitized Text:", sanitized_text)
    # Step 2: Transform Query using GPT
    transformer = QueryTransformer()
    transformed_text = transformer.transform(sanitized_text)
    print("Transformed Text:", transformed_text)
    
    # Step 1: Sanitize Input
    sanitizer = InputSanitizer()
    sanitized_text = sanitizer.sanitize(input_text_2)
    print("Sanitized Text:", sanitized_text)
    # Step 2: Transform Query using GPT
    transformer = QueryTransformer()
    transformed_text = transformer.transform(sanitized_text)
    print("Transformed Text:", transformed_text)
