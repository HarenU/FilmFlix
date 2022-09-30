import readData
import insertData
import updateData
import deleteData


def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", ""]:
        print("Songs Menu options \nEnter \n1. Print \n2. Add. \n3. Update.\n4. Delete.\n5. Search")

        options = input(
            "Enter one of the options listed above (Press Enter to exit): ")

        if options not in ["1", "2", "3", "4", "5", ""]:
            print("please enter one of the options")

        return options


mainProgram = True
mainMenu = 0
while mainProgram:
    mainMenu = menuOptions()

    if mainMenu == "1":
        readData.readFilms()
    elif mainMenu == "2":
        insertData.addFilm()
    elif mainMenu == "3":
        updateData.updateFilm()
    elif mainMenu == "4":
        deleteData.delFilm()
    elif mainMenu == "5":
        readData.searchFilm()
    elif mainMenu == "":
        mainProgram = False
    else:
        print("An Error Occured")
