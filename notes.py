from glob import glob


def create():
    f_name = input('Make a title for your note: ')
    f_content = input('Create a note: ')
    with open(f'{f_name}.txt', 'w') as f:
        f.write(f_content)  # Saving data to a file


def view():
    f_name = input('Type name of your note: ')
    with open(f'{f_name}.txt', 'r') as f:
        text = f.read()
    print(f'View of the {f_name} note: {text}')


def updates():
    f_name = input('Type name of your note: ')
    f_update = input('Update your note: ')
    with open(f'{f_name}.txt', 'a') as f:
        f.write(f'\n{f_update}')


def all_notes():
    print(glob('*.txt'))


while True:
    print('1 - Create a new note\n'
          '2 - Read a note\n'
          '3 - Update your note\n'
          '4 - View all notes\n'
          '5 - Exit')

    option = int(input())
    if option == 5:
        break
    switch = {
        1: create,
        2: view,
        3: updates,
        4: all_notes
    }

    # Executing right function based on given option
    switch.get(option, lambda: 'Undefined option')()
