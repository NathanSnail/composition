import functools

defs = {"<greek>": "<Multi_key> <g>", "<math>": "<Multi_key> <m>"}
with open("compose_src.XCompose", "r", encoding="utf-8") as f:
    base = f"# REAL FILE IN COMPOSITION CODE\n{f.read()}"
    remapped = functools.reduce(lambda a, b: a.replace(b[0], b[1]), defs.items(), base)
    out = ""
    lines = remapped.split("\n")
    while len(lines) > 0:
        first = lines[0]
        lines = lines[1:]
        if "<!" not in first:
            out += first + "\n"
            continue
        parts = first.split("<!")
        s = parts[1].split(">")
        parts[1] = s[0].upper() + ">" + ">".join(s[1:])
        lines.append("<".join(parts))
        parts[1] = s[0].lower() + ">" + ">".join(s[1:])
        lines.append("<".join(parts))

    with open("compose_out.XCompose", "w", encoding="utf-8") as file:
        file.write(out)
