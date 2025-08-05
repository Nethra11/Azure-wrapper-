import pandas as pd
import requests
import argparse
import logging
from concurrent.futures import ThreadPoolExecutor

# Logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

API_URL = "http://127.0.0.1:5000/chat"
AUTH_TOKEN = "Bearer my-secret-token"

def call_api(prompt, comment):
    payload = {"prompt": prompt, "comment": comment}
    headers = {"Authorization": AUTH_TOKEN}
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {
                "prompt": prompt,
                "comment": comment,
                "response": data["data"]["output"]
            }
        else:
            logging.error(f"API Error: {response.status_code}")
            return {
                "prompt": prompt,
                "comment": comment,
                "response": "API Error"
            }
    except Exception as e:
        logging.error(f"Connection Error: {e}")
        return {
            "prompt": prompt,
            "comment": comment,
            "response": f"Error: {e}"
        }

def process_file(input_path, output_path):
    df = pd.read_excel(input_path)
    logging.info(f"Loaded {len(df)} prompts from {input_path}")

    results = []

    def process_row(row):
        prompt = str(row.get("prompt", "")).strip()
        comment = str(row.get("comment", "")).strip()
        logging.info(f"Sending: {prompt} | {comment}")
        return call_api(prompt, comment)

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_row, [row for _, row in df.iterrows()]))

    df_out = pd.DataFrame(results)
    df_out.to_excel(output_path, index=False)
    logging.info(f"Results saved to {output_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input Excel file")
    parser.add_argument("--output", required=True, help="Output Excel file")
    args = parser.parse_args()

    process_file(args.input, args.output)

if __name__ == "__main__":
    main()
