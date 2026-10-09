"""Riche News email builder.

Renders every issue in ISSUES (issues.py) into out/<slug>.html using the
Riche News format: cream newsprint body, VIERICHE masthead, question headline,
data chart, problem/solution cards, product blocks, black Riche Worldwide footer.

Usage: python3 build.py
"""
import html
import os

from issues import ISSUES

SITE = "https://www.vie-riche.com"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")

CSS = """
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Inter:wght@400;500;600&display=swap");
body{margin:0;padding:0;background:#fdf3ea;-webkit-text-size-adjust:100%}
table{border-collapse:collapse}
img{border:0;display:block;outline:none;text-decoration:none}
a{color:#111}
.serif{font-family:"Playfair Display",Georgia,"Times New Roman",serif}
.sans{font-family:"Inter",Arial,Helvetica,sans-serif}
.mast{font-family:"Playfair Display",Georgia,serif;font-size:44px;letter-spacing:14px;color:#111;font-weight:400}
.rule{border-top:1px solid #111;border-bottom:1px solid #111;height:3px;font-size:0;line-height:0}
.kick{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-weight:700;font-size:15px;color:#111}
.issue{font-family:"Inter",Arial,sans-serif;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:#6b5f55}
h1{font-family:"Playfair Display",Georgia,serif;font-size:40px;line-height:1.08;font-weight:700;color:#111;margin:0;text-align:center}
h1 em{font-style:italic}
h2{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-size:34px;line-height:1.05;font-weight:400;color:#111;margin:0}
.p{font-family:"Playfair Display",Georgia,serif;font-size:16px;line-height:1.55;color:#2a2420;margin:0}
.p strong{font-weight:700}
.small{font-family:"Inter",Arial,sans-serif;font-size:11px;line-height:1.6;color:#6b5f55}
.pill{display:block;background:#111;color:#fdf3ea !important;font-family:"Playfair Display",Georgia,serif;font-size:20px;font-weight:700;text-decoration:none;text-align:center;border-radius:999px;padding:16px 20px;text-transform:uppercase}
.pill-o{display:block;border:2px solid #fdf3ea;color:#fdf3ea !important;font-family:"Playfair Display",Georgia,serif;font-size:18px;text-decoration:none;text-align:center;border-radius:999px;padding:12px 20px;text-transform:uppercase}
.card{background:#2b2826;border-radius:28px}
.card-t{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-size:22px;color:#fdf3ea}
.card-b{font-family:"Playfair Display",Georgia,serif;font-size:14px;line-height:1.5;color:#d9cfc6}
.bar-l{font-family:"Inter",Arial,sans-serif;font-size:12px;font-weight:600;color:#111;text-transform:uppercase;letter-spacing:1px}
.bar-v{font-family:"Playfair Display",Georgia,serif;font-size:16px;font-weight:700;color:#111}
.stat-n{font-family:"Playfair Display",Georgia,serif;font-size:40px;font-weight:900;color:#111;line-height:1}
.stat-l{font-family:"Inter",Arial,sans-serif;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#6b5f55}
.pname{font-family:"Playfair Display",Georgia,serif;font-size:18px;font-weight:700;color:#111;line-height:1.15}
.pprice{font-family:"Inter",Arial,sans-serif;font-size:13px;color:#2a2420}
.tag{display:inline-block;background:#111;color:#fdf3ea;font-family:"Inter",Arial,sans-serif;font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;padding:4px 10px;border-radius:999px}
.tag-r{background:#8c1c13}
.plink{font-family:"Inter",Arial,sans-serif;font-size:12px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:#111 !important;text-decoration:underline}
.foot-logo{font-family:"Playfair Display",Georgia,serif;color:#fdf3ea;font-size:30px;letter-spacing:6px}
.foot-sub{font-family:"Inter",Arial,sans-serif;color:#bdb3aa;font-size:10px;letter-spacing:4px;text-transform:uppercase}
.legal{font-family:"Inter",Arial,sans-serif;font-size:10px;line-height:1.8;color:#8a817a}
.legal a{color:#bdb3aa}
.afterpay{background:#b2fce4}
.ap{font-family:"Inter",Arial,sans-serif;font-size:15px;font-weight:600;color:#111;line-height:1.3}
@media (max-width:480px){
 .mast{font-size:30px !important;letter-spacing:9px !important}
 h1{font-size:30px !important}
 h2{font-size:27px !important}
 .col{display:block !important;width:100% !important;box-sizing:border-box}
 .stat-n{font-size:32px !important}
 .px{padding-left:22px !important;padding-right:22px !important}
}
"""


def esc(s):
    return html.escape(s, quote=True)


