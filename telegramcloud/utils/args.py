import argparse


def tgcloud_args():

    parser = argparse.ArgumentParser()
    # Read arguments from the command line
    parser.add_argument("--name", "-n", help = "That unique name you've set at the first", required = True)
    parser.add_argument("--username", "-u", help = "Set target username for sending file/files to her/him", required = True)
    parser.add_argument("--path", "-p", help = "Path of the file/files you want to upload", required = True)
    parser.add_argument("--mode", "-m", help="Change mode to upload or download", required=True)
    parser.add_argument("--format", default="text", dest="parse_mode", choices=["text", "markdown", "html"],
                        help="Parse mode for file caption. Choose from 'text', 'markdown', or 'html'. Default is 'text'")
    parser.add_argument("--caption", "-c", help = "for upload mode: write caption/text under file, for download mode: download file by its caption or name", default = '', required = False)
    
    args = parser.parse_args()
    return args

def tginfo_args():

    parser = argparse.ArgumentParser()
    # Read arguments from the command line
    parser.add_argument("--name", "-n", help = "That unique name you've set at the first", required = True)
    parser.add_argument("--username", "-u", help = "Set target username for getting info from conversation", required = True)
    parser.add_argument("--search", "-s", help="Search for specific extension likfe .pdf or name", required=False)    
    args = parser.parse_args()
    return args

def tgsend_args():

    parser = argparse.ArgumentParser(description="Send Telegram messages to users, channels and groups",
                                     epilog="Homepage: https://github.com/iw4p/telegram-cloud")
    # Read arguments from the command line
    parser.add_argument("message", help="Message to send", nargs="*")
    parser.add_argument("--name", "-n", help = "Unique profile name you've set at the first run", required = True)
    parser.add_argument("--username", "-u", help = "Recipient username or chat id", required = True)
    parser.add_argument("--format", default="text", dest="parse_mode", choices=["text", "markdown", "html"],
                        help="Parse mode for message body. Choose from 'text', 'markdown', or 'html'. Default is 'text'")
    parser.add_argument("--stdin", help="Read message text from stdin", action="store_true")
    parser.add_argument("--silent", help="Send silently, user will receive notification without sound", required=False, action="store_true")
    args = parser.parse_args()
    return args
