from ctables import create_tables
from broker import main_broker


def main():
	create_tables()
	main_broker()

main()