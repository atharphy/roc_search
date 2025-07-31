import re

def parse_roc_entries(line):
    match = re.search(r'(\w+_SEC\d+_LYR\d+_LDR\w+_MOD\d+)_ROC\[(\d+):(\d+)\]', line)
    if not match:
        return []
    base = match.group(1)
    start = int(match.group(2))
    end = int(match.group(3))
    return [f"{base}_ROC{i}" for i in range(start, end + 1)]

def search_lines(lines, search_terms, blacklist_only=False):
    results = []
    for line in lines:
        line_lower = line.lower()
        if all(term.lower() in line_lower for term in search_terms):
            if blacklist_only and "blacklisted" not in line_lower:
                continue
            roc_entries = parse_roc_entries(line)
            if roc_entries:
                results.append({
                    'line': line.strip(),
                    'rocs': roc_entries
                })
    return results

def save_results_to_file(results, filename, show_original):
    with open(filename, 'w') as f:
        for entry in results:
            if show_original:
                f.write(entry['line'] + '\n')
            for roc in entry['rocs']:
                f.write(f"  {roc}\n")
    print(f"\n Results saved to '{filename}'")

def get_input_lines():
    method = input("Load data from file (f) or paste manually (p)? [f/p]: ").strip().lower()
    if method == 'f':
        filename = input("Enter path to the text file: ").strip()
        try:
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            exit(1)
    elif method == 'p':
        print("\nPaste your text below. When done, type a single line with 'END' and press Enter.")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line + '\n')
        return lines
    else:
        print("Invalid choice. Please enter 'f' or 'p'.")
        return get_input_lines()

def main():
    print("=== ROC Search Tool ===\n")
    lines = get_input_lines()

    while True:
        query = input("\nEnter search terms (e.g., 'FED LYR2 BpO'), or type 'exit' to quit: ").strip()
        if query.lower() == 'exit':
            print("Goodbye!")
            break

        search_terms = query.split()
        blacklist_filter = input("Only show BLACKLISTED entries? (y/n): ").strip().lower() == 'y'
        show_original = input("Show original full entries? (y/n): ").strip().lower() == 'y'
        save_output = input("Save results to a file? (y/n): ").strip().lower() == 'y'

        results = search_lines(lines, search_terms, blacklist_only=blacklist_filter)

        if not results:
            print("No matches found.")
            continue

        print(f"\nFound {len(results)} matching entries:\n")
        for entry in results:
            if show_original:
                print(entry['line'])
            for roc in entry['rocs']:
                print(f"  {roc}")

        if save_output:
            out_name = input("Enter output filename (e.g., 'results.txt'): ").strip()
            save_results_to_file(results, out_name, show_original)

if __name__ == "__main__":
    main()
