import requests
# from urllib.parse import urlencode


# APP_ID = 6351851
# AUTH_URL = 'https://oauth.vk.com/authorize'
#
# auth_params = {
#     'client_id': APP_ID,
#     'redirect_uri': 'https://oauth.vk.com/blank.html',
#     'display': 'page',
#     'scope': 'friends ',
#     'response_type': 'token',
#     'v': 5.71
# }
# # Почему тут не получается сделать get-запрос с автоматическим считыванием токена, как в предыдущей домашке?
# # Чтобы не проделывать всё вручную?
# url = AUTH_URL + '?' + urlencode(auth_params)
# print(url)


def get_my_N_random_friends(num, token):
    QUERY_URL = 'https://api.vk.com/method/friends.get'
    query_params = {
        'access_token': token,
        'order': 'random',
        'count': num,
    }

    response = requests.get(QUERY_URL, params=query_params)
    return response.json()['response']


def get_my_mutual_friends(ids, token):
    QUERY_URL = 'https://api.vk.com/method/friends.getMutual'
    format_ids = ','.join(map(str, ids))
    query_params = {
        'access_token': token,
        'target_uids': format_ids,
    }

    response = requests.get(QUERY_URL, params=query_params)
    print('Список общих друзей у пользователей:', *ids)
    # preventing fail if user was deleted or banned
    if 'response' in response.json():
        all_friends = [set(friend['common_friends']) for friend in response.json()['response']]
    else:
        print(response.json())
        exit(1)
    common_friends = set.intersection(*all_friends)

    print('Общие друзья: {}'.format(len(common_friends)))
    print('\n'.join('id = {id:<10} https://vk.com/{id}'.format(id=id) for id in common_friends))


def main():
    # TODO: insert your token here
    TOKEN = ''
    friends_number = 2

    friends = get_my_N_random_friends(friends_number, TOKEN)
    get_my_mutual_friends(friends, TOKEN)


main()
