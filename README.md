# Invest Diary (Streamlit)

Personal investment portfolio tracker built with Streamlit.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Main tabs

- Dashboard
- Record Input
- FX
- Company Info
- Company Comparison
- Company Score
- API Settings

## Daily auto snapshot (price refresh -> recalc -> save)

- In `API 설정` tab, enable `하루 1회 자동 실행 사용`.
- Logic:
  - Uses **yesterday's** holdings + cash as baseline.
  - Refreshes today's prices.
  - Recalculates total asset / total PnL.
  - Saves today's snapshot automatically.

For true unattended execution, run scheduler command once per day:

```bash
python daily_auto_snapshot.py
```

Force run (ignore hour/once-per-day guard):

```bash
python daily_auto_snapshot.py --force
```

## Security

- API keys are saved in local `portfolio.db` (not committed).
- `.gitignore` excludes:
  - `portfolio.db`, `*.db`, `*.sqlite*`
  - `.env*`, `.streamlit/secrets.toml`
  - personal workbook `내 주식자산.xlsx`
- App access is protected by password gate. Set one of:
  - `APP_PASSWORD = "your_password"`
  - `APP_PASSWORD_HASH = "sha256:<64-hex>"`

## Streamlit Community Cloud deployment

1. Open Streamlit Community Cloud and click `New app`.
2. Repository: `ssungjun83/invest_diary`
3. Branch: `main`
4. Main file path: `app.py`
5. Click `Deploy`

If you need API keys in deployed environment, configure them in Streamlit Cloud `Secrets`.
Also set app password in `Secrets` using `APP_PASSWORD` or `APP_PASSWORD_HASH`.

To keep GitHub auto-load/save working after Cloud restart, set these Secrets too:

```toml
GITHUB_SYNC_ENABLED = "true"
GITHUB_REPO = "owner/repo"
GITHUB_BRANCH = "main"
GITHUB_EXCEL_PATH = "portfolio_auto.xlsx"
GITHUB_TOKEN = "ghp_..."
```
