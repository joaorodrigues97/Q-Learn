import math
import sys
import pygame

class Q_Learning():

    pygame.init()
    def py_init(self):
        background_colour = (255,255,255)
        (width, height) = (800, 600)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Tutorial 1')
        self.screen.fill(background_colour)
        pygame.display.flip()

    def py_draw(self, x, y):
        
        line_color = (0, 0, 0)
        ## Linhas perpendiculares
        pygame.draw.line(self.screen, line_color, (200,0), (200, 600), 4)
        pygame.draw.line(self.screen, line_color, (400,0), (400, 600), 4)
        pygame.draw.line(self.screen, line_color, (600,0), (600, 600), 4)
        ## Linhas horizontais
        pygame.draw.line(self.screen, line_color, (0,200), (800, 200), 4)
        pygame.draw.line(self.screen, line_color, (0,400), (800, 400), 4)
        ## Obstaculo
        pygame.draw.rect(self.screen, (100,100,100), pygame.Rect(202, 202, 198,198))
        ##Cruzes nos estados
        ## (1,3)
        pygame.draw.line(self.screen, line_color, (0, 0), (200, 200),4)
        pygame.draw.line(self.screen, line_color, (0, 200), (200, 0),4)
        ## (1,2)
        pygame.draw.line(self.screen, line_color, (0, 200), (200, 400), 4)
        pygame.draw.line(self.screen, line_color, (0, 400), (200, 200), 4)
        ## (1,1)
        pygame.draw.line(self.screen, line_color, (0, 400), (200, 600), 4)
        pygame.draw.line(self.screen, line_color, (0, 600), (200, 400), 4)
        ## (2,3)
        pygame.draw.line(self.screen, line_color, (200, 0), (400, 200), 4)
        pygame.draw.line(self.screen, line_color, (200, 200), (400, 0), 4)
        ## (2,1)
        pygame.draw.line(self.screen, line_color, (200, 400), (400, 600), 4)
        pygame.draw.line(self.screen, line_color, (200, 600), (400, 400), 4)
        ## (3,3)
        pygame.draw.line(self.screen, line_color, (400, 0), (600, 200), 4)
        pygame.draw.line(self.screen, line_color, (400, 200), (600, 0), 4)
        ## (3,2)
        pygame.draw.line(self.screen, line_color, (400, 200), (600, 400), 4)
        pygame.draw.line(self.screen, line_color, (400, 400), (600, 200), 4)
        ## (3,1)
        pygame.draw.line(self.screen, line_color, (400, 400), (600, 600), 4)
        pygame.draw.line(self.screen, line_color, (400, 600), (600, 400), 4)
        ## (4,1)
        pygame.draw.line(self.screen, line_color, (600, 400), (800, 600), 4)
        pygame.draw.line(self.screen, line_color, (600, 600), (800, 400), 4)
        ## Posição
        self.agent = pygame.draw.circle(self.screen, (0,0,255), (x,y), 10)

        font = pygame.font.Font('freesansbold.ttf', 20)
        ## STATE (1,1)
        text_1_1_up = font.render(str(round(self.state_1_1_up[0],2)), True, (0,0,0))
        self.screen.blit(text_1_1_up, (85, 430))
        text_1_1_down = font.render(str(round(self.state_1_1_down[0],2)), True, (0,0,0))
        self.screen.blit(text_1_1_down, (85, 560))
        text_1_1_left = font.render(str(round(self.state_1_1_left[0],2)), True, (0,0,0))
        self.screen.blit(text_1_1_left, (20, 490))
        text_1_1_right = font.render(str(round(self.state_1_1_right[0],2)), True, (0,0,0))
        self.screen.blit(text_1_1_right, (140, 490))
        ## STATE (1,2)
        text_1_2_up = font.render(str(round(self.state_1_2_up[0],2)), True, (0,0,0))
        self.screen.blit(text_1_2_up, (85, 230))
        text_1_2_down = font.render(str(round(self.state_1_2_down[0],2)), True, (0,0,0))
        self.screen.blit(text_1_2_down, (85, 360))
        text_1_2_left = font.render(str(round(self.state_1_2_left[0],2)), True, (0,0,0))
        self.screen.blit(text_1_2_left, (20, 290))
        text_1_2_right = font.render(str(round(self.state_1_2_right[0],2)), True, (0,0,0))
        self.screen.blit(text_1_2_right, (140, 290))
        ## STATE (1,3)
        text_1_3_up = font.render(str(round(self.state_1_3_up[0],2)), True, (0,0,0))
        self.screen.blit(text_1_3_up, (85, 30))
        text_1_3_down = font.render(str(round(self.state_1_3_down[0],2)), True, (0,0,0))
        self.screen.blit(text_1_3_down, (85, 160))
        text_1_3_left = font.render(str(round(self.state_1_3_left[0],2)), True, (0,0,0))
        self.screen.blit(text_1_3_left, (20, 90))
        text_1_3_right = font.render(str(round(self.state_1_3_right[0],2)), True, (0,0,0))
        self.screen.blit(text_1_3_right, (140, 90))
        ## STATE (2,1)
        text_2_1_up = font.render(str(round(self.state_2_1_up[0],2)), True, (0,0,0))
        self.screen.blit(text_2_1_up, (285, 430))
        text_2_1_down = font.render(str(round(self.state_2_1_down[0],2)), True, (0,0,0))
        self.screen.blit(text_2_1_down, (285, 560))
        text_2_1_left = font.render(str(round(self.state_2_1_left[0],2)), True, (0,0,0))
        self.screen.blit(text_2_1_left, (220, 490))
        text_2_1_right = font.render(str(round(self.state_2_1_right[0],2)), True, (0,0,0))
        self.screen.blit(text_2_1_right, (340, 490))
        ## STATE (2,3)
        text_2_3_up = font.render(str(round(self.state_2_3_up[0],2)), True, (0,0,0))
        self.screen.blit(text_2_3_up, (285, 30))
        text_2_3_down = font.render(str(round(self.state_2_3_down[0],2)), True, (0,0,0))
        self.screen.blit(text_2_3_down, (285, 160))
        text_2_3_left = font.render(str(round(self.state_2_3_left[0],2)), True, (0,0,0))
        self.screen.blit(text_2_3_left, (220, 90))
        text_2_3_right = font.render(str(round(self.state_2_3_right[0],2)), True, (0,0,0))
        self.screen.blit(text_2_3_right, (340, 90))
        ## STATE (3,1)
        text_3_1_up = font.render(str(round(self.state_3_1_up[0],2)), True, (0,0,0))
        self.screen.blit(text_3_1_up, (485, 430))
        text_3_1_down = font.render(str(round(self.state_3_1_down[0],2)), True, (0,0,0))
        self.screen.blit(text_3_1_down, (485, 560))
        text_3_1_left = font.render(str(round(self.state_3_1_left[0],2)), True, (0,0,0))
        self.screen.blit(text_3_1_left, (420, 490))
        text_3_1_right = font.render(str(round(self.state_3_1_right[0],2)), True, (0,0,0))
        self.screen.blit(text_3_1_right, (540, 490))
        ## STATE (3,2)
        text_3_2_up = font.render(str(round(self.state_3_2_up[0],2)), True, (0,0,0))
        self.screen.blit(text_3_2_up, (485, 230))
        text_3_2_down = font.render(str(round(self.state_3_2_down[0],2)), True, (0,0,0))
        self.screen.blit(text_3_2_down, (485, 360))
        text_3_2_left = font.render(str(round(self.state_3_2_left[0],2)), True, (0,0,0))
        self.screen.blit(text_3_2_left, (420, 290))
        text_3_2_right = font.render(str(round(self.state_3_2_right[0],2)), True, (0,0,0))
        self.screen.blit(text_3_2_right, (540, 290))
        ## STATE (3,3)
        text_3_3_up = font.render(str(round(self.state_3_3_up[0],2)), True, (0,0,0))
        self.screen.blit(text_3_3_up, (485, 30))
        text_3_3_down = font.render(str(round(self.state_3_3_down[0],2)), True, (0,0,0))
        self.screen.blit(text_3_3_down, (485, 160))
        text_3_3_left = font.render(str(round(self.state_3_3_left[0],2)), True, (0,0,0))
        self.screen.blit(text_3_3_left, (420, 90))
        text_3_3_right = font.render(str(round(self.state_3_3_right[0],2)), True, (0,0,0))
        self.screen.blit(text_3_3_right, (540, 90))
        ## STATE (4,1)
        text_4_1_up = font.render(str(round(self.state_4_1_up[0],2)), True, (0,0,0))
        self.screen.blit(text_4_1_up, (685, 430))
        text_4_1_down = font.render(str(round(self.state_4_1_down[0],2)), True, (0,0,0))
        self.screen.blit(text_4_1_down, (685, 560))
        text_4_1_left = font.render(str(round(self.state_4_1_left[0],2)), True, (0,0,0))
        self.screen.blit(text_4_1_left, (620, 490))
        text_4_1_right = font.render(str(round(self.state_4_1_right[0],2)), True, (0,0,0))
        self.screen.blit(text_4_1_right, (740, 490))
        ## Objective Positive
        text_pos = font.render(str(round(self.state_4_3_pos,2)), True, (0,0,0))
        self.screen.blit(text_pos, (690, 90))
        text_neg = font.render(str(round(self.state_4_2_neg,2)), True, (0,0,0))
        self.screen.blit(text_neg, (690, 290))

        pygame.display.flip()

    

    def initialize_var(self):
        ##Estado (1,1)
        self.state_1_1_up = [0.00, 'UP']
        self.state_1_1_down = [0.00, 'DOWN']
        self.state_1_1_left = [0.00, 'LEFT']
        self.state_1_1_right = [0.00, 'RIGHT']

        ##Estado (1,2)
        self.state_1_2_up = [0.00, 'UP']
        self.state_1_2_down = [0.00, 'DOWN']
        self.state_1_2_left = [0.00, 'LEFT']
        self.state_1_2_right = [0.00, 'RIGHT']

        ##Estado (1,3)
        self.state_1_3_up = [0.00, 'UP']
        self.state_1_3_down = [0.00, 'DOWN']
        self.state_1_3_left = [0.00, 'LEFT']
        self.state_1_3_right = [0.00, 'RIGHT']

        ##Estado (2,1)
        self.state_2_1_up = [0.00, 'UP']
        self.state_2_1_down = [0.00, 'DOWN']
        self.state_2_1_left = [0.00, 'LEFT']
        self.state_2_1_right = [0.00, 'RIGHT']

        ##Estado (3,3)
        self.state_2_3_up = [0.00, 'UP']
        self.state_2_3_down = [0.00, 'DOWN']
        self.state_2_3_left = [0.00, 'LEFT']
        self.state_2_3_right = [0.00, 'RIGHT']

        ##Estado (3,1)
        self.state_3_1_up = [0.00, 'UP']
        self.state_3_1_down = [0.00, 'DOWN']
        self.state_3_1_left = [0.00, 'LEFT]']
        self.state_3_1_right = [0.00, 'RIGHT']

        ##Estado (3,2)
        self.state_3_2_up = [0.00, 'UP']
        self.state_3_2_down = [0.00, 'DOWN']
        self.state_3_2_left = [0.00, 'LEFT']
        self.state_3_2_right = [0.00, 'RIGHT']

        ##Estado (3,3)
        self.state_3_3_up = [0.00, 'UP']
        self.state_3_3_down = [0.00, 'DOWN']
        self.state_3_3_left = [0.00, 'LEFT']
        self.state_3_3_right = [0.00, 'RIGHT']

        ##Estado (4,1)
        self.state_4_1_up = [0.00, 'UP']
        self.state_4_1_down = [0.00, 'DOWN']
        self.state_4_1_left = [0.00, 'LEFT']
        self.state_4_1_right = [0.00, 'RIGHT']

        ##Estado (4,2)
        self.state_4_2_neg = 0

        ##Estado (4,3)
        self.state_4_3_pos = 0

        self.state = (1,1)

        self.running = True
    
    def Q(self, q_atual, maxi, q_seguinte_up = None, q_seguinte_down = None, q_seguinte_left = None, q_seguinte_right = None):
        if maxi:
            q_atual += 0.5 * (-0.04 + 1 * max(q_seguinte_up, q_seguinte_down, q_seguinte_left, q_seguinte_right) - q_atual)
            return q_atual
        else:
            q_atual += 0.5 * (-0.04 + 1 * q_seguinte_up - q_atual)
            return q_atual

    def q_learning(self, key, state_inside):
        #STATE (1,1)
        if state_inside == (1,1):
            if key == 'UP':
                self.state_1_1_up[0] = math.floor(self.Q(self.state_1_1_up[0], True, self.state_1_2_down[0], self.state_1_2_up[0], self.state_1_2_left[0], self.state_1_2_right[0])*100)/100
                self.state = (1,2)
            if key == 'DOWN':
                self.state_1_1_down[0] = math.floor(self.Q(self.state_1_1_down[0], True, self.state_1_1_right[0], self.state_1_1_up[0], self.state_1_1_down[0], self.state_1_1_left[0])*100)/100
                self.state = (1,1)
            if key == 'LEFT':
                self.state_1_1_left[0] = math.floor(self.Q(self.state_1_1_left[0], True, self.state_1_1_right[0], self.state_1_1_up[0], self.state_1_1_down[0], self.state_1_1_left[0])*100)/100
                self.state = (1,1)
            if key == 'RIGHT':
                self.state_1_1_right[0] = math.floor(self.Q(self.state_1_1_right[0], True, self.state_2_1_up[0], self.state_2_1_down[0], self.state_2_1_left[0], self.state_2_1_right[0])*100)/100
                self.state = (2,1)
        #STATE (1,2)
        if state_inside == (1,2):
            if key == 'UP':
                self.state_1_2_up[0] = math.floor(self.Q(self.state_1_2_up[0], True, self.state_1_3_down[0], self.state_1_3_up[0], self.state_1_3_left[0], self.state_1_3_right[0])*100)/100
                self.state = (1,3)
            if key == 'DOWN':
                self.state_1_2_down[0] = math.floor(self.Q(self.state_1_2_down[0], True, self.state_1_1_up[0], self.state_1_1_down[0], self.state_1_1_left[0], self.state_1_1_right[0])*100)/100
                self.state = (1,1)
            if key == 'LEFT':
                self.state_1_2_left[0] = math.floor(self.Q(self.state_1_2_left[0], True, self.state_1_2_up[0], self.state_1_2_down[0], self.state_1_2_left[0], self.state_1_2_right[0])*100)/100
                self.state = (1,2)
            if key == 'RIGHT':
                self.state_1_2_right[0] = math.floor(self.Q(self.state_1_2_right[0], True, self.state_1_2_up[0], self.state_1_2_down[0], self.state_1_2_left[0], self.state_1_2_right[0])*100)/100
                self.state = (1,2)
        #STATE (1,3)
        if state_inside == (1,3):
            if key == 'UP':
                self.state_1_3_up[0] = math.floor(self.Q(self.state_1_3_up[0], True, self.state_1_3_right[0], self.state_1_3_left[0], self.state_1_3_up[0], self.state_1_3_down[0])*100)/100
                self.state = (1,3)
            if key == 'DOWN':
                self.state_1_3_down[0] = math.floor(self.Q(self.state_1_3_down[0], True, self.state_1_2_up[0], self.state_1_2_down[0], self.state_1_2_left[0], self.state_1_2_right[0])*100)/100
                self.state = (1,2)
            if key == 'LEFT':
                self.state_1_3_left[0] = math.floor(self.Q(self.state_1_3_left[0], True, self.state_1_3_right[0], self.state_1_3_left[0], self.state_1_3_up[0], self.state_1_3_down[0])*100)/100
                self.state = (1,3)
            if key == 'RIGHT':
                self.state_1_3_right[0] = math.floor(self.Q(self.state_1_3_right[0], True, self.state_2_3_left[0], self.state_2_3_up[0], self.state_2_3_down[0], self.state_2_3_right[0])*100)/100
                self.state = (2,3)
        #STATE (2,1)
        if state_inside == (2,1):
            if key == 'UP':
                self.state_2_1_up[0] = math.floor(self.Q(self.state_2_1_up[0], True, self.state_2_1_up[0], self.state_2_1_down[0], self.state_2_1_left[0], self.state_2_1_right[0])*100)/100
                self.state = (2,1)
            if key == 'DOWN':
                self.state_2_1_down[0] = math.floor(self.Q(self.state_2_1_down[0], True, self.state_2_1_up[0], self.state_2_1_down[0], self.state_2_1_left[0], self.state_2_1_right[0])*100)/100
                self.state = (2,1)
            if key == 'LEFT':
                self.state_2_1_left[0] = math.floor(self.Q(self.state_2_1_left[0], True, self.state_1_1_right[0], self.state_1_1_up[0], self.state_1_1_down[0], self.state_1_1_left[0])*100)/100
                self.state = (1,1)
            if key == 'RIGHT':
                self.state_2_1_right[0] = math.floor(self.Q(self.state_2_1_right[0], True, self.state_3_1_left[0], self.state_3_1_up[0], self.state_3_1_down[0], self.state_3_1_right[0])*100)/100
                self.state = (3,1)
        #STATE (2,3)
        if state_inside == (2,3):
            if key == 'UP':
                self.state_2_3_up[0] = math.floor(self.Q(self.state_2_3_up[0], True, self.state_2_3_up[0], self.state_2_3_down[0], self.state_2_3_left[0], self.state_2_3_right[0])*100)/100
                self.state = (2,3)
            if key == 'DOWN':
                self.state_2_3_down[0] = math.floor(self.Q(self.state_2_3_down[0], True, self.state_2_3_up[0], self.state_2_3_down[0], self.state_2_3_left[0], self.state_2_3_right[0])*100)/100
                self.state = (2,3)
            if key == 'LEFT':
                self.state_2_3_left[0] = math.floor(self.Q(self.state_2_3_left[0], True, self.state_1_3_right[0], self.state_1_3_left[0], self.state_1_3_up[0], self.state_1_3_down[0])*100)/100
                self.state = (1,3)
            if key == 'RIGHT':
                self.state_2_3_right[0] = math.floor(self.Q(self.state_2_3_right[0], True, self.state_3_3_left[0], self.state_3_3_right[0], self.state_3_3_up[0], self.state_3_3_down[0])*100)/100
                self.state = (3,3)
        #STATE (3,1)
        if state_inside == (3,1):
            if key == 'UP':
                self.state_3_1_up[0] = math.floor(self.Q(self.state_3_1_up[0], True, self.state_3_2_down[0], self.state_3_2_up[0], self.state_3_2_left[0], self.state_3_2_right[0])*100)/100
                self.state = (3,2)
            if key == 'DOWN':
                self.state_3_1_down[0] = math.floor(self.Q(self.state_3_1_down[0], True, self.state_3_1_up[0], self.state_3_1_down[0], self.state_3_1_left[0], self.state_3_1_right[0])*100)/100
                self.state = (3,1)
            if key == 'LEFT':
                self.state_3_1_left[0] = math.floor(self.Q(self.state_3_1_left[0], True, self.state_2_1_right[0], self.state_2_1_left[0], self.state_2_1_up[0], self.state_2_1_down[0])*100)/100
                self.state = (2,1)
            if key == 'RIGHT':
                self.state_3_1_right[0] = math.floor(self.Q(self.state_3_1_right[0], True, self.state_3_1_left[0], self.state_3_1_right[0], self.state_3_1_up[0], self.state_3_1_down[0])*100)/100
                self.state = (4,1)
        #STATE (3,2)
        if state_inside == (3,2):
            if key == 'UP':
                self.state_3_2_up[0] = math.floor(self.Q(self.state_3_2_up[0], True, self.state_3_3_down[0], self.state_3_3_up[0], self.state_3_3_left[0], self.state_3_3_right[0])*100)/100
                self.state = (3,3)
            if key == 'DOWN':
                self.state_3_2_down[0] = math.floor(self.Q(self.state_3_2_down[0], True, self.state_3_1_up[0], self.state_3_1_down[0], self.state_3_1_left[0], self.state_3_1_right[0])*100)/100
                self.state = (3,1)
            if key == 'LEFT':
                self.state_3_2_left[0] = math.floor(self.Q(self.state_3_2_left[0], True, self.state_3_2_up[0], self.state_3_2_down[0], self.state_3_2_left[0], self.state_3_2_right[0])*100)/100
                self.state = (3,2)
            if key == 'RIGHT':
                self.state_3_2_right[0] = math.floor(self.Q(self.state_3_2_right[0], False, self.state_4_2_neg)*100)/100
                self.state_4_2_neg = -0.5
                self.state = (1,1)
        #STATE (3,3)
        if state_inside == (3,3):
            if key == 'UP':
                self.state_3_3_up[0] = math.floor(self.Q(self.state_3_3_up[0], True, self.state_3_3_up[0], self.state_3_3_down[0], self.state_3_3_left[0], self.state_3_3_right[0])*100)/100
                self.state = (3,3)
            if key == 'DOWN':
                self.state_3_3_down[0] = math.floor(self.Q(self.state_3_3_down[0], True, self.state_3_2_up[0], self.state_3_2_down[0], self.state_3_2_left[0], self.state_3_2_right[0])*100)/100
                self.state = (3,2)
            if key == 'LEFT':
                self.state_3_3_left[0] = math.floor(self.Q(self.state_3_3_left[0], True, self.state_2_3_right[0], self.state_2_3_left[0], self.state_2_3_up[0], self.state_2_3_down[0])*100)/100
                self.state = (2,3)
            if key == 'RIGHT':
                self.state_3_3_right[0] = math.floor(self.Q(self.state_3_3_right[0], False, self.state_4_3_pos)*100)/100
                self.state_4_3_pos = 0.5
                self.state = (1,1)
        #STATE (4,1)
        if state_inside == (4,1):
            if key == 'UP':
                self.state_4_1_up[0] = math.floor(self.Q(self.state_4_1_up[0], False, self.state_4_2_neg)*100)/100
                self.state_4_2_neg = -0.5 
                self.state = (1,1)
            if key == 'DOWN':
                self.state_4_1_down[0] = math.floor(self.Q(self.state_4_1_down[0], True, self.state_4_1_up[0], self.state_4_1_down[0], self.state_4_1_left[0], self.state_4_1_right[0])*100)/100
                self.state = (4,1)
            if key == 'LEFT':
                self.state_4_1_left[0] = math.floor(self.Q(self.state_4_1_left[0], True, self.state_3_1_right[0], self.state_3_1_left[0], self.state_3_1_up[0], self.state_3_1_down[0])*100)/100
                self.state = (3,1)
            if key == 'RIGHT':
                self.state_4_1_right[0] = math.floor(self.Q(self.state_4_1_right[0], True, self.state_4_1_up[0], self.state_4_1_down[0], self.state_4_1_left[0], self.state_4_1_right[0])*100)/100
                self.state = (4,1)

    def automatic(self):
        if self.state == (1,1):
            q_max = max(self.state_1_1_up[0], self.state_1_1_down[0], self.state_1_1_left[0], self.state_1_1_right[0])

    def run(self):
        while self.running:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.q_learning('UP', self.state)
                        print("Key UP")
                    if event.key == pygame.K_DOWN:
                        self.q_learning('DOWN', self.state)
                        print("Key DOWN")
                    if event.key == pygame.K_LEFT:
                        self.q_learning('LEFT', self.state)
                        print("Key LEFT")
                    if event.key == pygame.K_RIGHT:
                        self.q_learning('RIGHT', self.state)
                        print("Key RIGHT")
                    if event.key == pygame.K_t:
                        pygame.quit()
                        sys.exit()
                    self.screen.fill((255,255,255))
                    if self.state == (1,1):
                        self.py_draw(100,500)
                    if self.state == (1,2):
                        self.py_draw(100,300)
                    if self.state == (1,3):
                        self.py_draw(100,100)
                    if self.state == (2,1):
                        self.py_draw(300,500)
                    if self.state == (2,3):
                        self.py_draw(300,100)
                    if self.state == (3,1):
                        self.py_draw(500,500)
                    if self.state == (3,2):
                        self.py_draw(500,300)
                    if self.state == (3,3):
                        self.py_draw(500,100)
                    if self.state == (4,1):
                        self.py_draw(700,500)
                    pygame.display.flip()

q_learn = Q_Learning()
q_learn.py_init()
q_learn.initialize_var()
q_learn.py_draw(100,500)
q_learn.run()



