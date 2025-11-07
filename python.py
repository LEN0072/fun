from rubik_solver import utils

# Represent the cube's state as a string (e.g., 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby')
# This string represents the colors of each sticker in a specific order.
scrambled_cube_state = 'wowgybwyogygybyoggrowbrgywrborwborgowryby'

# Solve the cube using the 'Beginner' method
solution_moves = utils.solve(scrambled_cube_state, 'Beginner')

print(f"Solution moves: {solution_moves}")
