/* ============================================================
   main.js - Frontend JavaScript for AI Assistant
   ============================================================
   Handles:
   - Sending requests to Flask backend (fetch API)
   - Displaying AI responses
   - Prompt style selection
   - Feedback submission
   ============================================================ */

/* ============================================================
   UTILITY FUNCTIONS
   ============================================================ */

/**
 * Shows the loading state on the submit button.
 * Disables button and shows a spinner while waiting for AI.
 */
function setLoading(isLoading) {
  const btn = document.getElementById("submitBtn");
  const spinner = document.getElementById("spinner");
  const btnText = document.getElementById("btnText");

  if (isLoading) {
    btn.disabled = true;
    spinner.style.display = "block";
    btnText.textContent = "Generating...";
  } else {
    btn.disabled = false;
    spinner.style.display = "none";
    btnText.textContent = "Generate Response";
  }
}

/**
 * Displays the AI response in the response card.
 * Also shows the feedback section below it.
 */
function showResponse(text) {
  const responseCard = document.getElementById("responseCard");
  const responseText = document.getElementById("responseText");
  const feedbackSection = document.getElementById("feedbackSection");

  responseText.textContent = text;
  responseCard.classList.add("visible");
  feedbackSection.classList.add("visible");

  // Scroll to the response smoothly
  responseCard.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

/**
 * Handles the prompt style selector buttons.
 * Clicking a style button marks it selected and updates hidden input.
 */
function initStyleSelector() {
  const styleBtns = document.querySelectorAll(".style-btn");

  styleBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      // Remove selected from all
      styleBtns.forEach((b) => b.classList.remove("selected"));
      // Mark this one selected
      this.classList.add("selected");
      // Update the hidden input with the selected style value
      document.getElementById("selectedStyle").value = this.dataset.style;
    });
  });
}

/**
 * Sends feedback (yes/no) to the backend.
 */
async function sendFeedback(endpoint, userInput, aiResponse, wasHelpful) {
  try {
    await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_input: userInput,
        ai_response: aiResponse,
        was_helpful: wasHelpful,
      }),
    });

    // Hide buttons, show thank you message
    document.querySelector(".feedback-buttons").style.display = "none";
    document.getElementById("feedbackThanks").style.display = "block";
  } catch (error) {
    console.error("Feedback error:", error);
  }
}

/* ============================================================
   FUNCTION 1 — QUESTION ANSWERING
   ============================================================ */
async function handleQA() {
  const question = document.getElementById("questionInput").value.trim();
  const style = document.getElementById("selectedStyle").value;

  if (!question) {
    alert("Please enter a question.");
    return;
  }

  setLoading(true);

  try {
    const res = await fetch("/qa/answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, style }),
    });
    const data = await res.json();

    if (data.success) {
      showResponse(data.response);
      // Store for feedback
      window._lastInput = question;
      window._lastResponse = data.response;
    } else {
      showResponse("⚠️ " + data.response);
    }
  } catch (err) {
    showResponse("⚠️ Network error. Please check your connection.");
  } finally {
    setLoading(false);
  }
}

/* ============================================================
   FUNCTION 2 — TEXT SUMMARIZATION
   ============================================================ */
async function handleSummarize() {
  const text = document.getElementById("textInput").value.trim();
  const style = document.getElementById("selectedStyle").value;

  if (!text) {
    alert("Please enter some text to summarize.");
    return;
  }

  setLoading(true);

  try {
    const res = await fetch("/summarize/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, style }),
    });
    const data = await res.json();

    if (data.success) {
      showResponse(data.response);
      window._lastInput = text;
      window._lastResponse = data.response;
    } else {
      showResponse("⚠️ " + data.response);
    }
  } catch (err) {
    showResponse("⚠️ Network error. Please check your connection.");
  } finally {
    setLoading(false);
  }
}

/* ============================================================
   FUNCTION 3 — CONTENT GENERATION
   ============================================================ */
async function handleGenerate() {
  const topic = document.getElementById("topicInput").value.trim();
  const contentType = document.getElementById("contentType").value;
  const style = document.getElementById("selectedStyle").value;

  if (!topic) {
    alert("Please enter a topic or theme.");
    return;
  }

  setLoading(true);

  try {
    const res = await fetch("/generate/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic, content_type: contentType, style }),
    });
    const data = await res.json();

    if (data.success) {
      showResponse(data.response);
      window._lastInput = topic;
      window._lastResponse = data.response;
    } else {
      showResponse("⚠️ " + data.response);
    }
  } catch (err) {
    showResponse("⚠️ Network error. Please check your connection.");
  } finally {
    setLoading(false);
  }
}

/* ============================================================
   FUNCTION 4 — STUDY ADVISOR
   ============================================================ */
async function handleAdvisor() {
  const query = document.getElementById("queryInput").value.trim();
  const style = document.getElementById("selectedStyle").value;

  if (!query) {
    alert("Please enter a topic you want study advice for.");
    return;
  }

  setLoading(true);

  try {
    const res = await fetch("/advisor/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query, style }),
    });
    const data = await res.json();

    if (data.success) {
      showResponse(data.response);
      window._lastInput = query;
      window._lastResponse = data.response;
    } else {
      showResponse("⚠️ " + data.response);
    }
  } catch (err) {
    showResponse("⚠️ Network error. Please check your connection.");
  } finally {
    setLoading(false);
  }
}

/* ============================================================
   PAGE INITIALIZATION
   Runs when the page fully loads
   ============================================================ */
document.addEventListener("DOMContentLoaded", function () {
  // Initialize style selector buttons on every page
  initStyleSelector();

  // Set default button text based on page
  const btnText = document.getElementById("btnText");
  if (btnText) btnText.textContent = "Generate Response";
});
