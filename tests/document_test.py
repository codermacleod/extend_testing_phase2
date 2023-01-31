import os.path
import random
from faker import Faker

fake = Faker('en-UK')

# Paths
finals = '../target_directory/finals'
originals = '../target_directory/originals'
updates = '../target_directory/updates'


def file_inserter(directory, number_of_files, seed):
    for i in range(number_of_files):
        Faker.seed(seed)
        name = fake.name()
        surname = name.split()[1]
        address = fake.address()
        file_object = open(f"../target_directory/{directory}/{surname}", 'a')
        file_object.write(name + '\n' + address)
        file_object.close()
        # os.path.join(originals, f"{name}")
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
            if surname in content:
                print('string exist')
            else:
                file_object.write(surname + '\n')
                file_object.close()
        seed_1 = seed_1 + 1


file_inserter('originals', 5, 1)
file_inserter('updates', 5, 6)

drop_or_allow_list_creator('drop', 5, 1)
# 1. Create a directory for originals and add several documents to it.
# 2. Create a droplist or allowlist file and add entries to it as per
# the rules above.
# 3. Create a directory for updates and add several documents to it.
# 4. Run the program and check that the expected behavior is achieved.
# 5. Check the new directory (finals) to ensure that the documents
# present are the ones expected, according to the droplist/allowlist
# file and the documents present in originals and updates.
# 6. Check the documents in finals to ensure that the correct
# version has been included (e.g. the document from updates
# if a document exists in both originals and updates).
# 7. Repeat the above steps with different documents,
# droplist/allowlist files and different combinations
# of documents in originals and updates to ensure that the
# program behaves as expected in all scenarios.
