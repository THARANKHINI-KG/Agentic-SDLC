from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

from langchain_google_genai import ChatGoogleGenerativeAI

from agents.tools import get_python_guidelines


class CodeGeneratorAgent:

    def __init__(
        self,
        api_key: str,
        model_name: str
    ):

        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=0.1
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

    def generate_code(
        self,
        user_prompt: str
    ) -> str:

        response = self.agent_executor.invoke(
            {
                "input": f"""
Before generating code:

1. Call get_python_guidelines.
2. Read every guideline.
3. Follow every guideline.
4. Generate production-ready Python code.

Requirement:

{user_prompt}
"""
            }
        )

        return response["output"]