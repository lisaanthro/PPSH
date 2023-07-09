import string
import codecs


def whole_string(read_from) -> string:  # 1
    with open(read_from, 'r') as f:
        s = f.read()
    return s


def first_string(read_from) -> string:  # 2
    with open(read_from, 'r') as f:
        s = f.readline()
    return s


def all_strings(read_from) -> list:  # 3
    with open(read_from, 'r') as f:
        strings_list = f.readlines()
    return strings_list


def all_strings_no_eof(read_from) -> list:  # 4
    with open(read_from, 'r') as f:
        file_text = f.read()
    strings_list = file_text.split('\n')
    return strings_list


def strings_iter(read_from):  # 5
    with open(read_from, 'r') as f:
        for line in f:
            print(line.rstrip('\n'))


def all_strings_spaced(read_from) -> string:  # 6
    with open(read_from, 'r') as f:
        strings_list = f.read().split('\n')
    spaced_string = ' '.join(strings_list)
    return spaced_string


def erase_specials(s) -> string:  # 7
    return s.rstrip(' \n\t')


def erase_marks(s) -> string:  # 8
    return s.rstrip('!?.')


def write_no_eof(write_to, s):  # 9
    with open(write_to, 'w') as f:
        f.write(s)


def write_with_eof(write_to, s):  # 10
    with open(write_to, 'a+') as f:
        f.write(s + '\n')


def write_list(write_to, strings_list):  # 11
    with open(write_to, 'w') as f:
        for line in strings_list:
            print(line, file=f)


def write_file(read_from, write_to):
    with open(read_from, 'r') as r, open(write_to, 'w') as w:  # 12
        for line in r:
            print(line.rstrip('\n'), file=w)


def write_file_hello_world(read_from, write_to):  # 13
    with open(read_from, 'r') as r, open(write_to, 'w') as w:
        for line in r:
            if line.startswith('hello') and line.endswith('world'):
                w.write(line)


def create_db(data_base_file) -> dict:  # 14
    data_base = {}
    with open(data_base_file, 'r', encoding='utf-8') as db:
        for person in db:
            data = person.split()
            if not data[2][0].isalpha():
                data_base[data[0]] = (data[1], data[2])
    return data_base


def main():
    read_from = 'input.txt'
    write_to = 'output.txt'
    data_base = 'data_base.txt'
    # print(whole_string(read_from))
    # print(first_string(read_from))
    # print(all_strings(read_from))
    # print(all_strings_no_eof(read_from))
    # strings_iter(read_from)
    # print(all_strings_spaced(read_from))
    # print(erase_specials('abcdedksmd\n \t'))
    # print(erase_marks('asfns/.!?'))
    write_no_eof(write_to, 'Have a nice day')
    write_with_eof(write_to, ' I love cookies')
    write_list(write_to, ['i am ', 'obsessed ', 'with ', 'cats.', '\nmeow'])
    write_file(read_from, write_to)
    write_file_hello_world(read_from, write_to)
    print(create_db(data_base))


if __name__ == '__main__':
    main()