def url(path, campaign, content):
    base = path if path.startswith("http") else SITE + path
    sep = "&" if "?" in base else "?"
    return (f"{base}{sep}utm_source=klaviyo&amp;utm_medium=email"
            f"&amp;utm_campaign={campaign}&amp;utm_content={content}")


def row(inner, pad="0 40px", bg=None):
    bga = f' bgcolor="{bg}" style="background:{bg};"' if bg else ""
    return f'<tr><td class="px" style="padding:{pad};"{bga}>{inner}</td></tr>\n'


def spacer(h):
    return f'<tr><td style="height:{h}px;font-size:0;line-height:0;">&nbsp;</td></tr>\n'


# ---- blocks -------------------------------------------------------------

def b_masthead(issue, _c):
    return (
        row('<div class="mast" style="text-align:center;">VIERICHE</div>', "34px 20px 10px")
        + row('<div class="rule">&nbsp;</div>', "0 40px")
        + row(f'<div style="text-align:center;"><span class="kick">Riche News</span>'
              f'<br><span class="issue">No. {esc(issue["no"])} &middot; {esc(issue["date_label"])}</span></div>',
              "10px 40px 0")
    )


def b_headline(b, _c):
    return row(f'<h1>{b["html"]}</h1>', "26px 34px 6px")


def b_text(b, _c):
    align = b.get("align", "center")
    return row(f'<p class="p" style="text-align:{align};">{b["html"]}</p>', b.get("pad", "14px 46px"))


def b_section(b, _c):
    sub = f'<p class="p" style="margin-top:12px;">{b["sub"]}</p>' if b.get("sub") else ""
    return row(f'<h2>{b["html"]}</h2>{sub}', "34px 40px 6px")


def b_button(b, c):
    return row(f'<a class="pill" href="{url(b["href"], c, b["utm"])}" target="_blank">{b["text"]}</a>',
               "22px 70px")


def b_rule(_b, _c):
    return row('<div style="border-top:1px solid #111;font-size:0;line-height:0;">&nbsp;</div>', "18px 40px")


def b_chart(b, c):
    mx = max(r[1] for r in b["rows"])
    any_thumb = any(len(r) > 3 for r in b["rows"])
    rows = ""
    for r in b["rows"]:
        label, val, shown = r[:3]
        p = r[3] if len(r) > 3 else None
        w = max(4, round(val / mx * 100))
        thumb = '<td style="width:44px;padding:5px 10px 5px 0;">&nbsp;</td>' if any_thumb else ""
        if p:
            thumb = ('<td style="padding:5px 10px 5px 0;width:44px;vertical-align:middle;">'
                     f'<a href="{url(p["path"], c, "chart_" + p["utm"])}" target="_blank">'
                     f'<img src="{p["img"]}" width="44" height="44" alt="{esc(p["name"])}" '
                     'style="width:44px;height:44px;object-fit:cover;border-radius:8px;"></a></td>')
        rows += (
            '<tr>' + thumb +
            f'<td class="bar-l" style="padding:7px 10px 7px 0;width:38%;vertical-align:middle;">{esc(label)}</td>'
            '<td style="padding:7px 0;vertical-align:middle;">'
            f'<table role="presentation" width="{w}%" cellpadding="0" cellspacing="0"><tr>'
            '<td style="background:#111;height:18px;font-size:0;line-height:0;border-radius:0 9px 9px 0;">&nbsp;</td>'
            '</tr></table></td>'
            f'<td class="bar-v" style="padding:7px 0 7px 10px;width:58px;text-align:right;vertical-align:middle;">{esc(shown)}</td>'
            '</tr>'
        )
    title = f'<p class="issue" style="text-align:center;margin:0 0 12px;">{esc(b["title"])}</p>' if b.get("title") else ""
    src = f'<p class="small" style="text-align:center;margin:12px 0 0;">{esc(b["source"])}</p>' if b.get("source") else ""
    return row(f'{title}<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows}</table>{src}',
               "22px 40px 6px")


def b_stats(b, _c):
    cells = ""
    w = int(100 / len(b["items"]))
    for n, l in b["items"]:
        cells += (f'<td class="col" width="{w}%" style="text-align:center;padding:10px 6px;vertical-align:top;">'
                  f'<div class="stat-n">{esc(n)}</div><div class="stat-l" style="margin-top:6px;">{esc(l)}</div></td>')
    return row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{cells}</tr></table>',
               "18px 30px")


def b_cards(b, _c):
    out = ""
    for t, body in b["items"]:
        out += (
            '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="card" '
            'style="background:#2b2826;border-radius:28px;margin:0 0 14px;"><tr>'
            '<td style="padding:22px 24px 22px 26px;">'
            '<table role="presentation" cellpadding="0" cellspacing="0"><tr>'
            '<td style="width:3px;background:#fdf3ea;font-size:0;">&nbsp;</td>'
            f'<td style="padding-left:14px;"><div class="card-t">{t}</div>'
            f'<div class="card-b" style="margin-top:6px;">{body}</div></td>'
            '</tr></table></td></tr></table>'
        )
    return row(out, "18px 30px 4px")


