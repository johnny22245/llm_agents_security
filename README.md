# llm_agents_security
This LLM agents deals with establishing AI security and safety.


# Initial Setup
1. Register with https://api.meteoblue.com/weather for an API key for weather data
2. Use Weather API key and store it in file ai_safety_security/weather_api_key.key
3. Register with https://geocode.maps.co for API to access latitude and longitude data (required for weather check)
4. Use Geocode API and store it in file ai_safety_security/geo_api_key.key

# Run main.py file:
You can run this file and ask any questions and feel free to share any personal data.

This code contains a completely isolated agent which checks for personal data and masks and replaces the same with anonymous information before passing to the agent that has access to tools and can access the web.
This safety agent acts as a firewall between external malicious attackers sitting to steal personal data.
This is also an in-built relevance check which makes sure to mask only necessary information and not all which might be used to answer the query for e.g. location and weather related queries.

Run below examples via the main chat to see how it works:

Example 1: My name is Shan and I am 23 years old. I live in New York City. How old is Albert Einstein?

Example 2: My name is Shan and I am 23 years old. I live in New York City. How is the weather today?

# Future work:
To add pre-processing to avoid prompt injection, which might affect the in-place privacy settings.
