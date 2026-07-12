# claude-agent-portfolio
claude-agent-portfolio/              ← one GitHub repo, three agents
├── README.md                        ← top-level: what this is, how to run each
├── .env.example
├── requirements.txt
├── .github/workflows/ci.yml         ← lint + smoke test on push
├── agents/
│   ├── discovery_analyzer/
│   │   ├── agent.py
│   │   ├── README.md
│   │   └── sample_input/transcript.txt
│   ├── battlecard/
│   │   ├── agent.py
│   │   ├── README.md
│   │   └── sample_output/example_battlecard.md
│   └── poc_architect/
│       ├── agent.py
│       ├── README.md
│       └── sample_output/architecture.png
└── shared/
    └── client.py                    ← one Anthropic client setup, reused by all three
