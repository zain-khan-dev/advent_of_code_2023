

class Constants:
    DELIMITER = ";"
    GREEN = "green"
    BLUE = "blue"
    RED = "red"
    BALLS_DELIMITER = ","
    GAMES_DELIMITER = ":"
    TOTAL_PERMITTED = {
        RED: 12,
        GREEN: 13,
        BLUE: 14
    }



def parse_ball_input(ball_input):
    count, color = ball_input.strip().split(" ")
    return int(count), color

def get_min_ball(input, ball_hash):
    for ball_input in input.split(Constants.BALLS_DELIMITER):
        count, color = parse_ball_input(ball_input)
        ball_hash[color] = max(ball_hash.get(color, count), count)
    return ball_hash

    

if __name__ == "__main__":
    final_result = 0
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            delimited = line.split(Constants.GAMES_DELIMITER)
            game_id = int(delimited[0].split(" ")[1])
            include = True
            ball_hash = {}
            for input in delimited[1].split(Constants.DELIMITER): # Skip first as it contains game meta info
                ball_hash = get_min_ball(input, ball_hash)
            result = 1 
            for count in ball_hash.values():
                result *= count
            final_result += result
    print(final_result)