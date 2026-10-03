const task = document.getElementById("task");
const inputText = document.getElementById("inputText");
const submitBtn = document.getElementById("submitBtn");
const result = document.getElementById("result");
const status = document.getElementById("status");
const copyBtn = document.getElementById("copyBtn");

const endpoints = {
    qa: "/qa",
    explain: "/explain",
    quiz: "/quiz",
    summarize: "/summarize",
    learn: "/learn/recommendations"
};

submitBtn.addEventListener("click", async () => {
    const text = inputText.value.trim();
    if (!text) {
        status.textContent = "Please enter some text first.";
        return;
    }

    submitBtn.disabled = true;
    status.textContent = "EduGenie is thinking...";
    result.textContent = "";

    try {
        const response = await fetch(endpoints[task.value], {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text})
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Request failed.");
        }

        renderResult(data.result);
        status.textContent = "Done.";
    } catch (error) {
        result.textContent = error.message;
        status.textContent = "Something went wrong.";
    } finally {
        submitBtn.disabled = false;
    }
});

function renderResult(data) {
    if (task.value !== "quiz" || !Array.isArray(data)) {
        result.textContent = data;
        return;
    }

    result.innerHTML = "";
    data.forEach((item, index) => {
        const box = document.createElement("div");
        box.className = "quiz-question";

        const title = document.createElement("strong");
        title.textContent = `${index + 1}. ${item.question}`;
        box.appendChild(title);

        item.options.forEach(option => {
            const optionDiv = document.createElement("div");
            optionDiv.className = "quiz-option";
            optionDiv.textContent = option;
            box.appendChild(optionDiv);
        });

        const answer = document.createElement("div");
        answer.style.marginTop = "10px";
        answer.textContent = `Correct answer: ${item.answer}`;
        box.appendChild(answer);

        result.appendChild(box);
    });
}

copyBtn.addEventListener("click", async () => {
    try {
        await navigator.clipboard.writeText(result.innerText);
        status.textContent = "Result copied.";
    } catch {
        status.textContent = "Copy is not available in this browser.";
    }
});

task.addEventListener("change", () => {
    const placeholders = {
        qa: "Example: What is the largest ocean?",
        explain: "Example: Pythagoras theorem",
        quiz: "Paste a passage or topic for 3 MCQs.",
        summarize: "Paste the educational passage you want summarized.",
        learn: "Example: SQL"
    };
    inputText.placeholder = placeholders[task.value];
});
