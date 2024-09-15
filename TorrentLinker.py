from tpblite import TPB
import os, webbrowser, subprocess, string

#Build: pyinstaller --onefile --icon=icon.ico TorrentLinker.py

GOLD = '\033[33m'
THEWORD = "Porn"
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
enter = RESET + YELLOW + " ENTER " + RESET


#CHATGPT WROTE THIS BLOCK [START:]
def has_whitespace_before_first_word(text):
    return text and text[0].isspace()


def find_shortcut_on_desktop(program_names, desktop_path):
    try:
        for file_name in os.listdir(desktop_path):
            if file_name.lower().endswith(".lnk") and any(name.lower() in file_name.lower() for name in program_names):
                return os.path.join(desktop_path, file_name)
    except FileNotFoundError:
        pass
    return None

def paste_magnet_url(magnet_url):
    program_names = ["WebTorrent", "WebTorrent.exe - Shortcut"]

    # Get the original desktop path
    original_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Construct the desktop paths for all drive letters
    drive_letters = [f"{letter}:\\" for letter in string.ascii_uppercase]
    drive_desktop_paths = [os.path.join(drive, original_path[3:]) for drive in drive_letters]

    # Iterate through the drive paths and find the shortcut
    for desktop_path in drive_desktop_paths:
        webtorrent_shortcut = find_shortcut_on_desktop(program_names, desktop_path)
        if webtorrent_shortcut:
            # Use the start command to open the shortcut
            command = ["cmd", "/c", "start", "", webtorrent_shortcut, magnet_url]
            try:
                subprocess.run(command, check=True)
                break
            except subprocess.CalledProcessError:
                os.system("cls")
                break
    else:
        print("Cannot find WebTorrent shortcut on your desktop.")
        input("Press Enter to continue...")
        return 0


def rationSeederLeecher(seeders, leechers, isGame):
    if(not isGame):
        if(seeders == 0 and leechers == 0):
            print(RED + "DEAD TORRENT, THE STREAM MAY NOT PLAY." + RESET)
            return False
        totalDL = seeders + leechers
        if(totalDL * .3 >= seeders and seeders >= 20 or seeders >= 20):
            print(GREEN + "THE STREAM MAY PLAY SMOOTHLY" + RESET)
        else:
            print(GREEN + "THE STREAM MAY NOT PLAY SMOOTHLY" + RESET)
    else:
        if(seeders == 0 and leechers == 0):
            print(RED + "DEAD TORRENT, DOWNLOAD MAY NOT EVEN START." + RESET)
            return False
        totalDL = seeders + leechers
        if(totalDL * .3 >= seeders or seeders >= 20):
            print(GREEN + "THIS TORRENT MAY DOWNLOAD FAST" + RESET)
        else:
            print(GREEN + "THIS TORRENT MAY DOWNLOAD SLOW" + RESET)
def nangluodNako():
    try:
        os.system("cls")
        print(RESET + "Hey smart stuff, that's rude, you don't have to do that...")
        input("Either hit the thing you just did or just hit" + enter + "if you want to terminate the program..." + RESET)
        exit()
    except KeyboardInterrupt:
        exit()

