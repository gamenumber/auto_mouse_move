import pyautogui
import time

# 2분마다 마우스 움직임을 수행하는 함수
def move_mouse():
    while True:
        # 마우스를 조금씩 이동시킵니다.
        pyautogui.moveRel(5, 5)
        # 2분을 기다립니다.
        time.sleep(120)

# 프로그램 실행
if __name__ == "__main__":
    move_mouse()