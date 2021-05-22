import pyautogui, pyperclip, random, time

msg = input("Nhập nội dung cần spam").split("||")
n = int(input("Nhập số lần spam"))
m = float(input("Nhập time delay"))

print("Chuẩn bị")
for i in range(5,0,-1):
    print(i, end="...", flush=True)
    print("Bắt đầu")
for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(m)