t = TPB()
def searchMovie(torrents, title, safeSearch, isGame):
    while True:
        os.system("cls")
        if(not safeSearch):
            print(RED + "Safe search is off in this query..." + RESET)
        elif(isGame):
            print(GREEN + "NOTE: You will still be redirected to Web Torrent" + RESET)
            
        print(GREEN + "Found " + str(len(torrents)) + " results of the search " + CYAN + title.upper() + RESET)
        for i, torrent in enumerate(torrents, 1):
            if(torrent.is_vip or torrent.is_trusted):
                status = GREEN + "Safe to download/stream." + RESET
            else:
                status = RED + "Unsafe to download/stream." + RESET
            print(YELLOW + str(i) + RESET, torrent.title + " STATUS: " + status)

        try:
            if(len(torrents) == 1):
                choice = 1
                os.system("cls")
            else:
                choice = input(GREEN + "\nChoose the " + RESET + YELLOW + "download option number" + RESET + GREEN + " and press" + enter + GREEN + "if you want to proceed to {Download?} prompt.\nType the word " + YELLOW + "new" + RESET + GREEN + " and hit" + enter + GREEN + "if you want to search for another title.\n" + RESET + CYAN + "Enter your choice: " + RESET).lower()
                if(choice == "new" or choice == "[new]"):
                    return True
                else:
                    choice = int(choice)
                os.system("cls")
        except KeyboardInterrupt:
            nangluodNako()
        except ValueError:
            os.system("cls")
            print(RED + "You have entered an invalid choice.")
            input("Hit" + enter + RED + "to try again..." + RESET)
            os.system("cls")
            continue

        if(choice > len(torrents) or choice <= 0):
            os.system("cls")
            print(RED + "You have chosen an index that is out of range.")
            input("Hit" + enter + RED +"to try again..." + RESET)
            os.system("cls")
            continue

        torrentChosen = torrents[choice - 1]
        print("Information about " + torrentChosen.title + " uploaded by " + torrentChosen.uploader)
        rationSeederLeecher(torrentChosen.seeds, torrentChosen.leeches, isGame)
        print("Seeders: " + str(torrentChosen.seeds) + ", Leechers: " + str(torrentChosen.leeches))
        print(GREEN + "Category: " + torrentChosen.category.split()[0] + RESET)
        print("File Size: " + torrentChosen.filesize)
        print("Upload Date: " + torrentChosen.upload_date)
        if(torrentChosen.is_vip or torrentChosen.is_trusted):
            print(GREEN + "STATUS: Safe to download/stream." + RESET)
        else:
            print(RED + "STATUS: Unsafe to download/stream."+ RESET)
        if(len(torrents) != 1):
            prompt = RESET + "Continue to download/stream?\nOPTIONS:" + GREEN + "\nPress " + YELLOW + "1" + GREEN + " and hit" + enter + GREEN +"for yes\nPress " + YELLOW + "2" + GREEN + " and hit" + enter + GREEN + "to exit\nPress " + YELLOW + "3" + GREEN + " and hit" + enter + GREEN + "to search for another title\nHit" + enter + GREEN +"or " + YELLOW + "any key " + GREEN + "to pick an option again\n" + CYAN + "Your Choice: " + RESET
        else:
            prompt = RESET + "Continue to download/stream?\nOPTIONS:" + GREEN + "\nPress " + YELLOW + "1" + GREEN + " and hit" + enter + GREEN +"for yes\nPress " + YELLOW + "2" + GREEN + " and hit" + enter + GREEN + "to exit\nPress " + YELLOW + "3" + GREEN + " and hit" + enter + GREEN + "to search for another title\n" + CYAN + "Your Choice: " + RESET
        continueChoice = input(prompt)
        if(continueChoice == "1"):
            paste_magnet_url(torrentChosen.magnetlink)
            os.system("cls")
            print("Have any reports of bugs? You can visit my facebook timeline and comment on the post or message me.")
            try:
                exitOrVisit = input(CYAN + "Press " + YELLOW + "1" + CYAN + " and hit" + enter + CYAN + "to visit my account and exit, Press " + YELLOW + "2" + CYAN + " and hit" + enter + CYAN + "to search again, or hit" + enter + CYAN + "to exit the program: " + RESET)
                if(exitOrVisit == "1"):
                    webbrowser.open("https://www.facebook.com/BruhPlsHelpMeChooseMyUsername")
                    break
                elif(exitOrVisit == "2"):
                    return True
                else:
                    exit()
            except KeyboardInterrupt:
                nangluodNako()
        elif(continueChoice == "2"):
            os.system("cls")
            try:
                print(RESET + "Have any reports of bugs? You can visit my facebook timeline and comment on the post or message me.")
                exitOrVisit = input(CYAN + "Press " + YELLOW + "1" + CYAN + " and hit" + enter + CYAN + "to visit my account and exit, Press " + YELLOW + "2" + CYAN + " and hit" + enter + CYAN + "to search again, or hit" + enter + CYAN + "to exit the program: " + RESET)
                if(exitOrVisit == "1"):
                    webbrowser.open("https://www.facebook.com/BruhPlsHelpMeChooseMyUsername")
                    break
                elif(exitOrVisit == "2"):
                    return True
                else:
                    exit()
            except KeyboardInterrupt:
                nangluodNako()
        elif(continueChoice == "3"):
            return True
        else:
            os.system("cls")
            continue

