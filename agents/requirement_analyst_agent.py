import json

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


class RequirementAnalystAgent:

    REQUIRED_SECTIONS = [
        "objective",
        "user_roles",
        "user_stories",
        "functional_requirements",
        "non_functional_requirements",
        "security_requirements",
        "technology_stack",
        "acceptance_criteria"
    ]

    def __init__(
        self,
        api_key: str,
        model_name: str
    ):

        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=0
        )

    def analyze_requirements(
    self,
    raw_requirement: str
) -> dict:

        messages = [
            SystemMessage(
                content="""
    You are a Senior Business Analyst.

    Analyze the requirement.

    Extract:

    1. objective
    2. user_roles
    3. user_stories
    4. functional_requirements
    5. non_functional_requirements
    6. security_requirements
    7. technology_stack
    8. acceptance_criteria

    Return ONLY valid JSON.

    Example:

    {
        "objective": "",
        "user_roles": [],
        "user_stories": [],
        "functional_requirements": [],
        "non_functional_requirements": [],
        "security_requirements": [],
        "technology_stack": [],
        "acceptance_criteria": []
    }
    """
            ),
            HumanMessage(
                content=raw_requirement
            )
        ]

        response = self.llm.invoke(messages)

        content = response.content

        # Gemini may return list
        if isinstance(content, list):

            text_parts = []

            for item in content:

                if isinstance(item, str):
                    text_parts.append(item)

                elif isinstance(item, dict):
                    text_parts.append(
                        item.get("text", "")
                    )

                else:
                    text_parts.append(
                        str(item)
                    )

            content = "".join(text_parts)

        # Remove markdown wrappers
        content = (
            str(content)
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        print("\nLLM RESPONSE:")
        print(content)

        try:
            result = json.loads(content)

        except Exception as ex:

            print(
                f"JSON Parse Error: {ex}"
            )

            result = {
                "objective": "",
                "user_roles": [],
                "user_stories": [],
                "functional_requirements": [],
                "non_functional_requirements": [],
                "security_requirements": [],
                "technology_stack": [],
                "acceptance_criteria": []
            }

        missing = []

        for section in self.REQUIRED_SECTIONS:

            value = result.get(section)

            if not value:
                missing.append(section)

        result["missing_sections"] = missing

        result["complete"] = (
            len(missing) == 0
        )

        return result

    def generate_srs(
        self,
        requirements: dict
    ) -> str:

        messages = [
            SystemMessage(
                content="""
Generate a professional Software
Requirements Specification document.

Sections:

1. Objective
2. User Roles
3. User Stories
4. Functional Requirements
5. Non Functional Requirements
6. Security Requirements
7. Technology Stack
8. Acceptance Criteria

Use professional SRS format.
"""
            ),
            HumanMessage(
                content=json.dumps(
                    requirements,
                    indent=2
                )
            )
        ]

        response = self.llm.invoke(messages)

        return response.content