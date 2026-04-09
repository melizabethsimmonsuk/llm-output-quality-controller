import json
import argparse

DIMENSIONS = [
    "accuracy",
    "relevance",
    "clarity",
    "completeness",
    "instruction_adherence",
    "safety"
]

def total_score(scores):
    return sum(scores.values())

def generate_markdown(data):
    md = "# AI Output Evaluation Report\n\n"

    for item in data:
        scores_a = item["scores_a"]
        scores_b = item["scores_b"]

        total_a = total_score(scores_a)
        total_b = total_score(scores_b)

        preferred = "A" if total_a > total_b else "B"

        md += f"## Prompt\n{item['prompt']}\n\n"
        md += f"### Response A\n{item['response_a']}\n\n"
        md += f"### Response B\n{item['response_b']}\n\n"

        md += "### Scores\n\n"
        md += "| Dimension | A | B |\n"
        md += "|---|---:|---:|\n"

        for d in DIMENSIONS:
            md += f"| {d} | {scores_a[d]} | {scores_b[d]} |\n"

        md += f"\n**Total A:** {total_a}  \n"
        md += f"**Total B:** {total_b}  \n"
        md += f"**Preferred:** Response {preferred}\n\n"
        md += "---\n\n"

    return md

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    with open(args.input, "r") as f:
        data = json.load(f)

    report = generate_markdown(data)

    with open(args.output, "w") as f:
        f.write(report)

    print("Report generated successfully.")

if __name__ == "__main__":
    main()
