#python3 update-env.py
import os

def transform_line(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    key, value = line.split("=", maxsplit=1)
    #return f"{key.strip()}={value.strip()}"
    return (f"{key.strip()}=\"${key.strip()}\"") # ajust transformed line to keys for envsubst

def write_to_file(filename, transformed_lines):
    with open(filename, "w") as file:
        for line in transformed_lines:
            file.write(line + '\n')

def main():
    transformed_lines = []
    
    try:
        with open(".env.example", "r") as file:
            line = file.readline()
            while line:
                transformed_line = transform_line(line)
                if transformed_line:
                    transformed_lines.append(transformed_line)
                line = file.readline()

        write_to_file(".env.tpl", transformed_lines)
    except FileNotFoundError:
        print(f'File: .env.example Not Found')

if __name__ == '__main__':
    main()
