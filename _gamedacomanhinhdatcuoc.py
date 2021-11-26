import pygame , sys , random , os
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('ChanHuy')
WINDOW_SIZE = (1500,800)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)   
display = pygame.Surface((1500,800))
font = pygame.font.SysFont(None, 90)

BUTTON_WIDTH=120
BUTTON_HEIGHT=50

betvalue=0 
money=200
def win(x):
    if(x==1):
        draw_text('BLUE WIN', font, (250, 0, 0), screen, 600, 300)
    if(x==2):
        draw_text('RED WIN', font, (250, 0, 0), screen, 600, 300)
    if(x==3):
        draw_text('PURPLE WIN', font, (250, 0, 0), screen, 600, 300)
#hambet
def bet():
    global betvalue
    global money
    #Thuoc tinh Button
    buttonc_image = pygame.image.load('buttonc.png')
    buttonc_location = [50,150]
    buttonc_image=pygame.transform.scale(buttonc_image,(BUTTON_WIDTH,BUTTON_HEIGHT))

    buttons_image = pygame.image.load('button1.png')
    buttons_location = [400,150]
    buttons_image=pygame.transform.scale(buttons_image,(BUTTON_WIDTH,BUTTON_HEIGHT))
    betvalue=0
    

    running=True
    while running:
        

        
        #ve cai background voi cai chu thoi
        screen.fill((0,0,0))
        draw_text(str(betvalue), font, (255, 255, 255), screen, 20, 90)
        draw_text(str(money), font, (255, 255, 255), screen, 20, 400)
        draw_text('How much do you want to bet', font, (255, 255, 255), screen, 20, 20)
        draw_text('money left', font, (255, 255, 255), screen, 20, 340)
        
        #lay vi tri con tro chuot
        mx, my = pygame.mouse.get_pos()

        #set rect for button
        button_c = pygame.Rect(buttonc_location[0],buttonc_location[1],BUTTON_WIDTH,BUTTON_HEIGHT)
        button_s = pygame.Rect(buttons_location[0],buttons_location[1],BUTTON_WIDTH,BUTTON_HEIGHT)

        if button_c.collidepoint((mx, my)):
            if click: #neu click=true va vi tri con chuot nam trong vung rect button 1 thi chay toi ham game
                if(money>=50):
                    betvalue+=50
                    money-=50

        if button_s.collidepoint((mx, my)):
            if click: #neu click=true va vi tri con chuot nam trong vung rect button 1 thi chay toi ham game
                game()
                running=False

        
        # draw button
        screen.blit(buttonc_image,buttonc_location)
        screen.blit(buttons_image,buttons_location)

 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
#ham animtion, tach may cai ham ra rieng de len dau ne.
def load_animation(path,frame_durations): #[7,7]
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((2,139,218))
        
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame

#ham viet chu thoi, khong quan trong
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

 
click = False
 #ham menu chinh
def main_menu():
    #Thuoc tinh Button
    button2_image = pygame.image.load('button2.png')
    button2_location = [50,150]
    button2_image=pygame.transform.scale(button2_image,(BUTTON_WIDTH,BUTTON_HEIGHT))
    
    button1_image = pygame.image.load('button1.png')
    button1_image=pygame.transform.scale(button1_image,(BUTTON_WIDTH,BUTTON_HEIGHT))
    button1_location = [50,50]   

    button3_image = pygame.image.load('button1.png')
    button3_image=pygame.transform.scale(button1_image,(BUTTON_WIDTH,BUTTON_HEIGHT))
    button3_location = [50,250]  

    while True:
        #cap nhat lai kich thuoc khi chay lap
        button1_image=pygame.transform.scale(button1_image,(BUTTON_WIDTH,BUTTON_HEIGHT))
        button2_image=pygame.transform.scale(button2_image,(BUTTON_WIDTH,BUTTON_HEIGHT))   
        button3_image=pygame.transform.scale(button3_image,(BUTTON_WIDTH,BUTTON_HEIGHT)) 
        
        #ve cai background voi cai chu thoi
        screen.fill((0,0,0))
        #draw_text(str(money), font, (255, 255, 255), screen, 20, 20)

        #lay vi tri con tro chuot
        mx, my = pygame.mouse.get_pos()

        #set rect for button
        button_1 = pygame.Rect(button1_location[0],button1_location[1],BUTTON_WIDTH,BUTTON_HEIGHT)
        button_2 = pygame.Rect(button2_location[0],button2_location[1],BUTTON_WIDTH,BUTTON_HEIGHT)
        button_3 = pygame.Rect(button3_location[0],button3_location[1],BUTTON_WIDTH,BUTTON_HEIGHT)
        
        if button_1.collidepoint((mx, my)):
            button1_image=pygame.transform.scale(button1_image,(150,70))# dua con tro chuot se zoom bu ra
            if click: #neu click=true va vi tri con chuot nam trong vung rect button 1 thi chay toi ham game
                bet()
        if button_2.collidepoint((mx, my)):
            button2_image=pygame.transform.scale(button2_image,(150,70))# dua con tro chuot se zoom bu ra
            if click: #neu click=true va vi tri con chuot nam trong vung rect button 2 thi thoat game
                pygame.quit()
                sys.exit()
        if button_3.collidepoint((mx, my)):
            button3_image=pygame.transform.scale(button3_image,(150,70))# dua con tro chuot se zoom bu ra
            if click: #neu click=true va vi tri con chuot nam trong vung rect button 2 thi thoat game
                pygame.quit()
                sys.exit()
        # draw button
        screen.blit(button1_image,button1_location)
        screen.blit(button2_image,button2_location)
        screen.blit(button3_image,button3_location)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)


