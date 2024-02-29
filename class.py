class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password



    def display(self):
        print(f"name : {self.name}, username(ID) : {self.username}")


members = []

members.append(Member("가나다", "abc", "123"))
members.append(Member("라마바", "def", "456"))
members.append(Member("사아자", "ghi", "789"))

            #append()는 요소 한 개씩 밖에 추가 못함.


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author



posts = []
posts.append(Post("spain1", "happy uno", members[0].username))
posts.append(Post("japan1", "sakura", members[1].username))
posts.append(Post("korea1", "hana", members[2].username))
posts.append(Post("spain2", "happy dos", members[0].username))
posts.append(Post("japan2", "hi", members[1].username))
posts.append(Post("korea2", "dul", members[2].username))
posts.append(Post("spain3", "happy tres", members[0].username))
posts.append(Post("japan3", "so", members[1].username))
posts.append(Post("korea3", "sat", members[2].username))


for member in members:
    print(member.name)

t1 = []
t2 = []
for post in posts:
    if post.author == members[2].username:
        t1.append(post.title)
    else:
        pass
    if "happy" in list(post.content.split()):
        t2.append(post.title)
    else:
        pass
    # split() 는 only 문자열에서만 적용 가능. 리스트는 적용 안 됨.

print(f"happy라는 단어가 포함된 게시글의 title : {t2}")
print(f"'사아자'가 작성한 글의 title: {t1}")

a = ""
d = ""


a = input("Member의 인스턴스를 추가하시길 원하나요? >> (Y/N)")
while a not in ['y', 'Y', 'n', 'N']:
    a = input("(Y/N)의 형식으로 입력하셔야 됩니다.  Member의 인스턴스를 추가하시길 원하나요? >> (Y/N) ")

if a == 'y' or a =='Y':
    b = input("name, username, password를 입력해주세요")
    if len(b.split(',')) == 3:
        c = b.split(',')
    else:
        while len(b.split(',')) != 3:
            b  = input("양식에 맞게 입력해주세요. name, username, password.")
    
    members.append(Member(b[0], b[1], b[2]))
    print(f"현재 Member의 인원 : {len(members)}")
if a == 'n' or a =='N':
    print("수고하셨습니다. 작업을 마치겠습니다.")




d = input("Post의 인스턴스를 추가하시길 원하나요? >> (Y/N)")
while d not in ['y', 'Y', 'n', 'N']:
    d = input("(Y/N)의 형식으로 입력하셔야 됩니다.  Post의 인스턴스를 추가하시길 원하나요? >> (Y/N) ")

if d == 'y' or d =='Y':
    e = input("title, content, author를 입력해주세요")
    if len(e.split(',')) == 3:
        f = e.split(',')
    else:
        while len(e.split(',')) == 3:
            e  = input("양식에 맞게 입력해주세요. title, content, author.")
    
    members.append(Member(b[0], b[1], b[2]))
    print(f"현재 Member의 인원 : {len(posts)}")
if d == 'n' or d =='N':
    print("수고하셨습니다. 작업을 마치겠습니다.")