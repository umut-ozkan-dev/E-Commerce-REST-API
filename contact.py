FILEPATH = "./pages/contact.html"


with open(FILEPATH, "r", encoding="utf-8") as file:
    raw_html = file.read()
    contact_page = raw_html.replace("{{name}}", "UmutÖZKAN")
