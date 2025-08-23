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
  {"action": "fill", "selector": "#search", "text": "hello"},
  {"action": "wait_for_selector", "selector": "#result"},
  {"action": "assert_url_contains", "text": "example"}
]
```
Supported actions: `goto`, `click`, `fill`, `wait_for_selector`, `assert_url_contains`.

### Example: open a YouTube video

`youtube_scenario.json` demonstrates navigating to the YouTube homepage, clicking the first
video link, and asserting that the browser lands on a watch page:

```json
[
  {"action": "goto", "url": "https://www.youtube.com"},
  {"action": "wait_for_selector", "selector": "ytd-rich-grid-media a#video-title"},
  {"action": "click", "selector": "ytd-rich-grid-media a#video-title"},
  {"action": "wait_for_selector", "selector": "ytd-watch-flexy"},
  {"action": "assert_url_contains", "text": "watch"}
]
```

## Testing

Unit tests cover loading of scenario files:
```bash
pytest
```
