distro = {
    "name": "ubuntu",
    "releaseType": ["LTS", "point release"],
    "packageManager": "apt"
}

distro["releaseDate"] = "2004"
del distro["packageManager"]
print("dictionary: ")
print(distro)
print("dictionary item:")
print(distro.items())
for key, value in distro.items():
    print(f"{key}: {value}")

linux = [{"name": "ubuntu", "packageManager": "apt"}, {"name": "fedora"}]
