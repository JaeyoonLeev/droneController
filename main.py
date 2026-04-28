from djitellopy import Tello
import keyboard
import time


# ---------------------------
# 드론 연결
# ---------------------------
def connect_drone():
    tello = Tello()
    try:
        tello.connect()
        battery = tello.get_battery()
        print(f"배터리: {battery}%")
        return tello
    except Exception as e:
        print("❌ 드론 연결 실패:", e)
        return None


# ---------------------------
# 동작 함수
# ---------------------------
def takeoff_drone(tello):
    try:
        tello.takeoff()
        print("이륙")
    except Exception as e:
        print("이륙 실패:", e)


def move_left(tello):
    try:
        tello.move_left(20)
        print("왼쪽 이동")
    except Exception as e:
        print("이동 실패:", e)


def rotate_ccw(tello):
    try:
        tello.rotate_counter_clockwise(90)
        print("반시계 회전")
    except Exception as e:
        print("회전 실패:", e)


def move_forward(tello):
    try:
        tello.move_forward(20)
        print("전진")
    except Exception as e:
        print("전진 실패:", e)


# ---------------------------
# 메인 루프 (keyboard)
# ---------------------------
def main_loop(tello):
    print("조작 키:")
    print("A: 왼쪽 이동")
    print("Q: 반시계 회전")
    print("W: 전진")
    print("ESC: 종료")

    # 디바운싱용 상태 변수
    key_state = {
        'a': False,
        'q': False,
        'w': False
    }

    while True:
        # A 키
        if keyboard.is_pressed('a'):
            if not key_state['a']:
                move_left(tello)
                key_state['a'] = True
        else:
            key_state['a'] = False

        # Q 키
        if keyboard.is_pressed('q'):
            if not key_state['q']:
                rotate_ccw(tello)
                key_state['q'] = True
        else:
            key_state['q'] = False

        # W 키
        if keyboard.is_pressed('w'):
            if not key_state['w']:
                move_forward(tello)
                key_state['w'] = True
        else:
            key_state['w'] = False

        # ESC 종료
        if keyboard.is_pressed('esc'):
            print("착륙 후 종료")
            tello.land()
            break

        time.sleep(0.05)  # CPU 과부하 방지


# ---------------------------
# 실행
# ---------------------------
def main():
    tello = connect_drone()

    if tello is None:
        return

    takeoff_drone(tello)
    main_loop(tello)


if __name__ == "__main__":
    main()
