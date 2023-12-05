import math
import requests
import argparse

#Write you own function that moves the dron from one place to another 
#the function returns the drone's current location while moving
#====================================================================================================
def your_function(origin,target):
    difference = (target[0] - origin[0], target[1] - origin[1])
    distance = math.sqrt(math.pow(direction[0],2) + math.pow(direction[1], 2))
    direction = (abs(difference[0])/difference[0],abs(difference[1])/difference[1])
    
    
    if distance == 0:
        return origin
    
    
    new_coords = [0,0]
    
    distance_multi = 1/10000
    
    new_coords[0] = origin[0] + direction[0]/distance_multi
    new_coords[1] = origin[1] + direction[1]/distance_multi
    
    return tuple(new_coords)
    
    
def is_close_enough(coords1, coords2, tolerance=1e-4):
    return abs(coords1[0] - coords2[0]) < tolerance and abs(coords1[1] - coords2[1]) < tolerance

    
    #longitude = origin[0]
    #latitude = origin[1]
    #state = True
    #while state:
     #   if origin == targe:
      #      state = False
       # elif abs(longitude - target[0]) =< 1 and abs(latitude - target[1]) =< 1:
    #longitude = 13.21008
    #latitude = 55.71106
    #return (longitude, latitude)
#====================================================================================================


def run(current_coords, from_coords, to_coords, SERVER_URL):
    # Compmelete the while loop:
    # 1. Change the loop condition so that it stops sending location to the data base when the drone arrives the to_address
    # 2. Plan a path with your own function, so that the drone moves from [current_address] to [from_address], and the from [from_address] to [to_address]. 
    # 3. While moving, the drone keeps sending it's location to the database.
    #====================================================================================================
    while not is_close_enough(current_coords,from_coords):
        drone_coords = your_function(current_coords,from_coords)
        with requests.Session() as session:
            drone_location = {'longitude': drone_coords[0],
                              'latitude': drone_coords[1]
                        }
            resp = session.post(SERVER_URL, json=drone_location)
        current_coords = drone_coords
            
     while not is_close_enough(current_coords,to_coords):
        drone_coords = your_function(current_coords,to_coords)
        with requests.Session() as session:
            drone_location = {'longitude': drone_coords[0],
                              'latitude': drone_coords[1]
                        }
            resp = session.post(SERVER_URL, json=drone_location)
        current_coords = drone_coords
  #====================================================================================================

   
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    print(current_coords)
    print(from_coords)
    print(to_coords)

    run(current_coords, from_coords, to_coords, SERVER_URL)
