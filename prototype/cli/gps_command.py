import argparse


def main():
    parser = argparse.ArgumentParser(description="GPS Assessment Runner")
    parser.add_argument("model", help="Path to GPS YAML model")
    args = parser.parse_args()

    print(f"GPS model selected: {args.model}")


if __name__ == "__main__":
    main()
