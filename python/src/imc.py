"""Top-level main program for fcimc."""

import argparse
import logging
import random
import time as pytime

import imc_global_io_data as io
import imc_global_part_data as part

import imc_mesh
import imc_opcon
import imc_user_input


def setup_logger():
    """Set up logging."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(name)24s %(levelname)8s: %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def parse_args():
    """Parse command-line arguments and options."""
    parser = argparse.ArgumentParser(
        description="Python implementation of Fleck and Cummings (1971) implicit Monte Carlo code."
    )

    parser.add_argument("-i", "--input", default="fcimc.in", help="Name of input deck")

    return parser.parse_args()


def main():
    """Top-level main function for fcimc."""
    tm0 = pytime.perf_counter()

    io.logger = setup_logger()

    args = parse_args()
    io.input_file = args.input

    rng_seed = 12345
    #io.logger.info("Initialising RNG with seed %d", rng_seed)
    random.seed(rng_seed)

    part.n_max = 20000

    imc_user_input.read()
    imc_user_input.echo()

    imc_mesh.make()
    #imc_mesh.echo()

    imc_opcon.run()

    tm1 = pytime.perf_counter()
    print("Time taken for calculation= {:10.2f} s".format(tm1 - tm0))


if __name__ == "__main__":

    # Call the main function
    main()
