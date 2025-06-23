\# 🚀 GitHub to Asana Sync

A Python integration that automatically syncs \*\*open GitHub issues\*\* to \*\*Asana tasks\*\*, helping you streamline project tracking between development and management workflows.

\---

\## 📦 Features

\- 🔄 Syncs open issues from GitHub Projects to Asana

\- ✅ Prevents duplicates by storing processed issues

\- 🔐 Uses \`.env\` for configuration and secrets

\- 🧠 Uses GitHub GraphQL + Asana REST API

\- 🧰 Lightweight, no database required

\---

\## 🗂️ Project Structure

GitHub-Asana/

├── src/

│ ├── main.py # Core logic for syncing

│ ├── init.py # Loads environment variables

│ └── util/

│ └── load\_env.py # Custom .env loader

├── env/

│ ├── .env # Secret config (ignored)

│ └── template.env # Sample .env file

├── processed\_github\_issues.json

├── .gitignore

└── README.md

yaml

\---

\## ⚙️ Setup Instructions

\### 1. Clone the repository

\`\`\`bash

git clone https://github.com/YOUR\_USERNAME/github-asana-sync.git

cd github-asana-sync

2\. Create and activate a virtual environment

bash

python -m venv venv

source venv/bin/activate # macOS/Linux

venv\\Scripts\\activate # Windows

3\. Install dependencies

bash

pip install -r requirements.txt

Or manually install:

bash


pip install python-dotenv requests

🔐 Environment Configuration

Edit env/.env using the following template:

env

\# GitHub

GITHUB\_TOKEN=your\_github\_token\_here

GITHUB\_PROJECT\_ID=your\_project\_node\_id\_here

\# Asana

ASANA\_ACCESS\_TOKEN=your\_asana\_token\_here

ASANA\_WORKSPACE\_ID=your\_workspace\_id\_here

ASANA\_PROJECT\_ID=your\_asana\_project\_id\_here

\# Processed Issues File

PROCESSED\_ISSUES\_FILE=processed\_github\_issues.json

Important: Keep your .env file safe and do not commit it.

▶️ Running the Sync

From the root of the project, run:

bash

Copy

Edit

python -m src.main

You'll see output like:

yaml


Starting GitHub to Asana sync at 2025-06-23T...

Found 0 previously processed issues

Found 2 open GitHub issues

Created Asana task for GitHub issue #42

Sync completed at 2025-06-23T...

🚧 To Do

Add CLI interface

Add webhook trigger support

Improve Asana task formatting

Add support for issue comments

Docker support

📜 License

Licensed under the MIT License.

Feel free to fork, contribute, and adapt!

🙌 Contributions

Pull requests and feature ideas are welcome.

Feel free to open an issue or PR!

yaml


\---

Let me know if you’d like this saved into a file and staged for a commit, or if you'd like a version that includes CI setup, badges, or Docker instruction