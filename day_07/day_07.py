
def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        out_lines = []
        for line in lines:
            out_lines.append(line.strip())
        return out_lines

class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

class Dir(File):
    def __init__(self, name):
        File.__init__(0, name)
        self.size = self.calc_size()
        self.contents = []
    
    def calc_size(self):
        return sum([file.size for file in self.contents])


def is_command(line):
    return line[0] == "$"

def cd(filesystem, cwd, ):

def is_dir_listing(line):
    return line[0] == "dir"

def is_file_listing(line):
    return line[0].isnumeric()

def construct_filesystem(cmdline_out):
    filesystem = Dir("/")
    for line in cmdline_out:
        if is_command(line):
            if line[1] == "ls":
                

if __name__ == "__main__":
    lines = read_file("./test.txt")
    cmdline_out = [line.split() for line in lines]
    filesystem = construct_filesystem(cmdline_out)
    root = Dir("/") # start at root directory
    for line in cmdline_output:
        if is_command(line):
            # simulate command
        elif is_dir_listing(line):
            # found a directory listing
        elif is_file_listing(line):
            # found a file listing
        else:
            raise ValueError("Unexpected input")
    