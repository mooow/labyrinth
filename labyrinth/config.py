from sys import argv as args
import logging

class Configure(object):
    DEFAULT_PROBABILITY = 0.15
    DEFAULT_DELAY = 0.005

    def __init__(self, height, width):
        self.height = height
        self.width  = width
        self.maxrows = self.height - 2
        self.maxcols =  (self.width-1)//2
        self.conf = {
            'rows': self.maxrows,
            'cols': self.maxcols,
            'delay': Configure.DEFAULT_DELAY,
            'prob': Configure.DEFAULT_PROBABILITY,
            'log': "INFO"
        }
        self.__parse_args__()
        self.__validate__()

    def __parse_args__(self):
        i = 1
        while i < len(args):
            if args[i].startswith('--'):
                arg = args[i].replace('--', '')
                if arg not in self.conf.keys():
                    self.usage()
                self.conf[arg] = args[i+1]
                i += 2
            else: self.usage()

    def usage(self):
        print("""Usage: {} [option [value]] ...

--rows rows         -- Labyrinth's number of rows
--cols columns      -- Labyrinth's number of columns
--delay delay       -- Delay after a move (in seconds). Default: {}
--prob probability  -- Probability of walls. Default: {}
--log loglevel      -- Sets the verbosity of logging. Default: INFO""".format(
                            args[0],
                            Configure.DEFAULT_DELAY,
                            Configure.DEFAULT_PROBABILITY))
        exit(1)

    def __validate__(self):
        self.conf['rows']  =  int(self.conf['rows'])
        self.conf['cols']  =  int(self.conf['cols'])
        self.conf['prob']  =  float(self.conf['prob'])
        self.conf['delay'] =  float(self.conf['delay'])

        if not 3 <= self.conf['rows'] <= self.maxrows:
            print("Invalid number of rows, using max:", self.maxrows)
            self.conf['rows'] = self.maxrows

        if not 3 <= self.conf['cols'] <= self.maxcols:
            print("Invalid number of columns, using max:", self.maxcols)
            self.conf['cols'] = self.maxcols

        if self.conf['delay'] < 0: self.conf['delay'] *= -1

        if not 0 <= self.conf['prob'] <= 1:
            print("Probabilities must belong in interval [0,1], using default")
            self.conf['prob'] = Configure.DEFAULT_PROBABILITY

        loglevel = self.conf['log']
        numeric_level = getattr(logging, loglevel.upper(), logging.INFO)
        logging.basicConfig(level=numeric_level)
