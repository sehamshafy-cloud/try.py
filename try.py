
import pgzrun
TITLE = "Quiz Master"

WIDTH = 970
HEIGHT = 750

marquee_box = Rect(0,0,930,65)
question_box = Rect(0,0,430,350)
timer_box = Rect(0,0,140,100)
answer_box1 = Rect(0,0,350,100)
answer_box2 = Rect(0,0,350,100)
answer_box3 = Rect(0,0,350,100)
answer_box4 = Rect(0,0,350,100)
skip_box = Rect(0,0,140,65)

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0

score = 0
time_left = 10
marquee_message = ""
is_game_over = False

marquee_box.move_ip(20,665)
question_box.move_ip(30,180)
timer_box.move_ip(420,40)
answer_box1.move_ip(570,180)
answer_box2.move_ip(570,295)
answer_box3.move_ip(570,410)
answer_box4.move_ip(570,525)
skip_box.move_ip(750,55)

def draw():
    screen.clear()
    screen.fill(color="black")

    screen.draw.filled_rect(marquee_box,"dark blue")
    screen.draw.filled_rect(question_box,"navy blue")
    screen.draw.filled_rect(timer_box,"dark green")
    screen.draw.filled_rect(skip_box,"dark orange")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"pink")

pgzrun.go()

