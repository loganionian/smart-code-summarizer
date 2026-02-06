import argparse
from .main import summarize_function_code, summarize_module_code

def main():
    parser = argparse.ArgumentParser(description="Summarize code.")
    parser.add_argument("code", help="Code to summarize")
    parser.add_argument("--function", action="store_true", help="Summarize function code")
    parser.add_argument("--module", action="store_true", help="Summarize module code")
    args = parser.parse_args()

    if args.function:
        summary = summarize_function_code(args.code)
    elif args.module:
        summary = summarize_module_code(args.code)
    else:
        summary = "Please specify --function or --module."

    print(summary)

if __name__ == "__main__":
    main()