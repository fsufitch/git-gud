import argparse, pyfiglet, sys

class git(object):
    @staticmethod
    def parse_args(cmdname):
        parser = argparse.ArgumentParser(description="Have you been told to 'get %s'? Now you can!" % cmdname)
        parser.add_argument("name", metavar="NAME", type=str, nargs="?", default=None,
                            help="who is getting %s" % cmdname)
        parser.add_argument("-s", "--super", action="store_true", default=False,
                            help="get super %s" % cmdname)
        args = parser.parse_args()
        return args

    @staticmethod
    def fig(text):
        fig = pyfiglet.Figlet()
        return fig.renderText(text)
    
    @staticmethod
    def gud():
        args = git.parse_args("good")
        name = args.name or "You"
        sup = args.super
        text = "{name} {verb} now {qual} gud!".format(name=name,
                                                      verb="is" if args.name else "are",
                                                      qual="super" if sup else "so")
        if sup:
            text = git.fig(text)
        print(text)

    @staticmethod
    def rekt():
        args = git.parse_args("rekt")
        name = args.name or "You"
        sup = args.super
        text = "{name} got {qual}#rekt!".format(name=name,
                                                qual="super " if sup else "")
        if sup:
            text = git.fig(text)
        print(text)