def b_image(b, c):
    img = (f'<img src="{b["src"]}" width="600" alt="{esc(b["alt"])}" '
           'style="width:100%;max-width:600px;height:auto;">')
    if b.get("href"):
        img = f'<a href="{url(b["href"], c, b["utm"])}" target="_blank">{img}</a>'
    cap = f'<p class="small" style="text-align:center;margin:10px 0 0;padding:0 30px;">{esc(b["caption"])}</p>' if b.get("caption") else ""
    return row(img + cap, b.get("pad", "18px 0 0"))


def _tag(p):
    if not p.get("tag"):
        return ""
    cls = "tag tag-r" if p.get("hot") else "tag"
    return f'<span class="{cls}">{esc(p["tag"])}</span><br>'


def b_feature(b, c):
    p = b["product"]
    href = url(p["path"], c, p["utm"])
    return row(
        f'<a href="{href}" target="_blank"><img src="{p["img"]}" width="520" alt="{esc(p["name"])}" '
        'style="width:100%;max-width:520px;height:auto;border-radius:18px;"></a>'
        f'<div style="padding:16px 4px 0;">{_tag(p)}'
        f'<div class="pname" style="font-size:24px;margin-top:8px;">{esc(p["name"])}</div>'
        f'<div class="pprice" style="margin-top:6px;">{esc(p["price"])}</div>'
        + (f'<p class="p" style="margin-top:10px;font-size:15px;">{p["blurb"]}</p>' if p.get("blurb") else "")
        + f'<div style="margin-top:14px;"><a class="plink" href="{href}" target="_blank">{esc(p.get("cta", "Shop it"))} &rarr;</a></div></div>',
        "20px 40px 10px",
    )


def b_grid(b, c):
    items = b["products"]
    trs = ""
    for i in range(0, len(items), 2):
        tds = ""
        for p in items[i:i + 2]:
            href = url(p["path"], c, p["utm"])
            tds += (
                '<td class="col" width="50%" style="width:50%;padding:0 8px 26px;vertical-align:top;">'
                f'<a href="{href}" target="_blank"><img src="{p["img"]}" width="252" alt="{esc(p["name"])}" '
                'style="width:100%;max-width:252px;height:auto;border-radius:14px;"></a>'
                f'<div style="padding-top:12px;">{_tag(p)}'
                f'<div class="pname" style="margin-top:6px;">{esc(p["name"])}</div>'
                f'<div class="pprice" style="margin-top:4px;">{esc(p["price"])}</div>'
                f'<div style="margin-top:10px;"><a class="plink" href="{href}" target="_blank">Shop &rarr;</a></div>'
                '</div></td>'
            )
        if len(items[i:i + 2]) == 1:
            tds += '<td class="col" width="50%" style="width:50%;">&nbsp;</td>'
        trs += f"<tr>{tds}</tr>"
    return row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{trs}</table>',
               "18px 22px 0")


def b_vote(b, c):
    cells = ""
    for i, (name, hexc) in enumerate(b["options"]):
        href = url(b["href"], c, "vote_" + name.lower().replace(" ", "_"))
        cells += (
            '<td class="col" width="50%" style="padding:5px;">'
            f'<a href="{href}" target="_blank" style="display:block;text-decoration:none;border:1px solid #111;'
            'border-radius:999px;padding:11px 14px;font-family:Inter,Arial,sans-serif;font-size:13px;font-weight:600;'
            'letter-spacing:1px;text-transform:uppercase;color:#111;">'
            f'<span style="display:inline-block;width:14px;height:14px;border-radius:7px;background:{hexc};'
            f'vertical-align:middle;margin-right:10px;border:1px solid #111;"></span>{esc(name)}</a></td>'
        )
        if i % 2 == 1 and i < len(b["options"]) - 1:
            cells += "</tr><tr>"
    return row(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{cells}</tr></table>',
               "14px 34px")


def b_strip(b, c):
    tds = ""
    for p in b["products"]:
        href = url(p["path"], c, "strip_" + p["utm"])
        tds += ('<td width="33%" style="width:33%;padding:0 5px;vertical-align:top;text-align:center;">'
                f'<a href="{href}" target="_blank"><img src="{p["img"]}" width="170" alt="{esc(p["name"])}" '
                'style="width:100%;max-width:170px;height:auto;border-radius:12px;margin:0 auto;"></a>'
                f'<a href="{href}" target="_blank" style="text-decoration:none;"><div class="pname" '
                f'style="font-size:13px;margin-top:8px;">{esc(p["name"])}</div>'
                f'<div class="pprice" style="font-size:12px;margin-top:2px;">{esc(p["price"])}</div></a></td>')
    title = f'<p class="issue" style="text-align:center;margin:0 0 12px;">{esc(b["title"])}</p>' if b.get("title") else ""
    return row(f'{title}<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{tds}</tr></table>',
               "18px 25px 6px")


