
import numpy as np
import matplotlib.pyplot as plt

# System constants
dt = 0.01  # time step
g = -9.81 

graph_plot_array = []

def get_user_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Please try again, using numbers only")

def get_initial_conditions():
    t_f = get_user_input('Over how many seconds would you like your simulation to model the particles projectile motion?')
    x_i = get_user_input('What is the inital position of the particle in the horizontal plane?' )
    y_i = get_user_input('What is the initial position of the particle in the vertical plane?' )
    theta_d = get_user_input('What is the particles angle of inclination to the horizontal in degrees? ')
    v_i = get_user_input(' What is the particles intial velocity?' )
    return t_f, x_i, y_i, theta_d, v_i


def run_simulation(t_f, x_i, y_i, theta_d, v_i):
    theta_r = np.radians(theta_d)   # convert to radians
    vx_i = (v_i) * np.cos(theta_r)  # horz velocity
    vy_i = (v_i) * np.sin(theta_r)  # vert velocity
    
    t = 0
    plot_points = []
    
    while t < t_f:
        plot_points.append((x_i,y_i))
        
        # updating values for the next time step
        t += dt
        x_i += vx_i * dt
        y_i += vy_i * dt
        vx_i += 0 * dt     # constant - here for conceptualisation
        vy_i += g * dt
        
        # Check if the projectile is about to go below the ground level
        if y_i < 0:
            # Append the point just before it goes below 0
            plot_points.append((x_i, 0))
            break  # Exit the loop since the projectile hit the ground
        

    x_points = []
    y_points = []
    for coords in plot_points:
        x, y = coords
        x_points.append(x)
        y_points.append(y)
    return x_points, y_points
                


def plot_trajectory(x_points, y_points):
    plt.plot(x_points, y_points, '-ro', markersize=2)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid()
    plt.title("Projectile Motion")
    plt.show()



t_f, x_i, y_i, theta_d, v_i = get_initial_conditions()   
x_points, y_points = run_simulation(t_f, x_i, y_i, theta_d, v_i) 
plot_trajectory(x_points, y_points)   




