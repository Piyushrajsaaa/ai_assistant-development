# ============================================================
# test_cases.py - Formal Test Cases for All 4 Functions
# ============================================================
# Run: python test_cases.py
# This tests every function with multiple inputs and styles.
# ============================================================

from services.qa_service        import answer_question
from services.summarize_service import summarize_text
from services.generate_service  import generate_content
from services.advisor_service   import get_study_advice

PASS = "✅ PASS"
FAIL = "❌ FAIL"

def run_test(test_name, result, expect_failure=False):
    """
    Checks if a service result is valid and prints status.
    
    Args:
        test_name      (str) : Description of the test
        result         (dict): Return value from service function
        expect_failure (bool): True for edge cases that should fail
    """
    if expect_failure:
        # For edge cases — we EXPECT success=False (validation working)
        if not result["success"]:
            print(f"✅ PASS | {test_name} → validation working correctly")
        else:
            print(f"❌ FAIL | {test_name} → should have been rejected!")
    else:
        if result["success"] and len(result["response"]) > 10:
            print(f"✅ PASS | {test_name}")
        else:
            print(f"❌ FAIL | {test_name} → {result['response']}")


print("\n" + "="*60)
print("   AI ASSISTANT — FORMAL TEST CASES")
print("="*60)

# ── FUNCTION 1: Question Answering ──────────────────────────
print("\n📌 FUNCTION 1: Question Answering")
print("-"*40)

run_test("QA | Simple      | What is Python?",
    answer_question("What is Python?", "simple"))

run_test("QA | Educational | Explain OOP concepts",
    answer_question("Explain OOP concepts", "educational"))

run_test("QA | Detailed    | What is Artificial Intelligence?",
    answer_question("What is Artificial Intelligence?", "detailed"))

# Edge case — empty input should be rejected
run_test("QA | Edge        | Empty input handled",
    answer_question("", "simple"), expect_failure=True)

# ── FUNCTION 2: Text Summarization ──────────────────────────
print("\n📌 FUNCTION 2: Text Summarization")
print("-"*40)

sample = """
Machine learning is a subset of artificial intelligence that provides 
systems the ability to automatically learn and improve from experience 
without being explicitly programmed. It focuses on the development of 
computer programs that can access data and use it to learn for themselves. 
The process begins with observations or data to look for patterns in data 
and make better decisions in the future.
"""

run_test("Summarize | Quick    | ML paragraph",
    summarize_text(sample, "quick"))

run_test("Summarize | Bullet   | ML paragraph",
    summarize_text(sample, "bullet"))

run_test("Summarize | Academic | ML paragraph",
    summarize_text(sample, "academic"))

# Edge case — too short text should be rejected
run_test("Summarize | Edge     | Too short text handled",
    summarize_text("Hello world", "quick"), expect_failure=True)

# ── FUNCTION 3: Content Generation ──────────────────────────
print("\n📌 FUNCTION 3: Content Generation")
print("-"*40)

run_test("Generate | Simple     | Poem about autumn",
    generate_content("autumn", "poem", "simple"))

run_test("Generate | Detailed   | Story about a robot",
    generate_content("a robot learning to paint", "story", "detailed"))

run_test("Generate | Structured | Essay about AI",
    generate_content("impact of AI on education", "essay", "structured"))

run_test("Generate | Idea       | Science fiction novel",
    generate_content("time travel paradox", "idea", "simple"))

# ── FUNCTION 4: Study Advisor ────────────────────────────────
print("\n📌 FUNCTION 4: Study Advisor")
print("-"*40)

run_test("Advisor | Quick   | DSA tips",
    get_study_advice("Data Structures and Algorithms", "quick"))

run_test("Advisor | Roadmap | Machine Learning",
    get_study_advice("Machine Learning for beginners", "roadmap"))

run_test("Advisor | Expert  | System Design interviews",
    get_study_advice("System Design interview preparation", "expert"))

# ── Summary ─────────────────────────────────────────────────
print("\n" + "="*60)
print("   TEST RUN COMPLETE — 13 Tests | 13 Expected PASS")
print("="*60 + "\n")