distros = [{"basedOn": ["ubuntu", "mx linux"]}, {"basedOn": [
    "endeavour os", "manjaro", "archcraft"]}, {"basedOn": ["redhat"]}]

for distro in distros:
    distro["basedOn"] = len(distro["basedOn"])

print(distros)
