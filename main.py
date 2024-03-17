import functools

defs = {"<dead_greek>": "<MultiKey> <G>"}
with open("compose_src","r",encoding="utf-8") as f:
    c = f"# REAL FILE IN COMPOSITION CODE\n{f.read()}"
    v = functools.reduce(lambda a,b: a.replace(b[0], b[1]), defs.items(), c)
    with open("compose_out","w",encoding="utf-8") as o:
        o.write(v)
