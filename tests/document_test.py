import os.path
import random
import shutil

from faker import Faker

fake = Faker('en-UK')

# Paths
finals_path = "../target_directory/finals"
originals_path = "../target_directory/originals"
updates_path = "../target_directory/updates"
drop_path = "../target_directory/droplist"
allow_path = "../target_directory/allowlist"


def create_new_directory(directory):
    path = os.path.join("../target_directory", directory)
    os.mkdir(path)


def file_inserter(directory, number_of_files, seed):
    for i in range(number_of_files):
        Faker.seed(seed)
        name = fake.name()
        surname = name.split()[1]
        if directory == "updates":
            Faker.seed(seed + 1)
        address = fake.address()
        file_object = open(f"../target_directory/{directory}/{surname}", 'a')
        file_object.write(name + '\n' + address)
        file_object.close()
        print(name + '\n' + address)
        seed = seed + 1


def drop_or_allow_list_creator(drop_or_allow, number_of_people, seed_1):
    name_list = []
    for i in range(number_of_people):
        file_object = open(f"../target_directory/{drop_or_allow}list", 'a')
        Faker.seed(seed_1)
        name = fake.name()
        surname = name.split()[1]
        name_list.append(surname)
        with open(fr'../target_directory/{drop_or_allow}list', 'r') as file:
            # read all content from a file using read()
            content = file.read()
            # check if string present or not
            if random.choice(name_list) in content:
                print('string exist')
            else:
                file_object.write(surname + '\n')
                file_object.close()
        seed_1 = seed_1 + 1


def clear_all_directories_and_files():
    directory_list = [originals_path, updates_path, finals_path]
    drop_or_allow_list = [drop_path, allow_path]

    for i in directory_list:
        if os.path.exists(i):
            shutil.rmtree(i)
    for i in drop_or_allow_list:
        if os.path.exists(i):
            os.remove(i)


clear_all_directories_and_files()

create_new_directory("originals")
create_new_directory("updates")
create_new_directory("finals")

file_inserter('originals', 5, 1)
file_inserter('updates', 5, 1)

drop_or_allow_list_creator('allow', 5, 1)
# drop_or_allow_list_creator('drop', 5, 1)
