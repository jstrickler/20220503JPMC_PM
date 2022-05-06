#!/usr/bin/env python


class TrimmedFile:
    def __init__(self, file_name):  # <1>
        self._file_in = open(file_name)

    def __iter__(self):  # <2>
        return self

    def __next__(self):  # <3>
        line = self._file_in.readline()
        if line == '':
            print("END OF FILE!")
            self._file_in.seek(0)  # go to beginning of file
            raise StopIteration  # <4>
        else:
            return line.rstrip('\n\r')  # <5>


if __name__ == '__main__':
    trimmed = TrimmedFile('../DATA/mary.txt')  # <6>
    for line in trimmed:  #next() next() next()
        # line = TrimmedFile.__next__(trimmed)
        print(line)
    print('-' * 60)
    for line in trimmed:
        print(line)
    print('=' * 60)
    for line in trimmed:
        print(line)