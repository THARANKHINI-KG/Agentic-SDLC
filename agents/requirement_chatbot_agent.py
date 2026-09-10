class RequirementChatbotAgent:

    QUESTIONS = {
        "objective":
            "What is the primary objective of the application?",

        "user_roles":
            "Who are the user roles in the system?",

        "user_stories":
            "Provide key user stories for each role.",

        "functional_requirements":
            "What features should the system provide?",

        "non_functional_requirements":
            "What performance, scalability or availability requirements are needed?",

        "security_requirements":
            "What security requirements are needed (authentication, authorization, encryption etc.)?",

        "technology_stack":
            "Do you have any preferred frontend, backend or database technologies?",

        "acceptance_criteria":
            "What conditions must be met for the project to be considered successful?"
    }

    def get_next_question(
        self,
        state: dict
    ):

        missing = state.get(
            "missing_sections",
            []
        )

        if not missing:
            return None

        section = missing[0]

        return {
            "section": section,
            "question": self.QUESTIONS[section]
        }

    def update_state(
        self,
        state: dict,
        section: str,
        answer
    ):

        state[section] = answer

        state["missing_sections"].remove(
            section
        )

        state["complete"] = (
            len(
                state["missing_sections"]
            ) == 0
        )
        print(type(response.content))
        print(response.content)
        return state


    class RequirementChatbotAgent:

        QUESTIONS = {
            "objective":
                "What is the primary objective of the application?",

            "user_roles":
                "Who are the user roles in the system?",

            "user_stories":
                "Provide key user stories for each role.",

            "functional_requirements":
                "What features should the system provide?",

            "non_functional_requirements":
                "What performance, scalability or availability requirements are needed?",

            "security_requirements":
                "What security requirements are needed (authentication, authorization, encryption etc.)?",

            "technology_stack":
                "Do you have any preferred frontend, backend or database technologies?",

            "acceptance_criteria":
                "What conditions must be met for the project to be considered successful?"
        }

    def get_next_question(
        self,
        state: dict
    ):

        missing = state.get(
            "missing_sections",
            []
        )

        if not missing:
            return None

        section = missing[0]

        return {
            "section": section,
            "question": self.QUESTIONS[section]
        }

    def update_state(
        self,
        state: dict,
        section: str,
        answer
    ):

        state[section] = answer

        state["missing_sections"].remove(
            section
        )

        state["complete"] = (
            len(
                state["missing_sections"]
            ) == 0
        )

        return state