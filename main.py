import sys


def create_folder_names(amount_of_dirs):
    dir_names_list = []
    for num in range(1, amount_of_dirs + 1):
        dir_names_list.append(f'Dir_{str(num)}/')
    return dir_names_list


def create_paths(starting_path_str, depth, dir_name_list):
    amount_of_dirs = _calculate_total_amount_of_dirs(depth=depth, amount_of_dirs=len(dir_name_list))
    paths_list = [starting_path_str]
    path_counter = 0
    for path in paths_list:
        for folder in dir_name_list:
            if len(paths_list) > amount_of_dirs:
                break
            paths_list.append(path + folder)
            path_counter += 1
    return paths_list


def _calculate_total_amount_of_dirs(depth: int, amount_of_dirs: int):
    amount = 0
    for num in range(1, depth + 1):
        amount += amount_of_dirs ** num
    return amount


if __name__ == "__main__":
    sys.argv = sys.argv + ["/home/user/commands/", 6, 6]

    dir_names = create_folder_names(amount_of_dirs=int(sys.argv[3]))
    list_of_paths = create_paths(starting_path_str=sys.argv[1], depth=int(sys.argv[2]), dir_name_list=dir_names)
