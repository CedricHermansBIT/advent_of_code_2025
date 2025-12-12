import numpy as np
import time
import random

# rotate and flip pieces
def get_all_variants(base_shape):
    """Generate all 8 unique orientations (rotations + flips)."""
    variants = []
    seen = set()

    current = base_shape
    for _ in range(4):
        # Add current rotation
        h, w = current.shape
        # Create hashable tuple to check duplicates
        s_tuple = tuple(current.flatten())
        if s_tuple not in seen:
            variants.append(current)
            seen.add(s_tuple)

        # Add flipped version
        flipped = np.flip(current, axis=1) # Flip horizontal
        s_tuple_f = tuple(flipped.flatten())
        if s_tuple_f not in seen:
            variants.append(flipped)
            seen.add(s_tuple_f)

        # Rotate 90 degrees for next loop
        current = np.rot90(current)

    # Sort based on height (biggest first)
    variants.sort(key=lambda x: -x.shape[1])
    return variants

# Solve for given h,w,pieces,counts
def solve_greedy(grid_h, grid_w, pieces, counts, max_attempts=100):
    #Sort pieces so biggest areas are put in first
    pieces = sorted(pieces, key=lambda p: p['area'], reverse=True)

    start_time = time.time()

    for attempt in range(max_attempts):
        # Initialize empty grid
        grid = np.zeros((grid_h, grid_w), dtype=bool)
        placed_count = 0

        # If not the first attempt, shuffle the list slightly to try new combos
        if attempt > 0:
            random.shuffle(pieces)

            if attempt % 5 == 0:
                # Every 5th attempt, enforce size ordering again but with slight swaps
                pieces.sort(key=lambda p: p['area'] + random.random(), reverse=True)

        success = True

        # Try to place every piece
        for i, piece in enumerate(pieces):
            placed = False

            # Try every possible orientation for this piece
            for var_idx, mask in enumerate(piece['variants']):
                h, w = mask.shape
                # Check if the piece fits somewhere
                for r in range(grid_h - h + 1):
                    for c in range(grid_w - w + 1):
                        # FAST COLLISION CHECK using NumPy boolean logic
                        # If grid slice AND mask has any overlap, it's a collision.
                        # We want NO overlap.
                        region = grid[r:r+h, c:c+w]

                        # If we would have a piece already on the region, than we would get a true somewhere
                        if not np.any(region & mask):
                            # If not, we can place the piece
                            grid[r:r+h, c:c+w] |= mask
                            placed = True
                            break
                    if placed: break
                if placed: break

            if not placed:
                success = False
                break # Failed this attempt, move to next retry

        if success:
            print(f"Success on attempt {attempt+1}!")
            print(f"Time taken: {time.time() - start_time:.4f}s")
            return grid

        # If too many pieces don't fit, chance that they suddenly will fit afterwards is small, so we kinda just say: it doesn't
        # Note that this could be wrong, but it was worth the try, and it worked for the puzzle input somehow :D
        if (len(pieces)-i)>10:
            print(f"Attempt {attempt+1} failed. Best so far: {i}/{len(pieces)} pieces. However, due to too many unfitting pieces, we say this one will probably never fit")
            return None

        if (attempt + 1) % 10 == 0:
            print(f"Attempt {attempt+1} failed. Best so far: {i}/{len(pieces)} pieces.")


    print("Could not fit all pieces after max attempts.")
    return None


if __name__ == "__main__":
    # Parse input
    shapes=dict()
    grids=[]
    counts=[]

    with open("input.txt") as ifile:
        currentshape=-1
        for line in ifile:
            if "x" in line:
                grid,count=line.strip().split(": ")
                grids.append([int(x) for x in grid.split("x")])
                counts.append({i:int(x) for i,x in enumerate(count.split(" "))})
            elif line.strip()=="":
                continue
            elif ":" in line:
                currentshape=int(line[0])
                shapes[currentshape]=[]
            else:
                shapes[currentshape].append(line.strip())

    # Convert shapes to numpy boolean arays
    shapes_map=dict()
    for shape in shapes:
        shapes_map[shape]=np.array([[0 if x=="." else 1 for x in y] for  y in shapes[shape]],dtype=bool)

    # Solve for every input grid
    r=0
    for grid,count in zip(grids,counts):
        print("solving ",grid,count)
        # Build the library of all pieces to be placed (including rotations and flips!)
        piece_library = []
        for pid, c in count.items():
            variants = get_all_variants(shapes_map[pid])
            # Store (Piece ID, List of Mask Variants)
            for _ in range(c):
                piece_library.append({
                    'id': pid,
                    'variants': variants,
                    'area': np.sum(variants[0])
                })

        # RUN IT
        solution_grid = solve_greedy(grid[0], grid[1], piece_library, count, max_attempts=500)

        if solution_grid is not None:
            r+=1
            # If we want to visualize the grid
#            import matplotlib.pyplot as plt
#            plt.imshow(solution_grid, cmap='Greys', origin='upper')
#            plt.title("Packed Grid (Binary View)")
#            plt.show()
    print(r)
