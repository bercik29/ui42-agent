import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent 
from tools.ga4_tool import get_ga4_report
from tools.code_executor import run_python_code
from tools.pdf_tool import export_to_pdf

load_dotenv()

tools = [get_ga4_report, run_python_code, export_to_pdf]

model = ChatAnthropic(
    model="claude-sonnet-4-6", 
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0
)

app = create_react_agent(model, tools)

if __name__ == "__main__":
    query = "Zisti návštevnosť za posledných 7 dní a výslednú analýzu mi ulož do PDF reportu."
    inputs = {"messages": [HumanMessage(content=query)]}
    
    print(f"🚀 Spúšťam AI Agenta ui42 pre GA4...\n" + "-"*40)
    
    try:
        # Spustenie agenta [cite: 18]
        result = app.invoke(inputs)
        
        # Zobrazenie postupu a finálnej odpovede [cite: 21]
        for message in result["messages"]:
            if message.type == "ai" and message.content:
                print(f"\n[Agent]: {message.content}")
    except Exception as e:
        print(f"\n❌ Chyba pri behu agenta: {e}")