# ============================================================
# test_services.py - Quick Service Test (Delete after testing)
# ============================================================

from services.qa_service import answer_question
from services.summarize_service import summarize_text
from services.generate_service import generate_content
from services.advisor_service import get_study_advice

print("\n--- Testing QA Service ---")
result = answer_question("What is Python programming?", "simple")
print(result["response"][:200])   # Print first 200 chars

print("\n--- Testing Summarize Service ---")
sample_text = """
Artificial Intelligence is the simulation of human intelligence 
by machines. It includes learning, reasoning, and self-correction. 
AI is used in many fields including healthcare, finance, education, 
and transportation. Machine learning is a subset of AI that allows 
systems to learn from data without being explicitly programmed.
"""
result = summarize_text(sample_text, "bullet")
print(result["response"][:200])

print("\n--- Testing Generate Service ---")
result = generate_content("a robot learning to paint", "poem", "simple")
print(result["response"][:200])

print("\n--- Testing Advisor Service ---")
result = get_study_advice("Data Structures and Algorithms", "quick")
print(result["response"][:200])

print("\n✅ All services working!")