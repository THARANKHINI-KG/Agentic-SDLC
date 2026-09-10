from agents.requirement_analyst_agent import (
    RequirementAnalystAgent
)

from agents.requirement_chatbot_agent import (
    RequirementChatbotAgent
)

from config import (
    GEMINI_API_KEY,
    MODEL_NAME
)


analyst = RequirementAnalystAgent(
    api_key=GEMINI_API_KEY,
    model_name=MODEL_NAME
)

chatbot = RequirementChatbotAgent()


initial_requirement = input(
    "Enter initial requirement:\n"
)

state = analyst.analyze_requirements(
    initial_requirement
)

while not state["complete"]:

    next_item = chatbot.get_next_question(
        state
    )

    answer = input(
        f"\n{next_item['question']}\n"
    )

    state = chatbot.update_state(
        state,
        next_item["section"],
        answer
    )

print("\nRequirements Complete")

srs = analyst.generate_srs(
    state
)

print("\n")
print("=" * 80)
print("SRS DOCUMENT")
print("=" * 80)
print(srs)