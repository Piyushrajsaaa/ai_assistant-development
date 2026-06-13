# ============================================================
# prompts/qa_prompts.py - Question Answering Prompt Templates
# ============================================================
# Three prompts varying in length, tone, and complexity.
# ============================================================

def get_qa_prompt(style, user_question):
    """
    Returns a prompt for Question Answering based on selected style.
    
    Args:
        style (str): "simple" | "educational" | "detailed"
        user_question (str): The question entered by the user
    
    Returns:
        str: A complete prompt string ready to send to Gemini
    """

    if style == "simple":
        # --------------------------------------------------------
        # PROMPT 1: SHORT & DIRECT
        # --------------------------------------------------------
        # Length     : 1 line
        # Tone       : Direct, conversational
        # Complexity : Low - just asks the question plainly
        # Best for   : Quick factual lookups
        # Why it works: Simple prompts get clean, direct answers.
        #               No extra instructions = no extra fluff.
        # --------------------------------------------------------
        return f"Answer this question clearly and concisely: {user_question}"

    elif style == "educational":
        # --------------------------------------------------------
        # PROMPT 2: MEDIUM - ROLE-BASED WITH CONTEXT
        # --------------------------------------------------------
        # Length     : 3 lines
        # Tone       : Educational, teacher-like
        # Complexity : Medium - assigns a role + sets expectations
        # Best for   : Students who want to understand concepts
        # Why it works: Assigning a role ("expert teacher") guides
        #               the AI to use the right tone and depth.
        #               Asking for examples improves understanding.
        # --------------------------------------------------------
        return (
            f"You are an expert teacher explaining to a university student.\n"
            f"Answer the following question with a clear explanation and "
            f"at least one real-world example.\n"
            f"Question: {user_question}"
        )

    elif style == "detailed":
        # --------------------------------------------------------
        # PROMPT 3: LONG - STRUCTURED OUTPUT WITH CONTEXT
        # --------------------------------------------------------
        # Length     : 6+ lines
        # Tone       : Academic, professional
        # Complexity : High - specifies exact output structure
        # Best for   : In-depth research or study notes
        # Why it works: Structured prompts produce structured output.
        #               Specifying format (Definition, Explanation,
        #               Examples, Key Points) ensures completeness.
        #               This technique is called "output scaffolding".
        # --------------------------------------------------------
        return (
            f"You are a knowledgeable academic assistant.\n"
            f"Provide a comprehensive answer to the following question "
            f"using this exact structure:\n\n"
            f"1. DEFINITION: A one-sentence definition\n"
            f"2. DETAILED EXPLANATION: 2-3 paragraphs\n"
            f"3. REAL-WORLD EXAMPLES: At least 2 examples\n"
            f"4. KEY TAKEAWAYS: 3 bullet points\n\n"
            f"Question: {user_question}\n\n"
            f"Be accurate, clear, and suitable for a computer science student."
        )

    else:
        # Default fallback
        return f"Answer this question: {user_question}"