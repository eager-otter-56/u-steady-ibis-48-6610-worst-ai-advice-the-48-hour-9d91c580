"""Write the one-line worst-AI-advice entry to the output directory."""
import os

ENTRY = "Of course! Impress your boss: reply-all 'Per my last email, I accept your apology,' attach your search history, and send before rereading."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
