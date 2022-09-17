import os
import pathlib


def create_participant_dirs(users):
    count = 0
    warning = input(f"WARNING: This will initialize the repository in the following directory:\n\n{pathlib.Path().resolve()}\n\nAre you sure you want to continue? [(y)es|(n)o]: ")
    if warning.lower() == "y" or warning.lower() == "yes":
        for user in users: # Creating directories for specific users
            try:
                os.mkdir('./' + user)
                for folder in range(1,26): # Creating folders for each day for each user
                    os.mkdir(os.path.join('./' + user, 'Day_' + str(folder)))
                    with open('./' + user + '/Day_' + str(folder) + '/main.py', 'w') as f:
                        f.write('# Day {}'.format(str(folder)))
                count += 1
            except FileNotFoundError:
                print(f"Folder for '{user}' could not be created due to invalid characters in name.\nPlease rerun the script with another name")
        print(f"Initialized folders for {count} participants")
    else:
        print("Aborded initialization.")


if __name__ == "__main__":
    users = [i.strip() for i in input("Please enter the participating persons comma separated: ").split(",") if not i=='']
    create_participant_dirs(users)