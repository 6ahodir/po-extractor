# Each message ID and STR are assumed to be on a single line

PO_FILE = ''  # TODO: add file path here

in_ = []
out = []
msg_id = msg_str = ""

with open(PO_FILE) as f:
    for line in f.readlines():
        if line.startswith('msgid "'):
            msg_id = line.lstrip('msgid "').rstrip().rstrip('"').strip()  # remove msgid, and "s
        elif line.startswith('msgstr "'):
            msg_str = line.lstrip('msgstr "').rstrip().rstrip('"').strip()  # remove msgstr, and "s
            if msg_id and msg_str:
                in_.append(msg_id)
                out.append(msg_str)
            msg_id = msg_str = ""

with open("corpus.in", 'w') as f:
    for l in in_:
        f.write("%s\n" % l)

with open("corpus.out", 'w') as f:
    for l in out:
        f.write("%s\n" % l)

