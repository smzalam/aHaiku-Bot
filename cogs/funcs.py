def getting_pos(db_rules):
    pos = []

    for i in db_rules:
        pos.append(i[0])

    return pos

def getting_rules(db_rules):
    rule = []

    for i in db_rules:
        rule.append(i[1])

    return rule