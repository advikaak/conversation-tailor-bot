# Conversation Tailor Bot

A rule-based Python bot that detects tone/sentiment/urgency and adapts response style
(formal, casual, empathetic, motivational, concise business) while keeping conversations
aligned to a clear business goal (e.g., schedule a call, collect email, confirm donation, book demo).

## Why this exists
It mirrors real stakeholder conversations: be adaptive to different people **and** keep the dialog focused on an outcome.
This aligns with client-facing roles and sales training experience.

## Features
- Lightweight tone/sentiment/urgency detection via heuristics
- Style routing to 5 response modes
- Goal-aligned CTA
- CLI runner and optional Streamlit UI
- Tiny evaluation script with sample test cases

## Run (CLI)
```bash
python main.py
```

## Optional UI
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project layout
```
conversation-tailor-bot/
├─ README.md
├─ requirements.txt
├─ main.py
├─ classifier.py
├─ responder.py
├─ app.py
├─ data/
│  └─ keywords.yml   # optional future expansion
└─ tests/
   ├─ test_cases.json
   └─ eval.py
```

## Notes
- Heuristics are intentionally simple so you can explain the logic in interviews.
- You can expand detection by editing word lists in `classifier.py` or by loading from YAML later.
