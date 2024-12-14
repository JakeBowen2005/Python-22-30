import turtle as t
import paddle
import ball
import scoreboard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = scoreboard.Scoreboard()





game = True


paddle1 = paddle.Paddle(position=(350,0))
paddle2 = paddle.Paddle(position=(-350,0))
ball = ball.Ball()

screen.listen()
screen.onkey(fun=paddle1.up, key="Up")
screen.onkey(fun=paddle1.down, key="Down")
screen.onkey(fun=paddle2.up, key="w")
screen.onkey(fun=paddle2.down, key="s")

while game:
    # time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y()

    if (paddle1.xcor() - 15 < ball.xcor() < paddle1.xcor() + 15 and
        paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50):
        ball.increase_speed()
        ball.change_x()


    if (paddle2.xcor() - 15 < ball.xcor() < paddle2.xcor() + 15 and
        paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50):
        ball.increase_speed()
        ball.change_x()

    if ball.xcor() > 395:
       ball.reset()
       scoreboard.plus_left()

    if ball.xcor() < -395:
        ball.reset()
        scoreboard.plus_right()





screen.exitonclick()