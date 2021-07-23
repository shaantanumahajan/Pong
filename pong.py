import pygame
import random
pygame.mixer.pre_init(44100 , -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(width/2 - 7.5, height/2 - 7.5, 15, 15)
player = pygame.Rect(width - 10, height/2 - 50, 10, 100)
opponent = pygame.Rect(0, height/2 - 50, 10, 100)
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)


ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
opponent_speed = 6

player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 20)

score_time = None
pong_sound = pygame.mixer.Sound('Games\pong.wav')
loss = pygame.mixer.Sound('Games\loss.wav')

def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
        pygame.mixer.Sound.play(pong_sound)

    if ball.left <=0:
        player_score +=1
        pygame.mixer.Sound.play(loss)
        score_time = pygame.time.get_ticks()
        

    if ball.right >= width:
        opponent_score += 1
        pygame.mixer.Sound.play(loss)
        score_time = pygame.time.get_ticks()
        

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(opponent) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        

def player_animation():
    player.y += player_speed
    if player.bottom >= height:
        player.bottom = height
    if player.top <= 0:
        player.top = 0
def opponent_animation():
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top < ball.y:
        opponent.bottom += opponent_speed
    if opponent.bottom >= height:
        opponent.bottom = height
    if opponent.top <= 0:
        opponent.top = 0
def ball_restart():
    global ball_speed_y, ball_speed_x, score_time
    current_time = pygame.time.get_ticks() 
    ball.center = (width/2, height/2)
    
    if current_time - score_time < 2000:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_x = 5 * random.choice((1,-1))
        ball_speed_y = 5 *random.choice((1,-1))
        score_time = None 

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball) 
    pygame.draw.aaline(screen, light_grey, (width/2, 0), (width/2, height))
    
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (460,300))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (430,300))
    if score_time:
        ball_restart()

    pygame.display.flip()
    clock.tick(60)






if __name__ == "__main__":
    main()