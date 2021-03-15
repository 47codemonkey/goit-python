main_dict = {}

# tuple with commands words
EXIT = ("good bye", "close", "exit")
ADD = ("add")
GREETINGS = ("hello")
SHOW_PHONE = ("phone",)
SHOW_ALL = ("show all",)


def input_error(func):
    def inner(str):
        try:
            return func(str)
        except ValueError:
            return "Give me name and phone after command"
        except KeyError:
            return "Give me correct name"
    return inner


def check_dict(func):
    def inner(str):
        if len(main_dict) == 0:
            return "Your phonebook is empty"
        else:
            return func(str)
    return inner


def exit_command(str):
    return "Good bye!"


@input_error
def add_command(str):
    name, phone = str.split(' ')
    main_dict[name] = phone
    return "Nice!"


def greeting_command(str):
    return 'How can I help you?'


@check_dict
@input_error
def show_phone_command(str):
    return f'Name: {str}, phone: {main_dict[str]}'


@check_dict
@input_error
def show_all_command(str):
    result = ''
    for i in main_dict:
        result += f'Name: {i} Phone: {main_dict[i]}\n'
    return result


def non_command():
    return 'I don`t know this command'


COMMANDS = {ADD: add_command, GREETINGS: greeting_command,
            SHOW_PHONE: show_phone_command, SHOW_ALL: show_all_command, EXIT: exit_command}


def parse_data(command, list):
    for i in list:
        if command.startswith(i):
            return command.replace(i, '').strip()


def parse_command(command):
    for i in COMMANDS.keys():
        com = command.lower()
        if com.startswith(i):
            data = parse_data(command, i)
            return COMMANDS[i](data)
    return non_command()


def main():
    while True:
        command = input('Enter command:')
        result = parse_command(command)
        if result == 'Good bye!':
            print(result)
            break
        print(result)


if __name__ == '__main__':
    main()