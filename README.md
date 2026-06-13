⚡ F.R.I.D.A.Y — Local Voice AI Assistant






A fully offline, voice-controlled AI assistant built using Python, integrating local LLMs (Ollama), speech recognition, and system automation. Designed as a privacy-first alternative to cloud-based assistants.

🚀 Overview

F.R.I.D.A.Y is a modular AI assistant that runs completely locally on your machine. It listens to voice commands, processes them using a local LLM, and executes system-level tasks like opening apps, searching the web, and automating workflows.

Unlike cloud-based assistants, it ensures:

🔒 No data leaves your device
⚡ No API costs
🧠 Fully customizable AI behavior
🎯 Core Capabilities
🎙️ Voice-based interaction (Speech-to-Text + Text-to-Speech)
🤖 Local LLM reasoning via Ollama (Llama models)
💾 Persistent memory using JSON-based storage
🌐 Web browsing and automation
⌨️ Mouse & keyboard control (GUI automation)
🧠 Context-aware conversations
⏰ System utilities (time, apps, tasks)
🧠 System Architecture

F.R.I.D.A.Y follows a modular AI pipeline:

1. Voice Input Layer

Captures microphone input using SpeechRecognition

2. Memory Manager

Stores and retrieves conversation history from memory.json

3. LLM Engine (Ollama)

Processes user input using local Llama model

4. Action Parser

Detects whether the response is:
Conversational reply
System command (open app, search, etc.)

5. Execution Layer

Performs automation using PyAutoGUI / system libraries

6. Voice Output

Converts response to speech using pyttsx3

📁 Project Structure

friday-ai-assistant/
│
├── main.py              # Core assistant logic
├── config.py            # Configuration settings
├── memory.json          # Persistent memory storage
├── test.py              # Testing script
├── tests/
│   └── test_main.py     # Unit tests
├── screenshot.png      # System preview
└── README.md


⚙️ Installation
1. Clone Repository
git clone https://github.com/anirudh657/friday-ai-assistant.git
cd friday-ai-assistant
2. Install Dependencies
pip install pyttsx3 SpeechRecognition pyautogui pywhatkit requests ollama

⚠️ If SpeechRecognition fails, install PyAudio separately.

3. Install Local LLM (Ollama)
ollama run llama3
▶️ Run the Assistant
python main.py

Make sure:

Microphone is enabled
Ollama is running in background
💬 Example Commands
“Open YouTube”
“Search AI news”
“What time is it?”
“Play music on YouTube”
“Remember my favorite color is blue”
“What did I tell you earlier?”
📸 Output Preview

Add screenshot.png in repository root to display system UI/output

🔄 Execution Flow

User speaks → Microphone captures audio
→ Speech converted to text
→ Memory context loaded
→ Input sent to Ollama LLM
→ Response generated
→ Action detected (if any)
→ System executes command
→ Response spoken aloud
→ Memory updated

📈 Future Enhancements
Wake word detection (“Hey F.R.I.D.A.Y”)
Real-time screen understanding (computer vision)
Web-based GUI dashboard
Faster inference optimization
IoT / smart home integration
Multi-model support (switch between LLMs)
⚠️ Limitations
Performance depends on CPU/GPU capability
Background noise affects speech accuracy
GUI automation requires active unlocked screen
Ollama model must be running locally
👨‍💻 Author

Anirudh
B.Tech Computer Science Engineering Student

GitHub: https://github.com/anirudh657

⭐ Support

If you like this project, consider starring the repository ⭐
