import os


def print_directory_contents(path, space):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if item.startswith('.'):
            continue
        elif os.path.isfile(item_path) and item_path.endswith('.db'):
            continue
        elif os.path.isdir(item_path):
            print(space + "├──" + item)
            print_directory_contents(item_path, space + "│   ")
        else:
            print(space + "└──" + item)
            try:
                with open(item_path, 'r') as f:
                    content = f.read()
                    print(space + "    " + content.strip().replace('\n', '\n' + space + '    '))
            except UnicodeDecodeError:
                print(space + "    <Binary file>")


print_directory_contents("/Users/colindavis/PycharmProjects/ATS", "")
