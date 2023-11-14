from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    screen.update()

    car.create_car()
    car.move_cars()

    # Detect collision with car
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect when player has reached the finish line
    if player.is_at_finish_line():
        player.reset_position()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()
