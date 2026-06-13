# ============================================================
# prompts/generate_prompts.py - Content Generation Prompts
# ============================================================

def get_generate_prompt(content_type, style, user_input):
    """
    Returns a content generation prompt.
    
    Args:
        content_type (str): "story" | "poem" | "essay" | "idea"
        style (str): "simple" | "detailed" | "structured"
        user_input (str): Topic or theme from user
    
    Returns:
        str: Complete prompt string
    """

    if style == "simple":
        # --------------------------------------------------------
        # PROMPT 1: SHORT - MINIMAL CREATIVE PROMPT
        # --------------------------------------------------------
        # Length     : 1 line
        # Tone       : Open, creative
        # Complexity : Low - gives AI full creative freedom
        # Best for   : Quick creative bursts, brainstorming
        # Why it works: Minimal constraints = maximum creativity.
        #               The AI fills in genre, style, and structure.
        # --------------------------------------------------------
        return f"Write a short creative {content_type} about: {user_input}"

    elif style == "detailed":
        # --------------------------------------------------------
        # PROMPT 2: MEDIUM - CHARACTER AND SETTING DRIVEN
        # --------------------------------------------------------
        # Length     : 5 lines
        # Tone       : Narrative, engaging
        # Complexity : Medium - adds storytelling elements
        # Best for   : Stories and poems with specific feel
        # Why it works: Providing narrative elements (character,
        #               setting, mood) guides the AI without
        #               restricting its creativity. This technique
        #               is called "creative scaffolding".
        # --------------------------------------------------------
        return (
            f"Write a creative and engaging {content_type} about: {user_input}\n\n"
            f"Guidelines:\n"
            f"- Include vivid descriptions and strong imagery\n"
            f"- Create an emotional connection with the reader\n"
            f"- Use an interesting narrative arc (beginning, middle, end)\n"
            f"- Length: 150-200 words\n"
            f"- Make it original and memorable"
        )

    elif style == "structured":
        # --------------------------------------------------------
        # PROMPT 3: LONG - GENRE + FORMAT + QUALITY SPECIFIED
        # --------------------------------------------------------
        # Length     : 8+ lines
        # Tone       : Professional writer tone
        # Complexity : High - specifies genre, structure, quality
        # Best for   : Essays, formal stories, academic content
        # Why it works: Acting as a "professional writer" persona
        #               elevates quality. Specifying structure
        #               (intro/body/conclusion) ensures completeness.
        #               This is called "persona + structure prompting".
        # --------------------------------------------------------
        return (
            f"You are a professional creative writer with 10 years of experience.\n"
            f"Write a high-quality {content_type} on the following topic: {user_input}\n\n"
            f"Requirements:\n"
            f"- Structure: Clear introduction, developed body, strong conclusion\n"
            f"- Style: Engaging, polished, and suitable for publication\n"
            f"- Length: 200-300 words\n"
            f"- Use literary devices (metaphor, imagery, or symbolism where appropriate)\n"
            f"- Ensure originality - avoid clichés\n"
            f"- End with a thought-provoking closing line\n\n"
            f"Topic: {user_input}"
        )

    else:
        return f"Write a {content_type} about: {user_input}"