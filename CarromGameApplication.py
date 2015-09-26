import pygame
import random
import math

background_colour = (238,197,145)
(width, height) = (560,560)
drag = 0.999
elasticity = 0.75
gravity = (math.pi, 0.002)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
ORANGE=(255,165,0)
WOODEN =(238,197,145)


def addVectors((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

def collide(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors((p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass), (angle, 2*p2.speed*p2.mass/total_mass))
        (p2.angle, p2.speed) = addVectors((p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass), (angle+math.pi, 2*p1.speed*p1.mass/total_mass))
        p1.speed *= elasticity
        p2.speed *= elasticity

        overlap = 0.5*(p1.size + p2.size - dist+1)
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap

class Particle():
    def __init__(self,colour, (x, y), size,mass):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.mass=mass
        
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag
        

    def strikers(self,ycor):
        (mX,mY) = pygame.mouse.get_pos()
        if mX>440:
           self.x=440
        elif mX<120:
           self.x=120
        else:
           self.x= mX
        self.y= ycor
    

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

screen = pygame.display.set_mode((800,560))
pygame.display.set_caption('My Carrom ')

#number_of_particles = 10
my_particles = []

#for n in range(number_of_particles):
#    size = random.randint(10, 20)
#    x = random.randint(size, width-size)
#    y = random.randint(size, height-size)

striker = Particle(GREEN,(160,470), 15,50)

particle = Particle(BLACK,(300,280), 10,5)
my_particles.append(particle)
particle = Particle(BLACK,(260,280), 10,5)
my_particles.append(particle)
particle = Particle(BLACK,(340,280), 10,5)
my_particles.append(particle)
particle = Particle(BLACK,(220,280), 10,5)
my_particles.append(particle)
particle = Particle(BLACK,(280,300), 10,5)
my_particles.append(particle)
particle = Particle(BLACK,(280,260), 10,5)
my_particles.append(particle)
particle = Particle(ORANGE,(280,280), 10,5)
my_particles.append(particle)
particle = Particle(WHITE,(320,280), 10,5)
my_particles.append(particle)
particle = Particle(WHITE,(240,280), 10,5)
my_particles.append(particle)
particle = Particle(WHITE,(280,320), 10,5)
my_particles.append(particle)
particle = Particle(WHITE,(260,300), 10,5)
my_particles.append(particle)
particle = Particle(WHITE,(280,240), 10,5)
my_particles.append(particle)

particle = Particle(WHITE,(100,320), 10,5)
my_particles.append(particle)
 
      

    
    
    
    
    
    #pygame.draw.line(screen,BLUE,(my_particles[0].x,my_particles[0].y),(mX,mY),2)
    
    
    

def back_color():
    screen.fill(background_colour)



    

    

selected_particle = None
running = True
state =0
count1=0
count2=0
flip=0
while running:
    
    screen.fill(background_colour)
    
    """ Draw all circles"""
    pygame.draw.circle(screen,BLACK,(280,280),60,1)
    pygame.draw.circle(screen,BLACK,(20,20),20,0)
    pygame.draw.circle(screen,BLACK,(540,20),20,0)
    pygame.draw.circle(screen,BLACK,(20,540),20,0)
    pygame.draw.circle(screen,BLACK,(540,540),20,0)

    """ Draw all lines"""
    pygame.draw.line(screen, BLACK, (120,80), (440,80), 3)
    pygame.draw.line(screen, BLACK, (120,100), (440,100), 2)
    
    pygame.draw.line(screen, BLACK, (80,120), (80,440), 3)
    pygame.draw.line(screen, BLACK, (100,120), (100,440), 2)
    
    pygame.draw.line(screen, BLACK, (120,460), (440,460), 2)
    pygame.draw.line(screen, BLACK, (120,480), (440,480), 3)
    
    pygame.draw.line(screen, BLACK, (460,120), (460,440), 2)
    pygame.draw.line(screen, BLACK, (480,120), (480,440), 3)

    """ Draw small circles"""
    
    pygame.draw.circle(screen,RED,(120,90),10,0)
    pygame.draw.circle(screen,RED,(440,90),10,0)
    
    pygame.draw.circle(screen,RED,(90,120),10,0)
    pygame.draw.circle(screen,RED,(90,440),10,0)
    
    pygame.draw.circle(screen,RED,(120,470),10,0)
    pygame.draw.circle(screen,RED,(440,470),10,0)
    
    pygame.draw.circle(screen,RED,(470,120),10,0)
    pygame.draw.circle(screen,RED,(470,440),10,0)

    """ Draw inclined lines"""
    pygame.draw.line(screen, BLACK, (60,500), (200,360), 1)
    pygame.draw.line(screen, BLACK, (360,360), (500,500), 1)
    pygame.draw.line(screen, BLACK, (60,60), (200,200), 1)
    pygame.draw.line(screen, BLACK, (360,200), (500,60), 1)

    """ Draw arrow lines"""
    pygame.draw.line(screen, BLACK, (200,360), (200,400), 1)
    pygame.draw.line(screen, BLACK, (200,360), (160,360), 1)
    
    pygame.draw.line(screen, BLACK, (360,360), (360,400), 1)
    pygame.draw.line(screen, BLACK, (360,360), (400,360), 1)

    pygame.draw.line(screen, BLACK, (200,200), (160,200), 1)
    pygame.draw.line(screen, BLACK, (200,200), (200,160), 1)

    pygame.draw.line(screen, BLACK, (360,200), (400,200), 1)
    pygame.draw.line(screen, BLACK, (360,200), (360,160), 1)

    pygame.draw.line(screen, BLACK, (560,0), (560,560), 5)
    pygame.draw.line(screen, BLACK, (0,0), (560,0), 10)
    pygame.draw.line(screen, BLACK, (0,0), (0,560), 10)
    pygame.draw.line(screen, BLACK, (0,560), (560,560), 10)
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
          
        if state == 0:
           if flip%2==0:
              ycor=470
           elif flip%2!=0:
              ycor=90
           
           striker.strikers(ycor)
           if event.type == pygame.MOUSEBUTTONDOWN:
               (mouseX, mouseY) = pygame.mouse.get_pos()
               if mouseX>440:
                   striker.x=440
               elif mouseX<120:
                   striker.x=120
                   
               else:
                   striker.x=mouseX
               
               state =1
               continue
              
        if state ==1:
            if event.type == pygame.MOUSEBUTTONDOWN:
               (mouseX2, mouseY2) = pygame.mouse.get_pos()
               dx = mouseX2 - striker.x
               dy = mouseY2 - striker.y
               striker.angle = 0.5*math.pi + math.atan2(dy, dx)
               striker.speed = math.hypot(dx, dy) * .02
               state=2

        
            
               
                  
             
    
     
               
    striker.move()
    striker.bounce()
    if striker.speed>0 and striker.speed<0.02:
        striker.x=160
        flip+=1
        if flip%2==0:
            striker.y=470
        elif flip%2!=0:
            striker.y=90
        if striker.x<30 and striker.speed>0:
            if striker.y<30:
                if flip%2==0:
                    
                   count1-=1
                elif flip%2!=0:
                   count2-=1

        if striker.x<30 and striker.speed>0:
            if striker.y>530:
                if flip%2==0:
                    
                   count1-=1
                elif flip%2!=0:
                   count2-=1

        if striker.x>530 and striker.speed>0:
            if striker.y<30:
                if flip%2==0:
                    
                   count1-=1
                elif flip%2!=0:
                   count2-=1

        if striker.x>530 and striker.speed>0:
            if striker.y>530:
                if flip%2==0:
                    
                   count1-=1
                elif flip%2!=0:
                   count2-=1
            
        striker.speed=0

        
        
        state=0
    
    
    for i, particle in enumerate(my_particles):
    
        particle.move()
        particle.bounce()
        collide(striker,particle)
        if particle.x<30 and particle.speed>0:
            if particle.y<30:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1

        if particle.x<30 and particle.speed>0:
            if particle.y>530:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1

        if particle.x>530 and particle.speed>0:
            if particle.y<30:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1

        if particle.x>530 and particle.speed>0:
            if particle.y>530:
                my_particles.remove(particle)
                if flip%2==0:
                    count1+=1
                elif flip%2!=0:
                    count2+=1
                flip-=1

        
        if count1!=0:
            print "1:"+ str(count1)
        if count2!=0:
            print "2:" + str(count2)
        for particle2 in my_particles[i+1:]:
            
            collide(particle,particle2)
            
            striker.display()
            particle.display()
            if particle.speed<0.08:
                particle.speed=0

        
    
    
    pygame.display.flip()        
      
            
       
        
            
            
          
        

       
            
            

            
   
            
            
            #pygame.time.wait()
            
            
            
            
            
       
    
    """if selected_particle:
        
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = 0.5*math.pi + math.atan2(dy, dx)
        selected_particle.speed = math.hypot(dx, dy) * 0.1"""

    

   


    
