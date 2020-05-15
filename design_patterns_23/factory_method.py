# !/usr/bin/python
# coding:utf8
'''
Factory Method
'''


class ChinaGetter:
    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    """Simply echoes the msg ids"""

    def get(self, msgid):

        if msgid == "parrot":
            return str(msgid)+"ssssss"
        return str(msgid)


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    print(languages)
    print("------")
    return languages[language]()


# Create our localizers
e, g = get_localizer("English"), get_localizer("China")
print(e,g)
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(msgid)
    print(e.get(msgid), g.get(msgid))
