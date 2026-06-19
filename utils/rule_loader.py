def load_rules():
    rule_dict = {}
    with open("rules/dq_rules.txt") as f:
        for line in f:
            if "-" in line:
                rule_id, description = line.split("-", 1)
                rule_dict[rule_id.strip()] = description.strip()
    return rule_dict