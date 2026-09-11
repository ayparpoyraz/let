# res200

A simple Python HTTP login request-response tool.

Made for learning Python, HTTP requests, and web security.

## Usage

```bash
python3 let.py \
    --url http://127.0.0.1:5000 \
    --username ayparr \
    --range 10000 \
    --zfill 4 \
    --username-parser username \
    --password-parser password
```

### Arguments

* `--url` → Target URL
* `--username` → Username
* `--range` → Number range
* `--zfill` → Password digit count
* `--username-parser` → HTML username field
* `--password-parser` → HTML password field

## Requirements

```bash
pip install requests beautifulsoup4 colorama
```
