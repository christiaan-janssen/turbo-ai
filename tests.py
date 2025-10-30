from functions.get_file_info import get_files_info


def main():
    get_files_info("calculator", ".")
    print("---------------------------------------------")
    get_files_info("calculator", "pkg")
    print("---------------------------------------------")
    get_files_info("calculator", "/bin")
    print("---------------------------------------------")
    get_files_info("calculator", "../")
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
