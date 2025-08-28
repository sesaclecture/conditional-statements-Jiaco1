from datetime import datetime


# 1 사용자 정보 딕셔너리
users = {
    "jiacoco": {
        "uid": "jiacoco",
        "password": "1115",
        "username": "Jia",
        "birthdate": "19961115",
        "role": "admin"
    },
    "nickolodian": {
        "uid": "nickolodian",
        "password": "0828",
        "username": "Nick",
        "birthdate": "19980527",
        "role": "editor"
    },
    "mmic": {
        "uid": "mmic",
        "password": "4569",
        "username": "Mike",
        "birthdate": "20000101",
        "role": "viewer"
    }
}

def print_users(user_dict): #아이디 기준 출력 (+역할)
    print("\n====== 전체 사용자 목록 ======")
    for uid, info in user_dict.items():
        print(f"\nID: {uid}")
        print(f"  역할     : {info['role']}")


# 2 회원가입
def register_user(users):
    print("\n[ 회원가입 ]")

    while True:                                                            
        new_uid = input("아이디: ").strip()
        if new_uid in users:
            print("이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.")
        else:
            break

    name = input("이름: ").strip()                                             

    while True:                                                           
        birth = input("생년월일 (YYYYMMDD): ").strip()
        try:
            birth_date = datetime.strptime(birth, "%Y%m%d")
            
            
            if birth_date.year > 2011:
                print("2011년생 이상만 가입할 수 있습니다.")
            else:
                break
        except ValueError:
            print("형식 오류. 예: 20110315")

    while True:
        password = input("비밀번호 (숫자만, 4자리 이상): ").strip()
        if not password.isdigit():
            print("숫자로만 입력해주세요")
        elif len(password) < 4:
            print("4자리 이상 입력해주세요")
        else:
            break

    roles = ['viewer', 'editor', 'admin']
    while True:
        role = input("역할 선택 (viewer/editor/admin): ").strip().lower()
        if role in roles:
            break
        else:
            print("viewer/editor/admin 중 하나를 선택하세요.")

    users[new_uid] = {
        "uid": new_uid,
        "password": password,
        "username": name,
        "birthdate": birth,
        "role": role
    }

    print(f"\n'{new_uid}' 계정이 성공적으로 등록되었습니다.")
    print_users(users)



# 3 로그인
def login(users):
    print("\n[ 로그인 ]")
    uid = input("아이디: ").strip()
    password = input("비밀번호: ").strip()

    if uid not in users:
        print("존재하지 않는 아이디입니다.")
        return None

    if users[uid]['password'] != password:
        print("비밀번호가 일치하지 않습니다.")
        return None

    print(f"{uid}님 로그인 성공! (권한: {users[uid]['role']})")
    return users[uid]



def print_user_info(user):  #조회
    print("\n[ 사용자 정보 ]")
    print(f"ID       : {user['uid']}")
    print(f"비밀번호 : {user['password']}")
    print(f"사용자명 : {user['username']}")
    print(f"생년월일 : {user['birthdate']}")
    print(f"역할     : {user['role']}")


def edit_user(users, uid):  #수정``
    user = users[uid]
    print("\n[ 사용자 정보 수정 ]")
    name = input(f"새 이름 (현재: {user['username']}): ") or user['username']
    birth = input(f"새 생년월일 (현재: {user['birthdate']}): ") or user['birthdate']
    password = input(f"새 비밀번호 (현재: {user['password']}): ") or user['password']
    role = input(f"새 역할 (viewer/editor/admin, 현재: {user['role']}): ") or user['role']

    if role not in ['viewer', 'editor', 'admin']:
        print("역할은 viewer/editor/admin 중 하나여야 합니다.")
        return

    user['username'] = name
    user['birthdate'] = birth
    user['password'] = password
    user['role'] = role

    print(f"'{uid}' 정보가 수정되었습니다.")
    print_users(users)

# 4  Admin
def show_admin_menu(users):
    while True:
        print("\n[ 관리자(admin) 메뉴 ]")
        print("1. 전체 사용자 목록 보기")
        print("2. 사용자 정보 수정")
        print("3. 사용자 삭제")
        print("4. 로그아웃")

        choice = input("선택: ")

        if choice == '1':
            print_users(users)

        elif choice == '2':
            target_id = input("수정할 사용자 아이디 입력: ")
            if target_id in users:
                edit_user(users, target_id)
            else:
                print("존재하지 않는 사용자입니다.")

        elif choice == '3':
            target_id = input("삭제할 사용자 아이디 입력: ")
            if target_id in users:
                confirm = input(f"'{target_id}' 계정을 정말 삭제할까요? (y/n): ")
                if confirm.lower() == 'y':
                    del users[target_id]
                    print(f"'{target_id}' 삭제 완료.")
                    print_users(users)
            else:
                print("존재하지 않는 사용자입니다.")

        elif choice == '4':
            print("로그아웃 되었습니다.")
            break

        else:
            print("잘못된 선택입니다.")

# 5  Editor
def show_editor_menu(current_user, users):
    while True:
        print("\n[ 에디터(editor) 메뉴 ]")
        print("1. 내 정보 보기")
        print("2. 내 정보 수정")
        print("3. 내 계정 삭제")
        print("4. 로그아웃")

        choice = input("선택: ")

        if choice == '1':
            print_user_info(current_user)

        elif choice == '2':
            edit_user(users, current_user['uid'])

        elif choice == '3':
            confirm = input("정말 계정을 삭제하시겠습니까? (y/n): ")
            if confirm.lower() == 'y':
                del users[current_user['uid']]
                print("계정이 삭제되었습니다.")
                print_users(users)
                break

        elif choice == '4':
            print("로그아웃 되었습니다.")
            break

        else:
            print("잘못된 선택입니다.")

# 6 Viewer
def show_viewer_menu(current_user, users):
    while True:
        print("\n[ 뷰어(viewer) 메뉴 ]")
        print("1. 내 정보 보기")
        print("2. 내 계정 삭제")
        print("3. 로그아웃")

        choice = input("선택: ")

        if choice == '1':
            print_user_info(current_user)

        elif choice == '2':
            confirm = input("정말 계정을 삭제하시겠습니까? (y/n): ")
            if confirm.lower() == 'y':
                del users[current_user['uid']]
                print("계정이 삭제되었습니다.")
                print_users(users)
                break

        elif choice == '3':
            print("로그아웃 되었습니다.")
            break

        else:
            print("잘못된 선택입니다.")



if __name__ == "__main__":
    print_users(users)  

    while True:
        print("\n1. 로그인")
        print("2. 회원가입")
        print("3. 종료")
        menu = input("메뉴 선택: ").strip()

        if menu == '1':
            logged_in = login(users)
            if logged_in:
                role = logged_in['role']
                if role == 'admin':
                    show_admin_menu(users)
                elif role == 'editor':
                    show_editor_menu(logged_in, users)
                elif role == 'viewer':
                    show_viewer_menu(logged_in, users)

        elif menu == '2':
            register_user(users)

        elif menu == '3':
            print("프로그램 종료")
            break

        else:
            print("올바른 메뉴 번호를 입력해주세요.")