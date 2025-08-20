# easy-website-test

This repository provides a minimal example of running scripted browser actions.
Steps are described in a JSON scenario file and executed with [Playwright](https://playwright.dev/).

## Usage

1. Install dependencies (requires network access):
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
2. Create a scenario JSON file or use `example_scenario.json`.
3. Run the scenario:
   ```bash
   python runner.py example_scenario.json
   ```

## Scenario format

A scenario is a list of steps:
```json
[
  {"action": "goto", "url": "https://example.com"},
  {"action": "click", "selector": "text=More information"},
  {"action": "fill", "selector": "#search", "text": "hello"}
]
```
Supported actions: `goto`, `click`, `fill`.

## Testing

Unit tests cover loading of scenario files:
```bash
pytest
```
