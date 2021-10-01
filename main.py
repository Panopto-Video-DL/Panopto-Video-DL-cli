import os
import PanoptoDownloader
from PanoptoDownloader import SUPPORTED_FORMATS
from tqdm import tqdm

from utils import utils


def main():
    print('Panopto-Video-DL', end='\n\n')

    url = None
    while not url:
        url = input('URL: ')

    while True:
        filepath = None
        while not filepath:
            filepath = input('\nOUTPUT file: ')

        if os.path.isdir(filepath):
            print('ERROR. Cannot be a folder')
            continue
        if not os.path.isdir(os.path.split(filepath)[0] or './'):
            print('ERROR. Folder not exist')
            continue

        extension = os.path.splitext(filepath)[1]
        if not extension or extension == '.':
            filepath += SUPPORTED_FORMATS[0] if filepath[-1] != '.' else SUPPORTED_FORMATS[0][1:]

        if os.path.exists(filepath):
            print('\nFile already exist')
            result = utils.input_yesno('Replace it [Y, n]? ')
            if result:
                os.remove(filepath)
            else:
                continue
        if os.path.splitext(filepath)[1] not in SUPPORTED_FORMATS:
            print('\nExtension not officially supported. Choose from: ' + str(SUPPORTED_FORMATS))
            result = utils.input_yesno('Continue anyway [Y, n]? ')
            if not result:
                continue
        break

    print(f'\nDownload started: {filepath}\n')

    bar = tqdm(total=100)

    def callback(progress: int) -> None:
        bar.n = progress
        bar.refresh()

    try:
        PanoptoDownloader.download(url, filepath, callback)
    except Exception as e:
        bar.close()
        print('ERROR.', str(e))
    except KeyboardInterrupt:
        bar.close()
        raise KeyboardInterrupt
    else:
        bar.close()
        print('\nDownload completed')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram closed')