BLOCKS = {
    "headline": b_headline, "text": b_text, "section": b_section, "button": b_button,
    "rule": b_rule, "chart": b_chart, "stats": b_stats, "cards": b_cards, "image": b_image,
    "feature": b_feature, "grid": b_grid, "vote": b_vote, "strip": b_strip,
}


def footer(c):
    btns = ""
    for text, path, utm in [("VR CORE", "/collections/vie-riche-core", "footer_core"),
                            ("NEW ITEMS", "/collections/new-arrivals", "footer_new"),
                            ("ON SALE", "/collections/sale", "footer_sale")]:
        btns += (f'<tr><td style="padding:0 0 12px;"><a class="pill-o" href="{url(path, c, utm)}" '
                 f'target="_blank">{text}</a></td></tr>')
    return (
        spacer(30)
        + '<tr><td bgcolor="#000000" style="background:#000;padding:40px 70px 34px;text-align:center;" class="px">'
        '<div class="foot-logo">RICHE</div><div class="foot-sub" style="margin-top:6px;">Worldwide &middot; Est. 2013</div>'
        f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:28px;">{btns}</table>'
        '</td></tr>\n'
        '<tr><td class="afterpay" bgcolor="#b2fce4" style="background:#b2fce4;padding:20px 34px;">'
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
        '<td class="ap">Shop now. Pay later.<br>Always interest-free.</td>'
        '<td style="text-align:right;font-family:Inter,Arial,sans-serif;font-size:22px;font-weight:700;color:#111;">afterpay</td>'
        '</tr></table></td></tr>\n'
        '<tr><td bgcolor="#000000" style="background:#000;padding:22px 30px 30px;text-align:center;">'
        f'<p class="legal" style="margin:0;"><a href="https://www.instagram.com/viericheparis" target="_blank">Instagram</a>'
        f' &nbsp;&middot;&nbsp; <a href="{url("/", c, "footer_site")}" target="_blank">vie-riche.com</a></p>'
        '<p class="legal" style="margin:6px 0 0;">{{ organization.name }} &middot; {{ organization.full_address }}</p>'
        '<p class="legal" style="margin:6px 0 0;">{% unsubscribe \'Unsubscribe\' %}</p>'
        '</td></tr>\n'
    )


def render(issue):
    c = issue["utm_campaign"]
    body = b_masthead(issue, c)
    for b in issue["blocks"]:
        body += BLOCKS[b["type"]](b, c)
    body += b_strip(dict(title=issue.get("strip_title", "Most wanted right now"),
                         products=issue["most_wanted"]), c)
    body += footer(c)
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="x-apple-disable-message-reformatting">\n'
        f'<title>{esc(issue["title"])} | Riche News</title>\n<style>{CSS}</style>\n</head>\n'
        '<body style="margin:0;padding:0;background:#fdf3ea;">\n'
        f'<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">{esc(issue["preview"])}</div>\n'
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" bgcolor="#fdf3ea" style="background:#fdf3ea;">'
        '<tr><td align="center">\n'
        '<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:100%;max-width:600px;background:#fdf3ea;">\n'
        f'{body}'
        '</table>\n</td></tr></table>\n</body>\n</html>\n'
    )


def plaintext(issue):
    lines = [f'RICHE NEWS No. {issue["no"]} | {issue["date_label"]}', "", issue["title"].upper(), "", issue["preview"], ""]
    for b in issue["blocks"]:
        if b["type"] == "button":
            lines.append(f'{html.unescape(b["text"])}: {SITE}{b["href"]}')
        if b["type"] in ("feature",):
            p = b["product"]
            lines.append(f'{p["name"]} ({p["price"]}): {SITE}{p["path"]}')
        if b["type"] == "grid":
            for p in b["products"]:
                lines.append(f'{p["name"]} ({p["price"]}): {SITE}{p["path"]}')
    lines += ["", "{{ organization.name }}, {{ organization.full_address }}", "{% unsubscribe 'Unsubscribe' %}"]
    return "\n".join(lines)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for issue in ISSUES:
        with open(os.path.join(OUT, issue["slug"] + ".html"), "w") as f:
            f.write(render(issue))
        with open(os.path.join(OUT, issue["slug"] + ".txt"), "w") as f:
            f.write(plaintext(issue))
        print(issue["slug"], len(render(issue)))
