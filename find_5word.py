import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--positions', help='set postion letter: a=3,p=5')
parser.add_argument('-n', '--nonpositions', help='set non pos letter: a=4,p=1')
parser.add_argument('-i', '--in', help='set letter in word: a,e,o')
parser.add_argument('-u', '--nonin', help='set letters non in word: к,л,м')
args = parser.parse_args()


def conv_pos(arg: str | None):
    if arg:
        return { int(b): a for a, b in [i.split('=') for i in arg.split(',')]}
    else:
        return None


def conv_non_pos(arg: str | None):
    res = {}
    if arg:
        for a, b in [i.split('=') for i in arg.split(',')]:
            if k := res.get(a):
                res[a].append(int(b))
            else:
                res[a] = [int(b)]
        return res
    else:
        return None


def conv_in_uin(arg: str | None):
    if arg:
        return [i for i in arg.split(',')]
    else:
        return None


def position(word: str, alphapos: dict[str:int] | None):
    if alphapos:
        for pos, alpha in alphapos.items():
            if word[pos - 1] != alpha:
                return False
    return True


def non_position(word: str, alphanonpos: dict[str:int] | None):
    if alphanonpos:
        for alpha, indexes in alphanonpos.items():
            for i in indexes:
                if word[i-1] == alpha:
                    return False
    return True


def ain(word: str, alphain: list | None):
    if alphain:
        for i in alphain:
            if i not in word:
                return False
    return True


def uin(word: str, alphain: list | None):
    if alphain:
        for i in alphain:
            if i in word:
                return False
    return True


input_file = 'russian.utf8.txt'
output_tile = 'result'


if __name__ == '__main__':
    print(args)
    alphapos = conv_pos(args.__dict__['positions'])
    alphanonpos = conv_non_pos(args.__dict__['nonpositions'])
    alphain = conv_in_uin(args.__dict__['in'])
    alphauin = conv_in_uin(args.__dict__['nonin'])

    print(alphapos, alphanonpos, alphain, alphauin, sep='\n')

    with open(input_file) as f:
        result = []
        for line in f:
            line = line.strip()
            if len(line) == 5 and line.isalpha():
                if position(line, alphapos) and non_position(line, alphanonpos) and ain(line, alphain) and uin(line, alphauin):
                    print(line)
