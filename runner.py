import json
from typing import List, Dict


def load_steps(path: str) -> List[Dict[str, str]]:
    """Load a scenario JSON file and return list of steps."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Scenario file must contain a list of steps")
    return data


def run_steps(steps: List[Dict[str, str]]) -> None:
    """Execute the given steps using Playwright."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for step in steps:
            action = step.get("action")
            if action == "goto":
                page.goto(step["url"])
            elif action == "click":
                page.click(step["selector"])
            elif action == "fill":
                page.fill(step["selector"], step["text"])
            else:
                raise ValueError(f"Unknown action: {action}")
        browser.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run a simple web scenario")
    parser.add_argument("scenario", help="Path to scenario JSON file")
    args = parser.parse_args()
    steps = load_steps(args.scenario)
    run_steps(steps)
