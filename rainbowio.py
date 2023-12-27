def print_rgb(color, text):
    match color:
        case "red":
            print(f"\033[91m{text}\033[0m")
        case "green":
            print(f"\033[92m{text}\033[0m")
        case "blue":
            print(f"\033[94m{text}\033[0m")
        case "yellow":
            print(f"\033[93m{text}\033[0m")
        case "magenta":
            print(f"\033[95m{text}\033[0m")
        case "cyan":
            print(f"\033[96m{text}\033[0m")
        case "white":
            print(f"\033[97m{text}\033[0m")

def input_rgb(color, text):
    match color:
        case "red":
            return input(f"\033[91m{text}\033[0m")
        case "green":
            return input(f"\033[92m{text}\033[0m")
        case "blue":
            return input(f"\033[94m{text}\033[0m")
        case "yellow":
            return input(f"\033[93m{text}\033[0m")
        case "magenta":
            return input(f"\033[95m{text}\033[0m")
        case "cyan":
            return input(f"\033[96m{text}\033[0m")
        case "white":
            return input(f"\033[97m{text}\033[0m")