from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

from langchain_google_genai import ChatGoogleGenerativeAI

from agents.tools import get_python_guidelines


class CodeReviewerAgent:

    def __init__(
        self,
        api_key: str,
        model_name: str
    ):

        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=0
        )

        tools = [
            get_python_guidelines
        ]

        prompt = hub.pull(
            "hwchase17/react"
        )

        agent = create_react_agent(
            llm=llm,
            tools=tools,
            prompt=prompt
        )

        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=True
        )

    def review_code(
        self,
        generated_code: str
    ) -> str:

        response = self.agent_executor.invoke(
            {
                "input": f"""
Before reviewing:

1. Call get_python_guidelines.
2. Review code against EVERY guideline.
3. Identify violations.
4. Suggest improvements.
5. Calculate compliance percentage.

Code:

{generated_code}

Output format:

# REVIEW REPORT

## Guideline Checks

## Violations

## Improvements

## Compliance Percentage

## Final Status
APPROVED / NEEDS_CHANGES
"""
            }
        )

        return response["output"]