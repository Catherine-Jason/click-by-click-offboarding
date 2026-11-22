"""Keeps the Content Security Policy in index.html and demo.html in step with their script and styles.

The policy only lets a page run the exact script and styles that are in it, using a hash of each.
Any change to a <script> or <style> block changes its hash, and the browser then refuses to run it,
so run this after every change:

    python tools/update-csp.py           writes the new hashes into the pages
    python tools/update-csp.py --check   only checks, and exits with 1 if any hash is out of date

It uses only Python's standard library and changes nothing but the script-src and style-src hashes.
A page with no script has no script-src, so the default-src 'none' rule blocks every script there.
"""
import base64, hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [p for p in (ROOT / "index.html", ROOT / "demo.html") if p.exists()]

def sha(text):
    # browsers hash the text after turning every line ending into \n
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return "'sha256-" + base64.b64encode(hashlib.sha256(text.encode("utf-8")).digest()).decode() + "'"

def update(page, name):
    meta = re.search(r'<meta http-equiv="Content-Security-Policy" content="([^"]*)">', page)
    if not meta: raise SystemExit("No Content Security Policy meta tag found in " + name + ".")
    content = meta.group(1)
    for directive, tag in (("script-src", "script"), ("style-src", "style")):
        blocks = re.findall(r"<%s>(.*?)</%s>" % (tag, tag), page, re.S)
        if re.search(directive + r" ", content):
            if not blocks: raise SystemExit(name + " has " + directive + " but no <" + tag + "> block.")
            content = re.sub(directive + r" [^;]*", directive + " " + " ".join(sha(b) for b in blocks), content)
        elif blocks:
            raise SystemExit(name + " has a <" + tag + "> block but no " + directive + " in its policy.")
    return page[:meta.start(1)] + content + page[meta.end(1):]

if __name__ == "__main__":
    check = "--check" in sys.argv; stale = []
    for p in PAGES:
        raw = p.read_bytes().decode("utf-8"); new = update(raw, p.name)
        if new != raw:
            stale.append(p.name)
            if not check: p.write_bytes(new.encode("utf-8"))
    if check:
        if stale: print("The Content Security Policy hashes are out of date in " + ", ".join(stale) + ". Run: python tools/update-csp.py"); sys.exit(1)
        print("The Content Security Policy hashes match the script and styles in " + ", ".join(p.name for p in PAGES) + "."); sys.exit(0)
    print(("Updated the Content Security Policy hashes in " + ", ".join(stale) + ".") if stale else "The Content Security Policy hashes were already up to date.")
