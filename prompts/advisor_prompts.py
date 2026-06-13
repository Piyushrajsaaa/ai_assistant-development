# ============================================================
# prompts/advisor_prompts.py - Study Advisor Prompt Templates
# ============================================================

def get_advisor_prompt(style, user_query):
    """
    Returns a study advisor prompt based on selected style.
    
    Args:
        style (str): "quick" | "roadmap" | "expert"
        user_query (str): The study question from user
    
    Returns:
        str: Complete prompt string
    """

    if style == "quick":
        # --------------------------------------------------------
        # PROMPT 1: SHORT - CASUAL QUICK ADVICE
        # --------------------------------------------------------
        # Length     : 1 line
        # Tone       : Friendly, casual
        # Complexity : Low - gets straight to practical tips
        # Best for   : Quick motivation or study tips
        # Why it works: A casual tone feels approachable.
        #               Short prompt = concise, actionable advice.
        # --------------------------------------------------------
        return (
            f"Give 3 to 5 practical and actionable study tips for: {user_query}"
        )

    elif style == "roadmap":
        # --------------------------------------------------------
        # PROMPT 2: MEDIUM - STRUCTURED LEARNING ROADMAP
        # --------------------------------------------------------
        # Length     : 5 lines
        # Tone       : Mentoring, encouraging
        # Complexity : Medium - requests timeline and resources
        # Best for   : Students starting a new subject
        # Why it works: Asking for a "roadmap with timeline" forces
        #               the AI to think sequentially — Week 1, Week 2
        #               etc. — which is far more useful than general
        #               advice. Adding "free resources" adds value.
        # --------------------------------------------------------
        return (
            f"You are an experienced academic mentor.\n"
            f"Create a structured 4-week learning roadmap for: {user_query}\n\n"
            f"Include for each week:\n"
            f"- Specific topics to cover\n"
            f"- Recommended free resources (YouTube, websites, books)\n"
            f"- A small practice task or mini-project\n"
            f"- Estimated daily study time\n\n"
            f"Keep the tone encouraging and realistic for a busy student."
        )

    elif style == "expert":
        # --------------------------------------------------------
        # PROMPT 3: LONG - EXPERT COMPREHENSIVE STUDY PLAN
        # --------------------------------------------------------
        # Length     : 10+ lines
        # Tone       : Expert, authoritative, professional
        # Complexity : High - covers strategy, resources, pitfalls
        # Best for   : Interview prep, competitive exams, deep study
        # Why it works: Multi-section prompts produce multi-section
        #               responses. Asking about "common mistakes"
        #               adds unique value not found in simple prompts.
        #               This technique is called "multi-aspect prompting".
        # --------------------------------------------------------
        return (
            f"You are a senior software engineer and expert educator "
            f"with 15 years of teaching experience.\n\n"
            f"Provide a comprehensive study guide for: {user_query}\n\n"
            f"Structure your response with these sections:\n\n"
            f"1. OVERVIEW: Why this topic matters and real-world applications\n"
            f"2. PREREQUISITES: What to learn first before starting\n"
            f"3. CORE CONCEPTS: The 5 most important things to master\n"
            f"4. STUDY STRATEGY: Best approach (theory vs practice ratio)\n"
            f"5. RESOURCES: Top 3 books, top 3 websites, top 2 YouTube channels\n"
            f"6. PRACTICE PLAN: Daily/weekly practice schedule\n"
            f"7. COMMON MISTAKES: Top 3 mistakes beginners make and how to avoid them\n"
            f"8. MILESTONE CHECK: How to know you've truly learned this topic\n\n"
            f"Target audience: Computer Science student preparing for placement/internship."
        )

    else:
        return f"Give study advice for: {user_query}"