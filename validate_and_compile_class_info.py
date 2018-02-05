
# CRV start of assignement outline from Palmeri notes
#def main():
#    collect_all_csv_filenames()
#    read_csv()
#    write_data()


#def collect_all_csv_filenames():
#    from glob import glob
#    pass


#def read_csv():
#    check_no_spaces()
#    check_camel_case()
#    pass


#def write_data(type='json'):
#    pass


#def check_no_spaces():
#    pass


#def check_camel_case():
#    pass

# CRV send of assignement outline from Palmeri notes

def main():
    csv_files_in_dir = collect_all_csv_filenames()
    read_csvs(csv_files_in_dir)


def collect_all_csv_filenames():
    import glob
    all_csvs = glob.glob("*.csv")
    return all_csvs

def read_csvs(csvs_array):
    import csv, sys
    TEAM_NAME_INDEX = 4
    EXPECTED_INDEXES = 5
    num_teams_used_camel_case = 0
    num_teams = 0

    for csv_filename in csvs_array:
        with open(csv_filename) as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                # CRV first, make sure that each row from the csvs has the expected number of items and isn't a comment
                # CRV this ensures that our script doesn't choke on empty rows and excludes any comments that are part of imported csvs
                if(len(row) == EXPECTED_INDEXES and row[0][0] != '#'):
                    print('==========NEW ROW========')
                    print(row)
                    num_teams += 1
                    check_no_spaces(row[TEAM_NAME_INDEX])
                    is_team_name_camel_case = is_camel_case(row[TEAM_NAME_INDEX])
                    if(is_team_name_camel_case):
                        num_teams_used_camel_case += 1
                        print(num_teams_used_camel_case)




    sys.stdout.write('num teams that used camel case: ' + str(num_teams_used_camel_case) + ' out of ' + str(num_teams) + ' teams')


# def validate_rows(rows):
#
#     print("a***** validate rows called")
#     import sys
#     TEAM_NAME_INDEX = 4
#     EXPECTED_INDEXES = 5
#     num_teams_used_camel_case = 0
#
#
#     for row in rows:
#         # CRV first, make sure that each row from the csvs has the expected number of items and isn't a comment
#         # CRV this ensures that our script doesn't choke on empty rows and excludes any comments that are part of imported csvs
#         if(len(row) == EXPECTED_INDEXES and row[0][0] != '#'):
#             print('==========NEW ROW========')
#             print(row)
#             check_no_spaces(row[TEAM_NAME_INDEX])
#             is_team_name_camel_case = is_camel_case(row[TEAM_NAME_INDEX])
#             if(is_team_name_camel_case):
#                 num_teams_used_camel_case += 1
#                 print(num_teams_used_camel_case)
#
#
#
#
#     sys.stdout.write('num teams that used camel case: ' + str(num_teams_used_camel_case))


def check_no_spaces(team_name):
    has_space = team_name.isspace()
    print(has_space)


# CRV open question here - do we want to allow acronyms or numbers in our camel case validator?
def is_camel_case(team_name):
    # CRV note - following solution for determining camel case from William Bettridge-Radford
    # https://stackoverflow.com/questions/10182664/check-for-camel-case-in-python
    return (team_name != team_name.lower() and team_name != team_name.upper())


if __name__ == "__main__":
    main()
