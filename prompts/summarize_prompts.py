# ============================================================
# prompts/summarize_prompts.py - Summarization Prompt Templates
# ============================================================

def get_summarize_prompt(style, text):
    """
    Returns a summarization prompt based on selected style.
    
    Args:
        style (str): "quick" | "bullet" | "academic"
        text (str): The text to summarize
    
    Returns:
        str: Complete prompt string
    """

    if style == "quick":
        # --------------------------------------------------------
        # PROMPT 1: SHORT - ONE LINE SUMMARY REQUEST
        # --------------------------------------------------------
        # Length     : 1 line
        # Tone       : Neutral, casual
        # Complexity : Low
        # Best for   : Getting the gist of a paragraph quickly
        # Why it works: Minimal instruction lets the AI decide
        #               what's most important naturally.
        # --------------------------------------------------------
        return f"Summarize the following text in 2-3 sentences:\n\n{text}"

    elif style == "bullet":
        # --------------------------------------------------------
        # PROMPT 2: MEDIUM - BULLET POINT EXTRACTION
        # --------------------------------------------------------
        # Length     : 4 lines
        # Tone       : Professional, structured
        # Complexity : Medium - specifies format (bullet points)
        # Best for   : Quick review before an exam or meeting
        # Why it works: Requesting bullet points forces the AI to
        #               identify distinct, separate key ideas rather
        #               than blending them into prose.
        # --------------------------------------------------------
        return (
            f"Read the following text carefully and extract the key information.\n"
            f"Present your response as:\n"
            f"- 5 to 7 clear bullet points\n"
            f"- Each bullet should be one complete sentence\n"
            f"- Focus on facts, not opinions\n\n"
            f"Text: {text}"
        )

    elif style == "academic":
        # --------------------------------------------------------
        # PROMPT 3: LONG - ACADEMIC SUMMARY WITH CONSTRAINTS
        # --------------------------------------------------------
        # Length     : 7+ lines
        # Tone       : Formal, analytical
        # Complexity : High - word limit + audience + structure
        # Best for   : Writing assignments, research notes
        # Why it works: Adding constraints (word limit, audience,
        #               structure) forces precision. Specifying the
        #               audience changes vocabulary and depth.
        #               This is called "constrained generation".
        # --------------------------------------------------------
        return (
            f"You are an academic writing assistant.\n"
            f"Write a formal summary of the text below following these rules:\n\n"
            f"- Word limit: 100-150 words\n"
            f"- Audience: University professor or researcher\n"
            f"- Structure: Opening sentence stating the topic, "
            f"body with main points, closing sentence with conclusion\n"
            f"- Tone: Formal and objective (no first person)\n"
            f"- Highlight: Any technical terms or key concepts\n\n"
            f"Text to summarize:\n{text}"
        )

    else:
        return f"Summarize this text: {text}"