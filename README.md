# 🌦️ Weather Info Agent - Assignment 4
  
The goal is to build an **AI agent** that can provide **(mocked) weather information** for different cities using a tool.

---

## 🎯 Objective
- Create a tool `get_weather(city)` that returns **mock weather data**.
- Register this function as a **tool** with the agent.
- Instruct the agent to **always use the tool** when the user asks about weather.
- Test the agent with different cities such as **Karachi, Lahore, New York, London**.

---



## 🚀 Usage
Run the program:
```bash
python main.py
```

You will see:
```bash
🌦️  Welcome to the Weather Info Agent! 🌍
💬 Ask me about the weather in any city. Type 'exit' or 'quit' to leave.
```

## 🌤️ Example Interaction
```pgsql
👤 You: karachi
🤖 WeatherBot: 🌡️ The current temperature in Karachi is 34°C, clear skies ☀️

👤 You: Lahore
🤖 WeatherBot: 🌡️ The current temperature in Lahore is 36°C, hot and humid 🌡️

👤 You: New York
🤖 WeatherBot: 🌡️ The current temperature in New York is 22°C, light rain 🌧️

👤 You: exit
👋 Goodbye! Stay safe and weather-aware! ☔

```

## 🧪 Mock Weather Data
The agent uses a dictionary of mock data:

```python
mock_data = {
    "Karachi": "34°C, clear skies ☀️",
    "Lahore": "36°C, hot and humid 🌡️",
    "Islamabad": "30°C, partly cloudy ⛅",
    "New York": "22°C, light rain 🌧️",
    "London": "18°C, foggy 🌫️"
}
```

If a city is not found, the response will be:
```arduino
Weather data not available ❌
```

