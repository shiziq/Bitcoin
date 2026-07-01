f = open(r"C:\Users\User\Batolink\4. Bitcoin_Cryptocurrency\Consultancy Agreement — Batolink Global Limited & Consultant.html", encoding="utf-8")
c = f.read(); f.close()

dark = c.count('class="page dark"')
light = c.count('class="page light"')
print(f"Total pages: {dark + light} ({dark} dark, {light} light)")
print(f"Total chars: {len(c):,}")

checks = [
    ("height: 297mm", "Fixed height A4"),
    ("min-height: 297mm", "Min height A4"),
    ("width: 210mm", "Fixed width"),
    ("overflow: hidden", "Overflow hidden"),
    ("page-break-after: always", "Page break after"),
    ("@page { size: A4", "A4 print size"),
]
for pattern, label in checks:
    print(f"  [{'OK' if pattern in c else 'XX'}] {label}")

divs_open = c.count("<div")
divs_close = c.count("</div>")
if divs_open != divs_close:
    print(f"  DIV MISMATCH: {divs_open} opens vs {divs_close} closes (diff={divs_open - divs_close})")
else:
    print(f"  DIV tags: {divs_open} open = {divs_close} close (OK)")

p_open = c.count("<p")  # matches <p> and <p style=...>
p_close = c.count("</p>")
if p_open != p_close:
    print(f"  P tags: {p_open} open vs {p_close} close (diff={p_open - p_close})")

h3_count = c.count("<h3>") + c.count("<h3 ")
print(f"  h3 headings: {h3_count}")

h4_count = c.count("<h4>") + c.count("<h4 ")
print(f"  h4 headings: {h4_count}")

# Check for inline styles that might break layout
inline_styles = c.count('style="')
print(f"  Inline style attributes: {inline_styles}")

# Last 200 chars
print(f"\nFile ends with (last 200 chars):")
print(c[-200:-1] if c.endswith('\n') else c[-200:])
