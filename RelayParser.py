#import models.py

class RelayParser:

    def parse_file(selfself):
        f = open('prints', 'r')
        output = f.readlines()
        f.close()

        for line in output:
            print line.strip()

    def main(self):
        self.parse_file()

if __name__ == "__main__":
    x = RelayParser()
    x.main()
