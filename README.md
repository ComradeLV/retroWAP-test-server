# retroWAP Test Server

Minimal local WML server used to exercise retroWAP's rendering and navigation.

## Purpose
- Serve a single WML deck over HTTP with the correct content-type.
- Provide a stable, small deck that covers the core WML features retroWAP currently supports.

## What's Served
`server.py` responds to:
- `/` and `/index.wml` with `index.wml`
- Content-Type: `text/vnd.wap.wml; charset=utf-8`

## Deck Contents (index.wml)
Cards and elements included:

1. `main` card (title: "retroWAP Demo")
    - Text formatting: `<b>`, `<i>`, `<u>`, `<big>`, `<small>`
    - Line break: `<br/>`
    - Anchor links to other cards: `<a href="#form">`, `<a href="#nav">`
    - Action: `<do type="accept" label="Go Form"><go href="#form"/></do>`

2. `form` card (title: "Inputs")
    - Text inputs:
        - `<input name="username" type="text" value="guest"/>`
        - `<input name="password" type="password"/>`
        - `<input name="pin" type="numeric"/>`
    - Selects:
        - Single select `<select name="color">` with options
        - Multi-select `<select name="fruits" multiple="true">` with a preselected option
    - `<textarea name="notes">` with default text
    - Link back to main card

3. `nav` card (title: "Navigation")
    - Anchor link back to main
    - `<do type="prev" label="Back"><prev/></do>` action

## What This Tests
- WML parsing for cards, actions, and text nodes
- Inline formatting and line breaks
- Anchor navigation within a deck (`#fragment`)
- `<do>` actions including `accept` and `prev`
- Form widgets and value collection
- Variable substitution is not explicitly covered in this deck

## How To Run
Requirements:
- Python 3.x

Run:
```bash
python3 server.py
```

Open in retroWAP:
```
http://localhost:8080/index.wml
```

## Configuration
Change the port by editing `PORT` in `server.py`.
