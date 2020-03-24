import argparse

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--iteration", dest = "iteration", default = "-1", help="Number of iterations", type=int)
    args = parser.parse_args()
    
    return args.iteration