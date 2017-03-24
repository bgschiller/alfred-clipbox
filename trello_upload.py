import requests
import json
import os
import sys
import datetime

def read_from_file(fname):
    try:
        with open(os.path.expanduser(fname), 'r') as f:
            val = f.read().strip()
    except IOError:
        return None
    try:
        return json.loads(val)
    except ValueError:
        return val

def write_to_file(val, fname):
    try:
        with open(os.path.expanduser(fname), 'w') as f:
            json.dump(val, f)
    except IOError:
        return None

class ScreenshotStorage(object):
    def __init__(self, key=None, token=None):
        self.key = key or os.getenv('trello_api_key')
        self.token = token or read_from_file('~/.clipbox/token')
        self._board_id = read_from_file('~/.clipbox/board_id') or self.get_clipbox_board_id()
        self._today_list = read_from_file('~/.clipbox/list_details') or self.get_todays_list_id()


    # visit this site to get your token:
    #   https://trello.com/1/authorize?response_type=token&key=[[  YOUR KEY HERE ]]&scope=read,write&expiration=never&name=Trello+API+Demo

    base_url = 'https://trello.com/1/'

    @property
    def auth_params(self):
        return {'key': self.key, 'token': self.token}

    def get_clipbox_board_id(self):
        boards = requests.get(self.base_url+ 'members/me/boards', params=self.auth_params, data={'fields':'name'})
        boards.raise_for_status()
        for board in boards.json():
            if board['name'] == 'Clipbox Screenshots':
                write_to_file(board['id'], '~/.clipbox/board_id')
                return board['id']
        else:
            return self.create_board()

    def create_board(self):
        board = requests.post(self.base_url+ 'boards', params=self.auth_params, data={'name': 'Clipbox Screenshots'}).json()
        return board['id']

    def get_todays_list_id(self):
        """
        We will separate lists by day. If there isn't a list for today, make one.
        """
        todays_list_name = datetime.datetime.now().strftime('%B %Y')
        board = requests.get(
            self.base_url+ 'boards/' + self._board_id,
            params=dict(self.auth_params, lists='all', list_fields='name'),
        ).json()
        list_id = None
        for lst in board['lists']:
            if lst['name'] == todays_list_name:
                list_id = lst['id']
                break
        if list_id is None:
            return self.create_list(todays_list_name)
        return {'id': list_id, 'name': todays_list_name}

    @property
    def todays_list_id(self):
        """
        Use the cached value until it expires.
        """
        todays_list_name = datetime.datetime.now().strftime('%B %Y')
        if self._today_list['name'] != todays_list_name:
            list_details = {'id': list_id, 'name': todays_list_name}
            write_to_file(list_details, '~/.clipbox/list_details')

            self._today_list = self.create_list(todays_list_name)
        return self._today_list['id']


    def create_list(self, name):
        resp = requests.post(self.base_url+ 'lists', params=self.auth_params, data={
            'name': name,
            'idBoard': self._board_id,
        }).json()
        list_details = {'id': list_id, 'name': name}
        write_to_file(list_details, '~/.clipbox/list_details')

        return list_details

    def store_screenshot(self, path):
        card = requests.post(self.base_url+ 'cards', params=self.auth_params, data={
            'name': datetime.datetime.now().isoformat(),
            'due': datetime.datetime.now().isoformat(),
            'dueComplete': 'true',
            'idList': self.todays_list_id,
        })
        card = card.json()
        attachment = requests.post(
            self.base_url+ 'cards/' + card['id'] + '/attachments',
            params=self.auth_params,
            files={'file': open(path, 'rb')}
        )
        attachment = attachment.json()
        return attachment['url']

if __name__ == '__main__':
    file_name = sys.argv[1]
    sss = ScreenshotStorage()
    if file_name == '--test-token':
        try:
            sss.get_clipbox_board_id()
            print('Successfully authenticated with trello')
        except requests.HTTPError:
            print("hmm, that token didn't work")
    else:
        sys.stdout.write(sss.store_screenshot(file_name)) # no newline on the end
