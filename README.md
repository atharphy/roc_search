# ROC Search Tool

This Python script allows you to search and extract specific masked ROC (Read-Out Chip) entries from a list provided in a text format. It supports filtering based on user-defined search terms, optional BLACKLISTED filtering, original line display, and result export.

## Features

- Search using any combination of terms like `FED`, `BPix`, `LYR`, `SEC`, `MOD`, etc.
- Expand ROC ranges such as `ROC[4:7]` to `ROC4`, `ROC5`, `ROC6`, `ROC7`
- Filter for only `BLACKLISTED` entries (optional)
- Choose whether to display the full original entry
- Load data from a text file or paste it directly into the terminal
- Optionally save the results to an output file

## Requirements

- Python 3.x

No external packages are required.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/atharphy/roc-search-tool.git
cd roc-search-tool
```

### 2. Run the Script

```bash
python roc_search.py
```

If you have multiple versions of Python installed, you may need to use:

```bash
python3 roc_search.py
```

### 3. Choose Input Method

When prompted:

```
Load data from file (f) or paste manually (p)? [f/p]:
```

- Press `f` to load a `.txt` file containing your ROC list.
- Press `p` to paste the list directly into the terminal. After pasting the list, press `Enter`, then type `END` and press `Enter` again to finish.

### 4. Enter Search Terms

You will be asked to provide search terms like:

```
FED LYR2 BpO
```

The script will match all lines containing all these terms, case-insensitively.

### 5. Additional Options

You will be prompted for:

- Filtering only `BLACKLISTED` entries
- Displaying the original matched lines
- Saving the results to a file

### 6. Exit

Type `exit` when asked for search terms to quit the script.

## Example

Given a line in the list like:

```
FED 1215 channel 41 -> BPix_BpO_SEC2_LYR2_LDR3F_MOD3_ROC[0:3] - BLACKLISTED
```

And you search:

```
BpO SEC2 LYR2
```

The script will output:

```
  BPix_BpO_SEC2_LYR2_LDR3F_MOD3_ROC0
  BPix_BpO_SEC2_LYR2_LDR3F_MOD3_ROC1
  BPix_BpO_SEC2_LYR2_LDR3F_MOD3_ROC2
  BPix_BpO_SEC2_LYR2_LDR3F_MOD3_ROC3
```

