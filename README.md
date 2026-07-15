# 🤖 Deedee — Rule-Based Chatbot

A simple rule-based chatbot developed as part of the **CodeAlpha Python Programming Internship** (Task 4: Basic Chatbot).

Deedee responds to everyday conversational inputs — greetings, mood check-ins, jokes, laughter, and more — using keyword-based pattern matching. It also remembers the user's name for the duration of the chat and can save the full conversation transcript to a file.

---

## ✨ Features

- 👋 Responds to greetings (hello, good morning, good night, etc.)
- 😊 Understands mood-related messages (happy, sad, tired, bored)
- 😂 Detects laughter (haha, lol, lmao, emojis) and reacts accordingly
- 🙋 Remembers the user's name during the conversation (e.g. "my name is Sara")
- 🕒 Tells the current time and date
- 😄 Tells jokes on request
- 🎨 Answers simple fun questions (favorite color, favorite food, age)
- 🔀 Multiple randomized replies per topic, so conversations feel less repetitive
- 📝 Saves the full chat transcript to a `.txt` file at the end (optional)
- 🎨 Optional colored terminal interface (works without Colorama as well)

---

## 🛠️ Technologies Used

- Python 3
- `random` module (for varied responses)
- `datetime` module (for time/date replies)
- Colorama (Optional)

---

## 📂 Project Structure

```text
CodeAlpha_Chatbot/
│── chatbot.py
│── README.md
```

> Chat transcripts (e.g. `chat_transcript_*.txt`) are generated automatically if you choose to save them, and are not part of the repository.

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python chatbot.py
```

5. Start chatting! Try saying things like:
   - `hello`
   - `my name is Sara`
   - `how are you`
   - `joke`
   - `haha that's funny`
   - `bye` (to end the chat)

**Optional:** Install Colorama for a colored terminal interface.

```bash
pip install colorama
```

The application also works correctly without Colorama (plain text mode).

---

## 🎯 Learning Outcomes

This project demonstrates the use of:

- Conditional Statements (if-elif logic via rule matching)
- Functions and Modular Programming
- Loops (continuous chat loop)
- Lists, Tuples, and Dictionaries
- Basic String Processing and Pattern Matching
- File Handling (saving chat transcripts)
- User Input Validation

---

## 👩‍💻 Developed By

**Saleha Shahid**
BS Electrical Engineering
University of Management and Technology (UMT)

---

## 📌 Internship

CodeAlpha – Python Programming Internship
