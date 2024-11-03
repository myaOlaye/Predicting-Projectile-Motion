# Projectile Motion Simulation

This project simulates the projectile motion of a particle using Euler's method of integration. It calculates the trajectory based on user-defined initial conditions such as position, angle, and velocity.

## How It Works

The simulation employs Euler's method to iteratively calculate the position of the particle at discrete time intervals. The position updates are given by the equations:

- \( x(t + dt) = x(t) + v_x \cdot dt \)
- \( y(t + dt) = y(t) + v_y \cdot dt \)
- \( v_y(t + dt) = v_y(t) + g \cdot dt \)

Where:
- \( dt \) is the time step,
- \( v_x \) is the horizontal velocity (constant),
- \( v_y \) is the vertical velocity,
- \( g \) is the gravitational acceleration (approximately -9.81 m/s²).

## Packages Used

- **NumPy**: For mathematical operations and handling numerical calculations.
- **Matplotlib**: For plotting the trajectory of the projectile.

To run this code, the above packages must be installed. You can install the packages using pip or conda:

```bash
pip install numpy matplotlib
```
```bash
conda install numpy matplotlib
```
Execute the script in a Python interactive window (e.g., Jupyter Notebook, or your IDE's interactive terminal). The simulation will prompt you for input parameters and display the projectile motion plot.

## Limitations

- **Time Step Dependency**: The accuracy of the simulation is highly dependent on the chosen time step \( dt \). Smaller time steps improve accuracy but increase computation time.
- **Ignoring Weight and Size**: The simulation assumes the particle is a point mass, simplifying calculations by neglecting its weight and dimensions. This model focuses solely on projectile motion, ignoring potential effects from air resistance or other forces that could influence larger or heavier objects.
