import pandas as pd
import requests
import argparse

API_URL = 'http://127.0.0.1:5000/chat'

def call_api(prompt, comment):
    payload = {"prompt": prompt, "comment": comment}
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            return {
                "Prompt": prompt,
                "Comment": comment,
                "Response": data["data"]["output"],
                "Score": data["data"]["score"]
            }
        else:
            return {
                "Prompt": prompt,
                "Comment": comment,
                "Response": "API Error",
                "Score": "N/A"
            }
    except Exception as e:
        return {
            "Prompt": prompt,
            "Comment": comment,
            "Response": f"Connection Error: {e}",
            "Score": "N/A"
        }

def save_to_file(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"✅ Results saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Excel Prompt Processor")
    parser.add_argument("--input", required=True, help="Path to the input Excel file")
    parser.add_argument("--output", required=True, help="Path to save the output Excel file")

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output

    df_in = pd.read_excel(input_file)

    results = []
    for i, row in df_in.iterrows():
        prompt = str(row.get("Prompt", "")).strip()
        comment = str(row.get("Comment", "")).strip()

        print(f"👉 Sending row {i+1}: Prompt = {prompt}, Comment = {comment}")
        result = call_api(prompt, comment)
        print(f"✅ Got response: {result['Response']}")
        results.append(result)

    save_to_file(results, output_file)

if __name__ == "__main__":
    main()
