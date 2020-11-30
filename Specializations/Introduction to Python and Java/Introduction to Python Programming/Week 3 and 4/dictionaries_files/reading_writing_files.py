def open_read_file(file):
    """Opens the given file, reads each line and prints to the console.
    Closes the given file."""

    # open the given file in read mode
    f = open(file, "r")
    print(type(f))  # print the type of stream f

    cnt = 0

    line = f.readline()

    # reads and prints each line in f, while there is a line to read
    while line:
        print(line, end='')
        line = f.readline()

        cnt += 1

    print('')
    print('there are', cnt, 'lines in the file')

    f.close()


def open_read_append_new_file(file1, file2):
    """Opens the first file, and reads all lines into a list.
    Reverses the lines, and appends them to the second file."""

    # open the first file in read mode

    with open(file1) as fin:
        # read all lines into a list
        lst = fin.readlines()

        # reverse the list
        lst.reverse()

        # open second file for appending
        fout = open(file2, "a")

        # write reversed lines to second file
        fout.writelines(lst)

        # close the second file
        fout.close()


def open_read_append_same_file(file):
    """Opens the given filea and reads all lines in a list.
    Appends lines to same file."""

    # open the file for reading and writing
    f = open(file, "r+")

    # read all lines into a list
    lst = f.readlines()

    # updating list for appending back to same file
    lst.insert(0, '\n')
    lst.insert(0, 'here is some new text')
    lst.insert(0, '\n')

    # append the lines back to same file
    f.writelines(lst)

    # close file
    f.close()

def open_read_write_new_file(file1, file2):
    """Opens the first file and reads all text as a string.
    Copies or writes all text to the second file."""

    # open the first file for reading
    with open(file1) as fin:
        # reads all lines as a single string
        text = fin.read()

        # open second file in write mode
        fout = open(file2, "w")

        # write single string to second file
        fout.write(text)

        # close second file
        fout.close

def main():
    # open_read_file('news.txt')
    #open_read_append_new_file('news.txt', 'news_out.txt')
    #open_read_append_same_file('news.txt')
    open_read_write_new_file('news.txt', 'news_copy.txt')

if __name__ == '__main__':
    main()
