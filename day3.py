import turtle
import random
import time

# স্ক্রিন সেটআপ
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Victory Day Celebration - 16 December")
screen.setup(width=800, height=600)

# টেক্সট দেখানোর জন্য ফাংশন
def show_text(text, y, size, color):
    pen = turtle.Turtle()
    pen.color(color)
    pen.hideturtle()
    pen.penup()
    pen.goto(0, y)
    pen.write(text, align="center", font=("Arial", size, "bold"))
    time.sleep(2)
    pen.clear()

# বাংলাদেশের পতাকা আঁকার ফাংশন
def draw_flag():
    flag = turtle.Turtle()
    flag.speed(0)

    # সবুজ রঙের আয়তক্ষেত্র
    flag.penup()
    flag.goto(-180, -90)  # নিচের বাম দিক থেকে শুরু
    flag.pendown()
    flag.color("green")
    flag.begin_fill()
    for _ in range(2):
        flag.forward(360)  # আয়তক্ষেত্রের দৈর্ঘ্য
        flag.left(90)
        flag.forward(180)  # আয়তক্ষেত্রের প্রস্থ
        flag.left(90)
    flag.end_fill()

    # লাল বৃত্ত (পতাকার মাঝখানে)
    flag.penup()
    flag.goto(0, -40)  # মাঝখানে বৃত্তের পজিশন
    flag.pendown()
    flag.color("red")
    flag.begin_fill()
    flag.circle(50)  # বৃত্তের ব্যাসার্ধ
    flag.end_fill()

    flag.hideturtle()

# ঝর্ণাবাজি (sparklers) তৈরির ফাংশন
def sparklers():
    spark = turtle.Turtle()
    spark.speed(0)
    spark.hideturtle()
    spark.penup()
    colors = ["yellow", "white", "gold", "orange"]

    # পতাকার চারপাশে ঝর্ণাবাজি তৈরি
    positions = [(-200, -100), (200, -100), (-200, 100), (200, 100)]  # 4 কোণে পজিশন
    for pos in positions:
        spark.goto(pos)
        for _ in range(36):  # চারদিকে লাইন ছড়ানো
            spark.color(random.choice(colors))
            spark.forward(50)
            spark.backward(50)
            spark.right(10)
        spark.clear()

# আতশবাজির ইফেক্ট তৈরির ফাংশন
def fireworks(x, y):
    colors = ["red", "yellow", "blue", "green", "orange", "white", "purple"]
    firework = turtle.Turtle()
    firework.speed(0)
    firework.hideturtle()
    firework.penup()
    firework.goto(x, y)
    firework.pendown()

    for _ in range(36):
        firework.color(random.choice(colors))
        firework.forward(100)
        firework.right(170)
        firework.forward(100)
        firework.right(10)

    firework.hideturtle()

# মেইন প্রোগ্রাম
show_text("16 ডিসেম্বর", 50, 30, "red")  # প্রথমে 16 ডিসেম্বর শো করানো
draw_flag()  # বাংলাদেশের পতাকা আঁকা
sparklers()  # পতাকার চারপাশে ঝর্ণাবাজি

show_text("Happy Victory Day!", -150, 25, "white")  # হ্যাপি ভিক্টরি ডে শো করানো

# ফায়ারওয়ার্ক ইফেক্ট
for _ in range(5):  # ৫ বার আতশবাজি ইফেক্ট দেখানো হবে
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    fireworks(x, y)

time.sleep(5)
turtle.done()