#ham game, copy het hau het code vao day, chi chua ham voi lai may cai setting window ơ ngoai
def game():
    blue_turtle_location = [0,50]
    purple_turtle_location=[0,120]
    red_turtle_location = [0,190]

    blue_turtle_rect = pygame.Rect(blue_turtle_location[0],blue_turtle_location[1],36,15)
    purple_turtle_rect = pygame.Rect(purple_turtle_location[0],purple_turtle_location[1],36,15)
    red_turtle_rect = pygame.Rect(red_turtle_location[0],red_turtle_location[1],36,15)

    global animation_frames
    animation_frames = {}
    
    
    
    animation_database1 = {}
    animation_database1['turtle_blue_walk'] = load_animation('blue_turtle/turtle_blue_walk',[7,7])

    animation_database2 = {}
    animation_database2['purple_turtle_walk'] = load_animation('purple_turtle/purple_turtle_walk',[7,7])

    animation_database3 = {}
    animation_database3['red_turtle_walk'] = load_animation('red_turtle/red_turtle_walk',[7,7])

    blue_turtle_walk = 'turtle_blue_walk'
    blue_turtle_frame = 0
    blue_turtle_flip = False

    purple_turtle_walk = 'purple_turtle_walk'
    purple_turtle_frame = 0
    purple_turtle_flip = False

    red_turtle_walk = 'red_turtle_walk'
    red_turtle_frame = 0
    red_turtle_flip = False

    test_rect = pygame.Rect(1400,0,1,1000)
    boon_rect = pygame.Rect(700,50,20,20)
    
    running=True
    #bat dau game loop
    while running: #game loop

        display.fill((231,231,104))
        pygame.draw.rect(display,(255,0,0),boon_rect)
        #speed
        if blue_turtle_flip:
            speed1  = -random.randint(1,7)
        else :
            speed1 = random.randint(1,7)
        speed2 = random.randint(3,9)
        speed3 = random.randint(5,7)
        
        blue_turtle_rect.x = blue_turtle_location[0]
        purple_turtle_rect.x = purple_turtle_location[0]
        red_turtle_rect.x = red_turtle_location[0]

        if blue_turtle_rect.colliderect(boon_rect) or purple_turtle_rect.colliderect(boon_rect) or red_turtle_rect.colliderect(boon_rect):

            if blue_turtle_rect.colliderect(boon_rect):
                blue_turtle_flip = True
            if purple_turtle_rect.colliderect(boon_rect):
                purple_turtle_flip = True
            if red_turtle_rect.colliderect(boon_rect):
                red_turtle_flip = True
            

        if blue_turtle_rect.colliderect(test_rect) or purple_turtle_rect.colliderect(test_rect) or red_turtle_rect.colliderect(test_rect):
            pygame.draw.rect(display,(255,0,0),test_rect)
            if blue_turtle_rect.colliderect(test_rect):
                speed1 = 0
                speed2 = 0
                speed3 = 0
                win(1)
                
            if purple_turtle_rect.colliderect(test_rect):
                speed1 = 0
                speed2 = 0
                speed3 = 0
                win(3)

            if red_turtle_rect.colliderect(test_rect):
                speed1 = 0
                speed2 = 0
                speed3 = 0
                win(2)
               
            
        else:
            pygame.draw.rect(display,(0,0,0),test_rect)

        blue_turtle_location[0] += speed1
        purple_turtle_location[0] += speed2
        red_turtle_location[0] += speed3   
        
        #blue turtle animation
        blue_turtle_frame += 1
        if blue_turtle_frame >= len(animation_database1[blue_turtle_walk]):
            blue_turtle_frame = 0
        blue_turtle_img_id = animation_database1[blue_turtle_walk][blue_turtle_frame]
        blue_turtle_img = animation_frames[blue_turtle_img_id]
        display.blit(pygame.transform.flip(blue_turtle_img,blue_turtle_flip,False),(blue_turtle_location))

        #purple turtle animation
        purple_turtle_frame += 1
        if purple_turtle_frame >= len(animation_database2[purple_turtle_walk]):
         purple_turtle_frame = 0
        purple_turtle_img_id = animation_database2[purple_turtle_walk][purple_turtle_frame]
        purple_turtle_img = animation_frames[purple_turtle_img_id]
        display.blit(purple_turtle_img,(purple_turtle_location))

        #red turtle animation
        red_turtle_frame += 1
        if red_turtle_frame >= len(animation_database3[red_turtle_walk]):
            red_turtle_frame = 0
        red_turtle_img_id = animation_database3[red_turtle_walk][red_turtle_frame]
        red_turtle_img = animation_frames[red_turtle_img_id]
        display.blit(red_turtle_img,(red_turtle_location))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            
        pygame.display.update()
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        mainClock.tick(60)
 

#goi ham menu khi chay chuong trinh
main_menu()