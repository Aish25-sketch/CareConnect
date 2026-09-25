// Both forms follow the same small send-and-confirm pattern.
document.querySelectorAll("form[data-endpoint]").forEach((form) => {
    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const responseText = document.getElementById(form.dataset.response);
        const values = Object.fromEntries(new FormData(form));

        try {
            const response = await fetch(form.dataset.endpoint, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(values)
            });
            const result = await response.json();
            responseText.textContent = result.message;
            if (response.ok) form.reset();
        } catch {
            responseText.textContent = "We couldn’t send that just now. Please try again.";
        }
    });
});

// A keyword-based FAQ helper; it works without an AI service or account.
function askFAQ() {
    const input = document.getElementById("faqInput");
    const question = input.value.trim();
    if (!question) return;

    const messages = document.getElementById("chatMessages");
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = question;
    messages.append(userMessage);

    const lowerQuestion = question.toLowerCase();
    let answer = "I don’t know that one yet. Send a note through the support form and the team can help.";

    if (lowerQuestion.includes("volunteer")) {
        answer = "Use the volunteer form to tell us what you’d like to help with. Our team can follow up by email.";
    } else if (lowerQuestion.includes("support") || lowerQuestion.includes("help") || lowerQuestion.includes("medical")) {
        answer = "Use the support form to share what you need. A team member can follow up with you.";
    } else if (lowerQuestion.includes("contact") || lowerQuestion.includes("reach") || lowerQuestion.includes("email")) {
        answer = "Send us a note through the support form and the team can get back to you.";
    } else if (lowerQuestion.includes("thank")) {
        answer = "You’re welcome. I’m glad I could point you in the right direction.";
    }

    const botMessage = document.createElement("div");
    botMessage.className = "bot-message";
    botMessage.textContent = answer;
    messages.append(botMessage);
    input.value = "";
    messages.scrollTop = messages.scrollHeight;
}

document.getElementById("askButton").addEventListener("click", askFAQ);
document.getElementById("faqInput").addEventListener("keydown", (event) => {
    if (event.key === "Enter") askFAQ();
});
