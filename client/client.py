import requests

endpoint = "http://localhost:8000"


def CreateUser(username, email, password):
    headers = {
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
    }
    json_data = {
        'username': username,
        'email': email,
        'password': password,
        'password_check': password
    }
    response = requests.post(
        f'{endpoint}/signup', headers=headers, json=json_data)
    print(response.json())


def LoginUser(email, password):
    headers = {
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
    }
    json_data = {
        'email': email,
        'password': password,
    }
    response = requests.post(
        f'{endpoint}/login', headers=headers, json=json_data)
    if (response.status_code == 200):
        response_json = response.json()
        access_token = response_json["access"]
        refresh_token = response_json["refresh"]
        print("user_loged_in_200")
        return access_token, refresh_token
    else:
        print(response.json())


def GetPosts():
    response = requests.get(
        f'{endpoint}/post')
    print(response.json())


def GetOnePost(postId):
    response = requests.get(
        f'{endpoint}/post/{postId}')
    print(response.json())


def CreatePost(access_token, title, description):
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    json_data = {
        'title': title,
        'description': description,
    }
    response = requests.post(
        f'{endpoint}/post', headers=headers, json=json_data)
    print(response.json())


def EditPost(access_token, title, description, postId):
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    json_data = {
        'title': title,
        'description': description,
    }
    response = requests.put(
        f'{endpoint}/post/{postId}', headers=headers, json=json_data)
    print(response.json())


def DeletePost(access_token, postId):
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    response = requests.delete(
        f'{endpoint}/post/{postId}', headers=headers)
    print(response)


userName = "blank"
userEmail = "test@test.com"
userPassword = 1234567

postTitle = "post title test1"
postDesc = "post desc test1"

flag = True
while flag == True:
    print(" Enter num of operation ")
    print(" (1) create user")
    print(" (2) login user")
    print(" (3) get all posts")
    print(" (4) get one posts")
    print(" (5) create post")
    print(" (6) edit post")
    print(" (7) delete post")
    print(" (8) exit")

    OP0 = input()

    match OP0:
        case '1':
            CreateUser(userName, userEmail, userPassword)
        case '2':
            LoginUser(userEmail, userPassword)
        case '3':
            GetPosts()
        case '4':
            postId = input("enter post id to get \n")
            GetOnePost(postId)
        case '5':
            tokens = LoginUser(userEmail, userPassword)
            CreatePost(tokens[0], postTitle, postDesc)
        case '6':
            tokens = LoginUser(userEmail, userPassword)
            postId = input("enter post id to edit \n")
            postTitle = input("enter new post title \n")
            postDesc = input("enter new post desc \n")
            EditPost(tokens[0], postTitle, postDesc, postId)
        case '7':
            tokens = LoginUser(userEmail, userPassword)
            postId = input("enter post id to delete \n")
            DeletePost(tokens[0], postId)
        case '8':
            flag = False
