import os
import platform
from ThermalMangement import get_file_list, process_files_combined, process_files_trip_by_trip


def pre_process():
    while True:
        print("1: Initial GS Data Parsing")
        print("2: Calculating Speed(m/s), Acceleration(m/s^2)")
        print("3: Trip by Trip Parsing")
        print("6: Quitting the program.")
        choice = int(input("Enter number you want to run: "))

        if choice == 1:
            if platform.system() == "Windows":
                folder_path = os.path.normpath(r"C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\2024-02-27")
                save_path = os.path.normpath(r"C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\Save_file")
            elif platform.system() == "Darwin":
                folder_path = os.path.normpath("C:/Users/chohs/BMS/아이오닉5/01241227999/2023-03")
                save_path = os.path.normpath("C:/Users/chohs/BMS/free")
            else:
                print("Unknown system.")
                return

            file_lists = get_file_list(folder_path)
            process_files_combined(file_lists, folder_path, save_path)
            break

        elif choice == 2:
            if platform.system() == "Windows":
                folder_path = os.path.normpath(r"C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\2024-02-27")
                save_path = os.path.normpath(r"C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\Save_file")
            elif platform.system() == "Darwin":
                folder_path = os.path.normpath("C:/Users/chohs/BMS/아이오닉5/01241227999/2023-03")
                save_path = os.path.normpath("C:/Users/chohs/BMS/free")
            else:
                print("Unknown system.")
                return

            file_list = get_file_list(folder_path)
            process_files_combined(file_list, folder_path, save_path)
            break

        elif choice == 3:
            if platform.system() == "Windows":
                folder_path = os.path.normpath(r"C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\2024-02-27")
                save_path = os.path.normpath(r"C:\Users\chohs\BMS\아이오닉5\01241227999\01241227999\Save_file")
            elif platform.system() == "Darwin":
                folder_path = os.path.normpath("C:/Users/chohs/BMS/아이오닉5/01241227999/2023-03")
                save_path = os.path.normpath("C:/Users/chohs/BMS/free")
            else:
                print("Unknown system.")
                return

            file_list = get_file_list(folder_path)
            process_files_trip_by_trip(file_list, folder_path, save_path)
            break

        elif choice == 6:
            print("Quitting the program.")
            return

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    pre_process()