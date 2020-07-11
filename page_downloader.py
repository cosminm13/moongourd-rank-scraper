import requests

def download(url):
    page = requests.get(url, verify=False)
    source = page.text
    source = source.split('\n')

    output_file = open("input.html", encoding="utf8", mode="w")
    for line in source:
        for c in line:
            output_file.write(c)
    output_file.close()
