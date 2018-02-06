def main():
    csv_files_in_dir = collect_all_valid_csv_filenames()
    read_and_validate_csvs_then_write_json(csv_files_in_dir)


def collect_all_valid_csv_filenames():
    import glob
    palmeri_csv_filename = "mlp6.csv"
    all_csvs = glob.glob("*.csv")
    # CRV remove the mlp6.csv from the list of valid csvs
    try:
        all_csvs.remove(palmeri_csv_filename)
    except:
        print(palmeri_csv_filename + ' does not exist in this directory')

    return all_csvs

def read_and_validate_csvs_then_write_json(csvs_array):
    import csv, sys, os
    TEAM_NAME_INDEX = 4
    EXPECTED_INDEXES = 5
    num_teams_used_camel_case = 0
    num_team_names_with_spaces = 0

    # CRV remove the everyone.csv file if it already exists in the directory
    remove_file_from_dir_before_creating('everyone.csv')

    everyone_file = open("everyone.csv", 'a')
    everyone_writer = csv.writer(everyone_file)

    for csv_filename in csvs_array:
        with open(csv_filename) as csvfile:

            rows = csv.reader(csvfile)
            for row in rows:
                # CRV first, make sure that each row from the csvs has the expected number of items and isn't a comment
                # CRV this ensures that our script doesn't choke on empty rows and excludes any comments that are part of imported csvs
                if(len(row) == EXPECTED_INDEXES and row[0][0] != '#'):
                    # CRV add this row to the everyone csv
                    everyone_writer.writerow(row)

                    #CRV check if team name has space in it
                    does_team_name_have_space = check_no_spaces(row[TEAM_NAME_INDEX])
                    if(does_team_name_have_space):
                        num_team_names_with_spaces += 1

                    #CRV check if team name is camel case
                    is_team_name_camel_case = is_camel_case(row[TEAM_NAME_INDEX])
                    if(is_team_name_camel_case):
                        num_teams_used_camel_case += 1

                    # CRV create a new json file for each csv
                    create_and_write_json_file(swap_csv_for_json_file_extension(csv_filename), row)



    everyone_file.close()
    sys.stdout.write('team names with spaces: ' + str(num_team_names_with_spaces))
    # CRV added print for readability puroses (adding new line char to sys.stdout.write through error)
    print("")
    sys.stdout.write('teams that used camel case: ' + str(num_teams_used_camel_case))
    # CRV added print for readability puroses (adding new line char to sys.stdout.write through error)
    print("")


def check_no_spaces(team_name):
    return(team_name.isspace())


# CRV open question here - do we want to allow acronyms or numbers in our camel case validator?
def is_camel_case(team_name):
    # CRV note - following solution for determining camel case from William Bettridge-Radford
    # https://stackoverflow.com/questions/10182664/check-for-camel-case-in-python
    return (team_name != team_name.lower() and team_name != team_name.upper())


def remove_file_from_dir_before_creating(filename):
    import os
    try:
        os.remove(filename)
    except:
        print(filename + ' does not exist in this directory')

def swap_csv_for_json_file_extension(filename):
    return(filename.replace('.csv', '.json'))

# CRV open question here - do we want the mlp6.csv file to have a json representation?
def create_and_write_json_file(filename, contents):
    import json
    remove_file_from_dir_before_creating(filename)
    with open(filename, 'wb') as new_json_file:
        json.dump(contents, new_json_file)


if __name__ == "__main__":
    main()
