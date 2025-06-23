# GitHub to Asana Sync

A Python integration that automatically syncs **open GitHub issues** to **Asana tasks**, helping you streamline project tracking between development and management workflows.

---

## Features

- 🔄 Syncs open issues from GitHub Projects to Asana
- ✅ Prevents duplicates by storing processed issues in JSON
- 🔐 Uses `.env` for configuration and secrets
- 🧠 Uses GitHub GraphQL + Asana REST API
- 🧰 Lightweight, no database required (S3 JSON DB once live)

---

## Project Structure

```
GitHub-Asana/
├── src/
│   ├── main.py                     # Core logic for syncing
│   ├── __init__.py                 # Loads environment variables
│   └── util/
│       └── load_env.py             # Custom .env loader
├── env/
│   ├── .env                        # Secret config (ignored)
│   └── template.env                # Sample .env file
├── processed_github_issues.json    # Will be created when script is ran
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/github-asana-sync.git
cd github-asana-sync
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install python-dotenv requests
```

---

## Environment Configuration

Edit `env/.env` using the following template:

```env
# GitHub
GITHUB_TOKEN=your_github_token_here
GITHUB_PROJECT_ID=your_project_node_id_here

# Asana
ASANA_ACCESS_TOKEN=your_asana_token_here
ASANA_WORKSPACE_ID=your_workspace_id_here
ASANA_PROJECT_ID=your_asana_project_id_here

# Processed Issues File
PROCESSED_ISSUES_FILE=processed_github_issues.json
```

> **Important:** Keep your `.env` file safe and **do not commit** it.

---

## Running the Sync

From the root of the project, run:

```bash
python -m src.main
```

You'll see output like:

```
Starting GitHub to Asana sync at 2025-06-23T...
Found 0 previously processed issues
Found 2 open GitHub issues
Created Asana task for GitHub issue #42
Sync completed at 2025-06-23T...
```

---

## To Do

- [ ] Add CLI interface
- [ ] Add webhook trigger support
- [ ] Improve Asana task formatting
- [ ] Add support for issue comments
- [ ] Docker support
- [ ] S3 JSON Database to store processed issues

---

## License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to fork, contribute, and adapt!

---

## Contributions

Pull requests and feature ideas are welcome.  
Feel free to open an issue or PR!