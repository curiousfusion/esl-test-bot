# ESL Test Bot Starter

Clone this, populate your key, install dependencies, and run:
```bash
git clone https://github.com/<your‑username>/esl-test-bot.git
cd esl-test-bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env with your OpenAI key
uvicorn main:app --reload
