from decouple import config
from agents import Agent, function_tool, RunConfig, Runner, OpenAIChatCompletionsModel, AsyncOpenAI


gemini_api_key = config("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("🚨 GEMINI_API_KEY environment variable is not set.")

# 🌐 Initialize Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 🤖 Setup the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# ⚙️ Run settings
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# 🌤️ Weather Tool (Mock Data)
@function_tool
def get_weather(city: str) -> str:
    """Return mock weather info for the given city."""
    mock_data = {
        "Karachi": "34°C, clear skies ☀️",
        "Lahore": "36°C, hot and humid 🌡️",
        "Islamabad": "30°C, partly cloudy ⛅",
        "New York": "22°C, light rain 🌧️",
        "London": "18°C, foggy 🌫️"
    }
    weather = mock_data.get(city.title(), "Weather data not available ❌")  
    return f"🌡️ The current temperature in {city.title()} is {weather}"

# 🚀 Main Program
def main():
    print("\n🌦️  Welcome to the Weather Info Agent! 🌍")
    print("💬 Ask me about the weather in any city. Type 'exit' or 'quit' to leave.\n")

    agent = Agent(
        name="WeatherBot",
        instructions=(
            "🌤️ You are a helpful weather assistant. "
            "If the user asks about the weather in a city, you MUST call the get_weather tool. "
            "Do not guess. Always use the tool to get the weather."
        ),
        model=model,
        tools=[get_weather]
    )

    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye! Stay safe and weather-aware! ☔")
            break

        result = Runner.run_sync(agent, user_input, run_config=config)
        print("🤖 WeatherBot:", result.final_output)


if __name__ == "__main__":
    main()
