import Slate.slate as slate

site = slate.Site()
site.name = "CLUB ENIGMA"
site.description = '''Club Enigma is the distinguished research-funded technical club at the Indian Institute of Information Technology Sri-City (IIITS) that is dedicated to pushing the boundaries of technology through practical, hands-on projects.
At Enigma, we believe in the power of doing, and our primary focus is on Computer Graphics, Cybersecurity, Distributed Systems, and System Software.'''
site.picture = "pfp.png"

site.blogs.append(slate.Blog("Welcome to Club Enigma!", "welcome.md", False))

cg_series = slate.Series("Computer Graphics")
cg_series.blogs.append(slate.Blog("Introduction to Computer Graphics", "cg/cg_intro.md", True))
site.blogs.append(cg_series)

site.contacts.append(slate.Contact.github("https://github.com/Enigma-IIITS"))
site.contacts.append(slate.Contact.instagram("https://instagram.com/enigmaiiits"))
site.contacts.append(slate.Contact.linkedin("https://www.linkedin.com/company/enigmaiiits"))
site.contacts.append(slate.Contact.mail("enigma.club@iiits.in"))
site.copyright = "© 2023 Club Enigma"
slate.generate_site(site)