#main lol
while True:
    try:
        os.system("cls")
        print(GOLD + "TORRENT LINKER v0.1\nScript by Bern Vein Balermo\n" + RESET)
        print(GREEN + "TIP: In searching, avoid putting spaces, and do not indent(tab) initial input.\nUSE A " + RED + "VPN" + GREEN + " WHENEVER POSSIBLE.")
        print(GREEN + "NOTE: If stuck after the search for too long, check your internet connection and exit then run this program again.")
        print("You can technically download anything you want but it is not recommended." + RESET)
        try:
            movieTitle = input(CYAN + "Please input the name of a movie, or series to stream and hit" + enter + CYAN + "when done: " + RESET)
            print(GREEN + "Looking for for " + movieTitle + "...\nPlease be patient. Could take a couple of seconds..." + RESET)
            if(has_whitespace_before_first_word(movieTitle) or movieTitle == ""):
                continue
            torrents = t.search(movieTitle)
            
            if("-safeSearchOff" in movieTitle):
                if(searchMovie(torrents, movieTitle.replace("-safeSearchOff", ""), False, False)):
                    print("Safe search is OFF on this search.")
                    continue
                else:
                    break
            counter = 0
            gameCounter = 0
            for torrent in torrents:
                if(torrent.category.split()[0] == THEWORD):
                    counter += 1
                if(torrent.category.split()[0] == "Games" or torrent.category.split()[0] == "Applications" or torrent.category.split()[0] == "Other"):
                    gameCounter += 1
            if(len(torrents) == 0):
                os.system("cls")
                print(RED + movieTitle + " yields 0 result.")
                input("Hit" + enter + RED + "to try again...")
                continue
            elif(counter == len(torrents)):
                os.system("cls")
                print("Brooooooooooooooooooooooooo hahahahhaha")
                input("Press" + enter + "again and enter a decent search...")
                continue
            elif(gameCounter >= len(torrents) / 2 and len(torrents) > 1):
                os.system("cls")
                file2 = [torrent for torrent in torrents if torrent.category.split()[0] != THEWORD]
                print(GREEN + "If you want to download a game or an application or other type of file, can still download it through Web Torrent though it is not recommended.\nIf you wish to proceed, press" + enter + GREEN + "to continue.\nPress" + YELLOW + " 1 " + GREEN + "and" + enter + GREEN + "to search again.")
                choice = input(CYAN + "Enter your Choice: " + RESET)
                if(choice == "1"):
                    continue
                else:
                    if(searchMovie(file2, movieTitle, True, True)):
                        continue
                    break

            files = [torrent for torrent in torrents if torrent.category.split()[0] != THEWORD and torrent.category.split()[0] not in {"Games", "Applications", "Other"}]
            if(len(files) == 0):
                os.system("cls")
                print(RED + movieTitle + " yields 0 result.")
                input("Hit" + enter + RED + "to try again...")
                continue
            elif(len(files) == 1):
                os.system("cls")
                print(GREEN + movieTitle + " yielded only 1 result.\nRedirecting you to the {Download/Stream?} prompt...")
                input("Hit" + enter + GREEN + "to proceed." + RESET)
            if(searchMovie(files, movieTitle, True, False)):
                continue
            else:
                break
        except KeyboardInterrupt:
            nangluodNako()
    except ConnectionError:
        try:
            print(RED + "Please connect to the internet.")
            input("Hit" + enter + "to exit..." + RESET)
        except KeyboardInterrupt:
            nangluodNako()